#!/usr/bin/env python

import csv
import json
import sqlalchemy
from sqlalchemy.orm import Session

# connect to the database
engine = sqlalchemy.create_engine("mysql+mysqlconnector://codetest:swordfish@host.docker.internal:3306/codetest")
connection = engine.connect()

# check if connect is successful
if connection:
  print("Connected to database successfully")
else:
  print("Failed to connect to database")

metadata = sqlalchemy.schema.MetaData(engine)

# make an ORM object to refer to the table
people = sqlalchemy.schema.Table('people', metadata, autoload=True, autoload_with=engine)
places = sqlalchemy.schema.Table('places', metadata, autoload=True, autoload_with=engine)

# read the places CSV data file into the table
with open('/data/places.csv') as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader: 
    connection.execute(places.insert().values(city = row[0], county= row[1], country = row[2]))

print("Data places uploaded successfully")

# read the people CSV data file into the table
with open ('/data/people.csv') as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader:
    # given_name,family_name,date_of_birth,place_of_birth
    connection.execute(people.insert().values(given_name = row[0], family_name = row[1], date_of_birth = row[2], place_of_birth = row[3]))

print("Data people uploaded successfully")

# update the people table with the place_id
update = sqlalchemy.sql.update(people).values(place_id = places.c.id).where(people.c.place_of_birth == places.c.city)
connection.execute(update)

session = Session(engine)

# output the table to a JSON file
with open('/data/summary_output.json', 'w') as json_file:
    country_count = sqlalchemy.sql.select([places.c.country, sqlalchemy.func.count(people.c.id)]).select_from(places.join(people)).group_by(places.c.country)
    #coutry_count = sqlalchemy.sql.query(places.country, sqlalchemy.func.count(people.id)).join(people).group_by(places.country).all()
    result = connection.execute(country_count).fetchall()
    data = {row['country']: row['count'] for row in result}
    json_data = json.dumps(data)
    json_file.write(json_data)