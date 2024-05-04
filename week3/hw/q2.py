def sed(file_input, pattern_string, file_output, replacement_string):
    try:
        with open(file_input, 'r') as reader:
            lines = reader.read()

        if pattern_string in lines :
            new_word = lines.replace(pattern_string, replacement_string)

        
        with open(file_output, 'w') as writer:
            writer.write(new_word)

    except FileNotFoundError:
        print(f"Error: File {file_input} not found.")
    except PermissionError:
        print("Error: No permission ")
    except IOError as e :
        print(f'Error : {e}')
    except Exception as e:
        print(f"Error: {e}")

  
sed("names.txt", "abolfazl", "output.txt", "rasouli")