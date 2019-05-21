import random
class Poetry():
    """Classe permettant de lire, couper, choisir et utiliser les vers et les mots."""
    towards = []
    words = []
    poetry = open("resources/documents/poeme.txt", encoding='utf8')
    towards_unsplited = poetry.readlines()
    def __init__(self):
        self.poetry = Poetry.towards_unsplited
        self.towards = Poetry.towards
        self.words = Poetry.words

    def split_poetry(self):
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
