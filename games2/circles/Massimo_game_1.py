import random

poetry = open("resources/documents/poeme.txt", encoding='utf8')


def split_poetry(ListWords):
        ListLines = poetry.readlines()
        ListWords = []
        for line in ListLines:
                words = line.split(' ')
                ListWords.append(words)
        return ListWords
def choose_words(words):
        words = []
        linesplited = split_poetry(1)
        i=0
        for __ in linesplited:
                wordsplited = random.choice(linesplited[i])
                i += 1
                words.append(wordsplited)
        return words

words = choose_words(1)
towards = split_poetry(1)