import streamlit as st 
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from streamlit_option_menu import  option_menu

def procesare_fisier( fisiere_de_incarcat):
  try:
   if fisiere_de_incarcat is not None :
     if fisiere_de_incarcat.name.endswith(".json"):
       df=pd.read_json(fisiere_de_incarcat)
       st.write("The data found in the files")
       st.session_state.data=df
       st.dataframe(df)
     else :
       df=pd.read_csv(fisiere_de_incarcat)
       st.write("The data found in the files")
       st.session_state.data=df
       st.dataframe(df)
  except Exception as e :
   st.error(f"Eroare la incarcarea fisierului!{e}")
   
def informatii_despre_date(df):
 st.markdown("<h3 style='font-size:23px'>Data Shape</h3>",unsafe_allow_html=True)
 st.write(df.shape)
 st.markdown("<h3 style='font-size:23px'>Data Description</h3>",unsafe_allow_html=True)
 st.write(df.describe())
 st.markdown("<h3 style='font-size:23px'>Columns Name</h3>",unsafe_allow_html=True)
 st.write(df.columns)
 st.markdown("<h3 style='font-size:23px'>The columns data type</h3>",unsafe_allow_html=True)
 st.write(df.dtypes)

def app():
 st.title("DashBoard Generator")
 st.markdown("<h3 style='font-size:24px'>Welcome to my app!</h3>",unsafe_allow_html=True)
 fisiere_de_incarcat=st.file_uploader(" ",type=["csv","json"])
 procesare_fisier(fisiere_de_incarcat)
 df=st.session_state.data
 df=pd.DataFrame(df)
 st.markdown("<h3 style='font-size:24px'> Information about the data!</h3>",unsafe_allow_html=True)
 informatii_despre_date(df)


    
  


