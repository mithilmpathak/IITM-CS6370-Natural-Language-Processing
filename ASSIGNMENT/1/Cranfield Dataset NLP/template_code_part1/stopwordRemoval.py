from util import *
from nltk.corpus import stopwords
import math
from collections import defaultdict

# Add your import statements here




class StopwordRemoval():

    def fromList(self, text):
        """
        Sentence Segmentation using the Punkt Tokenizer

        Parameters
        ----------
        arg1 : list
            A list of lists where each sub-list is a sequence of tokens
            representing a sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of tokens
            representing a sentence with stopwords removed
        """

        stopwordRemovedText = []

        #Fill in code here
        
        """
        creating set for O(1) look-up
        """
        
        stop_words = set(stopwords.words('english'))
        
        for sentence in text:
            stopwordRemoval = [word for word in sentence if word.lower() not in stop_words]
            stopwordRemovedText.append(stopwordRemoval)
        
        return stopwordRemovedText
    
    
    
    
    
    """
    
    BUILDING CUSTOM (BOTTOM-UP) TOKENIZER USING INFORMATION THEORETIC MEASURE: log(N/n)
    
    """
    def buildCustomList(self, tokenized_documents, threshold=1.0):
        
        """
        Building custom stopword list
        
        Parameters
        -----------------
        tokenized_documents : list
            A list of documents, where each document is a list of sentences,
            and each sentence is a list of tokens.
        
        threshold : float, optional
            The IDF score limit below which a word is a stopword. Default is 1.0.
        
        Returns
        -------------------
        set
            A set of unique stopwords identified from the corpus.
        """
        N = len(tokenized_documents)
        type_counts = defaultdict(set)
        
        for i, document in enumerate(tokenized_documents):
            
            document_words = set(
                word.lower()
                for sentence in document
                for word in sentence
            )
            
            for word in document_words:
                type_counts[word].add(i)
        
        custom_stopwords = set()
        
        for word, docs in type_counts.items():
        
            n = len(docs)
            idf_score = math.log(N/(n))
            
            if idf_score < threshold:
                custom_stopwords.add(word)
        
        return custom_stopwords
    
    def fromCustomList(self, text, custom_stopwords):
        """
        Removes stopwords from tokenized document using bottom-up constructed list.
        
        Parameters
        -----------------
        text: list
            A list of lists where each sub-list is a sequence of tokens representing a sentence.
        
        custom_stopwords: set
            A set of unique tokens identified as stopwords by the bottom-up approach.
        
        
        Returns
        ------------------
        list
            A list of lists where each sub-list is a sequence of tokens with 
            stopwords found using bottom-up approach removed.
        """
        stopwordRemovedText = []
        
        for sentence in text:
            stopwordRemoval = [
                word
                for word in sentence
                if word.lower() not in  custom_stopwords
            ]
            stopwordRemovedText.append(stopwordRemoval)
        
        return stopwordRemovedText
    
    def compareStopwords(self, custom_stopwords, nltk_stopwords):
        
        """
        Performs set comparison operations on bottom-up curated and NLTK English Stopwords.
        
        Parameters
        -----------------
        custom_stopwords: set
            The set of stopwords generated using bottom-up approach.
        nltk_stopwords: set
            The set of stopwords provided by NLTK.
        
        
        Returns
        ----------------
        tuple (set, set, set)
            A tuple containing:
            -overlap: Stopwords present in both lists.
            -only_in_custom: Stopwords identified using bottom-up approach but not in NLTK
            -only_in_nltk: Stopwords in NLTK but not identified by bottom-up approach.
        """
        
        # nltk_stopwords = set(stopwords.words('english'))
        
        overlap = custom_stopwords & nltk_stopwords
        only_in_custom = custom_stopwords - nltk_stopwords
        only_in_nltk = nltk_stopwords - custom_stopwords
        
        return overlap, only_in_custom, only_in_nltk