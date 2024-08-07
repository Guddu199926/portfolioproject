import streamlit as st
import pandas as pd

def read_rows(rows):
    for index, row in rows.iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code](row['url'])")

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
col3, empty_col ,col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("data.csv", sep = ";")

with col3:
    read_rows(df[:10])

with col4:
    read_rows(df[10:])