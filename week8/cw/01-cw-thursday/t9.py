import pickle


class DataMixin:
    
    
    def save_to_file(self,object_data:list):
        """for saving object data to the file"""
        with open('object.pickle', 'wb') as books_file:
            pickle.dump(object_data, books_file)
    

    def load_from_file(self):
        """for loading and updating object data from file"""
        
        obj = pickle.load(open("object.pickle", "rb"))
        for book in obj:
            print (book.title , end="-")