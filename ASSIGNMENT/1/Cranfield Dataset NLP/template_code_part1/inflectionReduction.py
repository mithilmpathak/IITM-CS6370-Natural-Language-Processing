from util import *
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Add your import statements here
# (Students may import required libraries such as nltk, WordNetLemmatizer, PorterStemmer, etc.)


class InflectionReduction:

    def porterStemmer(self, text):
        """
        Inflection Reduction using Porter Stemmer

        Parameters
        ----------
        arg1 : list
            A list of lists where each sub-list is a sequence of tokens
            representing a sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of
            stemmed tokens representing a sentence
        """

        reducedText = []
        
        # Fill in code here
        stemmer = PorterStemmer()
        for sentence in text:
            reducedSentence = [stemmer.stem(word) for word in sentence]
            reducedText.append(reducedSentence)
        return reducedText



    def wordnetLemmatizer(self, text):
        """
        Inflection Reduction using WordNet Lemmatizer

        Parameters
        ----------
        arg1 : list
            A list of lists where each sub-list is a sequence of tokens
            representing a sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of
            lemmatized tokens representing a sentence
        """

        reducedText = []

        # Fill in code here
        lemmatizer = WordNetLemmatizer()
        for sentence in text:
            reducedSentence = [lemmatizer.lemmatize(word) for word in sentence]
            reducedText.append(reducedSentence)

        return reducedText



    def reduce(self, text, option="stem"):
        """
        Wrapper function for inflection reduction.
        Students may choose which method to call
        or extend this function to support both options.
        """
        
        
        """
        Parameters
        ----------------
        arg1: list
            A list of lists where each sub-list is a sequence of tokens
            representing a sentence.
        
        
        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of
            lemmatized/stemmed tokens (based on user's choice) representing a sentence.
        """
        reducedText = None

        # Fill in code here
        if option == "stem":
            reducedText = self.porterStemmer(text)
        elif option == "lemmatize":
            reducedText = self.wordnetLemmatizer(text)
        else:
            reducedText = text
        return reducedText
