# AI-Based-Resume-Analysis

# NLP Resume Analyzer (Word2Vec)

A high-performance NLP application that evaluates resumes against job descriptions by understanding the semantic meaning behind candidate skills and experience. Instead of relying on strict keyword matches, this analyzer uses pre-trained word embeddings to capture context, synonyms, and conceptual similarities.

## Project Description
The core challenge in resume screening is that candidates and recruiters often use different words to describe the same concepts (e.g., "Python Developer" vs. "Software Engineer proficient in Python"). 

This project solves that by loading a **Word2Vec** model via **Gensim** to represent words as dense vectors in a continuous space. By calculating the average word vector for a resume and comparing it against the average vector of a job description, the analyzer computes a **Cosine Similarity** score. This allows the tool to successfully rank resumes that are conceptually aligned with the job requirement, even when direct keyword matches are sparse.

## Features
* **Semantic Vector Matching:** Leverages Word2Vec to match synonyms and related technical concepts.
* **Gensim Integration:** Uses Gensim for efficient loading, vocabulary building, and similarity queries on vector spaces.
* **Text Normalization:** Automated pipeline using NLTK/SpaCy for stop-word removal, tokenization, and lowercasing.
* **Similarity Score:** Generates a clean cosine similarity ranking between 0 and 1.
* **Gap Spotting:** Pinpoints specific structural skills present in the JD but missing in the resume's vector neighborhood.

## Tech Stack
* **Language:** Python 3.x
* **Vector Embeddings & Modeling:** Gensim (Word2Vec)
* **NLP Processing:** NLTK / SpaCy (for tokenization & cleaning)
* **Text Extraction:** pdfplumber / PyPDF2 (for PDFs), docx2txt (for DOCX)
* **Vector Math:** NumPy, Scikit-learn (Cosine Similarity)
* **UI (Optional):** Streamlit

## Project Structure
~
├── models/                # Saved Word2Vec models
├── data/                  # Resumes and Job Descriptions
├── src/
│   ├── parser.py          # PDF and Word document text extractors
│   ├── preprocess.py      # Lowercasing, stop-word removal, tokenization
│   └── vector_engine.py   # Gensim Word2Vec averaging & similarity logic
├── app.py                 # Main execution file
├── requirements.txt
└── README.md
~
