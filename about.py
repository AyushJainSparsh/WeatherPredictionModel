import streamlit as st
import home
def app():
    #st.header(':blue[About Us :]')
    st.markdown('# :blue[About :]')
    st.write(':red[As we all well aware that weather and its comaponent are natural phenomenon]'
             +':red[we only predict how the weather be today or tomorrow based on some parameters]'
              +':red[ beacause if say that today is rain or if clouds didn\'t rain down then ]'
              +':red[ we don\'t do anything .]')
    st.write(':red[So our team just prepare a model which predict that how ]'
             +':red[ weather gone by using some parameters.]')
    
    st.markdown('##### :blue[How our app work :]')
    st.write(':red[1. You First have to provide the temperature in c of that day.]')
    st.write(':red[2. Then you have to provide wind speed in kph.]')
    st.write(':red[3. Then you have to provide pressure in mb.]')
    st.write(':red[4. As a Output you will get humidity , feels like and heat index.]')
    
    st.markdown('##### :blue[Precaution :]')
    st.warning('Input is only accepted in integer or decimal format other'
               +' than these format will lead to error and you will don\'t get you required output you want.')
    
    st.markdown('#### :rainbow[Thank You]')