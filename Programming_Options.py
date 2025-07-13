import streamlit as st

st.title('Programming Language app')
st.subheader('Welcome to your first interactive app')
st.text("Choose your favorite programming language")
Code=st.selectbox("Your Programming language:",["Python","Java","C++","C","C#","JavaScript","Ruby","Go","R","Rust","PHP","SQL","Pandas","Numpy"])
st.success(f"You Choose {Code} Programming Language..",icon="✅")
# st.success(f"You Choose {Code} Programming Language..",icon="🐍")
# st.success(f"You Choose {Code} Programming Language..",icon="🦆")
