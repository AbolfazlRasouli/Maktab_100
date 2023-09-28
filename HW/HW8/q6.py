from typing import List
from contextlib import contextmanager


func_type = List[str]

@contextmanager
def file_opener(file_path: str, mode: str, process=None):

    open_file = open(file_path, mode)

    if mode == 'r':
        read_file = open_file.read()
        yield {read_file}
        
    elif mode == 'w' :
        open_file.writelines(process)
        yield{}
   
    open_file.close
    
    
def process_data(input_str: str) -> func_type:
    mylist = []
    for line in input_str:
        mylist.append(line)
    return mylist



input_file = 't1.txt'
output_file = 't2.txt'

result = None
with file_opener(input_file,'r') as reader :
    result = process_data(reader)

with file_opener(output_file,'w',result) as reader :
    print('objective completed ')















