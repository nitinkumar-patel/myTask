import os
import sys


class StrTest:

    def __init__(self, str_1, str_2):
        self.str_1 = set(str_1)
        self.str_2 = set(str_2)

    def common(self):
        print "output common characters-" + ''.join(sorted(self.str_1 & self.str_2))
        return ''.join(sorted(self.str_1 & self.str_2))

    def unique(self):
        print "output unique characters-" + ''.join(sorted(self.str_1 ^ self.str_2))
        return ''.join(sorted(self.str_1 ^ self.str_2))


def main(argv):
    str_1 = set(argv[0])
    str_2 = set(argv[1])

    print "output common characters-" + ''.join(sorted(str_1 & str_2))
    print "output unique characters-" + ''.join(sorted(str_1 ^ str_2))


if __name__ == "__main__":
    main(sys.argv[1:])
