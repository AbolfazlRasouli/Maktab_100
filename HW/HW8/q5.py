class Indenter:
    space = None
    def __init__(self):
        self.value_multiply = -1
        
    def __enter__(self):
        self.value_multiply += 1
        return self

    def show(self, txt):
        Indenter.space = self.value_multiply * '    '
        print(f'{Indenter.space}{txt}')
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.value_multiply -= 1


with Indenter() as indent:
    indent.show('hi')
    with indent:
        indent.show('talk is cheap')
        with indent:
            indent.show('show me the code...')
    indent.show('torvalds')



































# class Indenter:
   
#     def __init__(self):
#         self.level = 0
#         # self.space = ''
        

#     def __enter__(self):
#         # self.space= self.level * '\t'
#         self.level += 1
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.level -= 1

#     def print(self, text):
#         indent = '\t' * (self.level - 1)
#         print(f"{indent}{text}")


# with Indenter() as indent:
#     indent.print('hi')
#     with indent:
#         indent.print('talk me')
#         with indent:
#             indent.print('show')

#     indent.print('torvalds')































# class Indenter:
#     def __init__(self):
#         self.level = 0


#     def __enter__(self):
#         self.level += 1
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.level -= 1

#     def print(self, text):
#         indent = '    ' * self.level
#         print(f"{indent}{text}")


# with Indenter() as indent:
#     indent.print('hi')
#     with indent:
#         indent.print('talk me')
#         with indent:
#             indent.print('show')
#     indent.print('torvalds')





