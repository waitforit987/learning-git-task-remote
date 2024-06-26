from app import app, db
from app.models import Movie, Director, Borrowing

@app.shell_context_processor
def make_shell_context():
  return {
    'db': db,
    'Movie': Movie,
    'Director': Director,
    'Borrowing': Borrowing
  }