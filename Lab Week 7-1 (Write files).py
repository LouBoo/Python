def main():
    friends = open('myfile.txt', 'w')
    write_file(friends)
    movies = open('myfile2.txt', 'w')
    write_lines(movies)
    print("Files should be written. Check for \"myfile.txt\" & \"myfile2.txt\".")

def write_file(friends):
    """
    function name:  write_file
    purpose:        write string to text file (myfile.txt)
    parameters:     a file
    """
    friends.write('Mike Hyland\nDavid Dugan\nTom Gionet\n')
    ### Could also use:
    ### friends.write('Mike Hyland\n')
    ### friends.write('David Dugan\n')
    ### friends.write('Tom Gionet\n')
    friends.close()

def write_lines(movies):
    """
    function name:  write_lines
    purpose:        write list to text file (myfile2.txt)
    parameters:     a file
    """
    movie_list = ["Annihilation", "Interstellar", "The Martian", "Star Wars"]
    for i in range(len(movie_list)):
        movie = movie_list[i] + "\n"
        movies.writelines(movie)
    movies.close()

main()
