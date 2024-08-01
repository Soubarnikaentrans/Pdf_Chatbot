# import fitz  # PyMuPDF
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize
# import string
# from flask import Flask, request, jsonify, render_template
# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np

# nltk.download('punkt')
# nltk.download('stopwords')

# app = Flask(__name__)

# def extract_text_from_pdf(pdf_path):
#     document = fitz.open(pdf_path)
#     text = ""
#     for page_num in range(len(document)):
#         page = document.load_page(page_num)
#         text += page.get_text()
#     return text

# def preprocess_text(text):
#     sentences = sent_tokenize(text)
#     tokens = [word_tokenize(sentence) for sentence in sentences]
#     tokens = [[token.lower() for token in sentence] for sentence in tokens]
#     tokens = [[token for token in sentence if token not in string.punctuation] for sentence in tokens]
#     tokens = [[token for token in sentence if token not in stopwords.words('english')] for sentence in tokens]
#     return [" ".join(sentence) for sentence in tokens], sentences

# pdf_path = 'report.pdf'  
# pdf_text = extract_text_from_pdf(pdf_path)
# processed_text, original_sentences = preprocess_text(pdf_text)

# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(processed_text)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_input = request.json.get("message")
#     response = retrieve_information(user_input)
#     return jsonify({"response": response})

# def retrieve_information(query):
#     query_vec = vectorizer.transform([query.lower()])
#     results = (X * query_vec.T).toarray()
#     relevant_indices = np.argsort(results.flatten())[::-1]
#     top_n = 3  # Number of top results to return
#     relevant_sentences = [original_sentences[i] for i in relevant_indices[:top_n]]
#     return " ".join(relevant_sentences)

# if __name__ == "__main__":
#     app.run(debug=True, port=5001)

# import fitz  # PyMuPDF
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize
# import string
# from flask import Flask, request, jsonify, render_template
# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np
# import requests
# import os

# nltk.download('punkt')
# nltk.download('stopwords')

# app = Flask(__name__)

# # URL of the PDF on GitHub
# pdf_url = "https://raw.githubusercontent.com/Soubarnikaentrans/Glitch/main/report.pdf"
# pdf_path = "report.pdf"

# # Download the PDF from GitHub
# def download_pdf(url, path):
#     response = requests.get(url)
#     response.raise_for_status()  # Check if the request was successful
#     with open(path, 'wb') as file:
#         file.write(response.content)

# def extract_text_from_pdf(pdf_path):
#     if not os.path.exists(pdf_path):
#         print(f"File {pdf_path} does not exist.")
#         return ""
#     try:
#         document = fitz.open(pdf_path)
#         text = ""
#         for page_num in range(len(document)):
#             page = document.load_page(page_num)
#             text += page.get_text()
#         return text
#     except Exception as e:
#         print(f"An error occurred while extracting text from PDF: {e}")
#         return ""

# def preprocess_text(text):
#     try:
#         sentences = sent_tokenize(text)
#         tokens = [word_tokenize(sentence) for sentence in sentences]
#         tokens = [[token.lower() for token in sentence] for sentence in tokens]
#         tokens = [[token for token in sentence if token not in string.punctuation] for sentence in tokens]
#         tokens = [[token for token in sentence if token not in stopwords.words('english')] for sentence in tokens]
#         return [" ".join(sentence) for sentence in tokens], sentences
#     except Exception as e:
#         print(f"An error occurred during text preprocessing: {e}")
#         return [], []

# # Download the PDF file
# try:
#     download_pdf(pdf_url, pdf_path)
#     print(f"PDF downloaded successfully from {pdf_url}")
# except Exception as e:
#     print(f"An error occurred while downloading the PDF: {e}")

# # Extract and preprocess text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)
# processed_text, original_sentences = preprocess_text(pdf_text)

# # Check if the text extraction and preprocessing were successful
# if not processed_text:
#     raise Exception("Text extraction or preprocessing failed. Check the PDF file and path.")

# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(processed_text)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_input = request.json.get("message")
#     response = retrieve_information(user_input)
#     return jsonify({"response": response})

# def retrieve_information(query):
#     query_vec = vectorizer.transform([query.lower()])
#     results = (X * query_vec.T).toarray()
#     relevant_indices = np.argsort(results.flatten())[::-1]
#     top_n = 3  # Number of top results to return
#     relevant_sentences = [original_sentences[i] for i in relevant_indices[:top_n]]
#     return " ".join(relevant_sentences)

# if __name__ == "__main__":
#     app.run(debug=True, port=5001)

# import fitz  # PyMuPDF
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize
# import string
# from flask import Flask, request, jsonify, render_template
# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np
# import requests
# import os

# nltk.download('punkt')
# nltk.download('stopwords')

# app = Flask(__name__)

# # URL of the PDF on GitHub
# pdf_url = "https://raw.githubusercontent.com/Soubarnikaentrans/Glitch/main/report.pdf"
# pdf_path = "file"

# # Download the PDF from GitHub
# def download_pdf(url, path):
#     print(f"Current working directory: {os.getcwd()}")
#     print(f"Downloading PDF from {url} to {path}")
    
#     response = requests.get(url)
#     response.raise_for_status()  # Check if the request was successful
#     with open(path, 'wb') as file:
#         file.write(response.content)
#     print(f"PDF downloaded to {path}")

# def extract_text_from_pdf(pdf_path):
#     if not os.path.exists(pdf_path):
#         print(f"File {pdf_path} does not exist.")
#         return ""
#     try:
#         document = fitz.open(pdf_path)
#         text = ""
#         for page_num in range(len(document)):
#             page = document.load_page(page_num)
#             text += page.get_text()
#         return text
#     except Exception as e:
#         print(f"An error occurred while extracting text from PDF: {e}")
#         return ""

# def preprocess_text(text):
#     try:
#         sentences = sent_tokenize(text)
#         tokens = [word_tokenize(sentence) for sentence in sentences]
#         tokens = [[token.lower() for token in sentence] for sentence in tokens]
#         tokens = [[token for token in sentence if token not in string.punctuation] for sentence in tokens]
#         tokens = [[token for token in sentence if token not in stopwords.words('english')] for sentence in tokens]
#         return [" ".join(sentence) for sentence in tokens], sentences
#     except Exception as e:
#         print(f"An error occurred during text preprocessing: {e}")
#         return [], []

# # Download the PDF file
# try:
#     download_pdf(pdf_url, pdf_path)
#     print(f"PDF downloaded successfully from {pdf_url}")
# except Exception as e:
#     print(f"An error occurred while downloading the PDF: {e}")

# # Extract and preprocess text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)
# processed_text, original_sentences = preprocess_text(pdf_text)

# # Check if the text extraction and preprocessing were successful
# if not processed_text:
#     raise Exception("Text extraction or preprocessing failed. Check the PDF file and path.")

# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(processed_text)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_input = request.json.get("message")
#     print(f"Received message: {user_input}")
#     response = retrieve_information(user_input)
#     print(f"Response: {response}")
#     return jsonify({"response": response})

# def retrieve_information(query):
#     query_vec = vectorizer.transform([query.lower()])
#     results = (X * query_vec.T).toarray()
#     relevant_indices = np.argsort(results.flatten())[::-1]
#     top_n = 3  # Number of top results to return
#     relevant_sentences = [original_sentences[i] for i in relevant_indices[:top_n]]
#     return " ".join(relevant_sentences)

# if __name__ == "__main__":
#     app.run(debug=True, port=3000)

# import fitz  # PyMuPDF
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize
# import string
# from flask import Flask, request, jsonify, render_template
# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np
# import requests
# import io
# import os

# # Download necessary NLTK data
# import nltk
# nltk.download('punkt', quiet=True)
# nltk.download('stopwords', quiet=True)

# app = Flask(__name__)

