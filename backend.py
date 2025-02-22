from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Define the RapidAPI URL
RAPIDAPI_URL = "https://skin-analyze-pro.p.rapidapi.com/facebody/analysis/skinanalyze-pro"

# Set your RapidAPI Key
RAPIDAPI_KEY = "56a07c45d4msh38bf0a7024da080p13bc9fjsn1ef3fe154312"

@app.route('/analyze', methods=['POST'])
def analyze_skin():
    # Ensure an image file is received
    if 'image' not in request.files:
        return jsonify({"error": "No image file part"}), 400
    
    image_file = request.files['image']
    
    # Ensure an image file is actually uploaded
    if image_file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Prepare the image data for the API
    image_data = image_file.read()
    
    # Prepare headers for the RapidAPI request
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-rapidapi-host': 'skin-analyze-pro.p.rapidapi.com',
        'x-rapidapi-key': RAPIDAPI_KEY
    }
    
    # Prepare the payload (form data)
    payload = {
        'image': (image_file.filename, image_data, 'image/jpeg')  # Change to the correct MIME type if needed
    }

    try:
        # Send POST request to the RapidAPI endpoint
        response = requests.post(RAPIDAPI_URL, headers=headers, files=payload)
        
        # Check if the request was successful
        if response.status_code == 200:
            return jsonify(response.json())  # Return the API response as JSON
        else:
            return jsonify({"error": "Failed to analyze skin", "status_code": response.status_code}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
