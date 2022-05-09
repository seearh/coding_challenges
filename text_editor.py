from collections import deque


class TextEditor():
    def __init__(self, text='', ops=[]):
        self._ops = deque(ops)
        self._text = text

    def print(self, k):
        print(self._text[k-1])
        
    def append(self, text):
        self._ops.append(len(text))
        self._text += text

    def delete(self, k):
        self._ops.append(self._text[-k:])
        self._text = self._text[:-k]

    def undo(self):
        op = self._ops.pop()
        if type(op) == int:
            self._text = self._text[:-op]
        else:
            self._text += op
