# Usage:
#    docdist1.py filename1 filename2
#
# This program computes the "distance" between two text files
# as the angle between their word frequency vectors (in radians).
#
# For each input file, a word-frequency vector is computed as follows:
#    (1) the specified file is read in
#    (2) it is converted into a list of alphanumeric "words"
#        Here a "word" is a sequence of consecutive alphanumeric
#        characters.  Non-alphanumeric characters are treated as blanks.
#        Case is not significant.
#    (3) for each word, its frequency of occurrence is determined
#    (4) the word/frequency lists are sorted into order alphabetically
#
# The "distance" between two vectors is the angle between them.
# If x = (x1, x2, ..., xn) is the first vector (xi = freq of word i)
# and y = (y1, y2, ..., yn) is the second vector,
# then the angle between them is defined as:
#    d(x,y) = arccos(inner_product(x,y) / (norm(x)*norm(y)))
# where:
#    inner_product(x,y) = x1*y1 + x2*y2 + ... xn*yn
#    norm(x) = sqrt(inner_product(x,x))
import math
import sys
from timeit import default_timer as timer

# Step 1: Read the input file & return a list of lines
def read_file(filename):
    try:
        file = open(filename, 'r')
        return file.readlines()
    except IOError:
        print("Error opening the given file name: " + filename)
        sys.exit()


# Step 2: Return a List of all words found in the Line List
def get_words_from_line_list(linelist):
    word_list = []
    for line in linelist:
        words_in_line = get_words_from_line(line)
        word_list = word_list + words_in_line
    return word_list


def get_words_from_line(line):
    word_list = []
    character_list = []

    for char in line:
        if char.isalnum():
            character_list.append(char)
        elif len(character_list) > 0:
            word = "".join(character_list)
            word = word.lower()
            word_list.append(word)
            character_list = []
    if len(character_list) > 0:
        word = "".join(character_list)
        word = word.lower()
        word_list.append(word)
        character_list = []
    return word_list


# Step 3/4: Return a sorted list of [word, word_freq] from a list of words.
def count_frequency(word_list):
    wf_list = []
    for word in word_list:
        found = False
        for entry in wf_list:
            if word == entry[0]:
                entry[1] = entry[1] + 1
                found = True
                break
        if not found:
            wf_list.append([word, 1])
    return insertion_sort(wf_list)


# Step 4: return a List sorted in alphabetical order
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            A[i] = key
            i = i - 1
    return A


def word_frequency_for_file(filename):
    # Returns alphabetical sorted list of [word,frequency] pairs for a given file
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    # print(word_list)
    frequency_mapping = count_frequency(word_list)
    return frequency_mapping


def inner_product(L1, L2):
    """Inner product between two vectors, where vectors
       are represented as lists of (word,freq) pairs."""
    sum = 0.0
    for word1, count1 in L1:
        for word2, count2 in L2:
            if word1 == word2:
                sum = sum + (count1 * count2)
    return sum


def vector_angle(L1, L2):
    """
    The input is a list of (word,freq) pairs, sorted alphabetically.
    Return the angle between these two vectors.
    """
    numerator = inner_product(L1, L2)
    denominator = math.sqrt(inner_product(L1, L1) * inner_product(L2, L2))
    vector_angle = math.acos(numerator / denominator)
    return vector_angle


if __name__ == "__main__":
    start = timer()
    sorted_word_list1 = word_frequency_for_file("bobsey.txt")
    sorted_word_list2 = word_frequency_for_file("lewis.txt")

    print(vector_angle(sorted_word_list1, sorted_word_list2))
    end = timer()
    # Calculates document distance between bobsey & lewis in approx 98.07
    print(end - start)