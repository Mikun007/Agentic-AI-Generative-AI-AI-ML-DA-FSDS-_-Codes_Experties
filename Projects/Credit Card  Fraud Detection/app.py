import streamlit as st
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.metrics import classification_report, confusion_matrix

# -----------------------------
# Config
# -----------------------------
MODEL_NAME = "CreditCardFraudModel_XGB_SMOTE"
THRESHOLD = 0.96

mlflow.set_tracking_uri("http://localhost:5000")

# -----------------------------
# Load model
# -----------------------------
@st.cache_resource
def load_model():
    model_uri = f"models:/{MODEL_NAME}@challenger"
    return mlflow.sklearn.load_model(model_uri)

model = load_model()

# -----------------------------
# UI
# -----------------------------
st.title("💳 Credit Card Fraud Detection")
st.write("Upload a CSV file and compare predictions with actual labels.")

uploaded_file = st.file_uploader("Upload transaction CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📥 Uploaded Data Preview")
    st.dataframe(df.head())

    # -----------------------------
    # Separate target if exists
    # -----------------------------
    if "Class" in df.columns:
        y_true = df["Class"]
        X = df.drop(columns=["Class"])
        st.info("✔ `Class` column detected and removed before prediction.")
    else:
        y_true = None
        X = df
        st.warning("⚠ No `Class` column found. Comparison will be skipped.")

    if st.button("🔍 Predict"):
        probs = model.predict_proba(X)[:, 1]
        preds = (probs >= THRESHOLD).astype(int)

        df["fraud_probability"] = probs
        df["fraud_prediction"] = preds

        # -----------------------------
        # Results
        # -----------------------------
        st.subheader("📊 Prediction Results")
        st.dataframe(df)

        st.metric(
            "🚨 Fraud Transactions Detected",
            int(df["fraud_prediction"].sum())
        )

        # -----------------------------
        # Evaluation (if Class exists)
        # -----------------------------
        if y_true is not None:
            st.subheader("📈 Model Performance")

            cm = confusion_matrix(y_true, preds)
            report = classification_report(y_true, preds, output_dict=True)

            st.write("### Confusion Matrix")
            st.dataframe(
                pd.DataFrame(
                    cm,
                    index=["Actual Legit", "Actual Fraud"],
                    columns=["Predicted Legit", "Predicted Fraud"]
                )
            )

            st.write("### Classification Report")
            st.dataframe(pd.DataFrame(report).transpose())
