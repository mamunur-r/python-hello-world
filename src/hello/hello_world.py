"""

"""


class Hello:
    """
    just to say hello world
    """
    def __init__(self):
        self.hello_back = 'You said '

    def hello_me(self, msg: str):
        print('Hello world')
        return self.hello_back+msg+' to me!'

    def sum(self, x: int, y: int):
        result = x + y
        return result
