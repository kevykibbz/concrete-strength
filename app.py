from flask import Flask, render_template,jsonify
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__,static_url_path='/static')

database_url = os.getenv('DATABASE_URL')


def create_table():
    # Connect to PostgreSQL
    conn = psycopg2.connect(database_url)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS table_records (
            id SERIAL PRIMARY KEY,
            cement FLOAT,
            slag FLOAT,
            flyash FLOAT,
            water FLOAT,
            superplasticizer FLOAT,
            coarseaggregate FLOAT,
            fineaggregate FLOAT,
            age INTEGER,
            csMPa FLOAT
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()


def data_exists(cursor, values):
    query = """
        SELECT COUNT(*) FROM table_records
        WHERE cement = %s AND slag = %s AND flyash = %s
        AND water = %s AND superplasticizer = %s AND coarseaggregate = %s
        AND fineaggregate = %s AND age = %s AND csMPa = %s
    """
    cursor.execute(query, values)
    count = cursor.fetchone()[0]
    return count > 0


def insert_data():
    conn = psycopg2.connect(database_url)
    cursor = conn.cursor()

    data = [
    {'cement': 540, 'slag': 0, 'flyash': 0, 'water': 162, 'superplasticizer': 2.5, 'coarseaggregate': 1040, 'fineaggregate': 676, 'age': 28, 'csMPa': 79.99},  # clean
    {'cement': 540, 'slag': 0, 'flyash': 0, 'water': 162, 'superplasticizer': 2.5, 'coarseaggregate': 1055, 'fineaggregate': 676, 'age': 28, 'csMPa': 61.89},  # clean
    {'cement': 332.5, 'slag': 142.5, 'flyash': 0, 'water': 228, 'superplasticizer': 0, 'coarseaggregate': 932, 'fineaggregate': 594, 'age': 270, 'csMPa': 40.27},  # clean
    {'cement': 332.5, 'slag': 142.5, 'flyash': 0, 'water': 228, 'superplasticizer': 0, 'coarseaggregate': 932, 'fineaggregate': 594, 'age': 365, 'csMPa': 41.05},  # clean
    {'cement': 198.6, 'slag': 132.4, 'flyash': 0, 'water': 192, 'superplasticizer': 0, 'coarseaggregate': 978.4, 'fineaggregate': 825.5, 'age': 360, 'csMPa': 44.3},  # clean
    {'cement': 266, 'slag': 114, 'flyash': 0, 'water': 228, 'superplasticizer': 0, 'coarseaggregate': 932, 'fineaggregate': 670, 'age': 90, 'csMPa': 47.03},  # clean
    {'cement': 380, 'slag': 95, 'flyash': 0, 'water': 228, 'superplasticizer': 0, 'coarseaggregate': 932, 'fineaggregate': 594, 'age': 365, 'csMPa': 47.03},  # clean
    {'cement': 380, 'slag': 95, 'flyash': 0, 'water': 228, 'superplasticizer': 0, 'coarseaggregate': 932, 'fineaggregate': 594, 'age': 28, 'csMPa': 36.45},  # clean
    {'cement': 266, 'slag': 114, 'flyash': 0, 'water': 228, 'superplasticizer': 0, 'coarseaggregate': 932, 'fineaggregate': 670, 'age': 28, 'csMPa': 45.85},  # clean
    {'cement': 475, 'slag': 0, 'flyash': 0, 'water': 228, 'superplasticizer': 0, 'coarseaggregate': 932, 'fineaggregate': 594, 'age': 28, 'csMPa': 39.29},  # clean
    {'cement': 198.6, 'slag': 132.4, 'flyash': 0, 'water': 192, 'superplasticizer': 0, 'coarseaggregate': 978.4, 'fineaggregate': 825.5, 'age': 90, 'csMPa': 38.07},  # clean
    {'cement': 198.6, 'slag': 132.4, 'flyash': 0, 'water': 192, 'superplasticizer': 0, 'coarseaggregate': 978.4, 'fineaggregate': 825.5, 'age': 28, 'csMPa': 28.02},  # clean
    {'cement': 427.5, 'slag': 47.5, 'flyash': 0, 'water': 228, 'superplasticizer': 0, 'coarseaggregate': 932, 'fineaggregate': 594, 'age': 270, 'csMPa': 43.01},  # clean
    {'cement': 190, 'slag': 190, 'flyash': 0, 'water': 228, 'superplasticizer': 0, 'coarseaggregate': 932, 'fineaggregate': 670, 'age': 90, 'csMPa': 42.33},  # clean
    {'cement': 304, 'slag': 76, 'flyash': 0, 'water': 228, 'superplasticizer': 0, 'coarseaggregate': 932, 'fineaggregate': 670, 'age': 28, 'csMPa': 47.81},  # clean
    {'cement': 380, 'slag': 0, 'flyash': 0, 'water': 228, 'superplasticizer': 0, 'coarseaggregate': 932, 'fineaggregate': 670, 'age': 90, 'csMPa': 52.91},  # clean
    {'cement': 139.6, 'slag': 209.4, 'flyash': 0, 'water': 192, 'superplasticizer': 0, 'coarseaggregate': 1047, 'fineaggregate': 806.9, 'age': 90, 'csMPa': 39.36},
    {'cement': 342, 'slag': 38, 'flyash': 0, 'water': 228, 'superplasticizer': 0, 'coarseaggregate': 932, 'fineaggregate': 670, 'age': 365, 'csMPa': 56.14},
    {'cement': 380, 'slag': 95, 'flyash': 0, 'water': 228, 'superplasticizer': 0, 'coarseaggregate': 932, 'fineaggregate': 594, 'age': 90, 'csMPa': 40.56}
]




    for record in data:
        # Check if the record already exists
        if not data_exists(cursor, (record['cement'], record['slag'], record['flyash'], record['water'],
                                     record['superplasticizer'], record['coarseaggregate'], record['fineaggregate'],
                                     record['age'], record['csMPa'])):
            # Insert data into the table
            cursor.execute("""
                INSERT INTO table_records
                (cement, slag, flyash, water, superplasticizer, coarseaggregate, fineaggregate, age, csMPa)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (record['cement'], record['slag'], record['flyash'], record['water'],
                  record['superplasticizer'], record['coarseaggregate'], record['fineaggregate'],
                  record['age'], record['csMPa']))

    conn.commit()
    cursor.close()
    conn.close()


@app.route('/prepare/data')
def prepare_data():
    create_table()
    insert_data()


    response_data = {
        'status': 'success',
        'message': 'Request Processed Successfully'
    }

    # Return JSON response
    return jsonify(response_data)


@app.route('/')
def index():
    # Retrieve the inserted data for display
    conn = psycopg2.connect(database_url)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM table_records")
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', records=records)


if __name__ == "__main__":
    port = int(os.getenv('PORT', 80))
    app.run(debug=False, host='0.0.0.0', port=port, threaded=True)


