
OCCURRENCE = 3

def print_result(word_counts):
    for word, num_times in word_counts.items():
        if num_times > OCCURRENCE:
            print(f'{word} appears {num_times} times')


def count_all_words(file):
    #create an empty dict to return
    word_counts = {}

    for word in file.read().replace(",","").replace(".", "").lower().split():
        if word in word_counts:
            #increment how many time we've encountered this word
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def main():

    with open("book.txt") as file:
        words = count_all_words(file)
        print_result(words)

main()