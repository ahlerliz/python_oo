from random import choice 

class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> wf = WordFinder("dictionary.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    
    """

    def __init__(self, file_url):
        """ Creates a WordFinder starting from a specified file """
        self.file_url = file_url
        self.word_list = self.read_file()

    def __repr__(self):
        """ This function describes the class when called"""
        return f"A WordFinder that finds random words from dictionary at {self.file_url}"

    def read_file(self):
        """ Opens the file at the specified file_url and stores the words in word_list """
        word_file = open(f"{self.file_url}", "r")
        self.word_list = word_file.readlines()

        corrected_word_list = [word.replace("\n", "") for word in self.word_list]
        #self.word_list = corrected_word_list

        print(f"{len(corrected_word_list)} words read")

        return corrected_word_list

    def random(self):
        """ Returns a random choice from the word_list"""
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """Word Finder: finds random words from a dictionary.
    
    >>> wf = SpecialWordFinder("dictionary.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    
    """

    
    def read_file(self):
        """Opens the file at the specified file_url and stores the words in word_list, removing empty lines and comments"""

        word_list = super().read_file()

        new_word_list=[word for word in word_list if not (word == "" or word.startswith("#"))]
        return new_word_list


    
    