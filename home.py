import streamlit as st
import pickle as pkl
def app():
    st.header(':blue[Weather] :red[Prediction Model]')
    value1 =st.text_input('Enter Temperature in Celsius :')
    value2 =st.text_input('Enter Wind speed in kph :')
    value3 =st.text_input('Enter Pressure in mb :')
    value1 = float(value1)
    value2 = float(value2)
    value3 = float(value3)
    try :
        if st.button('Predict') :
            if value1 == '' or value2 == '' or value3 == '' :
                st.warning('Please Enter all the details.')
            else :
                model1 = pkl.load(open('model1.pkl' , 'rb'))
                model2 = pkl.load(open('model2.pkl' , 'rb'))
                model3 = pkl.load(open('encoder_condition.pkl' , 'rb'))
                model4 = pkl.load(open('condition_model.pkl' , 'rb'))
                input1 = [[value1  , value2 ]]
                input2 = [[value2 , value3]]
                output1 = model1.predict(input1)
                output2 = model2.predict(input2)
                input3 = [[value1 , value2  , value3 , output2[0] , output1[0][1] , output1[0][0] ]]
                output3 = model4.predict(input3)
                output3 = model3.inverse_transform(output3)
                st.success('Feels Like (in C) :'+str(output1[0][0]))
                st.success('Heat Index (in C) :'+str(output1[0][1]))
                st.success('Humidity : '+str(output2[0]))
                st.success('Weather Condition : '+str(output3[0]))
    except :
        st.warning('Insert all the values as instructed in about section.')
