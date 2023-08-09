from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('request.html')

@app.route("/fetch_movies", methods=["POST"])
def fetch_movies():
    api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNDIyYTBmOTlkYWNlNDY3MGRlNDQyMjI5YTcxNDk3ZSIsInN1YiI6IjY0ZDMxZWU2OTQ2MzE4MDQzNDE3YmRmNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.eoRsDkPIiidUdTeGTQLsZHvJ7lZXkl3y-YRhNfv5JLo"
    genre = request.form.get("genre-value")
    print(genre)
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres={genre}"

    headers = {"accept": "application/json", "Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return render_template("result.html", movies=data["results"])
    except Exception as e:
        return jsonify({"error": str(e)})

