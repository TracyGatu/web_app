from flask import Flask, render_template
import psycopg2
import folium

# Initialize the Flask app
app = Flask(__name__)

# Database configuration
DB_CONFIG = {
    "database": "DEMO",
    "user": "postgres",
    "password": "admin2002",
    "host": "localhost",
    "port": 5432
}
# Define a route for the home page
@app.route("/")
def home():
    try:
        # Connect to the PostgreSQL database using a context manager
        with psycopg2.connect(**DB_CONFIG) as conn:
            # Create a cursor object to execute SQL queries
            with conn.cursor() as cur:
                # Execute a query to retrieve data from the table
                cur.execute("SELECT * FROM bel_cities")

                # Fetch all the rows returned by the query
                rows = cur.fetchall()

        # Render the home template and pass the data to it
        return render_template("home.html", data=rows)

    except psycopg2.Error as e:
        error_message = "Database error: " + str(e)
        return render_template("error.html", error_message=error_message)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