# # URL of the PDF on GitHub
# pdf_url = "https://raw.githubusercontent.com/Soubarnikaentrans/Glitch/main/report.pdf"

# # Download and process the PDF from GitHub
# def download_pdf_from_url(url):
#     response = requests.get(url)
#     response.raise_for_status()  # Check if the request was successful
#     return io.BytesIO(response.content)

# def extract_text_from_pdf(pdf_stream):
#     document = fitz.open(stream=pdf_stream)
#     text = ""
#     for page_num in range(len(document)):
#         page = document.load_page(page_num)
#         text += page.get_text()
#     return text

# def preprocess_text(text):
#     sentences = sent_tokenize(text)
#     tokens = [word_tokenize(sentence) for sentence in sentences]
#     tokens = [[token.lower() for token in sentence] for sentence in tokens]
#     tokens = [[token for token in sentence if token not in string.punctuation] for sentence in tokens]
#     tokens = [[token for token in sentence if token not in stopwords.words('english')] for sentence in tokens]
#     return [" ".join(sentence) for sentence in tokens], sentences

# # Fetch the PDF from GitHub and process it
# pdf_stream = download_pdf_from_url(pdf_url)
# pdf_text = extract_text_from_pdf(pdf_stream)
# processed_text, original_sentences = preprocess_text(pdf_text)

# # Check if the text extraction and preprocessing were successful
# if not processed_text:
#     raise Exception("Text extraction or preprocessing failed. Check the PDF file and path.")

# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(processed_text)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_input = request.json.get("message")
#     response = retrieve_information(user_input)
#     return jsonify({"response": response})

# def retrieve_information(query):
#     query_vec = vectorizer.transform([query.lower()])
#     results = (X * query_vec.T).toarray()
#     relevant_indices = np.argsort(results.flatten())[::-1]
#     top_n = 3  # Number of top results to return
#     relevant_sentences = [original_sentences[i] for i in relevant_indices[:top_n]]
#     return " ".join(relevant_sentences)

# if __name__ == "__main__":
#     port = int(os.environ.get('PORT', 3000))
#     app.run(host='0.0.0.0', port=port)

from pdfminer.high_level import extract_text
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string
from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import requests
import io
import os
import nltk

# Set up NLTK data path
nltk_data_dir = "/tmp/nltk_data"
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

nltk.download('punkt', download_dir=nltk_data_dir, quiet=True)
nltk.download('stopwords', download_dir=nltk_data_dir, quiet=True)

app = Flask(__name__)

# URL of the PDF on GitHub
pdf_url = "https://raw.githubusercontent.com/Soubarnikaentrans/Glitch/main/report.pdf"

def download_pdf_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    return io.BytesIO(response.content)

def extract_text_from_pdf(pdf_stream):
    text = extract_text(pdf_stream)
    return text

def preprocess_text(text):
    sentences = sent_tokenize(text)
    tokens = [word_tokenize(sentence) for sentence in sentences]
    tokens = [[token.lower() for token in sentence] for sentence in tokens]
    tokens = [[token for token in sentence if token not in string.punctuation] for sentence in tokens]
    tokens = [[token for token in sentence if token not in stopwords.words('english')] for sentence in tokens]
    return [" ".join(sentence) for sentence in tokens], sentences

# Fetch the PDF from GitHub and process it
pdf_stream = download_pdf_from_url(pdf_url)
pdf_text = extract_text_from_pdf(pdf_stream)
processed_text, original_sentences = preprocess_text(pdf_text)

if not processed_text:
    raise Exception("Text extraction or preprocessing failed. Check the PDF file and path.")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_text)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = retrieve_information(user_input)
    return jsonify({"response": response})

def retrieve_information(query):
    query_vec = vectorizer.transform([query.lower()])
    results = (X * query_vec.T).toarray()
    relevant_indices = np.argsort(results.flatten())[::-1]
    top_n = 3  # Number of top results to return
    relevant_sentences = [original_sentences[i] for i in relevant_indices[:top_n]]
    return " ".join(relevant_sentences)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)