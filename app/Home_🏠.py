import streamlit as st

st.set_page_config(page_title="HR Data Analytics", page_icon=":bar_chart:")

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
        text-align: center;
        margin-top: 20px;
        font-size: 1.2em;
    }
    </style>
    <h1 class="title">HR Data Analytics</h1>
    <h2 class="subtitle">Predicting and improving employee attrition rates.</h2>
    <p class="first-sentence"> Determine the probability of a current employee leaving your company,</p>
    <p class="first-sentence">improve hiring based on attrition analysis and predictions </p>
    <p class="first-sentence">and determining the main factors influencing attrition.</p>

    """,
    unsafe_allow_html=True
)

url = "https://netchex.com/wp-content/uploads/2022/12/HR-Analytics.png"
st.image(url)
