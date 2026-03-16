from util import *

# Add your import statements here
import re
import nltk
import spacy
from nltk.tokenize import sent_tokenize


class SentenceSegmentation():

    def __init__(self):
        # Load spaCy model (students may use this if needed)
        self.nlp = spacy.load("en_core_web_sm")
    
    def naive(self, text):
        """
        Sentence Segmentation using a Naive Approach
        
        Parameters
        ----------
        arg1 : str
            A string (a bunch of sentences)
            
        Returns
        -------
        list
            A list of strings where each string is a single sentence
        """
        
        segmentedText = None
        
        # Fill in code here
        segmentedText = re.split(r'[.!?:]+', text)
        segmentedText = [sentence.strip() for sentence in segmentedText if sentence.strip()]
        
        return segmentedText


    def punkt(self, text):
        """
        Sentence Segmentation using the Punkt Tokenizer
        
        Parameters
        ----------
        arg1 : str
            A string (a bunch of sentences)

        Returns
        -------
        list
            A list of strings where each string is a single sentence
        """

        segmentedText = None

        # Fill in code here
        """
        download pre-trained Punkt model, uncomment
        """
        # nltk.download('punkt)
        segmentedText = sent_tokenize(text)

        return segmentedText


    def spacySegmenter(self, text):
        """
        Sentence Segmentation using spaCy

        Parameters
        ----------
        arg1 : str
            A string (a bunch of sentences)

        Returns
        -------
        list
            A list of strings where each string is a single sentence
        """
        
        

        # Fill in code here
        
        """
        switching off named entitiy recognition and POS tagging as spacy was taking too long to segment.
        """
        document = self.nlp(text, disable=["ner", "lemmatizer"])
        segmentedText = [sentence.text.strip() for sentence in document.sents]
        return segmentedText
