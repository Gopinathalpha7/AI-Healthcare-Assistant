import streamlit as st
from PIL import Image

def display_home():
    st.header(":red[Home]")

    # Add your Home page content here
    st.subheader(":blue[Welcome to the AI Healthcare Assistant]")
    st.markdown('''Welcome to our cutting-edge AI Healthcare Assistant, a smart,
                 innovative assistant designed to transform the way healthcare professionals and patients interact with medical information. 
                Our app is powered by advanced AI technologies and offers a comprehensive suite of tools, 
                including an AI chatbot, a reports analyzer, an X-ray analyzer, and various disease-specific diagnostic tools.''')
    
    # Home page Image
    background_image = Image.open("Image/Home.jpg")
    st.image(background_image, use_column_width=True)


    st.header(":red[AI Assistants]")

    # col1, col2, col3 = st.columns(3)
    col1, col3 = st.columns(2)

    with col1:
        st.subheader(":blue[Ai chatbot]")
        Ai_chatbot_image = Image.open("Image/Chat_bot.jpg")
        st.image(Ai_chatbot_image, use_column_width=True)
        st.markdown('''**:blue[AI Chatbot:]** A virtual assistant that can answer medical queries, provide symptom checks, 
                    and assist with healthcare advice based on the latest medical knowledge.''')

    # with col2:
    #     st.subheader(":blue[X-Ray Analyzer]")
    #     X_Ray_image = Image.open("Image/X-Ray.jpg")
    #     st.image(X_Ray_image, use_column_width=True)
    #     st.markdown('''**:blue[X-Ray Analyzer:]** An advanced AI tool that assists in diagnosing conditions from X-ray images, 
    #                 helping doctors make faster and more accurate decisions.''')
        
    with col3:
        st.subheader(":blue[Reports Analyzer]")
        File_Analyzer_image = Image.open("Image/File_Analyzer.jpg")
        st.image(File_Analyzer_image, use_column_width=True)
        st.markdown('''**:blue[Reports Analyzer:]** Quickly upload and analyze medical reports, prescriptions, or other documents to extract key 
                    insights and information.''')


    st.header(":red[Diagnosers]")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.subheader(":blue[Cardiology]")
        cardiology_image = Image.open("Image/Cardiology.jpg")
        st.image(cardiology_image, use_column_width=True)
        st.markdown('''**:blue[Cardiology:]** Focused on diagnosing and treating heart-related conditions like cardiovascular diseases, heart failure, and more.''')

    with col5:
        st.subheader(":blue[Diabetology]")
        diabetology_image = Image.open("Image/Diabetology.jpg")
        st.image(diabetology_image, use_column_width=True)
        st.markdown('''**:blue[Diabetology:]** Specializes in the management and treatment of diabetes and its complications.''')

    with col6:
        st.subheader(":blue[Hepatology]")
        hepatology_image = Image.open("Image/Hepatology.jpg")
        st.image(hepatology_image, use_column_width=True)
        st.markdown('''**:blue[Hepatology:]** Provides expertise in liver diseases such as hepatitis, cirrhosis, and liver cancer.''')
    
    col7, col8, col9 = st.columns(3)

    with col7:
        st.subheader(":blue[HIV/AIDS]")
        hiv_aids_image = Image.open("Image/HIV_AIDS.jpg")
        st.image(hiv_aids_image, use_column_width=True)
        st.markdown('''**:blue[HIV/AIDS:]** Focused on managing and treating HIV/AIDS, improving the quality of life of affected individuals.''')

    with col8:
        st.subheader(":blue[Mammary Oncology]")
        mammary_oncology_image = Image.open("Image/Breast_Cancer.jpg")
        st.image(mammary_oncology_image, use_column_width=True)
        st.markdown('''**:blue[Mammary Oncology:]** Specializes in breast cancer diagnosis, treatment, and post-treatment care.''')

    with col9:
        st.subheader(":blue[Nephrology]")
        nephrology_image = Image.open("Image/Nephrology.jpg")
        st.image(nephrology_image, use_column_width=True)
        st.markdown('''**:blue[Nephrology:]** Expertise in kidney-related diseases such as chronic kidney disease and kidney failure.''')

    col10, col11, col12 = st.columns(3)

    with col10:
        st.subheader(":blue[Oncology]")
        oncology_image = Image.open("Image/Oncology.jpg")
        st.image(oncology_image, use_column_width=True)
        st.markdown('''**:blue[Oncology:]** Involved in diagnosing and treating various forms of cancer with modern therapeutic approaches.''')
    
    with col11:
        st.subheader(":blue[Psychiatry]")
        psychiatry_image = Image.open("Image/Psychiatry.jpg")
        st.image(psychiatry_image, use_column_width=True)
        st.markdown('''**:blue[Psychiatry:]** Focuses on diagnosing and treating mental health disorders such as depression, anxiety, and more.''')
    
    with col12:
        st.subheader(":blue[Pulmonology]")
        pulmonology_image = Image.open("Image/Pulmonology.jpg")
        st.image(pulmonology_image, use_column_width=True)
        st.markdown('''**:blue[Pulmonology (TB):]** Specializes in the diagnosis and treatment of tuberculosis and other respiratory diseases.''')

# Call the display function to show the Home
if __name__ == "__main__":
    display_home()
