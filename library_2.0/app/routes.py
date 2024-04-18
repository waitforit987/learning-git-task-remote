from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import Movie, Director


@app.route("/")
def homepage():
  movies = Movie.query.all()
  return render_template("index.html", title = "Library", movies = movies)

@app.route("/add_movie", methods=['POST', 'GET'])
def add_movie():
  if request.method == 'POST':
    name = request.form['name']
    production_year = request.form['production_year']
    director_name = request.form['director']
    lastname = request.form['lastname']

    director = Director.query.filter_by(name=director_name, lastname=lastname).first()
    if not director:
      director = Director(name=name, lastname=lastname)
      db.session.add(director)

    new_movie = Movie(name=name, production_year=production_year, directors=[director])
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("homepage"))
  return render_template("add_movie.html")

@app.route("/delete_movie/<int:movie_id>", methods=['POST', 'GET'])
def delete_movie(movie_id):
  if request.method == 'POST':
    movie = Movie.query.get_or_404(movie_id)
    directors = list(movie.directors)
    db.session.delete(movie)
    db.session.commit()

    for director in directors:
      if not director.movies:
        db.session.delete(director)
    
    db.session.commit()

    return redirect(url_for('homepage'))
  
@app.route("/toggle_movie/<int:movie_id>", methods=['POST', 'GET'])
def toggle_movie(movie_id):
  if request.method == 'POST':
    movie = Movie.query.get_or_404(movie_id)
    movie.is_borrowed = not movie.is_borrowed
    db.session.commit()
    return redirect(url_for("homepage"))


 