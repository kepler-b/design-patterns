from typing import List


class FormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.caps = [False for _ in plain_text]

    def capitalize(self, start, end):
        for i in range(start, end + 1):
            self.caps[i] = True

    def __str__(self):
        result = []
        for index, char in enumerate(self.plain_text):
            if self.caps[index]:
                result.append(char.upper())
            else:
                result.append(char)
        return "".join(result)


class TextRange:
    def __init__(self, start: int, end: int, capitalize=False):
        self.start = start
        self.end = end
        self.capitalize = capitalize

    def covers(self, position):
        return self.start <= position <= self.end

class BetterFormattedText:

    def __init__(self, plain_text: str):
        self.plain_text = plain_text
        self.formatting: List[TextRange] = []

    def get_range(self, start, end):
        range = TextRange(start, end)
        self.formatting.append(range)
        return range

    def __str__(self):
        result = []
        for index, char in enumerate(self.plain_text):
            for formatting in self.formatting:
                if formatting.covers(index) and formatting.capitalize:
                    result.append(char.upper())
                else:
                    result.append(char)
        return "".join(result)

def execute():
    text = "This is my text hello"
    to_caps = " is"
    index = text.index(to_caps)
    caps = (index, index + len(to_caps) - 1)
    print("Caps range:", caps)
    ft = FormattedText(text)
    ft.capitalize(*caps)
    print(ft)


    formatted_text = BetterFormattedText("No such file or directory")
    to_caps = " or"
    index = formatted_text.plain_text.index(to_caps)
    caps = (index, index + len(to_caps) - 1)
    formatted_text.get_range(*caps).capitalize = True
    print(formatted_text)
