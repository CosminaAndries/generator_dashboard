import streamlit as st
import pandas as pd
import numpy as np 

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
    "Name Column":col,
    "Count of missing values":numar,
    "The procent":procentaj})
  
 coloane_valori_lipsa=pd.DataFrame(coloane_valori_lipsa)
 st.dataframe(coloane_valori_lipsa)
 return coloane_valori_lipsa



def app():
  st.title("Data Cleaning Page")
  fisiere_de_incarcat=st.file_uploader(" ",type=["csv","json"])
  if 'data' in st.session_state:
    df = st.session_state.data
  else:
    return
  procesare_fisier(fisiere_de_incarcat)
  df=st.session_state.data
  coloane_valori_lipsa= verificare_coloane_null(df)
  if coloane_valori_lipsa :
    numerice=df.select_dtypes(include=['number']).columns.tolist()
    textuale=df.select_dtypes(include=['object','string']).columns.tolist()
    if numerice is not None:
     lista_coloane_modificate=st.multiselect("Choose the columns or the column you want to modify:",numerice)
     if lista_coloane_modificate is not None:
      preferinta_num=st.selectbox("How do you want to handle the missing data",options=["Remove Columns","Replace with mean ","Replace with median"])
      if preferinta_num=="Remove Columns":
       df.dropna(axis=1, inplace=True)
       st.dataframe(df)
       st.session_state.data=df
       file=df.to_csv(index=True)
       st.download_button(
         label="Download file",
          data=file,
         file_name="file.csv",
         mime="text/csv",
          key="download_csv"  
      )
      elif preferinta_num=="Replace with mean ":
       for col in textuale:
        df[col].fillna(df[col].mean(),inplace=True)
        st.session_state.data=df
        file=df.to_csv(index=True)
        st.download_button(
         label="Download file",
        data=file,
         file_name="file.csv",
         mime="text/csv",
         key="download4_csv"  
      )
         
      elif preferinta_num=="Replace with median ":
       for col in textuale:
        df[col].fillna(df[col].median(),inplace=True)
        st.session_state.data=df
        file=df.to_csv(index=True)
        st.download_button(
         label="Download file",
          data=file,
         file_name="file.csv",
         mime="text/csv",
        key="download3_csv"  
      )
    if textuale is not None:
     preferinta_text=st.selectbox("How do you want to handle the missing data",options=["None","Remove Columns","Replace with mode ", "Replace with 'Unknown'"])
     if preferinta_text=="Remove Columns":
      df.dropna(axis=1,inplace=True)
      st.dataframe(df)
      st.session_state.data=df
      file=df.to_csv(index=True)
      st.download_button(
         label="Download file",
          data=file,
         file_name="file.csv",
         mime="text/csv",
         key="download_csv"  
       )
     elif preferinta_text=="Replace with 'Unknown'":
      df.fillna('Unknown',inplace=True)
      st.session_state.data=df
      file=df.to_csv(index=True)
      st.download_button(
         label="Download file",
          data=file,
         file_name="file.csv",
         mime="text/csv",
        key="download1_csv"  
       )
    elif preferinta_text=="Replace with mode ":
      for col in textuale:
       df[col].fillna(df[col].mode()[0],inplace=True)
       st.session_state.data=df
      file=df.to_csv(index=True)
      st.download_button(
         label="Download file",
          data=file,
         file_name="file.csv",
         mime="text/csv",
        key="download2_csv"  
      )
         
