
def get_unique_sorted_words(input_sentences) :
    lst_word = ''.join(input_sentences).replace('.', ' ').split()
    return list(set(lst_word))


input_sentences = ['This is a sample sentence.','Python programming is fun.']

unique_sorted_words = get_unique_sorted_words(input_sentences)
print(unique_sorted_words)