import streamlit as st
from streamlit_option_menu import option_menu

import home , about , visualize

class Main :
    def __init__(self):
        self.apps = []
    def add_apps(self,title,function):
        self.apps.append({
            'title' : title , 
            'function' : function
        })
    def run():
        with st.sidebar :
            app = option_menu(
                menu_title = 'Weather Prediction' ,
                options = ['Home' , 'About' , 'Visualize'] , 
                icons = ['house-fill', 'info-circle-fill' , 'drawing'] ,
                menu_icon = 'cloud-rain-fill' , 
                default_index = 1 ,
                styles = {
                    "Container":{'Padding':'5!important','background-color' : 'blue'},
                        'icon':{'font-size' : '25px'},
                        'nav-link':{'font-size':'20px','text-align':'left','margin':'0px','--hover-color':'blue'},
                        'nav-link-selected':{'background-color':'red'}} 
            )
        if app == 'Home' :
            home.app()
        if app == 'About' :
            about.app()
        if app == 'Visualize':
            visualize.app()
    run()