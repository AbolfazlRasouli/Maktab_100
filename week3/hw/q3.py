def syntax_errors(file_name):
    count_syntax_error = 0
    with open(file_name, "r") as reader:
        source_code = reader.read()
        for line in source_code :
            try :
                compile(line, "<string>", "exec")

            except SyntaxError as e:
                count_syntax_error += 1
                print(f"SyntaxError on line {line}: {e}")
    
    return count_syntax_error
    


print(syntax_errors('syntax.py'))