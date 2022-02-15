"""Entry point for program."""

from args import ArgParcer
from text_analyzing import Analyzer


class Program:
    """Class with main function."""

    @staticmethod
    def print_dict(dictionary: dict) -> None:
        """Print keys and values."""
        for (key, value) in dictionary.items():
            print(f'{key}: {value}')

    @staticmethod
    def main():
        """Entry point."""
        k, n = ArgParcer.get_vars()
        text = ArgParcer.read_file()
        analyzer = Analyzer(text)

        word_map = analyzer.count_words()
        print("how many times each word is repeated in the text:")
        Program.print_dict(word_map)

        average, median = analyzer.words_per_sentence()

        print(f'average number of words in a sentence: {average:.3f}')
        print(f'median number of words in a sentence: {median}')

        ngram_dict = analyzer.top_ngrams(k, n)
        Program.print_dict(ngram_dict)


Program.main()
