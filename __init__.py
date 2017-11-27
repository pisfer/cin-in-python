import re


class ArgumentError(Exception):
    def __init__(self, message):
        super().__init__(message)

        
class cin:
    """cin func in python"""

    def __init__(self, *args, n):
        self.args = args
        self.n = n
        self.pora = "(?P<" + self.args[0] + ">.*)"
        self.index = ""
        self.vbn = {}
        for self.g in self.args[1:]:
            self.pora = self.pora + "\s+(?P<" + self.g + ">.*)"
        self.i = input(self.n)
        self.hpo = re.match(self.pora, self.i)
        if self.hpo:
            for self.k in self.args:
                self.vbn[self.k] = self.hpo.group(self.k)
        else:
            raise ArgumentError("You inserted false arguments")

    def get(self, index):
        self.index = index
        return self.vbn[self.index]


if __name__ == '__main__':
    print(cin("b", "n", n="d").get("b"))
