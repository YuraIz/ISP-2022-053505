"""Parce command line arguments."""

import argparse


class ArgParcer:
    """Get variables from command line arguments."""

    @staticmethod
    def parce():
        """Run parcer and get args."""
        parcer = argparse.ArgumentParser(description='Process input')
        parcer.add_argument('-n', type=int, default=4, help='legth of n-gram')
        parcer.add_argument(
            '-k',
            type=int,
            default=10,
            help='number of top n-grams to display'
        )
        parcer.add_argument(
            'filename',
            type=argparse.FileType('r'),
            nargs='?',
            default="text.txt",
            help='file to read'
        )
        return parcer.parse_args()

    @staticmethod
    def get_vars() -> tuple[int, int]:
        """Get variables k and n."""
        args = ArgParcer.parce()
        return (args.k, args.n)

    @staticmethod
    def read_file() -> str:
        """Text of file."""
        args = ArgParcer.parce()
        return args.filename.read()
