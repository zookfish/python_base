# encoding=UTF-8

class ShortInputException(Exception):
    '''自定义异常类'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something')
    if len(text) <3:
        raise ShortInputException(len(text),3)

except EOFError:
    print('why')
except ShortInputException as ex:
    print('input was {},but expected was {}'.format(ex.length,ex.atleast))
else:
    print('Nothing')


