# Assignment 1: Search Engine Preprocessing Pipeline

This project implements a modular preprocessing pipeline for the **Cranfield Dataset**, focusing on fundamental Natural Language Processing techniques used in search engines.

---

## 📑 Assignment Overview

The goal of this assignment was to implement and analyze four foundational NLP preprocessing stages:

1. **Sentence Segmentation**  
   Comparison of a naive regex-based approach, NLTK Punkt, and spaCy.

2. **Tokenization**  
   Implementation and comparison of Penn Treebank (PTB) tokenization and spaCy tokenization.

3. **Inflection Reduction**  
   Evaluation of **Porter Stemming** vs **WordNet Lemmatization**.

4. **Stopword Removal**  
   Comparison between curated NLTK stopword lists and a data-driven **Bottom-Up stopword detection approach**.

---

## 🧪 Adversarial Test Suite

A custom test suite of **15 adversarial sentences** was designed to evaluate sentence segmentation robustness against:

- abbreviations  
- acronyms  
- decimal numbers  
- technical formatting

---

## 📊 Performance & Complexity

### Vocabulary Reduction

| Stage | Vocabulary Size |
|------|------|
| Original | 8,371 |
| Stemmed | 5,734 |
| Lemmatized | 7,557 |

### Retrieval Complexity

**Naive Similarity Computation**

---

## 🚀 How to Run

Ensure **Python 3.12** is installed.

```bash
# Standard Run
py 3.12 main.py -dataset ../cranfield

# Custom Query Mode
py 3.12 main.py -dataset ../cranfield -custom

# Choose Reducer (stem or lemmatize)
py 3.12 main.py -dataset ../cranfield -reducer lemmatize