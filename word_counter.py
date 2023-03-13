def word_counter(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            words = contents.split()
            num_words = len(words)
            print(f"The file {filename} contains {num_words} words.")
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")

if __name__ == '__main__':
    word_counter('example.txt')
