
import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
       
        test_string = request.form.get("test_string", "")
        regex_pattern = request.form.get("regex", "")

      
        matches = list(re.finditer(regex_pattern, test_string))

        
        matches = [match.group() for match in matches]

        return render_template("index.html", test_string=test_string, regex=regex_pattern, matches=matches)
    else:
        return render_template("index.html")

@app.route("/validate_email", methods=["GET", "POST"])
def validate_email():
    if request.method == "POST":
        email = request.form.get("email")
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            validation_result = "Valid"
        else:
            validation_result = "Invalid"
        return render_template("validate_email.html", validation_result=validation_result, email=email)
    else:
        return render_template("validate_email.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
