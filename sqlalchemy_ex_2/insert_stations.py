import csv
from create_tables import stations, engine 

with open('clean_stations.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    conn = engine.connect()
    for row in reader:
        conn.execute(stations.insert(), row)

result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print(result)
conn.close()
