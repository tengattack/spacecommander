# StarNullabilitySpacer.py
# clang-format gets confused by nullability annotations, fix this in some simple cases
#
# If a filename is specified as a parameter, it will change that file in place.
# If input is provided through stdin, it will send the result to stdout.
# Copyright 2020 tengattack

from AbstractCustomFormatter import AbstractCustomFormatter

class StarNullabilitySpacer(AbstractCustomFormatter):
    def format_lines(self, lines):

        lines_to_write = []
        for line in lines:
            to_append = line
            # Check if the line contains with *_Nonnull or *_Nullable, but with no spaces in between
            if '*_Nonnull' in to_append:
                to_append = to_append.replace('*_Nonnull', '* _Nonnull')
            if '*_Nullable' in to_append:
                to_append = to_append.replace('*_Nullable', '* _Nullable')

            lines_to_write.append(to_append)

        return "".join(lines_to_write)

if __name__ == "__main__":
    StarNullabilitySpacer().run()
