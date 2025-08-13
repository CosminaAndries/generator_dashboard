import streamlit as st
import pandas as pd
import numpy as np 
from sklearn.neighbors import NearestNeighbors
from scipy import stats
def procesare_fisier(fisiere_de_incarcat):
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

def verificare_coloane_null(df):
 coloane_valori_lipsa=[]
 for col in df.columns:
   numar=df[col].isnull().sum()
   procentaj=(numar/df.shape[0])*100
   if numar>0 :
    coloane_valori_lipsa.append({
    "numecoloana":col,
    "numar valori lipsa":numar,
    "procentaj":procentaj})
  
 coloane_valori_lipsa=pd.DataFrame(coloane_valori_lipsa)
 st.dataframe(coloane_valori_lipsa)
 return coloane_valori_lipsa
 


def app():
  st.title("Data Cleaning Page")
  fisiere_de_incarcat=st.file_uploader(" ",type=["csv","json"])
  procesare_fisier(fisiere_de_incarcat)
  df=st.session_state.data
  coloane_valori_lipsa= verificare_coloane_null(df)
  if coloane_valori_lipsa is not None:
    numerice=df.select_dtypes(include=['number']).columns.tolist()
    textuale=df.select_dtypes(include=['object','string']).columns.tolist()
    if numerice:
     preferinta_num=st.selectbox("How do you want to handle the missing data",options=["None","Remove Columns","Replace with mean ","Replace with median"])
     if preferinta_num=="Remove Columns":
      df.dropna(axis=1, inplace=True)
      st.dataframe(df)
      st.session_state.data=df
     elif preferinta_text=="Replace with mean ":
      for col in textuale:
       df[col].fillna(df[col].mean()[0],inplace=True)
       st.session_state.data=df
     elif preferinta_text=="Replace with median ":
      for col in textuale:
       df[col].fillna(df[col].median()[0],inplace=True)
       st.session_state.data=df
      
    if textuale:
     preferinta_text=st.selectbox("How do you want to handle the missing data",options=["None","Remove Columns","Replace with mode ", "Replace with 'Unknown'"])
     if preferinta_text=="Remove Columns":
      df.dropna(axis=1,inplace=True)
      st.dataframe(df)
      st.session_state.data=df
     elif preferinta_text=="Replace with 'Unknown'":
      df.fillna('Unknown',inplace=True)
      st.session_state.data=df
    elif preferinta_text=="Replace with mode ":
      for col in textuale:
       df[col].fillna(df[col].mode()[0],inplace=True)
       st.session_state.data=df
