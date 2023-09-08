from flask import Flask, render_template
import csv

app = Flask(__name__)

# Function to read job listings from the CSV file
def read_job_listings():
    job_listings = []
    with open('job_listings.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            job_listings.append(row)
    return job_listings

# Route to display job listings
@app.route('/')
def index():
    job_listings = read_job_listings()
    return render_template('index.html', job_listings=job_listings)

if __name__ == '__main__':
    app.run(debug=True)
    