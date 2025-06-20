import streamlit as st
import fitz
import io

from streamlit import subheader

from src.parser.parser import *
from src.text_cleaner.text_cleaner import *
from src.matcher.similarity_engine import *
import pandas as pd

st.set_page_config(page_title="AI Resume Matcher", layout="wide")
st.title("AI-Powered Resume Scanner & Job Matcher")

# Upload resume
st.subheader("Upload Resume")
resume_files  = st.file_uploader("Upload your resumes (.PDF)",type=["pdf"],accept_multiple_files=True)

st.subheader("Job Descriptions")
job_files = st.file_uploader("Upload job decriptions (.TXT)",type=["txt"],accept_multiple_files=True)
job_texts=[]
if job_files:
    for file in job_files:
        job_txt = file.read().decode("utf-8")
        job_texts.append((file.name,job_txt))
st.markdown("OR Enter Job Descriptions Manually" )
num_jobs=st.number_input("Number of job descriptions you want to add", min_value = 0 , max_value = 5 ,step=1)
for i in range(num_jobs):
    job_name=st.text_input("Job Name #{i+1}")
    job_text=st.text_input("Job Description #{i+1}")
    if(job_text.strip()):
        job_texts.append((job_name,job_text))

if st.button("Submit"):
    if not resume_files:
        st.warning("Please upload at least one resume file")
    elif not job_texts:
        st.warning("Please upload at least one job description")
    else:
        st.info("Processing")
        resume_texts={}
        for file in resume_files:
            doc = fitz.open(stream=file.read(),filetype="pdf")
            text=""
            for page in doc:
                text+=page.get_text()
            resume_texts[file.name]=preprocess_text(text)
        job_descriptions={name:preprocess_text(text) for name,text in job_texts}
        scores = compute_similarity(resume_texts,job_descriptions)
        df = pd.DataFrame(scores).T.round(4)
        st.success("Matching complete!")
        st.subheader("Match Results Matrix")
        st.dataframe(df, use_container_width=True)
        csv_data=df.to_csv(index=True).encode("utf-8")
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="resume_matcher.csv",
            mime="text/csv",
        )





