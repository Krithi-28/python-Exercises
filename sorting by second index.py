input_string = "this is the paper"
word_list = input_string.split()

sorted_list = sorted(word_list, key=lambda x: x[1])

output_string = ' '.join(sorted_list)
print(output_string)