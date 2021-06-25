def is_in_set (letter):
    set_of_possible_letters = 'ABCDEF'
    return letter in set_of_possible_letters 

def contain_hex_word(word: str):
    for letter in word:
        if is_in_set(letter):
            continue
        else:
            return False
    return True

words_file = open(file = 'en_words.txt', mode = 'r')
result_file = open (file = 'hola :).txt', mode = 'w')

for line in words_file:
    line_without_newline = line.rstrip()
    line_upper = line_without_newline.upper()
    if contain_hex_word (line_upper):
        result_file.write(line)

words_file.close()
result_file.close()