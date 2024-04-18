# app/models.py
from app import db

movie_directors = db.Table('movie_directors',
                          db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
                          db.Column('director_id', db.Integer, db.ForeignKey('director.id'), primary_key=True)
                          )

class Movie(db.Model):
   __tablename__ = 'movie'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), index=True, nullable = False)
   production_year = db.Column(db.Integer)
   is_borrowed = db.Column(db.Boolean, default = False)
   directors = db.relationship("Director", secondary = movie_directors, back_populates="movies")

   def __str__(self):
       return f"<Movie {self.name}>"

class Director(db.Model):
   __tablename__ = 'director'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(150), index = True, nullable = False)
   lastname = db.Column(db.String(100), index=True, nullable = False)
   movies = db.relationship('Movie', secondary = movie_directors, back_populates = 'directors')


   def __str__(self):
       return f"<Director: {self.name} {self.lastname}>"
   

class Borrowing(db.Model):
   __tablename__ = 'borrowing'
   id = db.Column(db.Integer, primary_key = True)
   movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable = False)
   borrower_name = db.Column(db.String(100), nullable = False)
   borrowed_date = db.Column(db.DateTime, nullable = False)
   return_date = db.Column(db.DateTime)
   
   movie = db.relationship('Movie', backref = db.backref('borrowings', lazy = True))

   def __repr__(self):
      return f"<Borrowing {self.movie.name} by {self.borrower_name}>"
   

