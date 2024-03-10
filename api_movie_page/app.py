from flask import Flask, request, render_template, redirect, url_for, jsonify, abort, make_response

from forms import MovieForm
from models import movies

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/movies/", methods=["GET", "POST"])
def movies_list():
    form = MovieForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            movies.create(form.data)
            movies.save_all()
        return redirect(url_for("movies_list"))

    return render_template("movies.html", form=form, movies=movies.all(), error=error)


@app.route("/movies/<int:movie_id>/", methods=["GET", "POST"])
def movie_details(movie_id):
    movie = movies.get(movie_id - 1)
    form = MovieForm(data=movie)

    if request.method == "POST":
        if form.validate_on_submit():
            movies.update(movie_id - 1, form.data)
        return redirect(url_for("movies_list"))
    return render_template("movie.html", form=form, movie_id=movie_id)

@app.route("/api/v1/movies/", methods=["GET"])
def movies_list_api_v1():
    return jsonify(movies.all())



@app.route("/api/v1/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    movie = movies.get(movie_id)
    if not movie:
        abort(404)
    return jsonify({"movie": movie})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)



@app.route("/api/v1/movies/", methods=["POST"])
def create_movie():
    if not request.json or not 'title' in request.json:
        abort(400)
    movie = {
        'id': movies.all()[-1]['id'] + 1,
        'title': request.json['title'],
        'year': request.json.get('year', ""),
        'genre': request.json.get('genre', ""),
        'rating': request.json.get('rating', "")
    }
    movies.create(movie)
    return jsonify({'movie': movie}), 201

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)
#
@app.route("/api/v1/movies/<int:movie_id>", methods=['DELETE'])
def delete_movie(movie_id):
    result = movies.delete(movie_id)
    if not result:
        abort(404)
    return jsonify({'result': result})

@app.route("/api/v1/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    movie = movies.get(movie_id)
    if not movie:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json

    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'year' in data and not isinstance(data.get('year'), int),
        'genre' in data and not isinstance(data.get('genre'), str),
        'rating' in data and not isinstance(data.get('rating'), int)
    ]):
        abort(400)
    movie = {
        'title': data.get('title', movie['title']),
        'year': data.get('year', movie['year']),
        'genre': data.get('genre', movie['genre']),
        'rating': data.get('rating', movie['rating'])
    }
    movies.update(movie_id, movie)
    return jsonify({'movie': movie})



if __name__ == "__main__":
    app.run(debug=True)
#
#     # if request.method == "POST":
#     #     if form.validate_on_submit():
#     #         movies.update(movie_id - 1, form.data)
#     #     return redirect(url_for("movies_list"))
#     # return render_template("movie.html", form=form, todo_id=movie_id)
#
#


# from flask import Flask, request, render_template, redirect, url_for
#
# from forms import MovieForm
# from models import movies


# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, render_template, redirect, url_for
#
# from forms import TodoForm
# from models import todos
#
# app = Flask(__name__)
# app.config["SECRET_KEY"] = "nininini"
#
# @app.route("/todos/", methods=["GET", "POST"])
# def todos_list():
#     form = TodoForm()
#     error = ""
#     if request.method == "POST":
#         if form.validate_on_submit():
#             todos.create(form.data)
#             todos.save_all()
#         return redirect(url_for("todos_list"))
#
#     return render_template("todos.html", form=form, todos=todos.all(), error=error)
#
#
# @app.route("/todos/<int:todo_id>/", methods=["GET", "POST"])
# def todo_details(todo_id):
#     todo = todos.get(todo_id - 1)
#     form = TodoForm(data=todo)
#
#     if request.method == "POST":
#         if form.validate_on_submit():
#             todos.update(todo_id - 1, form.data)
#         return redirect(url_for("todos_list"))
#     return render_template("todo.html", form=form, todo_id=todo_id)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
