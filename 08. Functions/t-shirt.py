#8-3. T-Shirt:Write a function called make_shirt() that accepts a size and the 
#text of a message that should be printed on the shirt. The function should print 
#a sentence summarizing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. Call the 
#function a second time using keyword arguments.
#8-4. Large Shirts:Modify the make_shirt() function so that shirts are large 
#by default with a message that reads I love Python. Make a large shirt and a 
#medium shirt with the default message, and a shirt of any size with a different 
#message.

def make_shirt(size='l',message='I love Python.'):
	'''Take a size and a 
	message to be printed for a shirt.'''
	print(f'The shirt is size {size.upper()}')
	print('The shirt says:')
	print(message)

#make_shirt('xl','Be cool.')
#make_shirt(message='Just do it.',size='l')

make_shirt()
make_shirt('m')
make_shirt(message='Comedy central.')


