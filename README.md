# Emotion Detector Project

An AI-based web application that detects emotions from user-provided text. This project is developed as part of the Software Engineering Final Project.

## Description
This application analyzes text input and predicts the emotional tone, returning scores for five core emotions:
* **Joy**
* **Anger**
* **Disgust**
* **Sadness**
* **Fear**

It also determines the **dominant emotion** based on the highest score. The application is built using Python, packaged as a standalone module, and deployed as a web application using Flask.

## Project Structure
* `EmotionDetection/`: The core application package containing the emotion detection logic.
  * `__init__.py`: Initializes the folder as a Python package.
  * `emotion_detection.py`: Contains the `emotion_detector` function.
* `server.py`: The Flask web server handling the UI routing and error handling.
* `test_emotion_detection.py`: Unit tests to validate application accuracy.

## Features
* **Text Emotion Analytics**: Evaluates sentences and breaks down emotional percentages.
* **Error Handling**: Gracefully handles blank or invalid inputs with appropriate warning messages.
* **Static Code Analysis**: Fully compliant with PEP 8 standards using Pylint.
