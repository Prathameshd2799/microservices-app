from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    contact = request.form.get("contact")

    if not name or not email or not contact:
        return "All fields are required!"

    try:
        data = {
            "name": name,
            "email": email,
            "contact": contact
        }

        response = requests.post("http://localhost:3000/users", json=data)

        return "Data Submitted Successfully!"

    except Exception as e:
        return f"Backend connection failed: {str(e)}"

if __name__ == "__main__":
    app.run(port=5000, debug=True)