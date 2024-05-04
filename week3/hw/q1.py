list_data = [['mandana',5,7,3,15], ['hamid',3,9,4,20,9,1,8,160,5,2,4,7,2,1],
             ['sina',19,10,19,6,8,14,3], ['sara',0,5,20,14],
              ['soheila',13,2,5,1,3,10,12,4,13,17,7,7], ['ali',1,9],
               ['sarvin',0,16,16,13,19,2,17,8] ]


# 1
with open('file.csv', 'w') as writer :
    for row in list_data :
        writer.write(','.join(str(item) for item in row) + '\n')

# 2
dict_avg = {}
with open('file.csv', 'r') as reader :
    for line in reader :
        list_row = line.split(',')
        name = list_row[0]
        list_marks = []
        for mark in list_row[1:] :
            list_marks.append(int(mark))
        avg = sum(list_marks) / len(list_marks)
        dict_avg[name] = avg
        
with open('file_avg.csv', 'w') as writer :
    for name , average in dict_avg.items() :
        writer.write(f'{name}, {average:.6f} \n')



# 3
# روش اول
# averages_sorted = dict(sorted(dict_avg.items() , key= lambda value_sort : value_sort[1]))

# with open('file_avg_sorted.csv', 'w') as writer :
#     for name , average in averages_sorted.items() :
#         writer.write(f'{name}, {average:.6f} \n')


# روش دوم
averages_sorted = sorted(dict_avg.items() , key= lambda value_sort : value_sort[1])
print(averages_sorted, type(averages_sorted))

with open('file_avg_sorted.csv', 'w') as f :
    for name , average in averages_sorted :
        f.write(f'{name}, {average:.6f} \n')



# 4
# روش اول
# top_three_avg = []
# for name , avg in list(averages_sorted.items())[-3:] :
#     top_three_avg.append((name , avg))

# with open('file_top_tree_avg.csv', 'w') as writer :
#     for name , average in top_three_avg :
#         writer.write(f'{name}, {average:.6f} \n')



# روش دوم
top_three_avg = []
for name , avg in averages_sorted[-3:] :
    top_three_avg.append((name , avg))

with open('file_top_tree_avg.csv', 'w') as writer :
    for name , average in top_three_avg :
        writer.write(f'{name}, {average:.6f} \n')




# 5
three_low_avg = []
for name , avg in averages_sorted[:3] :
    three_low_avg.append((name , avg))

with open('file_tree_low_avg.csv', 'w') as writer :
    for name , average in three_low_avg :
        writer.write(f'{average:.6f} \n')



# 6
avg_grades = sum(dict_avg.values()) / len(dict_avg)
with open('file_avg_grades.csv', 'w') as writer :
    writer.write(f'avg grades: {avg_grades:.6f}\n')