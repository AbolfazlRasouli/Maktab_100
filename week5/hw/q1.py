
def Compression_digit_string(number_string):
    while True:
        dict_digit = {}
        # روش اول
        if 1000 >= len(number_string) >= 1 :
            for digit in number_string:
                if digit in dict_digit:
                    dict_digit[digit] += 1
                else:
                    dict_digit.setdefault(digit, 1)

            # روش دوم
            # for digit in number_string :
            #     reapet = number_string.count(digit)
            #     dict_digit[digit] = reapet
        
        # print(dict_digit)


        new_number_string = count_digit =  repeat_count = ''

        for digit, count in dict_digit.items():
            if count >= 2:
                repeat_count += str(count)
            count_digit += digit
            new_number_string = count_digit + repeat_count
        # print(new_number_string)


        sorted_number_string = "".join(sorted(new_number_string))
        # print(sorted_number_string)


        if sorted_number_string == number_string:
            break
        else:
            number_string = sorted_number_string
    
    return number_string


while True :
    # 442254545
    input_string = input('Enter digit string : ')
    if input_string.isdigit() :
        break
    else :
        print('Invalid digit string . Please try again')

print(Compression_digit_string(input_string))
