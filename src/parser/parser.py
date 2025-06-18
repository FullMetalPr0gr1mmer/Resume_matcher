import fitz #pymuPDF which will be used to handle pdfs
import os
#pdf_path="../data/resumes"

def extract_text_from_pdf(pdf_path): # runs over each page in a pda extracting all the text in it
    tetx=""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text = page.get_text()
    return text
#resume_dir="..\ data\ resumes"
def extract_all_resumes(resume_dir): # runs over each file in a directory and if it was a pds it send it to extract_text_from_pdf
    resumes={}
    for filename in os.listdir(resume_dir):
        if filename.endswith(".pdf"):
            path=os.path.join(resume_dir, filename)
            resumes[filename]=extract_text_from_pdf(path)
    return resumes #
#job_descriptions_dir="..\ data\ jobs"
def load_job_descriptions(job_dir): #reads job describtions
    jobs={}
    for filename in os.listdir(job_dir):
        if filename.endswith(".txt"):
            path=os.path.join(job_dir, filename)
            with open(path,"r",encoding="utf-8") as f:
                jobs[filename]=f.read()
    return jobs