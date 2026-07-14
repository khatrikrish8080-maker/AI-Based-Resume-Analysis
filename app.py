import streamlit as st
from PyPDF2 import PdfReader
from nlp import preprocess_resume, match_similarity

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

st.title("AI RESUME ANALYZER")
st.subheader("Check how well your resume matches the job description")

upload_resume=st.file_uploader("Upload your resume in pdf format",type=["pdf"])

job_description= st.text_area("Paste the job description here",height=250)

if st.button("Analyse Resume"):
    if upload_resume is not None and job_description.strip()!="":

        with st.spinner("Analysing your resume ...."):
            raw_resume=extract_text_from_pdf(upload_resume)

            cleaned_cv=preprocess_resume(raw_resume)
            cleaned_job=preprocess_resume(job_description)

            percentage=match_similarity(cleaned_cv,cleaned_job)

            st.success(f"Matching score : {percentage} %")

    else:
        st.error("Pls upload a resume or paste job description first")




