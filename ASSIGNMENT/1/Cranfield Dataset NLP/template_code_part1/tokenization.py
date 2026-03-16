from util import *
import re
from nltk.tokenize.treebank import TreebankWordTokenizer, TreebankWordDetokenizer
from spacy.lang.en import English
# Add your import statements here
# (Students may import required libraries such as nltk, spacy, re, etc.)


class Tokenization():

    def naive(self, text):
        """
        Tokenization using a Naive Approach

        Parameters
        ----------
        arg1 : list
            A list of strings where each string is a single sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of tokens
        """
        tokenizedText = []
        for sentence in text:
            tokens = re.findall(r"[A-Za-z0-9']+|[.,!?;]", sentence)
            tokenizedText.append(tokens)
        
        return tokenizedText



    def pennTreeBank(self, text):
        """
        Tokenization using the Penn Tree Bank Tokenizer

        Parameters
        ----------
        arg1 : list
            A list of strings where each string is a single sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of tokens
        """
        
        
        tokenizedText = []
        

        # Fill in code here
        tokenizer = TreebankWordTokenizer()
        for s in text:
            t = tokenizer.tokenize(s)
            tokenizedText.append(t)

        return tokenizedText



    def spacyTokenizer(self, text):
        """
        Tokenization using spaCy

        Parameters
        ----------
        arg1 : list
            A list of strings where each string is a single sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of tokens
        """

        tokenizedText = []
        
        # Fill in code here
        nlp = English()
        tokenizer = nlp.tokenizer
        
        for sentence in text:
            tokens = [tok.text for tok in tokenizer(sentence)]
            tokenizedText.append(tokens)
        
        return tokenizedText
