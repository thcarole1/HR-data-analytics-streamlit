import streamlit as st

st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    .subtitle {
        text-align: center;
        color: gray;
        font-size: 1.5em;
    }
    .first-sentence {
        text-align: left;
        margin-top: 20px;
        font-size: 1.2em;
    }
    </style>
    <h1 class="title">Team members </h1>
    <br>
    <br>

    """,
    unsafe_allow_html=True
)


st.image("app/images/Emily.jpg", width=200)
st.write("Emily ANDERSON")
st.image("app/images/Felix.jpg", width=200)
st.write("Felix HABERL")
st.image("app/images/Louis.jpg", width=200)
st.write("Louis GOKELAERE")
st.image("app/images/Sarah.jpg", width=200)
st.write("Sarah DIETHELM")
st.image("app/images/Thierry.jpg", width=200)
st.write("Thierry CAROLE")
