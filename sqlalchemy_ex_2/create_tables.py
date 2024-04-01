from sqlalchemy import Table, Column, Float, String, MetaData, Integer
from sqlalchemy import create_engine

engine = create_engine('sqlite:///task_database.db')

meta = MetaData()

stations = Table(
    'stations', meta,
    Column('station', String, primary_key=True),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String),
    Column('country', String),
    Column('state', String)
)

measures = Table(
    'measures', meta,
    Column('station', String, primary_key=True),
    Column('date', String),
    Column('precip', Float),
    Column('tobs', Integer)
)

meta.create_all(engine)
print(engine.table_names())
