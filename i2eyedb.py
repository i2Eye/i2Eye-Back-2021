# DB connection
import psycopg2
from psycopg2 import Error
import csv
import json
import requests


# This one i'm not v sure how to connect to a local db, so i've connected to another one i've deployed on heroku, can i get some help here?
def connect_db():
        connection = psycopg2.connect(user = "jhfdzctgeytrkt",
                            password = "6f0913d556bf6eee840e0e2ba8b4c0b3ef0331f6855852008be07eeb840cdb6f",
                            host = "ec2-35-173-94-156.compute-1.amazonaws.com",
                            port = "5432",
                            database = "dbpduk6f0fbp8q")
        return connection

# Create station table
def create_station():
      try:
            connection = connect_db()
            cursor = connection.cursor()

            create_stations_table_query = '''CREATE TABLE IF NOT EXISTS station
                  (station_id SERIAL PRIMARY KEY,
                  station_name TEXT UNIQUE); '''
            cursor.execute(create_stations_table_query)
            connection.commit()
            print("Table station created successfully in PostgreSQL ")

      except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while creating station table", error)

      finally:
            #closing database connection.
            if(connection):
                  cursor.close()
                  connection.close()
                  #print("PostgreSQL connection is closed")

# Create patient table
def create_patient():
      try:
            connection = connect_db()
            cursor = connection.cursor()

            create_patients_table_query = '''CREATE TABLE IF NOT EXISTS patient
                  (patient_id SERIAL PRIMARY KEY,
                  status TEXT,
                  completed_station INTEGER[]); '''
            cursor.execute(create_patients_table_query)
            connection.commit()
            print("Table patient created successfully in PostgreSQL ")

      except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while creating patient table", error)

      finally:
            #closing database connection.
            if(connection):
                  cursor.close()
                  connection.close()
                  #print("PostgreSQL connection is closed")

# Create question table
def create_question():
      try:
            connection = connect_db()
            cursor = connection.cursor()

            create_questions_table_query = '''CREATE TABLE IF NOT EXISTS question
                  (question_id SERIAL PRIMARY KEY,
                  question TEXT,
                  station_id INTEGER,
                  type_id INTEGER); '''
            cursor.execute(create_questions_table_query)
            connection.commit()
            print("Table question created successfully in PostgreSQL ")

      except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while creating question table", error)

      finally:
            #closing database connection.
            if(connection):
                  cursor.close()
                  connection.close()
                  #print("PostgreSQL connection is closed")

# Create answer table
def create_answer():
      try:
            connection = connect_db()
            cursor = connection.cursor()

            create_answers_table_query = '''CREATE TABLE IF NOT EXISTS answer
                  (answer_id SERIAL PRIMARY KEY,
                  patient_id INTEGER,
                  answers TEXT,
                  question_id INTEGER,
                  station_id INTEGER); '''
            cursor.execute(create_answers_table_query)
            connection.commit()
            print("Table answer created successfully in PostgreSQL ")

      except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while creating answer table", error)

      finally:
            #closing database connection.
            if(connection):
                  cursor.close()
                  connection.close()
                  #print("PostgreSQL connection is closed")

# Create type table
def create_type():
      try:
            connection = connect_db()
            cursor = connection.cursor()

            create_type_table_query = '''CREATE TABLE IF NOT EXISTS type
                  (type_id SERIAL PRIMARY KEY,
                  type_info TEXT); '''
            cursor.execute(create_type_table_query)
            connection.commit()
            print("Table type created successfully in PostgreSQL ")

      except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while creating type table", error)

      finally:
            #closing database connection.
            if(connection):
                  cursor.close()
                  connection.close()
                  #print("PostgreSQL connection is closed")

# Create all the tables
def db_setup():
      create_station()
      create_patient()
      create_question()
      create_answer()
      create_type()

# Insert stations into station table
def insert_station(station_name):
      try:
            connection = connect_db()
            cursor = connection.cursor()
            postgres_insert_query = """ INSERT INTO station (station_id, station_name) VALUES (DEFAULT, %s)"""
            record_to_insert = (station_name,)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into station table")
      except (Exception, psycopg2.Error) as error:
            if(connection):
                print("Failed to insert record into station table", error)
      finally:
            if(connection):
                cursor.close()
                connection.close()
                #print("PostgreSQL connection is closed")

# Insert patients into patient table
def insert_patient(status, completed_station):
      try:
            connection = connect_db()
            cursor = connection.cursor()

            postgres_insert_query = """ INSERT INTO patient (patient_id, status, completed_station) 
                                    VALUES (DEFAULT, %s, %s)"""
            record_to_insert = (status, completed_station,)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into patient table")
      except (Exception, psycopg2.Error) as error :
            if(connection):
                print("Failed to insert record into patient table", error)
      finally:
            if(connection):
                cursor.close()
                connection.close()
                #print("PostgreSQL connection is closed")

# Insert questions into question table
def insert_question(question, station_id, type_id):
      try:
            connection = connect_db()
            cursor = connection.cursor()
            postgres_insert_query = """ INSERT INTO question (question_id, question, station_id, type_id) VALUES (DEFAULT, %s, %s, %s)"""
            record_to_insert = (question, station_id, type_id,)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into question table")
      except (Exception, psycopg2.Error) as error:
            if(connection):
                print("Failed to insert record into question table", error)
      finally:
            if(connection):
                cursor.close()
                connection.close()
                #print("PostgreSQL connection is closed")

# Insert answers into answer table
def insert_answer(patient_id, answer, question_id, station_id):
      try:
            connection = connect_db()
            cursor = connection.cursor()
            postgres_insert_query = """ INSERT INTO answer (answer_id, patient_id, answers, question_id, station_id) VALUES (DEFAULT, %s, %s, %s, %s)"""
            record_to_insert = (patient_id, answer, question_id, station_id,)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into answer table")
      except (Exception, psycopg2.Error) as error:
            if(connection):
                print("Failed to insert record into answer table", error)
      finally:
            if(connection):
                cursor.close()
                connection.close()
                #print("PostgreSQL connection is closed")

