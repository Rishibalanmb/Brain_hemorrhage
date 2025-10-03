# Brain Hemorrhage Detection (Flask)

This repository contains a small Flask web application and a trained CNN model for detecting brain hemorrhage from medical images (CT scans). The app provides a simple web UI (in `templates/index.html`) where you can upload an image and get a model prediction.

## What is included

- `app.py` - Flask application that serves the web UI and performs model inference.
- `best_cnn_model_retrained_1.h5` - Trained Keras model used by the app for predictions.
- `Multiclass_customCNN_1.ipynb` - Jupyter notebook used during model development / retraining.
- `requirements.txt` - Python dependencies required to run the app.
- `templates/index.html` - Simple web interface for uploading images and viewing prediction results.

## Requirements

- Python 3.9 (Windows tested)
- PowerShell (instructions below target PowerShell)

Install Python dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If you prefer using the system Python without a virtual environment, run:

```powershell
pip install -r requirements.txt
```

## Run the app

Start the Flask app:

```powershell
python app.py
```

Open a browser and go to http://127.0.0.1:5000 (or the address printed by Flask). Use the upload form to submit a CT image and receive the model's prediction.

## Notes on the model and data

- The included file `best_cnn_model_retrained_1.h5` is the model artifact used by the Flask app. Keep in mind that medical image models should be validated carefully before any real-world use.
- `Multiclass_customCNN_1.ipynb` contains the training and evaluation code used to build the model. Use it to retrain or fine-tune the model on new data.

## Development / Retraining

1. Prepare your dataset following the same preprocessing pipeline used in the notebook (image size, normalization, class labels).
2. Open `Multiclass_customCNN_1.ipynb` and run the training cells to produce a new `.h5` model file.
3. Replace `best_cnn_model_retrained_1.h5` with your newly trained model (or update the filename in `app.py`).

## Troubleshooting

- If the server fails to start, check that all packages from `requirements.txt` are installed and that the virtual environment is activated.
- If model loading raises errors, confirm your Keras/TensorFlow versions match the version used to create the `.h5` file.

## Next steps / suggestions

- Add input validation and size checks to the Flask upload endpoint.
- Add unit tests for the inference pipeline.
- Add a LICENSE file if you want to make the repository open source with a clear license.

## Contact

If you want help improving the app or converting it to a production-ready service (Docker, API-only service, CI tests), open an issue or reach out in the repository.

---
*This README was generated to help get the project running and to clarify where to look to retrain or extend the model.*
