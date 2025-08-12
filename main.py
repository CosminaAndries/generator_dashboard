import streamlit as st 
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import home, data_cleaning_pane,visualization_pane


class Multiapp:
  def __init__(self):
    self.apps=[]   
  def add_app(self,title,function):
    self.apps.append({
      "title":title,
      "function":function
    })
  def run():
     with st.sidebar:
      app=option_menu(
        menu_title="Menu",
        menu_icon="list",
        options=['Home','Cleaning','Visualization'],     
        icons=['house','trash' ,'table'],
        styles={
          "icon":{ "color":"white", "font-size":"23px"},
          "nav-link":{"color":"white", "font-size":"20px","text-align":"left","margin":"0px","--hover-color":"blue"},
          "nav-link-selected":{"background-color":"#02ab21"},
          }
      )
     if app=="Home":
       st.set_page_config(
         page_title="Home Page"
            )
       home.app()
     elif app=="Visualization":
        st.set_page_config(
         page_title="Visualization Page"
            )
        visualization_pane.app()
     elif app=="Cleaning":
        st.set_page_config(
         page_title="Data Cleaning Page"
            )
        data_cleaning_pane.app()
      
  run()
