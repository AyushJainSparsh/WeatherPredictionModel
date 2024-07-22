import streamlit as st
import pickle as pkl
def app():
    st.header(':blue[Weather] :red[Prediction Model]')
    try:
        value1 =int(st.text_input('Enter Temperature in Celsius :'))
        value2 =int(st.text_input('Enter Wind speed in kph :'))
        value3 =int(st.text_input('Enter Pressure in mb :'))
        if st.button('Predict') :
            if value1 == '' or value2 == '' or value3 == '' :
                st.warning('Please Enter all the details.')
            else :
                model1 = pkl.load(open('model1.pkl' , 'rb'))
                model2 = pkl.load(open('model2.pkl' , 'rb'))
                input1 = [[value1  , value2 ]]
                input2 = [[value2 , value3]]
                output1 = model1.predict(input1)
                output2 = model2.predict(input2)
                st.success('Feels Like (in C) :'+str(output1[0][0]))
                st.success('Heat Index (in C) :'+str(output1[0][1]))
                st.success('Humidity : '+str(output2[0]))
                st.warning('Enter Data in right format as it is given in about section.')
    except :
        st.warning('Enter the data in given format as it is given About section.')