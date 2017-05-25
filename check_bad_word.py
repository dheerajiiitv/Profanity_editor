def read_text():
	text = open("/home/dheeraj/Desktop/FSND/python/Data/movie_quotes.txt")
	contents_of_the_file = text.read()
	print(contents_of_the_file)
	text.close()
	check_profanity(contents_of_the_file)
def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	connection.close()
	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("This document has no curse word!")
	else:
		print("Could not scan the document properly")
read_text()	
