from sklearn.feature_extraction.text import TfidfVectorizer
'''The difference between feature_extraction and feature_selection 
the former is used to transform arbitrary data such as images and text into numerical features usable for ML
while the latter is used a technique used by ML on the features'''
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_texts,job_texts):
    all_texts =list(resume_texts.values())+list(job_texts.values())
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    resume_vectors=tfidf_matrix[:len(resume_texts)]
    job_vectors=tfidf_matrix[len(resume_texts):]
    similarity_scores = {}
    

    '''learn vocab and idf, returns document-term matrix
     equivalent to fit followed by transform yet more efficient'''
