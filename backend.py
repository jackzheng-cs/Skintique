from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define the RapidAPI credentials
RAPIDAPI_URL = "https://skin-analyze-pro.p.rapidapi.com/facebody/analysis/skinanalyze-pro"
RAPIDAPI_KEY = "56a07c45d4msh38bf0a7024da080p13bc9fjsn1ef3fe154312"

@app.route('/', methods=['POST'])
def analyze_skin():
    print("Request received!")  # Debugging step

    # Ensure an image file is received
    if 'image' not in request.files:
        return jsonify({"error": "No image file part"}), 400
    
    image_file = request.files['image']
    
    # Ensure an image file is actually uploaded
    if image_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    print(f"Received file: {image_file.filename}")  # Debugging step

    # Read image data
    image_data = image_file.read()

    try:
        # Prepare headers
        headers = {
            'x-rapidapi-key': RAPIDAPI_KEY,
            'x-rapidapi-host': "skin-analyze-pro.p.rapidapi.com"
        }
        
        # Prepare file data
        files = {'image': ('image.jpg', image_data, 'image/jpeg')}
        
        # Send POST request
        response = requests.post(RAPIDAPI_URL, files=files, headers=headers)
        
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True)
