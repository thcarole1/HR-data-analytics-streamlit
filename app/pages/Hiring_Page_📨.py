import streamlit as st
import requests
import pandas as pd
import json

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
    <h1 class="title">Support HR Decisions in New Hiring</h1>
    <h2 class="subtitle">Based on the job description and an applicant's information,
    which applicant is more likely to be retained within the company?</h2>
    """,
    unsafe_allow_html=True
)

# ************************** Connection to API ***************************************
st.markdown('<p class="header-text no-space">Please upload the JSON file below</p>', unsafe_allow_html=True)

# Do not modify label please (no empty value + label_visibility = 'hidden')
label ="Upload a json file"
uploaded_file = st.file_uploader(label, label_visibility = "hidden")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    json_data = json.loads(bytes_data)
    X = pd.DataFrame(json_data)
    hiring_features_cols = ['Department','GEO','Role',
                            'average_montly_hours','salary',
                            'Will_Relocate','Gender']

    X = X[hiring_features_cols]

    st.write(f"## Description of applicants")
    st.write(X)

    # API endpoint
    URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/upload_predict_hiring"

    # Sending POST request and saving the response as a response object
    r = requests.post(url=URL, files={'upload_file': bytes_data})

    st.write(f"## Ranking of applicants based on probability of retention")
    ranking = json.loads(r.text)
    ranking_df = pd.DataFrame(ranking['Ranking'])
    st.write(ranking_df)
else:
    st.markdown('<p class="header-text">No File Uploaded</p>', unsafe_allow_html=True)
