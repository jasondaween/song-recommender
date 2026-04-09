from flask import Flask, redirect, render_template, request
import random

songs = {
    "Pop": [
        {
            "name": "Die With A Smile", "artist": "Lady Gaga & Bruno Mars", 
            "img": "https://i.scdn.co/image/ab67616d0000b27382ea2e9e1858aa012c57cd45", 
            "link": "https://open.spotify.com/track/2plbrEY59IikOBgBGLjaoe?si=56374fbd314f4f9b"
        },
        {
            "name": "BIRDS OF A FEATHER", "artist": "Billie Eilish",
            "img": "https://i.scdn.co/image/ab67616d0000b27371d62ea7ea8a5be92d3c1f62",
            "link": "https://open.spotify.com/track/6dOtVTDdiauQNBQEDOtlAB?si=5608afebcf8e4c52"
        },
        {
            "name": "Espresso", "artist": "Sabrina Carpenter",
            "img": "https://i.scdn.co/image/ab67616d0000b273659cd4673230913b3918e0d5",
            "link": "https://open.spotify.com/track/1vLqigPHwiFnXsfrLMehV1?si=14c317eac84c4c84"
        },
        {
            "name": "So Easy (To Fall In Love)", "artist": "Olivia Dean",
            "img": "https://i.scdn.co/image/ab67616d0000b2739a336bfb6d40bbd90a507417",
            "link": "https://open.spotify.com/track/6sGIMrtIzQjdzNndVxe397?si=4185bcc356fc4e3b"
        },
        {
            "name": "thank u, next", "artist": "Ariana Grande",
            "img": "https://i.scdn.co/image/ab67616d00001e0256ac7b86e090f307e218e9c8",
            "link": "https://open.spotify.com/track/3e9HZxeyfWwjeyPAMmWSSQ?si=e33bce6094f34ccb"
        }
    ]
}

app = Flask(__name__)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 1. Get the user's input
        genre = request.form.get("genres") 

        # 2. Check if user actually picked something
        if not genre:
            return redirect("/")

        # 3. Get the list of songs for that genre
        song_list = songs[genre]

        # 4. Get a random song from that list
        song = random.choice(song_list)

        return render_template("index.html", genre=genre, song=song)
    
    else:
        return render_template("index.html", genre=None, song=None)
    
if __name__ == "__main__":
    app.run(debug=True)