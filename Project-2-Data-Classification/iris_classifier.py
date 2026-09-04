import pandas as pd
import streamlit as st

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Abeeha's Bloom AI",
    page_icon="🌸",
    layout="centered"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

div.stButton > button {
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 18px;
    font-weight: bold;
    width: 100%;
}

div.stButton > button:hover {
    background-color: #218838;
    color: white;
    border: none;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATASET
# ============================================================

iris = load_iris()

X = iris.data
y = iris.target


# Create DataFrame for displaying dataset information
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["Species"] = [
    iris.target_names[i]
    for i in iris.target
]


# ============================================================
# SPLIT DATA INTO TRAINING AND TESTING
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ============================================================
# FEATURE SCALING
# ============================================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)


# ============================================================
# CREATE AND TRAIN KNN MODEL
# ============================================================

knn = KNeighborsClassifier(
    n_neighbors=3
)

knn.fit(
    X_train_scaled,
    y_train
)


# ============================================================
# TEST MODEL
# ============================================================

y_pred = knn.predict(X_test_scaled)

accuracy = accuracy_score(
    y_test,
    y_pred
)


# ============================================================
# UI HEADER
# ============================================================

st.title("🌸 Abeeha's Bloom AI")

st.write(
    "Welcome to Abeeha's Bloom AI! 🌷"
)

st.write(
    "Enter the measurements of an Iris flower below "
    "and let the AI predict its species using "
    "a K-Nearest Neighbors (KNN) model."
)

st.divider()


# ============================================================
# MODEL INFORMATION
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Dataset Samples",
        "150"
    )

with col2:
    st.metric(
        "Training Samples",
        "120"
    )

with col3:
    st.metric(
        "Model Accuracy",
        f"{accuracy * 100:.2f}%"
    )


st.divider()


# ============================================================
# FLOWER MEASUREMENTS
# ============================================================

st.subheader("🌿 Enter Flower Measurements")

st.write(
    "Enter the measurements in centimeters:"
)

col1, col2 = st.columns(2)


with col1:

    sepal_length = st.number_input(
        "Sepal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=5.1,
        step=0.1
    )

    petal_length = st.number_input(
        "Petal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=1.4,
        step=0.1
    )


with col2:

    sepal_width = st.number_input(
        "Sepal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=3.5,
        step=0.1
    )

    petal_width = st.number_input(
        "Petal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=0.2,
        step=0.1
    )


st.write("")


# ============================================================
# PREDICTION
# ============================================================

if st.button(
    "🌿 Predict Flower",
    use_container_width=True
):

    user_data = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]


    # Scale user input
    user_data_scaled = scaler.transform(
        user_data
    )


    # Make prediction
    prediction = knn.predict(
        user_data_scaled
    )


    # Get probability of each class
    probabilities = knn.predict_proba(
        user_data_scaled
    )


    # Convert prediction number into flower name
    flower_name = iris.target_names[
        prediction[0]
    ]


    # Get prediction confidence
    confidence = (
        probabilities[0][prediction[0]]
        * 100
    )


    # Display result
    st.success(
        f"🌸 Predicted Flower: {flower_name.title()}"
    )


    st.info(
        f"🤖 Model Confidence: {confidence:.2f}%"
    )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.divider()

st.subheader("📊 Model Performance")

st.write(
    "The model was trained using 80% of the dataset "
    "and evaluated using the remaining 20%."
)

st.metric(
    "Test Accuracy",
    f"{accuracy * 100:.2f}%"
)


# ============================================================
# ABOUT THE MODEL
# ============================================================

st.divider()

st.subheader("🧠 About Abeeha's Bloom AI")

st.write(
    "Abeeha's Bloom AI uses the "
    "K-Nearest Neighbors (KNN) supervised learning "
    "algorithm to classify Iris flowers."
)

st.write(
    "The model identifies three Iris species:"
)

st.write(
    "🌸 Iris Setosa  |  🌸 Iris Versicolor  |  🌸 Iris Virginica"
)


# ============================================================
# DATASET INFORMATION
# ============================================================

with st.expander("📋 View Dataset Information"):

    st.write(
        "The Iris dataset contains 150 flower samples "
        "with four measurements for each flower."
    )

    st.write("Features:")

    st.write(
        "• Sepal Length\n"
        "• Sepal Width\n"
        "• Petal Length\n"
        "• Petal Width"
    )

    st.dataframe(
        df.head(10),
        use_container_width=True
    )


# ============================================================
# HOW KNN WORKS
# ============================================================

with st.expander("🔍 How Does KNN Work?"):

    st.write(
        "K-Nearest Neighbors (KNN) classifies a new flower "
        "by looking at the most similar flowers in the "
        "training data."
    )

    st.write(
        "This project uses K = 3, meaning the model looks "
        "at the three nearest examples and uses their "
        "majority class to make the prediction."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🌸 Abeeha's Bloom AI | Built with Python, "
    "Scikit-learn & Streamlit"
)