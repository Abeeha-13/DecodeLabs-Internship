from flask import Flask, render_template, request, jsonify
from PIL import Image
import torch
from torchvision import models, transforms
import json
import time
import os


app = Flask(__name__)

# --------------------------------------------------
# Configuration
# --------------------------------------------------

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# --------------------------------------------------
# Load Pre-trained AI Model
# --------------------------------------------------

print("Loading AI model...")

weights = models.ResNet50_Weights.DEFAULT
model = models.resnet50(weights=weights)

model.eval()

preprocess = weights.transforms()
categories = weights.meta["categories"]

print("AI model loaded successfully!")


# --------------------------------------------------
# Home Page
# --------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------------------
# Image Recognition API
# --------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    start_time = time.time()

    # Check whether image was uploaded
    if "image" not in request.files:
        return jsonify({
            "success": False,
            "error": "No image was uploaded."
        }), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "error": "Please select an image."
        }), 400

    try:

        # Open uploaded image
        image = Image.open(file).convert("RGB")

        # Preprocess image
        input_tensor = preprocess(image)

        # Add batch dimension
        input_batch = input_tensor.unsqueeze(0)

        # Run model inference
        with torch.no_grad():
            output = model(input_batch)

        # Convert model output to probabilities
        probabilities = torch.nn.functional.softmax(output[0], dim=0)

        # Get top 5 predictions
        top5_probabilities, top5_indices = torch.topk(
            probabilities,
            5
        )

        predictions = []

        for probability, index in zip(
            top5_probabilities,
            top5_indices
        ):

            predictions.append({
                "label": categories[index.item()],
                "confidence": round(
                    probability.item() * 100,
                    2
                )
            })

        # Best prediction
        best_prediction = predictions[0]

        # Calculate processing time
        processing_time = round(
            time.time() - start_time,
            3
        )

        # Confidence level
        confidence = best_prediction["confidence"]

        if confidence >= 80:
            confidence_level = "High Confidence"
        elif confidence >= 50:
            confidence_level = "Moderate Confidence"
        else:
            confidence_level = "Low Confidence"

        # Return JSON response
        return jsonify({
            "success": True,

            "prediction": best_prediction["label"],

            "confidence": best_prediction["confidence"],

            "confidence_level": confidence_level,

            "processing_time": processing_time,

            "model": "ResNet-50",

            "dataset": "ImageNet",

            "predictions": predictions
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.route("/health")
def health():

    return jsonify({
        "status": "online",
        "model": "ResNet-50",
        "message": "AI Vision Studio backend is running."
    })


# --------------------------------------------------
# Run Flask Application
# --------------------------------------------------

if __name__ == "__main__":

    print("\n======================================")
    print("      AI VISION STUDIO")
    print("======================================")
    print("Backend: Flask")
    print("Model: ResNet-50")
    print("Status: Starting...")
    print("======================================\n")

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )