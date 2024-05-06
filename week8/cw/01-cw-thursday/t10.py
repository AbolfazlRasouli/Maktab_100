import csv

class DataMixin:
    
    def save_to_file(self,object_data:list):
        """for saving object data to the file"""
        with open("csv_file.csv", "w", newline="") as books_file:
            data=csv.writer(books_file)
            data.writerow(['title','author','publication_year'])
            for item in object_data:
                data.writerow([item.title,item.author,item.publication_year])
    
        
        
    def load_from_file(self):
        """for loading and updating object data from file"""
        with open("csv_file.csv", "r") as books_file:
            data=csv.reader(books_file)
            # next(data)
            for index,item in enumerate(data):
                if index == 0:
                    continue
                else:
                    print(f"{index}:{item}")
        