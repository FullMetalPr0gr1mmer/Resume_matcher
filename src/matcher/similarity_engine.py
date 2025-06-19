from sklearn.feature_extraction.text import TfidfVectorizer
'''The difference between feature_extraction and feature_selection 
the former is used to transform arbitrary data such as images and text into numerical features usable for ML
while the latter is used a technique used by ML on the features'''
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_texts,job_texts):
    all_texts =list(resume_texts.values())+list(job_texts.values())
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    '''learn vocab and idf, returns document-term matrix
     equivalent to fit followed by transform yet more efficient'''

    resume_vectors=tfidf_matrix[:len(resume_texts)]
    job_vectors=tfidf_matrix[len(resume_texts):]
    similarity_scores = {}
    for i,(resume_name,_) in enumerate(resume_texts.items()):
        scores={}
        for j,(job_name,_) in enumerate(job_texts.items()):
            score=cosine_similarity(resume_vectors[i],job_vectors[j])[0][0] #sklearn Cosine similarity returns 2D vectors
            # thats why we use [0][0]to access the single float value
            scores[job_name]=round(score,4)
        similarity_scores[resume_name]=scores
    return similarity_scores

def rank_matches(similarity_scores,top_k=3):
    ranked_results={}
    for resume,scores in similarity_scores.items():
        sorted_scored=sorted(scores.items(),key=lambda x:x[1],reverse=True)

        ranked_results[resume]=sorted_scored[:top_k]
    return ranked_results


