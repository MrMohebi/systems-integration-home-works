word_dic = ['apple', 'banana', 'orange', 'grape', 'peach', 'kiwi']


def find_word(letter):
    global word_dic
    result_list = [word for word in word_dic if word.startswith(letter)]
    if len(result_list) < 1:
        return "NO WORD FOUNDED!"
    return result_list[0]


print(find_word("c"))