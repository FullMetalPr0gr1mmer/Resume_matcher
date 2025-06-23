# AI-Powered Resume Scanner & Job Matcher

An intelligent resume screening and job matching tool built with Streamlit and BERT.  
This app allows users to upload multiple resumes and job descriptions, and receive a ranked similarity matrix powered by contextual language understanding (using Sentence-BERT).

## Features

- Upload multiple resumes (`.pdf`) and job descriptions (`.txt` or manual input)
- Match resumes to jobs using semantic similarity with `all-MiniLM-L6-v2`
- Display results in a sortable matrix
- View top N candidates per job in a dynamic table
- Download results as CSV
- Fully functional GUI with Streamlit
- Handles file uploads from any path (not limited to working directory)

## Technologies Used

- Python 3.10+
- [Streamlit](https://streamlit.io/) – for the GUI
- [sentence-transformers](https://www.sbert.net/) – for BERT embeddings
- PyMuPDF (`fitz`) – to extract text from PDFs
- Pandas, NumPy – for data manipulation
- Scikit-learn (optional) – for additional ML utilities
