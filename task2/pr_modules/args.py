"""Parce command line arguments."""

import argparse


class ArgParcer:
    """Get variables from command line arguments."""

    @staticmethod
    def parce():
        """Run parcer and get args."""
        parcer = argparse.ArgumentParser(description='Dump and load objects')
        # --load obj.xml fun.json
        parcer.add_argument('-l', '--load', dest='load', nargs='+', metavar='filename',
                            help='load objects from files')
        parcer.add_argument('-d', '--dump', dest='dump', nargs='+', metavar='filename.py:object:filetype',
                            help='dump object to file')
        return parcer.parse_args()

    @staticmethod
    def items_to_load() -> list[str]:
        """Get filenames."""
        args = ArgParcer.parce()
        return args.load

    @staticmethod
    def items_to_dump() -> list[str]:
        """Get items as filename:object:file_format."""
        args = ArgParcer.parce()
        return args.dump

    @staticmethod
    def getargs():
        args = ArgParcer.parce()
        return (args.dump, args.load)
