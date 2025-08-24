from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import json

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

print("🔄 Loading model and waste info...")
try:
    model = load_model('model.h5')
    with open('waste_info.json') as f:
        waste_info = json.load(f)

    MODEL_INPUT_SIZE = model.input_shape[1:3]
    waste_labels = list(waste_info.keys())
    
    print(f"✅ Model loaded. Expected input size: {MODEL_INPUT_SIZE}. Waste categories: {waste_labels}")

except Exception as e:
    print(f"❌ Error loading model or waste info: {str(e)}")
    exit()

def preprocess_image(image_path):
    img = load_img(image_path, target_size=MODEL_INPUT_SIZE)
    img_array = img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    filename = image.filename
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(path)

    try:
        img_array = preprocess_image(path)
        preds = model.predict(img_array)[0]
        
        predicted_class_index = np.argmax(preds)
        confidence = preds[predicted_class_index]
        
        # Check for low-confidence prediction
        if confidence < 0.7:
            return jsonify({
                "waste_detected": [],
                "message": "The waste type could not be confidently identified. Please try a clearer image."
            })
        
        predicted_label = waste_labels[predicted_class_index]
        
        info = waste_info.get(predicted_label, {})
        result = {
            "type": predicted_label,
            "decomposition": info.get("decomposition", "Unknown"),
            "tip": info.get("tip", "No tip available"),
            "disposal": info.get("disposal", "No disposal info")
        }

        return jsonify({"waste_detected": [result]})

    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

    finally:
        if os.path.exists(path):
            os.remove(path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)