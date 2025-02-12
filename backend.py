# backend code for the web application 
# team vision
# used skin analyze pro api
# 
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import base64

app = Flask(__name__)
# allows backend to connect to the fronend, kinda acts like a connector 
CORS(app)  

# API Details
API_URL = "https://skin-analyze-pro.p.rapidapi.com/facebody/analysis/skinanalyze-pro"
RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY"

# api documentation and keys 
# the link for reference "https://rapidapi.com/ailabapi-ailabapi-default/api/skin-analyze-pro/playground/apiendpoint_1ad6699e-3c18-4471-845e-07a6fff94632"
HEADERS = {
    "x-rapidapi-host": "skin-analyze-pro.p.rapidapi.com",
    "x-rapidapi-key": RAPIDAPI_KEY,
    "Content-Type": "application/x-www-form-urlencoded"
}

#web app details based on the api
@app.route('/analyze', methods=['POST'])
def analyze_skin():
    """Handles skin image analysis"""
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = request.files['image']

    # Convert image to base64
    image_base64 = base64.b64encode(image.read()).decode('utf-8')

    # Send to API
    payload = {"image": image_base64}
    response = requests.post(API_URL, headers=HEADERS, data=payload)

    if response.status_code != 200:
        return jsonify({"error": "Failed to analyze image", "details": response.json()}), 500

    return jsonify(response.json())  # Return analysis results

if __name__ == '__main__':
    app.run(debug=True)