# Insert types into type table
def insert_type(type_info):
      try:
            connection = connect_db()
            cursor = connection.cursor()
            postgres_insert_query = """ INSERT INTO type (type_id, type_info) VALUES (DEFAULT, %s)"""
            record_to_insert = (type_info,)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into type table")
      except (Exception, psycopg2.Error) as error:
            if(connection):
                print("Failed to insert record into type table", error)
      finally:
            if(connection):
                cursor.close()
                connection.close()
                #print("PostgreSQL connection is closed")

# Update the completed stations in patient table
def update_completed(patient_id, station_name):
      try:
            connection = connect_db()
            cursor = connection.cursor()

            postgres_select_query = """ SELECT completed_station FROM patient WHERE patient_id = %s"""
            record_to_select = (patient_id,)
            cursor.execute(postgres_select_query, record_to_select)
            completed = cursor.fetchone()[0]

            postgres_select_query = """ SELECT station_id FROM station WHERE station_name = %s"""
            record_to_select = (station_name,)
            cursor.execute(postgres_select_query, record_to_select)
            station_id = cursor.fetchone()[0]

            completed.append(station_id)

            postgres_update_query = """ UPDATE patient SET completed_station = %s WHERE patient_id = %s"""
            record_to_update = (completed, patient_id,)
            cursor.execute(postgres_update_query, record_to_update)
            connection.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into patient table")

      except (Exception, psycopg2.Error) as error :
            if(connection):
                print("Failed to insert record into patient table", error)
      finally:
            if(connection):
                cursor.close()
                connection.close()
                #print("PostgreSQL connection is closed")

# Read the questions from excel file
def read_questions(file):
      questions = []
      with open(file) as csvfile:
            file_reader = csv.reader(csvfile)
            for question in file_reader:
                  questions.append(question[0])
      return questions

# Insert questions from excel file into question table (I'm not v sure what to insert for the type, do we manually insert since there's not really a pattern?)
def save_questions(file):
      questions = read_questions(file)
      station_id = 0
      type_id = 0
      for q in questions:
            if (q == "Registration"):
                  station_id = 1
                  continue
            elif (q == "Tobacco Questionnare"):
                  station_id = 2
                  continue
            elif (q == "Anemia Questionnare"):
                  station_id = 3
                  continue
            elif (q == "BMI (Underweight measurement)"):
                  station_id = 4
                  continue
            elif (q == "Haemoglobin (Anemia measurement)"):
                  station_id = 5
                  continue
            elif (q == "Post campaign survey"):
                  station_id = 6
                  continue
            insert_question(q, station_id, type_id)
      print("all questions added")

# Get the questions and type from each station (I've printed the station name, questions, and types in list form but I'm not sure how to return it in the format needed)
def get_questions(station_name):
      try:
            connection = connect_db()
            cursor = connection.cursor()

            postgres_select_query = """ SELECT station_id FROM station WHERE station_name = %s"""
            record_to_select = (station_name,)
            cursor.execute(postgres_select_query, record_to_select)
            connection.commit()
            station_id = cursor.fetchall()
            print(station_name)

            if (not station_id is None):
                  postgres_select_query = """ SELECT question FROM question WHERE station_id = %s"""
                  cursor.execute(postgres_select_query, station_id)
                  connection.commit()
                  questions = cursor.fetchall()
                  questions = [i[0] for i in questions]
                  print(questions)

                  postgres_select_query = """ SELECT type_info FROM type INNER JOIN question ON question.type_id = type.type_id WHERE question.station_id = %s"""
                  cursor.execute(postgres_select_query, station_id)
                  connection.commit()
                  types = cursor.fetchall()
                  types = [i[0] for i in types]
                  print(types)
            
      except (Exception, psycopg2.Error) as error:
            if(connection):
                print("Failed to select from question table", error)
      finally:
            if(connection):
                cursor.close()
                connection.close()
                #print("PostgreSQL connection is closed")

# Get answers from a patient from a particular station (also printed in list form)
def get_answers(patient_id, station_id):
      try:
            connection = connect_db()
            cursor = connection.cursor()
            postgres_select_query = """ SELECT answers FROM answer WHERE patient_id = %s AND station_id = %s"""
            record_to_select = (patient_id, station_id,)
            cursor.execute(postgres_select_query, record_to_select)
            connection.commit()
            answers = cursor.fetchall()
            answers = [i[0] for i in answers]
            print(answers)
      except (Exception, psycopg2.Error) as error:
            if(connection):
                print("Failed to select from question table", error)
      finally:
            if(connection):
                cursor.close()
                connection.close()
                #print("PostgreSQL connection is closed")

# Testing if info is inserted successfully
def insert_stuff_test():
      insert_type("text")
      insert_type("radio")
      insert_patient("busy", [])
      insert_patient("busy", [])
      insert_answer(1, "answer", 1, 1)
      insert_answer(1, "answer", 2, 1)

# Insert all the stations
def insert_stations():
      insert_station("Registration")
      insert_station("Tobacco Questionnare")
      insert_station("Anemia Questionnare")
      insert_station("BMI (Underweight measurement)")
      insert_station("Haemoglobin (Anemia measurement)")
      insert_station("Post campaign survey")

def main():
      db_setup()
      #insert_stations()
      #save_questions("question.csv")
      #insert_stuff_test()
      #get_questions("Registration")
      #get_answers(1,1)
      #update_completed(1, "registration")

if __name__ == '__main__':
    main()