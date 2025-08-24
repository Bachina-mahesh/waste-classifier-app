Waste Classifier Application
A machine learning-powered web application that identifies the type of waste in an image and provides information on how to dispose of it properly. The application is built with a Python Flask backend for a deep learning model and a React frontend for the user interface.

Table of Contents
Features

Technologies Used

Prerequisites

Setup and Installation

Model Training

How to Run the Application

Repository Structure

Contact

Features
Image Classification: Classifies images into one of 9 waste categories: plastic, organic, metal, glass, paper, cardboard, e-waste, textiles, and styrofoam.

Waste Information: Provides detailed information for each waste type, including decomposition time, disposal tips, and disposal methods.

Confidence Score: The model's prediction confidence is checked, and a clear message is displayed if the prediction is not reliable.

Technologies Used
Backend
Python: The core programming language.

Flask: A micro web framework for the API.

TensorFlow/Keras: Used for building, training, and running the deep learning model.

Numpy: For numerical operations on image data.

Flask-CORS: To handle cross-origin resource sharing between the frontend and backend.

Frontend
React: A JavaScript library for building the user interface.

Prerequisites
Before you begin, ensure you have the following installed:

Python 3.x: (e.g., python --version)

Node.js & npm: (e.g., node --version and npm --version)

Git: (e.g., git --version)

Setup and Installation
Follow these steps to set up the project on your local machine.

1. Clone the Repository
git clone https://github.com/Bachina-mahesh/waste-classifier-app.git
cd waste-classifier-app

2. Backend Setup
Navigate to the backend directory and install the required Python libraries.

cd backend
pip install -r requirements.txt

(If you don't have a requirements.txt file, you can create one by running pip freeze > requirements.txt.)

3. Frontend Setup
Navigate to the frontend directory and install the Node.js packages.

cd frontend  # Or wherever your React project is located
npm install

Model Training
The pre-trained model (model.h5) is included, but if you wish to retrain the model with new data, follow these steps.

Download Images: The train_model.py script will automatically download and organize images into training and validation folders. Ensure waste_info.json is in the same directory.

python train_model.py

Train the Model: The script will proceed to train a new model and save it as waste_classifier_model.h5. This new file can then be renamed to model.h5 and used by the Flask application.

How to Run the Application
You need to run the backend and frontend simultaneously.

1. Run the Backend
Open a new terminal, navigate to the backend directory, and run the Flask server.

cd backend
python app.py

(The server will run on http://localhost:5001.)

2. Run the Frontend
Open another terminal, navigate to the frontend directory, and start the React development server.

cd frontend
npm start

(The application will be available at http://localhost:3000.)

You can now use the web interface to upload images and get waste classification predictions.

Repository Structure
waste-classifier-app/
├── backend/
│   ├── app.py                     # Flask application
│   ├── model.h5                   # Trained model file
│   ├── waste_info.json            # Waste category data
│   ├── uploads/                   # Directory for temporary file uploads
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.js                 # React component
│   │   └── App.css
│   └── package.json
├── train_model.py
└── README.md

Contact
For any questions or suggestions, please open an issue in this repository.
