from math import factorial
# 1
# روش مربی که گفت اینطور حل بشه
# n =int(input('Enter number :'))
# f1 = 0
# f2 = 1
# for _ in range(n) :
#     print(f1, end=' ')
#     f1 , f2 = f2 , f1 + f2

# #  روش خودمان که جالب نیست
# n =int(input('Enter number :'))
# f1 = 0
# f2 = 1
# f3 =0

# if n > 2 :
#     print(f1)
#     print(f2)
#     for i in range(1,n -1) :
#         f3 = f1 + f2
#         f1 = f2
#         f2 = f3
#         print(f3)
# elif n == 1 :
#     print(f1)
# else :
#     print(f1)



# 2
# روش اول
# n =int(input('Enter number :'))
# fact = 1
# for item in range(1, n + 1) :
#     fact *= item
# print(fact)

# # روش دوم
# print(factorial(n))



# 3
# روش مربی . که روش جالبی بود 
# n = int(input('Enter number :'))
# for i in range(2, n):
#     if n % i == 0:
#         print(f' {n} is not prime number.')
#         break
# else :
#     print(f'{n} is a prime number.')




# # روش خودمان
# n = int(input('Enter number :'))
# flag = True
# for i in range(2, n):
#     if n % i == 0:
#         flag = False
#         break

# if flag == True:
#     print(f' {n} is not prime number.')
# else:
#     print(f'{n} is a prime number.')



# 4
# n = input('Enter number :')
# letters_upper = 0
# letters_lower = 0

# for chr in n :
#     if chr.isupper() :
#         letters_upper += 1
#     elif chr.islower() :
#         letters_lower += 1
# print(f'"Uppercase letters : {letters_upper},Lowercase letters :{letters_lower}"')


# #  روش مربی 
# print(sum(1 for char in n if char.isupper()))


# 5
# روش پارسا
# input = 'python'
# s = ''
# for chr in input :
#     s = chr + s
# print(s)

# # روش دوم
# word = list(input)
# word.reverse()
# print(''.join(word))

# # روش سوم
# print(''.join(reversed(input)))


# 6
# روش اول
# input = '14587'
# sum_didit = 0
# for num in input :
#     sum_didit += int(num)
# print(sum_didit)

# # روش دوم
# number = 1234
# digi = 0
# temp = number
# while temp != 0 :
#     a = temp % 10
#     digi += a
#     temp = temp //10
    
# print(digi)


# روش سوم
# num = 'asd4587'
# for item in num :
#     if item.isdigit() :
#         sum_didit += item





# 7
# input = 'radar'
# if input == ''.join(reversed(input)) :
#     print("palindrome")
# else :
#     print('No Palindrom')


# 8
grading = int(input('Enter your number :'))

# if grading > 80 :
#     print('A')
# elif grading > 60 :
#     print('B')
# elif grading > 50 :
#     print('C')
# elif grading > 45 :
#     print('D')
# elif grading > 25 :
#     print('E')
# else :
#     print('F')


# match grading :
#     case 80 :
#         print('A')
#     case 60:
#         print('B')
#     case 50:
#         print('C')
#     case 40:
#         print('D')
#     case 25:
#         print('E')
#     case _ :
#         print('aaaaaaaaaaaaaaaaaaaaaaaaa')




# match grading :
#     case grading if grading > 80 :
#         print('A')
#     case grading if grading > 60:
#         print('B')
#     case 50:
#         print('C')
#     case 40:
#         print('D')
#     case 25:
#         print('E')
#     case _ :
#         print('aaaaaaaaaaaaaaaaaaaaaaaaa')
    
    




# 9
# def add (list_name):
#     while True :
#         text = input("Add:")
#         if text.lower() == "done":
#             break
#         list_name.append(text)
#     print(list_name)
#     cmd(list_name)


# def remove (list_name):
#     print(list_name)
#     while True :
#         name = input("remove:")

#         if name.lower() == "done":
#             break
#         elif name not in list_name:
#             print("not find")
#             continue
#         list_name.remove(name)
#     print(list_name)
#     cmd(list_name)


# def show (list_name):
#     print(list_name)
#     cmd(list_name)


# def cmd (list_name):
#     command = input(">")
#     if command.lower()=="add" :
#         add(list_name)
#     elif command.lower()=="remove":
#         remove(list_name)
#     elif command.lower()=="show":
#         show(list_name)
#     elif command.lower()=="exit":
#         exit()
#     else:
#         print(" is not command")

# list_name=[]
# cmd(list_name)




# # خودم نوشتم
# def add(list_name) :
#     while True :
#         text = input("enter :")
#         if text.lower() == 'done' :
#             break
#         list_name.append(text)
#     print(list_name)
#     cmd(list_name)


# def remove(list_name) :
#     while True :
#         text = input("enter :")
#         if text.lower() == 'done' :
#             break
#         elif text not in list_name :
#             print("not find")
#             continue
#         else :
#             list_name.remove(text)
#     print(list_name)
#     cmd(list_name)



# def show(list_name) :
#     print(list_name)
#     cmd(list_name)


# def cmd(list_name) :
#     user_input = input('Enter your name')
#     if user_input.lower() == 'add' :
#         add(list_name)
#     elif user_input.lower() == 'remove' :
#         remove(list_name)
#     elif user_input.lower() == 'show' :
#         show(list_name)
#     elif user_input.lower() == 'exit' :
#         exit()
#     else :
#         print('Invalid')


# list_name = []
# cmd(list_name)


# 10
# x , y = map(str, input('add number1, 2 :').split())
# t = 0

# if y.lower() == 'f' :
#     t = float(x) * (9/5) + 32
#     print(t)
# elif y.lower() == 'c' :
#     t = (float(x) - 32) * (5/9)
#     print(t)
# else :
#     print('Invalid')




# 11
# for i in range(1,101) :
#     if i % 3 == 0 and i % 5 == 0 :
#         print('fizbuzz' , end=' ')
#     elif i% 3 == 0 :
#         print('fiz' , end=' ')
#     elif i % 5 == 0 :
#         print('buzz', end =' ')
#     else :
#         print(i ,end=' ')



# 12
import random as re 
 
# lst = ['gilas', 'ananas', 'anbeh', 'mooooz'] 
# rand_word = re.choice(lst) 
# print(rand_word) 
 
# hidden_word = '_' * len(rand_word) 
# print(hidden_word) 
 
# hidden_word_list = list(hidden_word) 
# rand_word_list = list(rand_word) 
 
# for _ in range(len(rand_word_list) + 2): 
#     letter = input("Enter a letter: ") 
#     if letter in rand_word_list: 
#         while letter in rand_word_list: 
#             index = rand_word_list.index(letter) 
#             rand_word_list[index] = '@' 
#             hidden_word_list[index] = letter 
#         print("You guessed correctly!") 
#         print(" ".join(hidden_word_list)) 
#     else: 
#         print("You guessed incorrectly!")




word = ['babana' , 'mooooz','appele', 'orange']
ai_word = re.choice(word)
print(ai_word)

hiden_str ='-' * len(ai_word)
print(hiden_str)

list_word = list(ai_word)
list_hidden_str = list(hiden_str)

for _ in range(len(ai_word) + 2) :
    letters = input("enter letter :")
    if letters in list_word :
        while letters in list_word :
            index = list_word.index(letters)
            list_hidden_str[index] = letters
            list_word[index] = '@'
        print(''.join(list_hidden_str))
    else :
        print('guessed incorrect')

    if ai_word == ''.join(list_hidden_str) :
        print('you won. end ')
        break