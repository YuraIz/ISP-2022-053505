"""Module for simple text analyzing."""

import re

from simple_math import average, median


class Analyzer:
    """Class for text analyzing."""

    def __init__(self, text: str) -> None:
        """Create analyzer for text."""
        self.text = text

    def count_items(self, items: list) -> dict[any, int]:
        """Return sorted dictionary with count for each item."""
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
        """Return average and median word count per sentence."""
        sentences = re.split(r'\.|!|\?', self.text)
        sentences = list(filter(lambda sentence: sentence != '', sentences))
        count_per_sentence = [len(sentence.split()) for sentence in sentences]

        return (average(count_per_sentence), median(count_per_sentence))

    def count_words(self) -> dict[str, int]:
        """Сount the repetitions for each word."""
        words = re.split("[^a-zа-я']", self.text.lower())
        words = list(filter(lambda word: word != '', words))

        return self.count_items(words)

    def top_ngrams(self, k: int = 10, n: int = 4) -> dict[str, int]:
        """Return top k ngrams."""
        words = re.split("[^a-zа-я]", self.text.lower())
        words = list(filter(lambda word: len(word) >= n, words))

        ngrams = list()
        for word in words:
            ngrams_in_word = list(zip(*[word[i:] for i in range(n)]))
            for ngram in ngrams_in_word:
                ngrams.append(''.join(ngram))

        ngrams_count = self.count_items(ngrams)

        return dict(list(ngrams_count.items())[:k])
