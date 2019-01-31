#Write a function called write_movie_info. write_movie_info
#will take as input two parameters: a string and a
#dictionary.
#
#The string will represent the filename to which to write.
#
#The keys in the dictionary will be strings representing
#movie titles. The values in the dictionary will be lists
#of strings representing performers in the corresponding
#movie.
#
#write_movie_info should write the list of movies to the file
#given by the filename using the following format:
#
# Title: Actor 1, Actor 2, Actor 3, etc.
#
#The movies and the actor names should be sorted
#alphabetically.
#
#So, for this dictionary:
#
# {"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"],
#  "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}
#
#The file printed would look like this:
#
# Chocolat: Alfred Molina, Johnny Depp, Judi Dench, Juliette Binoche
# Skyfall: Daniel Craig, Javier Bardem, Judi Dench, Naomie Harris
#
#HINT: the keys() method of a Dictionary will return a list
#of the dictionary's keys. So, to get a sorted list of a_dict's
#keys, you could call key_list = a_dict.keys(), then call 
#key_list.sort().


#Write your function here!
def write_movie_info(filename, movie_dict):
    outfile = open(filename, 'w')

    movie_list = []
    for movie in movie_dict:
        movie_list.append(movie)
    movie_list.sort()
    
    for movie in movie_list:
        print(movie, file = outfile, end = ": ")
        actors = movie_dict[movie]
        actors.sort()

        act_count = 0
        act_max = len(actors)

        for actor in actors:
            act_count += 1
            if act_count < act_max:
                seperator = ", "
            else:
                seperator = ""
            print(actor, file = outfile, end = seperator)
        print(file = outfile)   
        
    outfile.close()



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print nothing -- however, it should write the same contents
#as Sample.txt to Test.txt.


movies = {"Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"], "Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"]}
write_movie_info("c:\\temp\\Test.txt", movies)



