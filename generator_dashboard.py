
import streamlit as st 
import pandas as pd

st.title("DashBoard Generator")
st.markdown("<h3 style='font-size:24px'>Upload a date file:</h3>",unsafe_allow_html=True)
fisiere_de_incarcat=st.file_uploader(" ",type=["csv","json"])
currenttheme="dark"
themes=["dark","light","blue","pink"]
df=None

def procesare_fisier():
 try:
   if fisiere_de_incarcat is not None :
     if fisiere_de_incarcat.name.endswith(".json"):
       df=pd.read_json(fisiere_de_incarcat)
       st.write("The data found in the files")
       st.dataframe(df)
     else :
       df=pd.read_csv(fisiere_de_incarcat)
       st.write("The data found in the files")
       st.dataframe(df)
 except Exception as e :
   st.error(f"Eroare la incarcarea fisierului!{e}")
    
procesare_fisier();

choice_of_which_chart_to_use=st.selectbox('What chart do you want your data to be displayed with?',('None','Bar Chart','Line Chart','Area Chart','Map Chart','Scatterplot Chart'))
if choice_of_which_chart_to_use=='Bar Chart' :
   x=st.text_input("What column do you use fot the x-axis:")
   y=st.text_input("What column do you use fot the y-axis:")
   if x is not None and y is not None:
    data=st.dataframe(df[[x,y]])
    x_label=st.text_input('x-label:')
    y_label=st.text_input('y label:')
    horizontal=st.text_input('Do you want the bars to be placed horizontally?')
    horizontal=True if  horizontal=='Yes' else False
    color=st.text_input('If you want collor you can only use RGA color code or HEX code:')
    stack=st.selectbox("Stacks(Implicit None):",("True","False","layered","center","normalize"))
    width=st.number_input("Specify the width of the chart:")
    height=st.number_input("Specify the height of the chart:")
    grafic=st.bar_chart(data, x= x, y=y, x_label=x_label, y_label=y_label, color=color, horizontal= horizontal, stack=stack, width=width, height=height, use_container_width=True)
    grafic
   
   