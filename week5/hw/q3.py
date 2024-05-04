import csv


def read_file(name_file) :
    dict_csv = {}
    with open(name_file, 'r') as file :
        data = csv.reader(file)
        # print(data)
        next(data)
        for line in data :
            name, mark = line
            dict_csv[name] = float(mark)
            # dict_csv.setdefault(line[0],float(line[1]))
    
    return dict_csv



def search(all_dict, name) :
    if name in all_dict :
        return all_dict[name]
    else :
        return 'not found'
    
    
all_data = read_file('txt.csv')
name = 'abolfazl'
print(search(all_data, name))


#  روش اول
student_17_to_20 = {}
for name , mark in all_data.items() :
    if 20 >= mark >= 17 :
        student_17_to_20.setdefault(name, mark)

# روش دوم
# student_17_to_20 = {name: mark for name, mark in all_data.items() if 17 <= mark <= 20}



# روش اول 
student_0_to_10 = {}
for name , mark in all_data.items() :
    if 10 >= mark >= 0 :
        student_0_to_10.setdefault(name, mark)

# روش دوم
# student_0_to_10 = {name: mark for name, mark in all_data.items() if 0 <= mark <= 10}


print(all_data)
print(student_0_to_10)
print(student_17_to_20)





































# with open('txt.csv' , 'r') as file :
#     data = {}
#     # date = csv.reader(file)
#     # for line in date :
#     #     print(line)


#     date = csv.DictReader(file)
#     for line in date :
#         print(line)