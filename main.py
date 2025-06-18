from src.parser.parser import * #imports
from src.text_cleaner.text_cleaner import *

resumes = extract_all_resumes("data/resumes")
for name,text in resumes.items():
    print(f"----{name}----\n {preprocess_text(text)}...\n")

    jobs = load_job_descriptions("data/jobs")
    for name,text in jobs.items():
        print(f"----{name}----\n {preprocess_text(text)}...\n")