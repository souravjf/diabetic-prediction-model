import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('SVC_model.sav', 'rb'))

# creating a function for Prediction
def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction[0]

def main():
    st.title('Diabetes Prediction Web App')

    # User input sliders
    Pregnancies = st.slider('Number of Pregnancies', 0, 20, 0)
    Glucose = st.slider('Glucose Level', 0, 200, 120)
    BloodPressure = st.slider('Blood Pressure value', 0, 150, 70)
    SkinThickness = st.slider('Skin Thickness value', 0, 100, 20)
    Insulin = st.slider('Insulin Level', 0, 900, 30)
    BMI = st.slider('BMI value', 0.0, 70.0, 25.0)
    DiabetesPedigreeFunction = st.slider('Diabetes Pedigree Function value', 0.0, 2.5, 0.5)
    Age = st.slider('Age of the Person', 1, 120, 25)

    # Code for Prediction
    if st.button('Diabetes Test Result'):
        result = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        if result == 0:
            # Display result in a popup style info box
            st.info("The person is not diabetic.")
            st.markdown("""
            ### Health Tips:
            - Maintain a balanced diet rich in whole grains, vegetables, and lean protein.
            - Exercise regularly – aim for at least 30 minutes of moderate activity most days.
            - Keep a healthy weight; even small weight losses can improve insulin sensitivity.
            - Avoid smoking and limit alcohol consumption.
            """)
        else:
            # Display result in a popup style warning box
            st.warning("The person is diabetic.")
            st.markdown("""
            ### Tips for Managing Diabetes:
            - **Monitor blood sugar**: Keep track of blood glucose levels regularly.
            - **Healthy Eating**: Focus on low-carb, high-fiber foods. Avoid sugary drinks and processed snacks.
            - **Regular Exercise**: Physical activity helps control blood sugar and maintain a healthy weight.
            - **Stress Management**: Practice relaxation techniques like meditation or yoga.
            - **Medication Adherence**: Take medications as prescribed by your healthcare provider.
            - **Routine Health Checks**: Schedule regular appointments for blood pressure, cholesterol, and eye exams.
            """)

if __name__ == '__main__':
    main()

    
    












# import numpy as np
# import pickle
# import streamlit as st


# # loading the saved model
# loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# # creating a function for Prediction

# def diabetes_prediction(input_data):
    

#     # changing the input_data to numpy array
#     input_data_as_numpy_array = np.asarray(input_data)

#     # reshape the array as we are predicting for one instance
#     input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

#     prediction = loaded_model.predict(input_data_reshaped)
#     print(prediction)

#     if (prediction[0] == 0):
#       return 'The person is not diabetic'
#     else:
#       return 'The person is diabetic'
  
    
  
# def main():
    
    
#     # giving a title
#     st.title('Diabetes Prediction Web App')
    
    
#     # getting the input data from the user
#     Pregnancies = st.text_input('Number of Pregnancies')
#     Glucose = st.text_input('Glucose Level')
#     BloodPressure = st.text_input('Blood Pressure value')
#     SkinThickness = st.text_input('Skin Thickness value')
#     Insulin = st.text_input('Insulin Level')
#     BMI = st.text_input('BMI value')
#     DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
#     Age = st.text_input('Age of the Person')
    
    
#     # code for Prediction
#     diagnosis = ''
    
#     # creating a button for Prediction
    
#     if st.button('Diabetes Test Result'):
#         diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
#     st.success(diagnosis)
    
    
    
    
    
# if __name__ == '__main__':
#     main()
    
    
    
    
    
    
  
    