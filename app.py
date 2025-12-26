from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "your_openweathermap_api_key"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
        response = requests.get(url).json()
        if response.get("main"):
            weather = {
                "city": city,
                "temp": response["main"]["temp"],
                "humidity": response["main"]["humidity"],
                "condition": response["weather"][0]["description"]
            }
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
