import random
class Poetry():
<<<<<<< HEAD
    """Classe permettant de lire, couper, choisir et utiliser les vers et les mots."""
=======
    """Read, cut, choose and use sentences and words of the poetry."""
>>>>>>> 7d6510ccb500526083c47b7114b79209bd1a0c53
    towards = []
    words = []
    poetry = open("resources/documents/poeme.txt", encoding='utf8')
    towards_unsplited = poetry.readlines()
    def __init__(self):
        self.poetry = Poetry.towards_unsplited
        self.towards = Poetry.towards
        self.words = Poetry.words

    def split_poetry(self):
<<<<<<< HEAD
            for line in self.poetry:
                    words_splited = line.split(' ')
                    self.towards.append(words_splited)
            return self.towards

    def choose_words(self):
            self.towards = Poetry().split_poetry()
            i = 0
            for __ in self.towards:
                    random_choice = random.choice(self.towards[i])
                    i += 1
                    self.words.append(random_choice)
            return self.words

    def save_words(self):
                remove_words = Poetry().choose_words()
                return remove_words
words = Poetry().choose_words()
print(words)
=======
        '''
        Return the poetry after splitting each sentences between them and put it into towards list.
        :return: list
        '''
        for line in self.poetry:
                words_splited = line.split(' ')
                self.towards.append(words_splited)
        return self.towards

    def choose_words(self):
        '''
        Choose a random word in each sentence and put it into words list.
        :return: list
        '''
        self.towards = Poetry().split_poetry()
        i = 0
        for __ in self.towards:
                random_choice = random.choice(self.towards[i])
                i += 1
                self.words.append(random_choice)
        return self.words

print(Poetry.choose_words())
>>>>>>> 7d6510ccb500526083c47b7114b79209bd1a0c53
