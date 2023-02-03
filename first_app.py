#streamlit run <streamlitapp>.py
#  code first_app.py
# streamlit run first_app.py


import streamlit as st
import pandas as pd

def main():
    st.title("first_APP")
    df = pd.DataFrame({
        "first_col":[1,2,3,4],
        "second_col":[10,20,30,40]
    })
    st.write(df)

if __name__ == "__main__":
    main()


#Mark Down
st.markdown('Markdown')
st.markdown('Streamlit is **_really_ cool**.')
st.markdown('This text is :red[colored red], and this is **:blue[colored]** and bold.')
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

