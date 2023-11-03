input_dictionary = {5:25, 6:36, 7:49}
output_dictionary = {}

for key in input_dictionary:
    output_dictionary[input_dictionary[key]] = key

print(f"Input: {input_dictionary}")
print(f"Output: {output_dictionary}")