def write_file(filename , item) :
    try :
        with open(filename , 'w') as writer :
            writer.write(item)
    except Exception as e :
        print(e)


def read_file(filename) :
    with open(filename, 'r') as reader:
        file_item = reader.read()
    print(file_item)

user_input = input('Enter Your name file :')
user_write = input('Enter your text write :')
write_file(user_input , user_write)
read_file(user_input)
