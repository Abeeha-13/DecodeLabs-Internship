// =====================================================
// AI VISION STUDIO
// Frontend JavaScript
// =====================================================


// -----------------------------------------------------
// DOM Elements
// -----------------------------------------------------

const uploadBox = document.getElementById("uploadBox");
const browseBtn = document.getElementById("browseBtn");
const imageInput = document.getElementById("imageInput");

const analysisSection =
    document.getElementById("analysisSection");

const imagePreview =
    document.getElementById("imagePreview");

const analyzeBtn =
    document.getElementById("analyzeBtn");

const analyzeText =
    document.getElementById("analyzeText");

const loadingSpinner =
    document.getElementById("loadingSpinner");

const prediction =
    document.getElementById("prediction");

const confidence =
    document.getElementById("confidence");

const confidenceFill =
    document.getElementById("confidenceFill");

const confidenceStatus =
    document.getElementById("confidenceStatus");

const predictionsList =
    document.getElementById("predictionsList");

const processingTime =
    document.getElementById("processingTime");

const historySection =
    document.getElementById("historySection");

const historyBody =
    document.getElementById("historyBody");

const clearHistoryBtn =
    document.getElementById("clearHistoryBtn");


// -----------------------------------------------------
// Application State
// -----------------------------------------------------

let selectedFile = null;

let predictionHistory = [];


// -----------------------------------------------------
// Choose Image Button
// -----------------------------------------------------

browseBtn.addEventListener("click", function (event) {

    event.stopPropagation();

    imageInput.click();

});


// -----------------------------------------------------
// Upload Box Click
// -----------------------------------------------------

uploadBox.addEventListener("click", function () {

    imageInput.click();

});


// -----------------------------------------------------
// File Selected
// -----------------------------------------------------

imageInput.addEventListener("change", function () {

    if (this.files.length > 0) {

        handleFile(this.files[0]);

    }

});


// -----------------------------------------------------
// Handle Selected File
// -----------------------------------------------------

function handleFile(file) {

    // Validate file type

    const allowedTypes = [
        "image/jpeg",
        "image/jpg",
        "image/png"
    ];

    if (!allowedTypes.includes(file.type)) {

        alert(
            "Please upload a JPG, JPEG, or PNG image."
        );

        return;
    }


    // Store selected file

    selectedFile = file;


    // Create image preview

    const reader = new FileReader();

    reader.onload = function (event) {

        imagePreview.src =
            event.target.result;

        analysisSection.style.display =
            "grid";

        analysisSection.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });

    };


    reader.readAsDataURL(file);

}


// -----------------------------------------------------
// Drag & Drop
// -----------------------------------------------------

uploadBox.addEventListener(
    "dragover",
    function (event) {

        event.preventDefault();

        uploadBox.classList.add("dragover");

    }
);


uploadBox.addEventListener(
    "dragleave",
    function () {

        uploadBox.classList.remove("dragover");

    }
);


uploadBox.addEventListener(
    "drop",
    function (event) {

        event.preventDefault();

        uploadBox.classList.remove("dragover");

        const files = event.dataTransfer.files;

        if (files.length > 0) {

            handleFile(files[0]);

        }

    }
);


// -----------------------------------------------------
// Analyze Image
// -----------------------------------------------------

analyzeBtn.addEventListener(
    "click",
    async function () {

        if (!selectedFile) {

            alert(
                "Please select an image first."
            );

            return;
        }


        // Loading state

        analyzeBtn.disabled = true;

        analyzeText.textContent =
            "Analyzing...";

        loadingSpinner.style.display =
            "inline-block";


        try {

            // Create form data

            const formData =
                new FormData();

            formData.append(
                "image",
                selectedFile
            );


            // Send image to Flask backend

            const response =
                await fetch(
                    "/predict",
                    {
                        method: "POST",
                        body: formData
                    }
                );


            const data =
                await response.json();


            // Handle backend error

            if (!response.ok || !data.success) {

                throw new Error(
                    data.error ||
                    "Unable to analyze image."
                );

            }


            // Display results

            displayResults(data);


            // Add to history

            addToHistory(data);


        }

        catch (error) {

            console.error(error);

            alert(
                "Analysis failed: " +
                error.message
            );

        }

        finally {

            analyzeBtn.disabled = false;

            analyzeText.textContent =
                "Analyze Image";

            loadingSpinner.style.display =
                "none";

        }

    }
);


// -----------------------------------------------------
// Display AI Results
// -----------------------------------------------------

function displayResults(data) {

    // Main prediction

    prediction.textContent =
        data.prediction;


    // Confidence

    confidence.textContent =
        `${data.confidence}%`;


    // Confidence progress bar

    confidenceFill.style.width =
        `${data.confidence}%`;


    // Confidence status

    confidenceStatus.textContent =
        data.confidence_level;


    // Processing time

    processingTime.textContent =
        `${data.processing_time}s`;


    // Display top predictions

    predictionsList.innerHTML = "";


    data.predictions.forEach(
        function (item, index) {

            const predictionItem =
                document.createElement("div");

            predictionItem.className =
                "prediction-item";


            predictionItem.innerHTML = `

                <div class="prediction-top">

                    <span class="prediction-name">
                        ${index + 1}. ${item.label}
                    </span>

                    <span class="prediction-percent">
                        ${item.confidence}%
                    </span>

                </div>

                <div class="prediction-progress">

                    <div
                        class="prediction-progress-fill"
                        style="width: ${item.confidence}%"
                    ></div>

                </div>

            `;


            predictionsList.appendChild(
                predictionItem
            );

        }
    );

}


// -----------------------------------------------------
// Prediction History
// -----------------------------------------------------

function addToHistory(data) {

    predictionHistory.push({

        prediction:
            data.prediction,

        confidence:
            data.confidence,

        processingTime:
            data.processing_time

    });


    renderHistory();

}


// -----------------------------------------------------
// Render History Table
// -----------------------------------------------------

function renderHistory() {

    historyBody.innerHTML = "";


    predictionHistory.forEach(
        function (item, index) {

            const row =
                document.createElement("tr");


            row.innerHTML = `

                <td>
                    ${index + 1}
                </td>

                <td>
                    ${item.prediction}
                </td>

                <td>
                    ${item.confidence}%
                </td>

                <td>
                    ${item.processingTime}s
                </td>

            `;


            historyBody.appendChild(row);

        }
    );


    // Show history section

    if (predictionHistory.length > 0) {

        historySection.style.display =
            "block";

    }

}


// -----------------------------------------------------
// Clear History
// -----------------------------------------------------

clearHistoryBtn.addEventListener(
    "click",
    function () {

        predictionHistory = [];

        historyBody.innerHTML = "";

        historySection.style.display =
            "none";

    }
);