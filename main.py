import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
with col2:
    st.title("Ravi Charan")
    content =  """
          Hi, I am Ravi! All I do is eat sleep and enjoy. Please help me to continue this process. Alcohol is not good for human since it effect the liver and causes obesity.
            """
    st.info(content)

    content2 ="""Below you can find some of the apps I have built in Python. Feel free to contact me!
               """
    st.info(content2)