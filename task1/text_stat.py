import sys

from numpy import average, median
import re

argv = sys.argv
argc = len(argv)

if(argc == 2 or argc == 4):
    fileName = sys.argv[1]
else:
    fileName = "text.txt"

if(len(sys.argv) == 3):
    k = int(sys.argv[1])
    n = int(sys.argv[2])
elif(len(sys.argv) == 4):
    k = int(sys.argv[2])
    n = int(sys.argv[3])
else:
    k = 10
    n = 4

file = open(fileName)
text = file.read()


class Analyzer:
    """class for text analyzing"""

    def __init__(self, text: str) -> None:
        self.text = text

    def count_items(self, items: list) -> dict[any, int]:
        """sorted dictionary with count for each item"""
        dictionary = dict()
        for item in items:
            dictionary[item] = dictionary.get(item, 0) + 1
        sorted_items = sorted(dictionary.items(),
                              key=lambda item: item[1],
                              reverse=True
                              )
        dictionary = dict(sorted_items)
        return dictionary

    def words_per_sentence(self) -> tuple[float, float]:
        """average and median word count per sentence"""

        sentences = re.split("\n|\.|!|\?", self.text)
        sentences = list(filter(lambda sentence: sentence != '', sentences))
        count_per_sentence = [len(sentence.split()) for sentence in sentences]

        return (average(count_per_sentence), median(count_per_sentence))

    def count_words(self) -> dict[str, int]:
        """count for each word"""
        # can't add symbols
        words = re.split("[^a-zа-я']", self.text.lower())
        words = list(filter(lambda word: word != '', words))

        return self.count_items(words)

    def top_ngrams(self, k: int = 10, n: int = 4) -> dict[str, int]:
        """dictionary with top k ngrams"""

        words = re.split("[^a-zа-я]", self.text.lower())
        words = list(filter(lambda word: len(word) >= n, words))

        ngrams = list()
        for word in words:
            ngrams_in_word = list(zip(*[word[i:] for i in range(n)]))
            for ngram in ngrams_in_word:
                ngrams.append(''.join(ngram))

        ngrams_count = self.count_items(ngrams)

        return dict(list(ngrams_count.items())[:k])


def print_dict(dictionary: dict) -> None:
    """prints keys and values"""
    for (key, value) in dictionary.items():
        print(f'{key}: {value}')
    return


analyzer = Analyzer(text)

word_map = analyzer.count_words()
print("how many times each word is repeated in the text:")
print_dict(word_map)

average, median = analyzer.words_per_sentence()

print(f'average number of words in a sentence: {average:.3f}')
print(f'median number of words in a sentence: {median}')

ngram_dict = analyzer.top_ngrams(k, n)
print_dict(ngram_dict)
