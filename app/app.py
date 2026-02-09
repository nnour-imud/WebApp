###Connects to a SQL database using mssql-python
from flask import Flask, request
import pyodbc
from os import getenv
from dotenv import load_dotenv
from db import connect_to_db

app = Flask(__name__)
load_dotenv()

def connect_to_db():
    try:
        conn = pyodbc.connect(getenv("SQL_CONNECTION_STRING"))
        print("Connection to database successful!")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def get_user_by_id(conn, user_id):
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE id = ?", user_id)
        user = cursor.fetchone()

        return user
    else:
        return None
    
def get_all_users(conn):
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users")
        users = cursor.fetchall()

        return users
    else:
        return None
    

@app.route("/")
def hello():
    return "Hello and welcome to my web app!"

@app.route("/contact")
def contact():
    return "Please reach out to us at nnour@imudsolutions."

@app.route("/about")
def about():
    return "We are over 1000 members and fastest growing platform. \n" \
           "Our community is expanding at an unprecedented rate, and we are proud to announce that we have officially surpassed 1,000 active members"

@app.route("/db_data/<int:user_id>")
def db_data(user_id):
    conn = connect_to_db()
    if conn:
        user = get_user_by_id(conn, user_id)  
        conn.close()
        if user:
            return f"User ID: {user[0]}, Name: {user[1]}"
        else:
            return f"User {user_id} not found."
    else:
        return "Error connecting to database."

if __name__ == "__main__":
    app.run(debug=True, port=8000)
