#!/usr/bin/env python
# coding: utf-8

# # Deployment the Web App

# ###### Importing required libraries

# In[1]:


import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


# ###### loading the saved models

# In[2]:

diabetes_model = pickle.load(open('F:/Year 3/2sd Semester/FYP/Diseases Detection Web App/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('F:/Year 3/2sd Semester/FYP/Diseases Detection Web App/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('F:/Year 3/2sd Semester/FYP/Diseases Detection Web App/parkinsons_model.sav', 'rb'))


# ###### sidebar for navigation

# In[3]:


with st.sidebar:
    selected = option_menu('Medical Checkup Web App',
                          ['Home',
                           'Diabetes Prediction',
                           'Heart Disease Prediction',
                           "Parkinson's Prediction"],
                          icons=['house','bi bi-droplet','heart','person'], menu_icon= "bi bi-clipboard-check", default_index=0)
    
    st.error("**Note:** This system does not replace a doctor's visit if necessary. This system is only for urgent and temporary consultations until a specialist doctor's visit.", icon = "🚨")
    

    
# ###### Home Page
    
if (selected == 'Home'):
    
    # page title
    st.header('Welcome To The Medical Checkup Web App')
    image = Image.open('F:/Year 3/2sd Semester/FYP/Diseases Detection Web App/image.jpg')
    st.image(image, caption='Source: Australian Government Department of Health and Aged Care')
    
    # page content
    st.markdown("**This Web App was created to produce a recommendation system for diabetes, heart disease, and Parkinson's Disease that can be used by patients to get urgent and accurate advice using machine learning algorithms by entering some data on the basis of which the system will predict whether you suffer from this disease or not. Patients can access the web app anytime and anywhere.**") 
    
    # Diabetes Symptoms
    st.subheader("Some of the Diabetes Symptoms:")
    st.markdown("- Increased thirst and urination")
    st.markdown("- Increased hunger")
    st.markdown("- Fatigue")
    st.markdown("- Blurred vision")
    st.markdown("- Numbness or tingling in the feet or hands")
    st.markdown("- Sores that do not heal")
    st.markdown("- unexplained weight loss")
    st.write("Source:")
    st.caption('https://www.niddk.nih.gov/health-information/diabetes/overview/symptoms-causes#whatelse')
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:40px;
    }
    </style>
    ''', unsafe_allow_html=True)
    
    # Heart disease Symptoms
    st.subheader("Some of the Heart Disease Symptoms:")
    st.markdown("- Chest pain or discomfort")
    st.markdown("- Dizziness")
    st.markdown("- Fainting (syncope) or near fainting")
    st.markdown("- Fluttering in the chest")
    st.markdown("- Lightheadedness")
    st.markdown("- Racing heartbeat (tachycardia)")
    st.markdown("- Shortness of breath")
    st.markdown("- Slow heartbeat (bradycardia)")
    st.write("Source:")
    st.caption('https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118')
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:40px;
    }
    </style>
    ''', unsafe_allow_html=True)
    
    # Parkinson's Symptoms
    st.subheader("Some of the Parkinson's Disease Symptoms:")
    st.markdown("- Tremor")
    st.markdown("- Slowed movement (bradykinesia)")
    st.markdown("- Rigid muscles")
    st.markdown("- Impaired posture and balance")
    st.markdown("- Loss of automatic movements")
    st.markdown("- Speech changes")
    st.markdown("- Writing changes")
    st.write("Source:")
    st.caption('https://www.mayoclinic.org/diseases-conditions/parkinsons-disease/symptoms-causes/syc-20376055')
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:40px;
    }
    </style>
    ''', unsafe_allow_html=True)
    
  
   
# ###### Diabetes Prediction Page

# In[4]:

if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML (Only For Females)')
    st.info('Please fill in all the following fields', icon = "🔽")
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    
    with col1:
        Age = st.number_input('Age',step=1)
    
    with col2:
        Pregnancies = st.number_input('Number of Pregnancies',step=1)
        
    with col1:
        Glucose = st.number_input('Glucose level in blood',step=1)
    
    with col2:
        BloodPressure = st.number_input('Blood Pressure measurement',step=1)
    
    with col1:
        SkinThickness = st.number_input('Skin Thickness value',step=1)
    
    with col2:
        Insulin = st.number_input('Insulin Level in blood',step=1)
    
    with col1:
        BMI = st.text_input('BMI value')
    
    with col2:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

        
     # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        
        if (len(BMI) == 0 or len(DiabetesPedigreeFunction) == 0):
            st.error('Please make sure all fields are filled in correctly', icon="🚨")
        else:
            diab_prediction = diabetes_model.predict([[int(Age), int(Pregnancies), int(Glucose), int(BloodPressure), int(SkinThickness), int(Insulin), float(BMI), float(DiabetesPedigreeFunction)]])
        
            if (diab_prediction[0] == 1):
                st.warning('Unfortunately, You may be Diabetic, so you should visit a specialist doctor as soon as possible!', icon="⚠️")
            
            else:
                st.success("You may be Non-Diabetic")
            

# ###### Heart Disease Prediction Page

# In[5]:


if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    st.info('Please fill in all the following fields', icon="🔽")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        gender = st.radio('Gender',('1 = Male', '0 = Female'))
        
    with col1:
        cp = st.selectbox('Chest Pain Type',('0 = No Pain', '1 = Typical angina', '2 = Atypical angina', '3 = Non-anginal pain', '4 = Asymptomatic'))
        
    with col2:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col1:
        chol = st.text_input('Serum Cholesterol in mg/dl')
        
    with col2:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl',('1 = True', '0 = False'))
        
    with col1:
        restecg = st.selectbox('Resting Electrocardiographic results',('0 = Normal', '1 =  Having ST-T wave abnormality', '2 = Showing probable or definite left ventricular hypertrophy by Estes'))
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col1:
        exang = st.selectbox('Exercise Induced Angina',('1 = Yes', '0 = No'))
        
    with col2:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
        
    with col1:
        slope = st.selectbox('The slope of the peak exercise ST segment',('0 = Upsloping', '1 = Flat', '2 = Downsloping'))
        
    with col2:
        ca = st.selectbox('Major vessels colored by fluoroscopy',('0','1','2','3'))
        
    with col1:
        thal = st.selectbox('A blood disorder called thalassemia',('1 = Normal', '2 = Fixed defect', '3 = Reversable defect')) 
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
  
    if st.button('Heart Disease Test Result'):

        if (len(age) == 0 or len(trestbps) == 0 or len(chol) == 0 or len(thalach) == 0 or len(oldpeak) == 0):
            st.error('Please make sure all fields are filled in correctly', icon="🚨")
        else:
            gender = gender[0]
            cp = cp[0]
            fbs = fbs[0]
            restecg = restecg[0]
            exang = exang[0]
            slope = slope[0]
            ca = ca[0]
            thal = thal[0]
            heart_prediction = heart_disease_model.predict([[int(age),int(gender),int(cp),int(trestbps),int(chol),int(fbs),int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]]) 

            if (heart_prediction[0] == 1):
                st.warning('Unfortunately, You may have Heart Disease, so you should visit a specialist doctor as soon as possible!', icon="⚠️")
                
            else:
                st.success("You may have no Heart Disease")
        

# ###### Parkinson's Prediction Page

# In[6]:


if (selected == "Parkinson's Prediction"):
        
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    st.info('Please fill in all the following fields', icon="🔽")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('MDVP : Fo(Hz) - Average vocal fundamental frequency')
        
    with col2:
        fhi = st.number_input('MDVP : Fhi(Hz) - Maximum vocal fundamental frequency')
        
    with col3:
        flo = st.number_input('MDVP : Flo(Hz) - Minimum vocal fundamental frequency')
        
    with col4:
        Jitter_percent = st.text_input('MDVP : Jitter(%) - A measure of variation in fundamental frequency')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP : Jitter(Abs) - A measure of variation in fundamental frequency')
        
    with col1:
        RAP = st.text_input('MDVP : RAP - A measure of variation in fundamental frequency')
        
    with col2:
        PPQ = st.text_input('MDVP : PPQ - A measure of variation in fundamental frequency')
        
    with col3:
        DDP = st.text_input('Jitter : DDP - A measure of variation in fundamental frequency')
        
    with col4:
        Shimmer = st.text_input('MDVP : Shimmer - A measure of variation in amplitude')
        
    with col5:
        Shimmer_dB = st.number_input('MDVP : Shimmer(dB) - A measure of variation in amplitude')
        
    with col1:
        APQ3 = st.text_input('Shimmer : APQ3 - A measure of variation in amplitude')
        
    with col2:
        APQ5 = st.text_input('Shimmer : APQ5 - A measure of variation in amplitude')
        
    with col3:
        APQ = st.text_input('MDVP : APQ - A measure of variation in amplitude')
        
    with col4:
        DDA = st.text_input('Shimmer : DDA - A measure of variation in amplitude')
        
    with col5:
        NHR = st.text_input('NHR - A measure of the ratio of noise to tonal components in the voice')
        
    with col1:
        HNR = st.number_input('HNR - A measure of the ratio of noise to tonal components in the voice')
        
    with col2:
        RPDE = st.text_input('RPDE - A nonlinear dynamical complexity measure')
        
    with col3:
        D2 = st.text_input('D2 - A nonlinear dynamical complexity measure')
        
    with col4:
        DFA = st.text_input('DFA - Signal fractal scaling exponent')
        
    with col5:
        spread1 = st.text_input('Spread1 - A nonlinear measure of fundamental frequency variation')
        
    with col1:
        spread2 = st.text_input('Spread2 - A nonlinear measure of fundamental frequency variation')
        
    with col2:
        PPE = st.text_input('PPE - A nonlinear measure of fundamental frequency variation')
    

    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
                
        if (len(spread1) == 0):
            st.error('Please make sure all fields are filled in correctly', icon="🚨")
        else:
            parkinsons_prediction = parkinsons_model.predict([[float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs), float(RAP), float(PPQ) ,float(DDP), float(Shimmer) ,float(Shimmer_dB) ,float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR), float(RPDE), float(D2), float(DFA), float(spread1), float(spread2), float(PPE)]])  
            
            if (parkinsons_prediction[0] == 1):
                st.warning("Unfortunately, You may have Parkinson's Disease, so you should visit a specialist doctor as soon as possible!", icon="⚠️")

            else:                 
                st.success("You may have no Parkinson's Disease")
