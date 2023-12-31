import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.static_folder = '../static'

@app.route('/')
def index():
    return render_template('request.html')

@app.route("/fetch_movies", methods=["POST"])
def fetch_movies():
    api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNDIyYTBmOTlkYWNlNDY3MGRlNDQyMjI5YTcxNDk3ZSIsInN1YiI6IjY0ZDMxZWU2OTQ2MzE4MDQzNDE3YmRmNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.eoRsDkPIiidUdTeGTQLsZHvJ7lZXkl3y-YRhNfv5JLo"
    genre = request.form.get("genre-value")
    print(genre)
    url = f"https://api.themoviedb.org/3/discover/movie?include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres={genre}"

    headers = {"accept": "application/json", "Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return render_template("result.html", movies=data["results"])
    except Exception as e:
        error = str(e)
        message = error.split(":")[1]
        return render_template("error.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)
