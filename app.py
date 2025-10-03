
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Define your class names in the correct order
class_names = ['EDH Class', 'Healthy Class', 'IPH Class', 'IVH Class', 'SAH Class', 'SDH Class']

# Load the Keras model (update filename if needed)
model = load_model('model//best_cnn_model_retrained_1.h5')

@app.route('/predict', methods=['POST'])
def predict():
	if 'file' not in request.files:
		return jsonify({'error': 'No file part in the request'}), 400
	file = request.files['file']
	if file.filename == '':
		return jsonify({'error': 'No selected file'}), 400

	# Save the file to a temporary location
	temp_path = os.path.join('temp_image.png')
	file.save(temp_path)

	# Preprocess the image
	img = image.load_img(temp_path, target_size=(224,224))
	img_array = image.img_to_array(img)/255.0
	img_array = np.expand_dims(img_array, axis=0)

	prediction = model.predict(img_array)
	class_index = int(np.argmax(prediction))
	class_name = class_names[class_index]
	probability = float(prediction[0][class_index])

	# Remove the temp file
	os.remove(temp_path)

	return jsonify({
		'predicted_class': class_index,
		'predicted_class_name': class_name,
		'probability': probability
	})

if __name__ == '__main__':
	app.run(debug=True)
