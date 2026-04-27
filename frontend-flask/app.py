from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Backend URL (Docker network service name)
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:5000")

# Home Page
@app.route("/")
def index():
    return render_template("index.html")


# Form Submit
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    contact = request.form.get("contact")

    # Validation
    if not name or not email or not contact:
        return "All fields are required!"

    try:
        data = {
            "name": name,
            "email": email,
            "contact": contact
        }

        # Call backend service
        response = requests.post(
            f"{BACKEND_URL}/users",
            json=data,
            timeout=5
        )

        # Check response
        if response.status_code == 200 or response.status_code == 201:
            return "✅ Data Submitted Successfully!"
        else:
            return f"❌ Backend error: {response.text}"

    except requests.exceptions.ConnectionError:
        return "❌ Cannot connect to backend service"

    except requests.exceptions.Timeout:
        return "❌ Backend request timeout"

    except Exception as e:
        return f"❌ Error: {str(e)}"


# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
