
import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from difflib import SequenceMatcher
# import PyPDF2
from odf import text, teletype
from odf.opendocument import load
import io
import pdfminer
from pdfminer.high_level import extract_text
import docx
import os

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')

# !pip install pdfminer.six
# !pip install odfpy
# !pip install ODTReader


def extract_text_from_odt(odt_file_path):
    text_content = ""
    textdoc = load(odt_file_path)
    allparas = textdoc.getElementsByType(text.P)

    for para in allparas:
        text_content += teletype.extractText(para)

    return text_content


def extract_text_from_txt(txt_file_path):
    with open(txt_file_path, 'r') as txt_file:
        text = txt_file.read()

    return text


def extract_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, "rb") as pdf_file:
        text = extract_text(pdf_file)

    return text


def extract_text_from_docx(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


def text_lowercase(text):
    return text.lower()


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def remove_whitespace(text):
    return " ".join(text.split())


def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return filtered_text


def stem_words(text):
    stemmer = PorterStemmer()
    stemmed_list = []
    for i in text:
        words = word_tokenize(i)
        stemmed_text = ' '.join([stemmer.stem(word) for word in words])
        stemmed_list.append(stemmed_text)
    return stemmed_list


def lemmatize_word(strings_list):
    lemmatizer = WordNetLemmatizer()
    lemmatized_list = []
    for text in strings_list:
        words = word_tokenize(text)
        lemmatized_text = ' '.join(
            [lemmatizer.lemmatize(word) for word in words])
        lemmatized_list.append(lemmatized_text)
    return lemmatized_list


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def split_file_path(file_path):
    base_path, file_extension = os.path.splitext(file_path)
    return file_extension


def main(file_path1, file_path2):
    file1_ext = split_file_path(file_path1)
    file2_ext = split_file_path(file_path2)
    text1 = ""
    text2 = ""
    if file1_ext == '.pdf':
        text1 = extract_text_from_pdf(file_path1)
    elif file1_ext == '.txt':
        text1 = extract_text_from_txt(file_path1)
    elif file1_ext == '.odt':
        text1 = extract_text_from_odt(file_path1)
    elif file1_ext == '.docx':
        text1 = extract_text_from_docx(file_path1)
    else:
        print('File format not supported !!')

    if file2_ext == '.pdf':
        text2 = extract_text_from_pdf(file_path2)
    elif file2_ext == '.txt':
        text2 = extract_text_from_txt(file_path2)
    elif file2_ext == '.odt':
        text2 = extract_text_from_odt(file_path2)
    elif file2_ext == '.docx':
        text2 = extract_text_from_docx(file_path2)
    else:
        print('File format not supported !!')

    text1 = text_lowercase(text1)
    text2 = text_lowercase(text2)
    text1 = remove_punctuation(text1)
    text2 = remove_punctuation(text2)
    text1 = remove_whitespace(text1)
    text2 = remove_whitespace(text2)
    text1 = remove_stopwords(text1)
    text2 = remove_stopwords(text2)
    text1 = stem_words(text1)
    text2 = stem_words(text2)
    text1 = lemmatize_word(text1)
    text2 = lemmatize_word(text2)
    similarity = similar(text1, text2)
    # print(similarity)
    return similarity
