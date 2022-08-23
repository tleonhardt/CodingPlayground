#!/usr/bin/env python
"""
 Given an English dictionary to search, create a program that will find all
 words in the dictionary which match the following criteria:

 The target word is exactly 7 letters long.
 The target word contains all the vowels [aeiou] exactly once.
 Two of the letters in the target word are not vowels.

 So if '.' represents any single non-vowel character, possible matched words
 would be:

 aeiou..
 aeio.u.
 aei.ou.
 ae.iou.
 a.eiou.
 .aeiou.
 aeio..u
 aei.o.u
 ae.io.u
 etc.

 Use your program to find at least 5 words which match this criteria.
"""
import csv

DICTIONARY_FILE = "fulldictionary00.txt"
MAGIC_WORD_LENGTH = 7
VOWELS = set("aeiou")


def find_matches(csv_reader):
    """Reads a CSV file and returns a list of words matching our criteria.

    :param csv_reader: (csv.reader) a reader object which will iterate over
        lines in a CSV file
    :return (list): List of words matching our criteria.
    """
    match_list = []
    for row in csv_reader:
        # If the row isn't empty
        if row:
            # Set the word to the contents of the first cell
            word = row[0]
            # If the word has 7 letters
            if len(word) == MAGIC_WORD_LENGTH:
                letters_in_word = set(word)
                # If the set of vowels is a subset of the letters in the word
                if VOWELS < letters_in_word:
                    # If the word has two consonants
                    if has_correct_consonants(letters_in_word, word):
                        match_list.append(word)
    return match_list


def has_correct_consonants(letters_in_word: set[str], word: str):
    """Make sure the word contains exactly two letters that are not vowels.

    :param word: (str) word to test
    :return (bool): True if words has exactly two consonants, False otherwise.
    """
    consonants = letters_in_word - VOWELS
    num_unique_consonants = len(consonants)

    # We need either 1 or 2 unique consonants for this to be possible
    if not 1 <= num_unique_consonants <= 2:
        return False

    # In the case of 1 unique consonant, make sure it is repeated
    if num_unique_consonants == 1:
        if word.count(consonants.pop()) != 2:
            return False

    return True


def main():
    """Main Execution - Parse through the dictionary file

    :return (list):  List of words which match the criteria
    """
    with open(DICTIONARY_FILE) as cur_file:
        # Create a csv.reader object to read a tab-delimited ASCII text file.
        # And then parse the file.
        cr = csv.reader(cur_file, delimiter="\t")
        matches = find_matches(cr)
    return matches


if __name__ == "__main__":
    word_matches = main()
    print(word_matches)
