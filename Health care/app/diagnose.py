try:
    import streamlit as st
    import datetime
    import pickle
    from PIL import Image
    import numpy as np
    import cv2
    import keras
    import os
except Exception as e:
    st.error(f"Library not installed. Please check the error details: {e}")

def display_diagnose():
    st.header(":red[Diagnoser page]")
    st.write("Welcome to the Diagnoser page!")
    

    # Cardiovascular Diseases (CVDs)
    def Cardiology():
        # Frontend layout
        st.subheader("Cardiovascular Diseases (CVDs) Diagnoser")

        col1, col2 =st.columns(2)

        with col1:
            dob = st.date_input("Enter your date of birth", min_value=datetime.date(1974, 1, 1), max_value=datetime.date.today())

            today = datetime.date.today()
            age_days = (today - dob).days
            age_years = age_days // 365
            st.write(f"Your age is: {age_years} years ({age_days} days)")

            weight = st.number_input("Enter your weight (kg)", min_value=0.0, value=62.0, step=0.1)
            systolic_blood_pressure = st.slider("Systolic Blood Pressure (mm Hg)", min_value=0, max_value=200, value=120)
            diastolic_blood_pressure = st.slider("Diastolic Blood Pressure (mm Hg)", min_value=0, max_value=200, value=80)

        with col2:
            cholesterol = st.selectbox("Cholesterol level", [1, 2, 3], format_func=lambda x: ["Normal", "Above normal", "Well above normal"][x-1])
            glucose = st.selectbox("Glucose level", [1, 2, 3], format_func=lambda x: ["Normal", "Above normal", "Well above normal"][x-1])
            smoking = st.selectbox("Smoking habit", [0, 1], format_func=lambda x: ["No", "Yes"][x])
            alcohol_intake = st.selectbox("Alcohol intake", [0, 1], format_func=lambda x: ["No", "Yes"][x])
            physical_activity = st.selectbox("Physical activity", [0, 1], format_func=lambda x: ["No", "Yes"][x])

        # Predict button
        if st.button('**Predict**',use_container_width=True, key="Cardiovascular Diseases (CVDs) Diagnoser "):

            # Backend processing
            # Load the scaler and model (update with your correct file paths)
            model_folder = r'./Model/'  # Use relative or absolute path to the Model folder

            try: 
                # Load the scaler
                with open(f'{model_folder}Heart_scaler.pkl', 'rb') as Heart_scaler_file:
                    Heart_scaler = pickle.load(Heart_scaler_file)
            except Exception as e:
                st.error(f"Error loading the scaler: {e}")
                st.text("Please make sure the scaler file are available with this name(Heart_scaler.pkl) .")
                st.stop()  # Stop the app execution

            try:
                # Load the Decision Tree Classifier model
                with open(f'{model_folder}Heart_dtc_model.pkl', 'rb') as Heart_model_file:
                    Heart_model_dtc = pickle.load(Heart_model_file)
            except Exception as e:
                st.error(f"Error loading the model: {e}")
                st.text("Please make sure the model file are available with this name(Heart_dtc_model.pkl) .")
                st.stop()  # Stop the app execution

            input_data = [[age_days, weight, systolic_blood_pressure, diastolic_blood_pressure, cholesterol, glucose, smoking, alcohol_intake, physical_activity]]

            # Scale the input data
            try:
                input_scaled = Heart_scaler.transform(input_data)
            except Exception as e:
                st.error(f"Error in Scaling input data.{e}")
                st.stop()

            # Make prediction
            try:
                prediction = Heart_model_dtc.predict(input_scaled)
            except Exception as e:
                st.error(f"Error loading model. Please check if the model is installed. {e}")
                st.stop() 

            # Display result
            if prediction[0] == 1:
                st.error("The patient is likely **Affected by Cardiovascular Disease**. Please consult a healthcare provider😔.")
            else:
                st.success("The patient is likely **Not Affected by Cardiovascular Disease**. Consult a doctor for further advice 😊.")


    # Diabetes
    def Diabetology():
        st.subheader("Diabetes Diagnoser")

        # Input fields for user data
        col1, col2 =st.columns(2)

        with col1:
            gender = st.selectbox("Gender", options=[1, 2], format_func=lambda x: "Male" if x == 1 else "Female")
            age = st.slider("Age (Years)", min_value=0, max_value=100, value=30, step=1)
            bmi = st.slider("Body Mass Index (BMI) (kg/m²)", min_value=15.0, max_value=50.0, value=25.0, step=0.1)

        with col2:
            hba1c_level = st.slider("HbA1c Level (%)", min_value=1.0, max_value=15.0, value=5.0, step=0.1)
            blood_glucose_level = st.slider("Blood Glucose Level (mg/dL)", min_value=50.0, max_value=400.0, value=100.0, step=1.0)
        
        # Backend processing
        if st.button('**Predict**',use_container_width=True, key="Diabetes Diagnoser"):
            # Load the scaler and model (update with your correct file paths)
            model_folder = r'./Model/'  # Use relative or absolute path to the Model folder

            try:
                # Load the scaler file 
                with open(f'{model_folder}Diabetes_scaler.pkl', 'rb') as Diabetes_scaler_file:
                    Diabetes_scaler = pickle.load(Diabetes_scaler_file)
            except Exception as e:
                st.error(f"Error loading the scaler: {e}")
                st.text("Please make sure the scaler file are available with this name(Diabetes_scaler.pkl) .")
                st.stop()  # Stop the app execution
            
            try:
                # Load the model file
                with open(f'{model_folder}Diabetes_catboost_model.pkl', 'rb') as Diabetes_catboost_model_file:
                    Diabetes_catboost_model = pickle.load(Diabetes_catboost_model_file)
            except Exception as e:
                st.error(f"Error loading the model: {e}")
                st.text("Please make sure the model file are available with this names(Diabetes_catboost_model.pkl) .")
                st.stop()  # Stop the app execution
            
            input_data = [[gender, age, bmi, hba1c_level, blood_glucose_level]]

            # Scale the input data
            try:
                input_data_scaled = Diabetes_scaler.transform(input_data)
            except Exception as e:
                st.error(f"Error in Scaling input data.{e}")
                st.stop()

            # Make prediction
            try:
                prediction = Diabetes_catboost_model.predict(input_data_scaled)
            except Exception as e:
                st.error(f"Error loading model. Please check if the model is installed. {e}")
                st.stop() 

            # Display the result with a medical explanation
            if prediction[0] == 1:
                st.error("The patient is likely **Affected by Diabetes Mellitus**. Please consult a healthcare provider😔.")
            else:
                st.success("The patient is likely **Not Affected by Diabetes Mellitus**. Consult a doctor for further advice 😊.")


    # Liver Condition Diagnoser
    def Hepatology():
        st.subheader("Liver Condition Diagnoser")

        # Input fields for liver metrics
        col1, col2 =st.columns(2)

        with col1:
            Total_Bilirubin = st.slider("Total Bilirubin (mg/dL)", 0.0, 6.0, step=0.01)
            Direct_Bilirubin = st.slider("Direct Bilirubin (mg/dL)", 0.0, 2.0, step=0.01)
            Alkphos_Alkaline_Phosphotase = st.slider("Alkaline Phosphatase (U/L)", 0, 500, step=1)
            Sgpt_Alamine_Aminotransferase = st.slider("Alamine Aminotransferase (U/L)", 0, 100, step=1)

        with col2:
            Sgot_Aspartate_Aminotransferase = st.slider("Aspartate Aminotransferase (U/L)", 0, 80, step=1)
            Total_Protiens = st.slider("Total Proteins (g/dL)", 0.0, 10.0, step=0.01)
            ALB_Albumin = st.slider("Albumin (g/dL)", 0.0, 10.0, step=0.01)
            AG_Ratio_Albumin_Globulin_Ratio = st.slider("Albumin/Globulin Ratio", 0.0, 5.0, step=0.01)

        # Backend processing
        if st.button('**Diagnose**', use_container_width=True, key="Liver Condition Diagnoser"):
            # Load the scaler and model (update with your correct file paths)
            model_folder = r'./Model/'  # Use relative or absolute path to the Model folder

            # Load scaler and model files
            try:
                with open(f'{model_folder}Hepatology_scaler.pkl', 'rb') as Hepatology_scaler_file:
                    Hepatology_scaler = pickle.load(Hepatology_scaler_file)
            except Exception as e:
                st.error(f"Error loading the scaler. Please ensure 'Hepatology_scaler.pkl' is available.{e}")
                st.stop()

            try:
                with open(f'{model_folder}Hepatology_rfc_model.pkl', 'rb') as Hepatology_rfc_model_file:
                    Hepatology_rfc_model = pickle.load(Hepatology_rfc_model_file)
            except Exception as e:
                st.error(f"Error loading the model. Please ensure 'Hepatology_rfc_model.pkl' is available.{e}")
                st.stop()

            # Collect input into an array
            input_data = [[Total_Bilirubin, Direct_Bilirubin, Alkphos_Alkaline_Phosphotase, Sgpt_Alamine_Aminotransferase, 
                Sgot_Aspartate_Aminotransferase, Total_Protiens, ALB_Albumin, AG_Ratio_Albumin_Globulin_Ratio]]

            # Scale the input data
            try:
                input_scaled = Hepatology_scaler.transform(input_data)
            except Exception as e:
                st.error(f"Error in Scaling input data.{e}")
                st.stop()

            # Make prediction
            try:
                y_pred = Hepatology_rfc_model.predict(input_scaled)
            except Exception as e:
                st.error(f"Error loading model. Please check if the model is installed. {e}")
                st.stop() 
        
            # Display results
            if y_pred[0] == 1:
                st.warning("The patient is likely **Affected by a Liver Disease**. Immediate consultation with a healthcare provider is advised. 😔")
            else:
                st.success("The patient is likely **Not Affected by a Liver Disease**. However, regular check-ups are recommended. 😊")


    # HIV/AIDS
    def HIV_AIDS():
        st.subheader("HIV/AIDS Diagnoser")

        col1, col2 =st.columns(2)
        with col1:
            # Age input
            age = st.slider("Age (years)", 0, 80, step=1)

            # HIV Test in Past Year input
            hiv_test_in_past_year = st.selectbox("HIV Test In Past Year", options=["Yes", "No"])
            hiv_test_past_year_map = {'No': 1, 'Yes': 2}
            hiv_test_in_past_year = hiv_test_past_year_map[hiv_test_in_past_year]

            # AIDS Education input
            aids_education = st.selectbox("AIDS Education", options=["Yes", "No"])
            aids_education_map = {'No': 1, 'Yes': 2}
            aids_education = aids_education_map[aids_education]

        with col2:
            # Places of Seeking Sex Partners input
            places_of_seeking_sex_partners = st.selectbox("Places of Seeking Sex Partners", options=["Internet", "Bar", "Public Bath", "Park", "Others"])
            places_seeking_partners_map = {'Internet': 1, 'Bar': 2, 'Public Bath': 3, 'Park': 4, 'Others': 5}
            places_of_seeking_sex_partners = places_seeking_partners_map[places_of_seeking_sex_partners]

            # Drug Taking input
            drug_taking = st.selectbox("Drug Taking", options=["Yes", "No"])
            drug_taking_map = {'No': 1, 'Yes': 2}
            drug_taking = drug_taking_map[drug_taking]

        # Diagnosis button
        if st.button('**Diagnose**', use_container_width=True, key="HIV/AIDS Diagnoser"):
            # Backend processing

            # Load the scaler and model (update with your correct file paths)
            model_folder = r'./Model/'  # Use relative or absolute path to the Model folder

            # Load scaler and model
            try:
                with open(f'{model_folder}HIV_AIDS_scaler.pkl', 'rb') as HIV_AIDS_scaler_file:
                    HIV_AIDS_scaler = pickle.load(HIV_AIDS_scaler_file)
            except Exception as e:
                st.error(f"Error loading the scaler file. Please ensure it's named 'HIV_AIDS_scaler.pkl'.{e}")
                st.stop()

            try:
                with open(f'{model_folder}HIV_AIDS_lgbm_model.pkl', 'rb') as HIV_AIDS_lgbm_model_file:
                    HIV_AIDS_model = pickle.load(HIV_AIDS_lgbm_model_file)
            except Exception as e:
                st.error(f"Error loading the model file. Please ensure it's named 'HIV_AIDS_lgbm_model.pkl'.{e}")
                st.stop()

            input_parameters = [[age, hiv_test_in_past_year, aids_education, places_of_seeking_sex_partners, drug_taking]]

            # Scale the input data
            try:
                input_scaled = HIV_AIDS_scaler.transform(input_parameters)
            except Exception as e:
                st.error(f"Error in Scaling input data.{e}")
                st.stop()

            # Make prediction
            try:
                prediction = HIV_AIDS_model.predict(input_scaled)
            except Exception as e:
                st.error(f"Error loading model. Please check if the model is installed. {e}")
                st.stop() 

            # Display the prediction result
            if prediction[0] == 1:
                st.warning("The patient is likely **Affected by HIV/AIDS**. Immediate consultation with a healthcare provider is advised.😔")
            else:
                st.success("The patient is likely **Not Affected by HIV/AIDS**. Regular testing and preventive measures are recommended.😊")

    
    # Chronic Kidney Disease (CKD)
    def Nephrology():
        st.subheader("Kidney Disease Diagnoser")

        # Input features in two columns
        col1, col2 = st.columns(2)

        with col1:
            SG = st.selectbox("Specific Gravity (SG)", options=[1.005, 1.010, 1.015, 1.020, 1.025])
            AL = st.selectbox("Albumin (AL)", options=[0, 1, 2, 3, 4, 5])
            BGR = st.slider("Blood Glucose Random (BGR) (mg/dL)", min_value=0, max_value=300, step=1)
            SC = st.slider("Serum Creatinine (SC) (mg/dL)", min_value=0.0, max_value=6.0, step=0.01)
            SOD = st.slider("Sodium (SOD) (mEq/L)", min_value=100, max_value=200, step=1)

        with col2:
            HEMO = st.slider("Hemoglobin (HEMO) (g/dL)", min_value=0.0, max_value=25.0, step=0.1)
            PCV = st.slider("Packed Cell Volume (PCV)", min_value=0, max_value=60, step=1)
            RBCC = st.slider("Red Blood Cell Count (RBCC) (millions/cmm)", min_value=0.0, max_value=10.0, step=0.1)
            HTN = st.selectbox("Hypertension (HTN)", options=["No", "Yes"])
            DM = st.selectbox("Diabetes Mellitus (DM)", options=["No", "Yes"])

        # Map binary inputs
        HTN_map = {'No': 0, 'Yes': 1}
        DM_map = {'No': 0, 'Yes': 1}
        HTN = HTN_map[HTN]
        DM = DM_map[DM]

        # Diagnosis button
        if st.button('**Diagnose**', use_container_width=True, key="Kidney Disease Diagnoser"):

            # Load the scaler and model (update with your correct file paths)
            model_folder = r'./Model/'  # Use relative or absolute path to the Model folder

            # Load scaler and model
            try:
                with open(f'{model_folder}Nephrology_scaler.pkl', 'rb') as Nephrology_scaler_file:
                    Nephrology_scaler = pickle.load(Nephrology_scaler_file)
            except Exception as e:
                st.error(f"Error loading the scaler file. Please ensure it's named 'Nephrology_scaler.pkl'.{e}")
                st.stop()

            try:
                with open(f'{model_folder}Nephrology_svm_model.pkl', 'rb') as Nephrology_svm_model_file:
                    Nephrology_svm_model = pickle.load(Nephrology_svm_model_file)
            except Exception as e:
                st.error(f"Error loading the model file. Please ensure it's named 'HIV_AIDS_svm_model.pkl'.{e}")
                st.stop()

            input_data = [[SG, AL, BGR, SC, SOD, HEMO, PCV, RBCC, HTN, DM]]

            # Scale the input data
            try:
                input_scaled = Nephrology_scaler.transform(input_data)
            except Exception as e:
                st.error(f"Error in Scaling input data.{e}")
                st.stop()

            # Make prediction
            try:
                prediction = Nephrology_svm_model.predict(input_scaled)
            except Exception as e:
                st.error(f"Error loading model. Please check if the model is installed. {e}")
                st.stop() 

            # Display prediction
            if prediction[0] == 1:
                st.warning("The patient is likely **Affected by a Kidney Disease**. Immediate consultation with a nephrologist is advised. 😔")
            else:
                st.success("The patient is likely **Not Affected by a Kidney Disease**. Regular check-ups are recommended. 😊")


    # Cancer
    def Oncology():
        st.subheader("Cancer Disorder")

        col1, col2 = st.columns(2)

        with col1:
            Age = st.slider("Age (years)", min_value=0, max_value=100, step=1)
            TimeRecurrence = st.slider("Time Since Recurrence (months)", min_value=0.0, max_value=20.0, step=0.1)
            Diam = st.slider("Tumor Diameter (mm)", min_value=0.0, max_value=100.0, step=0.1)
            PosNodes = st.slider("Positive Lymph Nodes Count", min_value=0, max_value=20, step=1)
            ESR1 = st.slider("ESR1 Gene Expression Level", min_value=-2.0, max_value=2.0, step=0.1)

        with col2:
            Chemo = st.selectbox("Chemotherapy", options=["No", "Yes"])
            Hormonal = st.selectbox("Hormonal Therapy", options=["No", "Yes"])
            Amputation = st.selectbox("Amputation", options=["No", "Yes"])
            HistType = st.selectbox("Histological Type", options=[1, 2, 3, 4, 5, 6, 7])
            Grade = st.selectbox("Tumor Grade", options=[ 'Low', 'Moderate', 'High'])
            AngioInv = st.selectbox("Angioinvasion", options=["Absent", "Present", "Extensive"])
            LymphInfil = st.selectbox("Lymphatic Infiltration", options=["None", "Mild", "Severe"])

        # Mapping binary and categorical inputs
        Chemo_map = {"No": 0, "Yes": 1}
        Hormonal_map = {"No": 0, "Yes": 1}
        Amputation_map = {"No": 0, "Yes": 1}
        Grade_map = {"Low": 1, "Moderate": 2, "High": 3}
        AngioInv_map = {"Absent": 1, "Present": 2, "Extensive": 3}
        LymphInfil_map = {"None": 1, "Mild": 2, "Severe": 3}

        Chemo = Chemo_map[Chemo]
        Hormonal = Hormonal_map[Hormonal]
        Amputation = Amputation_map[Amputation]
        Grade = Grade_map[Grade]
        AngioInv = AngioInv_map[AngioInv]
        LymphInfil = LymphInfil_map[LymphInfil]

        # Diagnosis button
        if st.button('**Diagnose**', use_container_width=True, key="Cancer Disorders"):

            # Load the scaler and model (update with your correct file paths)
            model_folder = r'./Model/'  # Use relative or absolute path to the Model folder

            # Load scaler and model
            try:
                with open(f'{model_folder}Cancer_scaler.pkl', 'rb') as Cancer_scaler_file:
                    Cancer_scaler = pickle.load(Cancer_scaler_file)
            except Exception as e:
                st.error(f"Error loading the scaler file. Please ensure it's named 'Cancer_scaler.pkl'.{e}")
                st.stop()

            try:
                with open(f'{model_folder}Cancer_rfc_model.pkl', 'rb') as Cancer_rfc_model_file:
                    Cancer_rfc_model = pickle.load(Cancer_rfc_model_file)
            except Exception as e:
                st.error(f"Error loading the model file. Please ensure it's named 'HIV_AIDS_svm_model.pkl'.{e}")
                st.stop()

            # Prepare input data
            input_data = [[Age, TimeRecurrence, Chemo, Hormonal, Amputation, HistType, Diam, PosNodes, Grade, AngioInv, LymphInfil, ESR1]]

            # Scale the input data
            try:
                input_scaled = Cancer_scaler.transform(input_data)
            except Exception as e:
                st.error(f"Error in Scaling input data.{e}")
                st.stop()

            # Make prediction
            try:
                prediction = Cancer_rfc_model.predict(input_scaled)
            except Exception as e:
                st.error(f"Error loading model. Please check if the model is installed. {e}")
                st.stop()         

            # Display prediction
            if prediction[0] == 1:
                st.warning("The prediction indicates a **High Risk of Cancer-Related Mortality**. It is essential to consult with healthcare providers for immediate and intensive care options. 😔")
            else:
                st.success("The prediction indicates a **Low Risk of Cancer-Related Mortality**. Continue with regular monitoring and preventive health practices. 😊")


    # Tuberculosis (TB)
    def Pulmonology():
        st.subheader("Pulmonary Tuberculosis  Disorder (TB)")
        uploaded_file = st.file_uploader("Upload a Chest X-Ray Image", type=["jpg", "jpeg", "png"])

        # Diagnosis Button
        if st.button('**Diagnose**', use_container_width=True, key="Pulmonary Tuberculosis  Disorder (TB)"):
            if uploaded_file is None:
                st.warning("Please upload a valid chest X-ray image.")
            else:
                try:
                    # Load the model (update with your correct file paths)
                    model_folder = r'./Model/'  # Use relative or absolute path to the Model folder
                    model_path = os.path.join(model_folder, 'tb_cnn_model.keras')
                except Exception as e:
                    st.error(f"Error loading model. Ensure the model file is present at '{model_path}'. {e}")
                    st.stop()
                
                # Load pre-trained CNN model
                try:
                    loaded_model = keras.models.load_model(model_path)
                except Exception as e:
                    st.error(f"Error loading model. Ensure the model file is present at'{model_path}'. {e}")
                    st.stop()

                try:
                    # Load and preprocess the image
                    image = Image.open(uploaded_file)
                    # Convert image to grayscale
                    if image.mode != 'L':
                        image = image.convert('L')  # Convert to grayscale

                    # Resize and normalize the image
                    image_size = 256
                    image_array = np.array(image)
                    image_array = cv2.resize(image_array, (image_size, image_size))
                    image_array = image_array.astype('float32') / 255.0
                    image_array = np.expand_dims(image_array, axis=(0, -1))  # Shape (1, 256, 256, 1)

                    col1, col2 = st.columns(2)

                    with col1:
                        # Display the uploaded image
                        st.image(image, caption="Uploaded image", use_column_width=True, clamp=True)

                    with col2:
                        # Display the preprocessed image
                        st.image(image_array, caption="Preprocessed Image", use_column_width=True, clamp=True)
                
                except Exception as e:
                    st.error(f"An error occurred during processing: {e}")

                try:
                    # Make a prediction
                    prediction = loaded_model.predict(image_array)
                    predicted_label = (prediction > 0.5).astype(int)[0, 0]
                except Exception as e:
                    st.error(f"Error loading model. Please check if the model is installed. {e}")
                    st.stop()

                # Display the result
                if predicted_label == 0:
                    st.success("The result indicates the patient is **Normal.** No immediate action is required, but maintaining regular health check-ups is advised. 😊")
                else:
                    st.error("The result indicates the patient is **Affected by Pulmonary Tuberculosis Disorder (TB).** Immediate medical intervention is strongly recommended. 😔")



    # Tabs for each specialty
    tab1, tab2, tab3, tab4, tab5, tab6, tab7= st.tabs(["Cardiology", "Diabetology", "Hepatology (Liver)", "HIV/AIDS", "Nephrology (Kidney)",  
                                                                    "Oncology (Cancer)", "Pulmonology (TB)"])

    # Display content for each tab
    with tab1:
        Cardiology()

    with tab2:
        Diabetology()

    with tab3:
        Hepatology()
        
    with tab4:
        HIV_AIDS()
        
    with tab5:
        Nephrology()
        
    with tab6:
        Oncology()

    with tab7:
        Pulmonology()


# Call the display function to show the Diagnose
if __name__ == "__main__":
    display_diagnose()