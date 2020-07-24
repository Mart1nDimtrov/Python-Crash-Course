filename = 'text_files\\pi_million_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip() #strip the ws on both sides of the line

print(f'{pi_string[:52]}...')
print(len(pi_string))