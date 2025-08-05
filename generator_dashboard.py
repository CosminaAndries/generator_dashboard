import streamlit as st 
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

st.title("DashBoard Generator")
st.markdown("<h3 style='font-size:24px'>Upload a date file:</h3>",unsafe_allow_html=True)
fisiere_de_incarcat=st.file_uploader(" ",type=["csv","json"])

def procesare_fisier():
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
    
procesare_fisier();

choice_of_which_chart_to_use=st.selectbox('What chart do you want your data to be displayed with?',('None','Bar Chart','Line Chart','Area Chart','Map Chart','Scatterplot Chart'))
if choice_of_which_chart_to_use=='Bar Chart' :
  if st.session_state.data is not None:
   x=st.text_input("What column do you use fot the x-axis:")
   y=st.text_input("What column do you use fot the y-axis:")
   df=st.session_state.data
   if x and  y  and x in df.columns and y in df.columns :
    data=st.dataframe(df[[x,y]])
    x_label=st.text_input('x-label:')
    y_label=st.text_input('y label:')
    horizontal=st.text_input('Do you want the bars to be placed horizontally?')
    horizontal=True if  horizontal=='Yes' else False
    color=st.text_input('If you want collor you can only use RGA color code or HEX code:')
    if color=="None"or color=="No":
       color="#d59a75"
    grafic=st.bar_chart(data=df,x=x,y=y,color=color,horizontal=horizontal )
    fn='scatter.png'
    plt.savefig(fn)
    with open(fn,"rb") as img:
      btn=st.download_button(
       label="Download image",
       data=img.read(),
       file_name=fn,
       mime="image/png"
      )
elif choice_of_which_chart_to_use=='Line Chart' :
  if st.session_state.data is not None:
    x=st.text_input("What column do you use fot the x-axis:")
    y=st.text_input("What column do you use fot the y-axis:")
    df=st.session_state.data
    if x and  y  and x in df.columns and y in df.columns :
      data=st.dataframe(df[[x,y]])
      x_label=st.text_input('x-label:')
      y_label=st.text_input('y label:')
      horizontal=st.text_input('Do you want the bars to be placed horizontally?')
      horizontal=True if  horizontal=='Yes' else False
      color=st.text_input('If you want collor you can only use RGA color code or HEX code:')
      if color=="None"or color=="No":
       color="#d59a75"
       grafic=st.line_chart(data=df,x=x,y=y,color=color,horizontal=horizontal )
       fn='scatter.png'
       plt.savefig(fn)
       with open(fn,"rb") as img:
        btn=st.download_button(
        label="Download image",
        data=img.read(),
        file_name=fn,
        mime="image/png"
      )
   