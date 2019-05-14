import random

poetry = open("resources/documents/poeme.txt")


def split_poetry(words):
        ListLines = poetry.readlines()
        ListWords = []
        for line in ListLines:
                words = line.split(' ')
                ListWords.append(words)
        return words
def choose_words():
        wordsplited = split_poetry(1)
        words = random.sample(wordsplited, k=5)
        words2 = random.sample(wordsplited, k=5)
        words3 = (random.sample(wordsplited, k=5)
        words.append(words2)
        print(words)
        return

choose_words()