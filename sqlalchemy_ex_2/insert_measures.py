import csv
from create_tables import measures, engine 

with open('clean_measure.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        ins = measures.insert().values(
            station=row['station'],
            date=row['date'],
            precip=(row['precip']),
            tobs=(row['tobs'])
        )
        conn = engine.connect()
        result = conn.execute(ins)
        conn.close()