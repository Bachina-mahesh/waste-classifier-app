# Waste Classifier Application

A machine learning-powered web application that identifies the type of waste in an image and provides information on how to dispose of it properly. The application is built with a Python Flask backend for a deep learning model and a React frontend for the user interface.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Model Training](#model-training)
- [How to Run the Application](#how-to-run-the-application)
- [Repository Structure](#repository-structure)
- [Contact](#contact)

## Features

- **Image Classification:** Classifies images into one of 9 waste categories: `plastic`, `organic`, `metal`, `glass`, `paper`, `cardboard`, `e-waste`, `textiles`, and `styrofoam`.
- **Waste Information:** Provides detailed information for each waste type, including decomposition time, disposal tips, and disposal methods.
- **Confidence Score:** The model's prediction confidence is checked, and a clear message is displayed if the prediction is not reliable.

## Technologies Used

### Backend
- **Python:** The core programming language.
- **Flask:** A micro web framework for the API.
- **TensorFlow/Keras:** Used for building, training, and running the deep learning model.
- **Numpy:** For numerical operations on image data.
- **Flask-CORS:** To handle cross-origin resource sharing between the frontend and backend.

### Frontend
- **React:** A JavaScript library for building the user interface.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x:** (e.g., `python --version`)
- **Node.js & npm:** (e.g., `node --version` and `npm --version`)
- **Git:** (e.g., `git --version`)

## Setup and Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone [https://github.com/Bachina-mahesh/waste-classifier-app.git](https://github.com/Bachina-mahesh/waste-classifier-app.git)
cd waste-classifier-app
