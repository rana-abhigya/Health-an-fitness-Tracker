from flask import Flask, request
import mysql.connector
from config import db_config  # Import DB credentials

app = Flask(__name__)

@app.route('/')
def form():
    return open('index.html').read()

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from form
    date = request.form['date']
    steps = request.form['steps']
    calories = request.form['calories']
    sleep = request.form['sleep_hours']

    try:
        # Connect to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert data into table
        cursor.execute("""
            INSERT INTO records (date, steps, calories, sleep_hours)
            VALUES (%s, %s, %s, %s)
        """, (date, steps, calories, sleep))

        conn.commit()
        conn.close()
        return "<h3>Data Submitted Successfully!</h3><a href='/'>Submit More</a>"

    except Exception as e:
        return f"<h3>Error: {e}</h3>"

if __name__ == '__main__':
    app.run(debug=True)
