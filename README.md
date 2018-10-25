Requirements: Write a program that reads in a paragraph form a file (input.txt) and generates a histogram of the words used, sorted from most occurrences to least. The output will consist of the word followed by a pipe character ("|"), a number of equal signs that are proportional to the number of occurrences found in the text, and the number of occurrences itself. Have the program read in the paragraph defined in the input.txt file below and generate a histograph stored in an output file (output.txt).

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
