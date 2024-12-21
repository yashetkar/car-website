from flask import Flask, render_template, request, jsonify # type: ignore
from flask_pymongo import PyMongo # type: ignore

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/car_database"
mongo = PyMongo(app)

# Route: Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route: Recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    preferences = request.form.get('preferences')
    # Query MongoDB for cars matching the preferences
    results = mongo.db.cars.find({"type": preferences})
    recommendations = [car['name'] for car in results]

    # Render the results
    return render_template('recommendations.html', recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
