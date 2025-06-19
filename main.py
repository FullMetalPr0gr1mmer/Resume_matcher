from src.parser.parser import * #imports
from src.text_cleaner.text_cleaner import *
from src.matcher.similarity_engine import *
resumes = extract_all_resumes("data/resumes")
jobs = load_job_descriptions("data/jobs")
'''for name,text in resumes.items():
    print(f"----{name}----\n {preprocess_text(text)}...\n")

    
    for name,text in jobs.items():
        print(f"----{name}----\n {preprocess_text(text)}...\n")'''


processed_resumes ={name:preprocess_text(text) for name,text in resumes.items()}
processed_jobs ={name:preprocess_text(text) for name,text in jobs.items()}
similarities = compute_similarity(processed_resumes, processed_jobs)

top_matches = rank_matches(similarities,2)
for resume, job_scores in top_matches.items():
    print(f"Resume: {resume}")
    for job, score in job_scores:
        print(f"  -> Match with '{job}': {score}")
    print()