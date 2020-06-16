#8-7. Album:Write a function called make_album() that builds a dictionary 
#describing a music album. The function should take in an artist name and an 
#album title, and it should return a dictionary containing these two pieces of 
#information. Use the function to make three dictionaries representing different 
#albums. Print each return value to show that the dictionaries are storing the 
#album information correctly.
#Use None to add an optional parameter to make_album() that allows you to 
#store the number of songs on an album. If the calling line includes a value for 
#the number of songs, add that value to the album’s dictionary. Make at least 
#ne new function call that includes the number of songs on an album.

def make_album(artist_name,album_title,number_of_songs=None):
	album = {'artist_name':artist_name,'album_title':album_title}
	if number_of_songs:
		album['number_of_songs'] = number_of_songs

	return album

print(make_album('jim','bussy'))
print(make_album('best','guess'))
print(make_album('stranger','road'))
print(make_album('loop','medicine',7))