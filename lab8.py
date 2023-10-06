"""
pseudo code

open with file
create empty dictionary
loop line
loop word

dict[word] = line #
if word repeat in another line #, append to a list
print

"""



def word_lines():
    with open("quote.txt") as file:
        word_counts = {}
        #loop line
        for line_number, line in enumerate(file.read().split("\n")):
            #loop word in line
            for word in line.split():
                if word in word_counts:
                    word_counts[word].append(line_number+1)
                else:
                    word_counts[word] = [line_number+1]
        
        
       
             
        for word, line in word_counts.items():
            print(word,' '.join(str(line_number) for line_number in line))

word_lines()