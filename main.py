# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename.txt, 'a') as f:
        for line in f:
            print(line)
        
    #return line


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    #word = []
    count = 0
    unique_dict = {}
    
    for line in text:
        if line in unique_dict:
            unique_dict[line] += 1;
        else:
            unique_dict[line] = 1;

    return(unique_dict)