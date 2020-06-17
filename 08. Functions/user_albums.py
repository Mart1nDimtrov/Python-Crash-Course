#8-8. User Albums:Start with your program from Exercise 8-7. Write a while
#loop that allows users to enter an album’s artist and title. Once you have that 
#information, call make_album() with the user’s input and print the dictionary 
#that’s created. Be sure to include a quit value in the whileloop.

def make_album(artist_name,album_title,number_of_songs=None):
	album = {'artist_name':artist_name,'album_title':album_title}
	if number_of_songs:
		album['number_of_songs'] = number_of_songs

	return album


while True:
	print("Write the artist's name and album title or type 'q' to quit:")
	
	artist_name = input("Artist's name:")
	if artist_name == 'q':
		break
	album_title = input("Album title:")
	if album_title == 'q':
		break

	print(make_album(artist_name,album_title))