"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """A class to generate random words from a provided file path to a word list
    >>> wf = WordFinder('words.txt')
    235886 words read

    >>> list = wf.generate_list('words.txt')
    >>> wf.random() in list
    True

    >>> wf.random() in list
    True

    >>> wf.random() in list
    True
    """

    def __init__(self, path):
        """Find list of words"""
        self.path = path
        self.list = self.generate_list(self.path)
        print(f'{len(self.list)} words read')

    def __repr__(self):
        """Show representation """
        return f"<WordFinder, path={self.path} word_count={len(self.list)}>"

    def random(self):
        """Generate a random word from the list"""
        import random
        random_i = random.randrange(len(self.list))
        random_word = self.list[random_i]
        return random_word

    def generate_list(self, path):
        """Reads list of words from a file, returns list of words"""
        file = open(self.path)
        list = []
        for line in file:
            list.append(line[:-1])

        return list


class SpecialWordFinder(WordFinder):
    """A class to generate random words from a provided file path to a word list
    This list may have comments or blank lines that will not be 

    >>> swf = SpecialWordFinder('specialwords.tx')
    4 words read

    >>> list = swf.generate_list('specialwords.tx')
    >>> swf.random() in list
    True

    >>> swf.random() in list
    True

    >>> swf.random() in list
    True"""

    def __init__(self, path):
        # get parent class [`super()`], call its `__init__()`
        super().__init__(path)

    def generate_list(self, path):
        """Reads list of words from a file, returns list of words"""
        file = open(self.path)
        list = []
        for line in file:
            if not line.isspace() and not line.startswith("#"):
                list.append(line[:-1])

        return list
