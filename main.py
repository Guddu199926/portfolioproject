import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    image=st.image("images/mypic.png")
with col2:
    st.title("Ravi Charan")
    content =  """
          Hi, I am Ravi! All I do is eat sleep and enjoy. Please help me to continue this process. Alcohol is not good for human since it effect the liver and causes obesity.
            """
    st.info(content)

content2 ="""Below you can find some of the apps I have built in Python. Feel free to contact me!
               """
st.info(content2)
col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep = ";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])

