from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# RapidAPI Credentials
RAPIDAPI_URL = "https://skin-analyze-pro.p.rapidapi.com/facebody/analysis/skinanalyze-pro"
RAPIDAPI_KEY = "56a07c45d4msh38bf0a7024da080p13bc9fjsn1ef3fe154312"

# Serve the HTML page
@app.route('/')
def home():
    return render_template('home.html')  # Ensure home.html is in the 'templates' folder

# Handle Skin Analysis
@app.route('/analyze', methods=['POST'])
def analyze_skin():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image_file = request.files['image']

    if image_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    image_data = image_file.read()

    try:
        headers = {
            'x-rapidapi-key': RAPIDAPI_KEY,
            'x-rapidapi-host': "skin-analyze-pro.p.rapidapi.com"
        }
        files = {'image': ('image.jpg', image_data, 'image/jpeg')}

        response = requests.post(RAPIDAPI_URL, files=files, headers=headers)
        return jsonify(response.json())

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
