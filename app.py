import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu

#loading the saved models
with open('C:/Users/tharu/OneDrive/Desktop/TARP/bagging_model1.pickle', 'rb') as f:
    cc_model = pickle.load(f)
#sidebar

# with st.sidebar:
#     selected=option_menu("CREDIT CARD FRAUD AND ATTRITION PREDICTION",
#                          ['FRAUD DETECTION',
#                           'ATTRITION PREDICTION',
#                           ],
#                           icons=['heart','activity','person'],
#                           default_index=0)
    
# if (selected=='ATTRITION PREDICTION'):

    # giving a title
    st.title('Stress and Depression Prediction')

    # getting the input data from the user

    # Create the input fields for the user to input values
    q1 = st.selectbox('Little interest or pleasure in doing things?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    # education_level = st.selectbox('Education Level', ['High School', 'Graduate', 'Uneducated', 'College', 'Post-Graduate', 'Doctorate'])
    q2 = st.selectbox('Feeling down, depressed, or hopeless?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    # Income_Category = st.selectbox('Income Category', ['$120K+', '$40k-$60k', '$60K-$80K', '$80K-$120K', 'Less than $40K'])
    q3 = st.selectbox('Trouble falling or staying asleep, or sleeping too much?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    q4 = st.selectbox('Feeling tired or having little energy?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    q5 = st.selectbox('Poor appetite or overeating?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    q6 = st.selectbox('Feeling bad about yourself - or that you are a failure or have let yourself or your family down?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    q7 = st.selectbox('Trouble concentrating on things, such as reading the newspaper or watching television?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    q8 = st.selectbox('Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    q9 = st.selectbox('Thoughts that you would be better off dead, or of hurting yourself in some way?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    # dependent_count = st.text_input('Dependent Count', '0')
    # total_relationship_count = st.text_input('Total Relationship Count', '0')
    # months_inactive_12_mon = st.text_input('Months Inactive 12 Months', '0')
    # contacts_count_12_mon = st.text_input('Contacts Count 12 Months', '0')
    # total_amt_chng_q4_q1 = st.text_input('Total Amount Change Q4 Q1', '0')
    # total_trans_ct = st.text_input('Total Transaction Count', '0')
    # total_ct = st.text_input('Total Transaction Change','0')

    # convert input data to numeric types
    # dependent_count = int(dependent_count)
    # total_relationship_count = int(total_relationship_count)
    # months_inactive_12_mon = int(months_inactive_12_mon)
    # contacts_count_12_mon = int(contacts_count_12_mon)
    # total_amt_chng_q4_q1 = float(total_amt_chng_q4_q1)
    # total_trans_ct = int(total_trans_ct)
    # total_ct = float(total_ct)

    Q1 = 0 if q1 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q2 = 0 if q2 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q3 = 0 if q3 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q4 = 0 if q4 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q5 = 0 if q5 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q6 = 0 if q6 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q7 = 0 if q7 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q8 = 0 if q8 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q9 = 0 if q9 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    #edu_val = 0 if education_level == 'High School' else 1 if education_level == 'Graduate' else 2 if education_level == 'Uneducated' else 3 if education_level == 'College' else 4 if Education_Level == 'Post-Graduate' else 5 if Education_Level == 'Doctorate' else 6
    # mrg_val = 0 if marital_status == 'Divorced' else 1 if marital_status == 'Married' else 2 if marital_status == 'Single' else 3 
    # #inc_val = 0 if Income_Category == '$120K+' else 1 if Income_Category == '$40k-$60k' else 2 if Income_Category == '$60K-$80K' else 3 if Income_Category == '$80K-$120K' else 4 if Income_Category == 'Less than $40K' else 5 
    # ctg_val = 0 if Card_Category == 'Blue' else 1 if Card_Category == 'Gold' else 2 if Card_Category == 'Platinum' else 3 
    
    
    # code for Prediction
    attrition = ''
    
    # creating a button for Prediction
    
    if st.button('Depression Prediction Result'):
        input_data_as_numpy_array = np.asarray([Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9])

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        att = cc_model.predict(input_data_reshaped)
        if (att[0] == 0):
            attrition= 'Mild Depression'
        elif (att[0]==1):
           attrition= 'Minimal Depression' 
        elif(att[0]==2):
            attrition='Moderate Depression'
        elif(att[0]==3):
            attrition='Moderately Severe Depression'
        else:
            attrition='Severe Depression'
        
        
    st.success(attrition)

# if (selected=='FRAUD DETECTION'):
    
#     #st.title
#     st.title('CREDIT CARD FRAUD DETECTION USING ML')

#     Amount = st.text_input('Amount', '0')
#     first = st.text_input('First name', '0')
#     last = st.text_input('Last Name', '0')
#     street = st.text_input('Contacts Count 12 Months', '0')
#     # total_amt_chng_q4_q1 = st.text_input('Total Amount Change Q4 Q1', '0')
#     # total_trans_ct = st.text_input('Total Transaction Count', '0')
#     # total_ct = st.text_input('Total Transaction Change','0')
    
    
    
    
# if __name__ == '__main__':
#    main()