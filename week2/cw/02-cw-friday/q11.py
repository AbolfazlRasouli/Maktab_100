def read_file (filename , word) :

    with open(filename , 'r') as reader :
        text = reader.read().split('.')
        print(text)
        for item in text :
            if word in item :
                print(item)

read_file('names' , 'abolfazl')
