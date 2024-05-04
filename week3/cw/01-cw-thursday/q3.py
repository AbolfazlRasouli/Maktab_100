# روش اول
# def schools(input_name, my_dict) :
#     return my_dict.get(input_name, 'not found')

# student_grades = {
#     'hohn': 85,
#     'Alice': 92,
#     'Bob': 78,
#     'Emily': 90,
#     'Michael': 88,
# }
# user_input = input("Enter yiour number :")

# print(schools(user_input, student_grades))



# روشدوم
def schools(input_name, my_dict) :
    try :
        return my_dict[input_name]
    except KeyError as e :
        return f'KeyError : {e}'
    
student_grades = {
    'hohn': 85,
    'Alice': 92,
    'Bob': 78,
    'Emily': 90,
    'Michael': 88,
}
user_input = input("Enter yiour number :")

print(schools(user_input, student_grades))