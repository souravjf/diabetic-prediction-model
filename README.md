🩺 Diabetes Prediction Web App

This repository contains a machine learning-powered web application built using Streamlit. The app predicts whether a person is diabetic based on health parameters such as glucose level, BMI, blood pressure, and more.

The prediction model is powered by a Support Vector Classifier (SVC) trained on medical data and stored as SVC_model.sav.

🚀 Features

Interactive Streamlit UI for user-friendly predictions

Inputs via sliders for easy parameter selection

Real-time diabetes prediction using a pre-trained ML model

Provides health tips for both diabetic and non-diabetic results

📂 Project Structure
├── app.py              # Main Streamlit web application  
├── SVC_model.sav       # Pre-trained Support Vector Classifier model  
└── README.md           # Project documentation  

⚙️ Installation & Setup

Clone the repository:

git clone https://github.com/your-username/diabetes-prediction-app.git
cd diabetes-prediction-app


Create and activate a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # On Mac/Linux  
venv\Scripts\activate      # On Windows


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

📊 Input Parameters

The model uses the following health features for prediction:

Pregnancies: Number of pregnancies

Glucose: Plasma glucose concentration

BloodPressure: Diastolic blood pressure (mm Hg)

SkinThickness: Triceps skin fold thickness (mm)

Insulin: 2-Hour serum insulin (mu U/ml)

BMI: Body mass index (weight in kg/(height in m)^2)

DiabetesPedigreeFunction: Diabetes pedigree function (genetic risk)

Age: Age in years

🖼️ Example Output

If not diabetic → Shows health maintenance tips

If diabetic → Provides diabetes management advice

🛠️ Tech Stack

Python

Streamlit (for web app)

NumPy (for data handling)

Pickle (for model loading)

Scikit-learn (for SVC model training – already trained)

🙌 Contribution

Pull requests are welcome! Feel free to fork this repo, improve the code, and submit a PR.

📜 License

This project is licensed under the MIT License.
