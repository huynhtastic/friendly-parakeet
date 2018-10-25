"""
Requirements: Write a program that reads in a paragraph form a file (input.txt) and generates a histogram
of the words used, sorted from most occurrences to least. The output will consist of the word followed by a
pipe character ("|"), a number of equal signs that are proportional to the number of occurrences found in the
text, and the number of occurrences itself. Have the program read in the paragraph defined in
the input.txt file below and generate a histograph stored in an output file (output.txt).

Example Input
Hickory, dickory, dock.
The mouse ran up the clock.
The clock struck one,
The mouse ran down,
Hickory, dickory, dock.

Example Output
    the | ==== (4)
    ran | == (2)
   dock | == (2)
  clock | == (2)
dickory | == (2)
hickory | == (2)
  mouse | == (2)
   down | = (1)
     up | = (1)
 struck | = (1)
    one | = (1)
"""

def solution_with_libraries():
    """This solution fills the requirements with more concise code using libraries.
    The idea is to get a frequency distribution of words and just format that
    frequency distribution into a string template.
    """
    from operator import itemgetter

    # natural language processing toolkit
    # will require a 'pip install nltk' and a 'nltk.download('punkt')'
    # in a python runtime
    import nltk
    from nltk.tokenize import RegexpTokenizer

    # read the file
    with open('input.txt', 'r') as in_file:
        text = in_file.read().lower()

    # create a tokenizer with a regex that just looks for words
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)

    # FreqDist creates a count of the appearance of the words in the text
    freqs = nltk.FreqDist(tokens)

    with open('output.txt', 'w') as out_file:
        # turns the frequency distribution into a tuple of (words, counts)
        # itemgetter tells the sort to sort by the second item in the tuple
        # which is the count
        sorted_vals = sorted(freqs.items(), key=itemgetter(1), reverse=True)

        # convert each word to its length and get the length of the longest 
        # word to know how much we need to pad the output by
        len_biggest_word = max([len(word) for word in freqs.keys()])
        for word, count in sorted_vals:
            out_line = '{word:<{fill}} | {equals} ({count})\n'.format(
                word=word,
                fill=len_biggest_word,
                equals='='*count,
                count=count
            )
            out_file.write(out_line)

def solution_without_libraries():
    """This solution answers the challenge without use of libraries.

    Same idea as above, except we make everything from scratch.
    """
    # read the file
    with open('input.txt', 'r') as in_file:
        text = in_file.read().lower()

    freqs = {}  # i'd love to use a defaultdict here

    """
    # i was going to scan the text and use a stringbuilder approach, but
    # processing the text for each character would be O(n) with n being number
    # of characters
    word = ''
    for char in text:
        if char.isalpha():
            word += char
        else:
            if word in freqs:
                freqs[word] += 1
            else:
                freqs[word] = 1
    """

    # instead, we're going to split and then strip punctuation off each word
    # if we discount the time for using the built-in split() function,
    # worst case would be O(n) with n being number of characters if every
    # split word was only punctuation, but would probably be amortized O(w) 
    # with w being number of words since the average split word would have at 
    # most 1 punctuation character at the end
    for word in text.split():
        # the while loop kicks us out if we stripped down to an empty string
        while(word):
            if not word[0].isalpha():
                word = word[1:]  # strip the first char if it's not a letter
                continue
            if not word[-1].isalpha():
                word = word[:-1]  # strip the last char if it's not a letter
                continue
            if word in freqs:
                freqs[word] += 1
            else:
                freqs[word] = 1
            break

    # same as above
    with open('output.txt', 'w') as out_file:
        sorted_vals = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
        len_biggest_word = max([len(word) for word in freqs.keys()])
        for word, count in sorted_vals:
            out_line = '{word:<{fill}} | {equals} ({count})\n'.format(
                word=word,
                fill=len_biggest_word,
                equals='='*count,
                count=count
            )
            out_file.write(out_line)

# Please uncomment whichever solution you'd like to try out
# solution_with_libraries()
 solution_without_libraries()
