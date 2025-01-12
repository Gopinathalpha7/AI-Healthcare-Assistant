# 🩺 AI Healthcare Assistant  

## 📋 **Description**  
In today’s fast-paced medical environment, access to timely, accurate, and personalized healthcare insights is crucial for improving patient outcomes. The **AI Healthcare Assistant** is an intelligent partner designed to assist healthcare professionals with a wide range of tasks, enabling them to focus on what matters most—patient care.  

---

## 🎯 **Purpose**  

### **What the Project Does**  
This project is a cutting-edge AI-powered healthcare assistant designed to enhance medical workflows and support healthcare professionals. Key features include:  
- **Healthcare Chatbot**: Providing accurate answers to medical queries.  
- **Medical Report Analyzer**: Extracting actionable insights from medical reports.  
- **X-Ray Analyzer**: Delivering high-accuracy diagnostics for pulmonary diseases such as TB.  
- **Specialized Diagnostic Tools**: Covering diverse specialties, including cardiology, diabetology, oncology, and more.  


### **Why It Was Built**  
To enhance diagnostic accuracy, improve workflow efficiency, and empower healthcare professionals with cutting-edge, data-driven decision-making tools.  

### **How It is Useful**  
By leveraging advanced technologies like **Retrieval-Augmented Generation (RAG)**, the AI Healthcare Assistant provides accurate, real-time insights, saving time and improving healthcare outcomes.  

---

## ✨ **Key Features**  
- **Healthcare Chatbot**: AI-powered chatbot for answering medical queries.  
- **Medical Report Analyzer**: Insight extraction from reports using RAG.  
- **X-Ray Analyzer**: Detects pulmonary conditions with 98.82% accuracy.  
- **Disease-Specific Diagnosers**: Tailored models for specialties including:  
  - Cardiology
  - Diabetology
  - Oncology
  - Hepatology
  - Nephrology
  - Pulmonology
  - HIV/AIDS
- **User-Friendly Interface**: Designed for seamless interaction by healthcare practitioners.  

---

## 🏗️ **Project Architecture**  

### **Data Collection**  
- **Medical Knowledge Bases**: Accesses and retrieves information from up-to-date medical databases and repositories.  
- **Patient Data**: Integrates inputs from medical reports, X-rays, and user queries for comprehensive analysis.  

### **Preprocessing**  
- **Medical Report Parsing**: Extracts, cleans, and structures data from uploaded reports.  
- **Imaging Data Preparation**: Normalizes and preprocesses X-ray images for accurate analysis.  
- **Query Understanding**: Uses advanced NLP techniques to interpret and refine user queries.  

### **Core Components**  
- **Retrieval-Augmented Generation (RAG)**:  
  - **Retrieval Phase**: Identifies relevant information from medical databases.  
  - **Generation Phase**: Synthesizes responses using generative AI.  
- **Diagnostic Models**: Specialized pre-trained models tailored for cardiology, diabetology, oncology, and other medical specialties.  
- **X-Ray Analysis**: Employs deep learning with CNN-based pre-trained models for disease detection and diagnostics.  

### **User Interaction**  
- **Healthcare Chatbot**: Provides personalized communication and real-time healthcare support.  
- **Dashboard**: Offers a user-friendly interface to display analysis results, trends, and diagnostic insights.  

### **Output**  
- **Actionable Insights**: Delivers diagnostic suggestions, key findings, and relevant references to enhance decision-making.  

---

## 🔧 **Technologies Used**  
- **Programming Language**: Python  
- **Libraries**: Pandas, NumPy, Matplotlib, Plotly  
- **Frameworks**: TensorFlow, Scikit-learn  
- **Large Language Models**: Llama 3.1, GenAI  
- **RAG Framework**: LangChain  
- **App Development**: Streamlit  

---

## 🛠️ **Workflow Overview**  

### **Home Page**  
- **Purpose**: Introduces the app and provides an overview of its features.



### **AI Healthcare Chatbot**  
- **Purpose**: Handles real-time medical queries and provides healthcare-related information.
- **Model Details**:
  - **Name**: Meta Llama 3.1 (8B Parameters).  
  - **Training Data**: Biomedical & general domain texts.  
  - **Capabilities**: Symptom analysis and answering medical questions.  
  - **Deployment**: Locally hosted for privacy and efficiency.  



### **AI Report Analyzer**  
- **Purpose**: Analyzes medical reports and generates actionable insights.  
- **Technology**:  
  - **Type**: Retrieval-Augmented Generation (RAG).  
  - **Features**:  
    - Real-time medical data retrieval for enhanced accuracy.  
    - Improves workflow efficiency.  
    - Supports complex and routine medical cases.  



### **Diagnoser Page**  
- **Purpose**: Provides diagnostic tools for various medical specialties.  
- **Technical Details**:
  - **Cardiology**: Decision Tree (Accuracy: 73.17%).  
  - **Diabetology**: CatBoost (Accuracy: 97.80%).  
  - **Hepatology (Liver)**: Random Forest (Accuracy: 99.94%).  
  - **HIV/AIDS**: LGBMClassifier (Accuracy: 71.03%).  
  - **Nephrology (Kidney)**: SVM (Accuracy: 97.50%).  
  - **Oncology (Cancer)**: Random Forest (Accuracy: 82.80%).  
  - **Pulmonology (TB)**: CNN (Accuracy: 98.82%).  



### **About Page**  
- **Purpose**: Contains all technical and app-related details for user reference.


---

## 📂 **Resources**  
**Author**: Gopinath  

<a href='https://docs.google.com/presentation/d/1yYgP5FiQ-sjgzmBTmZqQ90jC9_uEqtnsxjps4rh5eIY/edit?usp=drive_link'><img src="https://img.icons8.com/color/64/000000/google-slides.png" alt="Project PPT" width="30"></a> [![Project PPT](https://img.shields.io/badge/Project-PPT-yellow)](https://docs.google.com/presentation/d/1yYgP5FiQ-sjgzmBTmZqQ90jC9_uEqtnsxjps4rh5eIY/edit?usp=drive_link)

<a href='#'><img src="https://img.icons8.com/fluency/64/000000/video.png" alt="Project Video" width="30"></a> [![Project Video](https://img.shields.io/badge/Project-Video-red)](#)


---

## 📞 Contact Me

<a href='https://www.linkedin.com/in/gopinathaiml12/'><img src="https://img.icons8.com/color/64/000000/linkedin.png" alt="LinkedIn" width="30"></a> [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/gopinathaiml12/)

<a href='mailto:gopinathaiml12@gmail.com'><img src="https://img.icons8.com/color/64/000000/gmail-new.png" alt="Gmail" width="30"></a> [![Gmail](https://img.shields.io/badge/Gmail-Email-red)](mailto:gopinathaiml12@gmail.com)

<a href='https://gopinathalpha7.github.io/Gopinath-Portfolio/'><img src="https://img.icons8.com/color/64/000000/web.png" alt="Portfolio" width="30"></a> [![Portfolio](https://img.shields.io/badge/Portfolio-Website-yellow)](https://gopinathalpha7.github.io/Gopinath-Portfolio/)

<a href='https://leetcode.com/u/gopinathaiml12/'><img src="https://img.icons8.com/external-tal-revivo-color-tal-revivo/64/000000/external-level-up-your-coding-skills-and-quickly-land-a-job-logo-color-tal-revivo.png" alt="LeetCode" width="30"></a> [![LeetCode](https://img.shields.io/badge/LeetCode-Profile-orange)](https://leetcode.com/u/gopinathaiml12/)
