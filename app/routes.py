from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods=["GET", "POST"])
def results():
    #Store info from form opener
    user_input = dict(request.form)
    print (user_input)
    artist_name = user_input["artists"]
    print (artist_name)
    x = model.find_songs(artist_name)
    return render_template("results.html", song_list=x)

    #Access the list of songs from dictionary
    #Return the list of songs
