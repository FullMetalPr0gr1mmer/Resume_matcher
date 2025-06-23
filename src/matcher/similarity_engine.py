from sklearn.feature_extraction.text import TfidfVectorizer



'''The difference between feature_extraction and feature_selection 
the former is used to transform arbitrary data such as images and text into numerical features usable for ML
while the latter is used a technique used by ML on the features'''
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util
import numpy as np
# the below compute similarity uses tf_idf vectors
'''
def compute_similarity(resume_texts,job_texts):
    all_texts =list(resume_texts.values())+list(job_texts.values())
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
   #learn vocab and idf, returns document-term matrix
    # equivalent to fit followed by transform yet more efficient

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
'''

# the below compute similarity uses Bert model
model = SentenceTransformer("all-MiniLM-L6-v2")
#Computes semantic similarity between resumes and job descriptions using BERT embeddings.
def compute_similarity(resume_texts,job_texts):


    candidate_names=list(resume_texts.keys())
    job_titles=list(job_texts.keys())

    candidate_resumes = list(resume_texts.values())
    job_descriptions = list(job_texts.values())

    resume_embeddings = model.encode(candidate_resumes,convert_to_tensor=True)
    job_embeddings = model.encode(job_descriptions,convert_to_tensor=True)

    similarity_matrix = util.cos_sim(resume_embeddings,job_embeddings).cpu().numpy()

    final_result = {}
    for i,c_name in enumerate(candidate_names):
        final_result[c_name]={}
        for j,j_title in enumerate(job_titles):
            final_result[c_name][j_title]=float(similarity_matrix[i][j])
    return final_result

def rank_matches(similarity_scores,top_k=3):
    ranked_results={}
    for resume,scores in similarity_scores.items():
        sorted_scored=sorted(scores.items(),key=lambda x:x[1],reverse=True)

        ranked_results[resume]=sorted_scored[:top_k]
    return ranked_results
'''
SentenceTransformer: This is the main class from the library used to load models that can turn sentences into embeddings.
"all-MiniLM-L6-v2": This is the name of a specific, pre-trained model.
 It's known for being very fast and highly effective for general-purpose semantic similarity tasks.
Global Scope: This line is placed outside the function. This is a critical optimization.
The model is loaded into memory only once when the script starts. If it were inside the function,
it would have to be reloaded every single time the function is called, which would be extremely slow.

model.encode(...): This method takes a list of texts and feeds them through the MiniLM neural network.
The Output (Embeddings): For each text, it outputs a fixed-size numerical vector (an "embedding").
For this model, it's a vector of 384 numbers. This vector represents the semantic meaning of the text in a high-dimensional space.
Texts with similar meanings will have vectors that are numerically close to each other.
convert_to_tensor=True: This tells the function to output the embeddings as PyTorch Tensors,
 which are special arrays optimized for high-performance numerical computations, especially on a GPU.


'''

