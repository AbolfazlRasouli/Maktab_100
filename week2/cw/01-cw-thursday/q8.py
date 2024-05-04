def read_file(filename):
    try:
        with open(filename, 'r') as reader:
            file_item = reader.read()
            print(file_item)
    except Exception as e:
        print(e)
        
user_input = input('Enter Your name file :')
read_file(user_input)