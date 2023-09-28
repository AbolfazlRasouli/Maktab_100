import sys
import argparse


# def separate_numbers_from_string(input_grades) :
   
#     lst_float = []
#     for i in range(1, len(input_grades)) :
#         if input_grades[i].replace('.', '').isdigit():
#             lst_float.append(float(input_grades[i])) 
#     return lst_float


# def avg_list_of_scores(lst_float):

#     sum_float = 0
#     for item in lst_float :
#         sum_float += item
#     avg_float = sum_float // len(lst_float)
#     return avg_float


# input_sys = sys.argv
# result = separate_numbers_from_string(input_sys)
# print(avg_list_of_scores(result))



# =================================================================================



def avg_list_of_scores(lst_float, decimal):
    # sum_float = 0
    # for item in lst_float :
    #     sum_float += item
    avg_float = sum(lst_float) / len(lst_float)
    return round(avg_float, int(decimal))

def separate_numbers_from_string(input_grades) :
   
    lst_float = []
    for i in range(len(input_grades)) :
        if input_grades[i].replace('.', '').isdigit():
            lst_float.append(float(input_grades[i])) 
    return lst_float
    

def input_argparse() :
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--grades', type=str, required=True, nargs='+', help=' grades')
    parser.add_argument('-f', '--float', type=int, default=2, help='float bedeh')
    args = parser.parse_args()
    # print(args.grades)
    # print(args.float)
    return args.grades, args.float



input_grades, input_float = input_argparse()
result = separate_numbers_from_string(input_grades)
print(avg_list_of_scores(result, input_float))
