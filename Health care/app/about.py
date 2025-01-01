import streamlit as st
from PIL import Image


def display_about():
    st.header(":red[About the App] ")

    # Add your About page content here
    st.subheader(":blue[AI Healthcare Assistant]")
    st.markdown('''In today’s fast-paced medical environment, access to timely, accurate, 
                and personalized healthcare insights is crucial for improving patient outcomes. 
                That’s where our AI Healthcare Assistant steps in as your intelligent partner, 
                designed to assist healthcare professionals with a wide range of tasks.''')
    
    st.subheader(":blue[Why Choose AI Healthcare Assistant?]")
    st.markdown('''This AI-powered assistant is designed with healthcare professionals in mind, 
                offering an all-in-one tool for enhancing diagnostic accuracy, improving workflow efficiency, 
                and enabling data-driven decision-making. Whether you’re diagnosing complex cases or performing routine analysis, 
                our assistant offers valuable support, freeing up your time to focus on what matters most—your patients.''')
    
    # Open an image file using PIL
    background_image = Image.open("Image/About_background.jpg")
    # Display the image
    st.image(background_image, use_column_width=True)


    st.header(":red[Specification Details]")

    st.header(":red[AI Chatbot]")
    st.markdown('''
**Model Name:** Meta Llama 3.1 8B Instruct  
**Model Size:** 4.92 GB  
**Parameters:** 8 Billion  
**Number of Layers:** 36  
**Context Length:** 4096 tokens  
**Architecture Type:** Transformer-based LLM  
**Training Data:** Biomedical and General Domain Texts  
**Fine-tuning:** Instruction-tuned for healthcare tasks  
**Use Case:** Healthcare chatbot, symptom analysis, medical Q&A  
**Language:** English (Medical Terminology Support)  
**Deployment:** Locally hosted on your machine  
''')

    st.header(":red[Report Analyzer]")
    st.subheader(":blue[Retrieval - Augmented Generation Application]")
    st.markdown('''
    This app leverages advanced Retrieval-Augmented Generation (RAG) technology, combining the power of real-time information retrieval and generative AI to enhance decision-making processes for healthcare professionals. Designed to assist in both complex and routine medical cases, this RAG app provides accurate, context-rich insights that support diagnostic accuracy, streamline workflows, and promote data-driven decisions, ultimately allowing professionals to focus more on patient care.
    ''')

    st.subheader(":blue[Why Choose Retrieval - Augmented Generation Application?]")
    st.markdown('''
    1. **Enhanced Accuracy:** By dynamically pulling from vast, up-to-date medical databases, this app provides relevant information tailored to each clinical scenario.
    2. **Efficiency & Workflow Support:** With rapid access to relevant content and insights, healthcare professionals save valuable time, focusing on care rather than on research or manual data searches.
    3. **Data-Driven Decision Making:** The RAG app enables professionals to make informed decisions, offering references and insights drawn from reliable sources, thereby enhancing confidence in diagnostic and treatment decisions.
    4. **Adaptability Across Cases:** From rare cases requiring deep research to routine analyses that can benefit from context reinforcement, this app supports a wide range of clinical needs.
    ''')

    st.subheader(":blue[How It Works]")
    st.markdown(''' 
    The Retrieval-Augmented Generation application operates through a two-step process:

    1. **Retrieval Phase:** When presented with a clinical question or scenario, the app first searches relevant, up-to-date medical databases or knowledge repositories, identifying contextually appropriate data or documents.
    
    2. **Generation Phase:** Leveraging generative AI, the app synthesizes a comprehensive response, weaving the retrieved data into a coherent and insightful narrative that directly addresses the user's query or case. This combination of real-time data retrieval and AI generation allows for the creation of highly relevant, accurate content.

    This seamless integration makes the RAG app a powerful, dynamic tool in modern healthcare, aiding professionals in making better, faster, and more informed decisions.
    ''')
    
    st.header(":red[Diagnoser]")
    st.subheader(":blue[Cardiology Diagnoser]")
    st.markdown('''
**Input Parameters:** 
1. Years (days)
2. Weight (kg)
3. Systolic Blood Pressure (mm Hg)
4. Diastolic Blood Pressure (mm Hg)
5. Cholesterol level (mmol/L)
6. Glucose level (mg/dL)
7. Smoking habit (Yes/No)
8. Alcohol intake (g/day)
9. Physical activity (hours/week)

**Machine Learning Model:** Decision Tree Classification  
**Accuracy Level:** 73.17%
''')
    
    st.subheader(":blue[Diabetology Diagnoser]")
    st.markdown('''
**Input Parameters:**  
1. Gender
2. Age (Years)
3. Body Mass Index (BMI) (kg/m²)
4. HbA1c Level (%)
5. Blood Glucose Level (mg/dL)
                
**Machine Learning Model:** CatBoost  
**Accuracy Level:** 97.80%  
''')
    
    st.subheader(":blue[Hepatology (Liver) Diagnoser]")
    st.markdown('''
**Input Parameters:**  
1. Total Bilirubin (mg/dL)  
2. Direct Bilirubin (mg/dL)  
3. Alkaline Phosphatase (U/L)  
4. Alamine Aminotransferase (U/L)  
5. Aspartate Aminotransferase (U/L)  
6. Total Proteins (g/dL)  
7. Albumin (g/dL)  
8. Albumin/Globulin Ratio  
 
**Machine Learning Model:** Random Forest Classifier  
**Accuracy Level:** 99.94%  
''')
    
    st.subheader(":blue[HIV/AIDS Diagnoser]")
    st.markdown('''
**Input Parameters:**  
1. Age (years)  
2. HIV Test In Past Year (Yes/No)  
3. AIDS Education (Yes/No)  
4. Places of Seeking Sex Partners (Internet/Bar/Public Bath/Park/Others)  
5. Drug Taking (Yes/No)  

**Machine Learning Model:** LGBMClassifier  
**Accuracy Level:** 71.03%  
''')
    
    st.subheader(":blue[Nephrology (Kidney) Diagnoser]")
    st.markdown('''
**Input Parameters:**  
1. Specific Gravity (SG)  
2. Albumin (AL)  
3. Blood Glucose Random (BGR) (mg/dL)  
4. Serum Creatinine (SC) (mg/dL)  
5. Sodium (SOD) (mEq/L)  
6. Hemoglobin (HEMO) (g/dL)  
7. Packed Cell Volume (PCV)  
8. Red Blood Cell Count (RBCC) (millions/cmm)  
9. Hypertension (HTN) (Yes/No)  
10. Diabetes Mellitus (DM) (Yes/No)  
 
**Machine Learning Model:** Support Vector Machine (SVM) Classifier  
**Accuracy Level:** 97.50%  
''')
    
    st.subheader(":blue[Oncology (Cancer) Diagnoser]")
    st.markdown('''
**Input Parameters:**  
1. Age (years)  
2. Time Since Recurrence (months)  
3. Tumor Diameter (mm)  
4. Positive Lymph Nodes Count  
5. ESR1 Gene Expression Level  
6. Chemotherapy (Yes/No)  
7. Hormonal Therapy (Yes/No)  
8. Amputation (Yes/No)  
9. Histological Type (1/2/3/4/5/6/7)  
10. Tumor Grade (Low/Moderate/High)  
11. Angioinvasion (Absent/Present/Extensive)  
12. Lymphatic Infiltration (None/Mild/Severe)  

**Machine Learning Model:** Random Forest  
**Accuracy Level:** 82.80%
''')
    
    st.subheader(":blue[Pulmonology (TB) Diagnoser]")
    st.markdown('''
**Input Parameters:**  X - ray Image report  
**Machine Learning Model:**  CNN  
**Accuracy Level:** 98.82%  
''')
    
    
    with st.sidebar:
        # Title for the section
        st.title("Contact Details")

        # Contact information
        st.write("**Name:** Gopinath, Data Scientist")
        st.write("**Email:** [gopinathaiml12@gmail.com](mailto:gopinathaiml12@gmail.com)")
        st.write("**LinkedIn:** [Gopinath .](https://www.linkedin.com/in/gopinathaiml12/)")
        st.write("**Portfolio:** [gopinathportfolio.com](https://www.gopinathportfolio.com)")  # Replace with actual portfolio link
        st.write("**GitHub:** [Gopinathalpha7](https://github.com/Gopinathalpha7)")
        # Add more contact details here
    # Add your About and Contact page content here


# Call the display function to show the About
if __name__ == "__main__":
    display_about()