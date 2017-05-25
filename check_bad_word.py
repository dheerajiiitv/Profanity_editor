def read_text():
	text = open("/home/dheeraj/Desktop/FSND/python/Data/movie_quotes.txt")
	contents_of_the_file = text.read()
	print(contents_of_the_file)
	text.close()
read_text()	