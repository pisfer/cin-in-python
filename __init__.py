import re


class ArgumentError(Exception):
    def __init__(self, message):
        super().__init__(message)

        
class cin:
    """cin func in python"""

    def __init__(self, *args, text):
        self.args = args
        self.n = text
        self.pora = "(?P<" + self.args[0] + ">[\w\d\S]*)"
        self.index = ""
        self.vbn = {}
        for self.g in self.args[1:]:
            self.pora = self.pora + "\s+(?P<" + self.g + ">[\w\d\S]*)"
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
    cin_python = cin("first1", "second2", text = "input two or more words like 'hello everyone' - ")
    print("first word - " + cin_python.get("first1"))
    print("second word - " + cin_python.get("second2"))
