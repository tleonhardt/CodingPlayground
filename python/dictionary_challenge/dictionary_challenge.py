#!/usr/bin/env python3
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

 This example showcases the power of Python's built in set type and the
 associated set theory operations it provides.
"""
DICTIONARY_FILE = "fulldictionary00.txt"
MAGIC_WORD_LENGTH = 7
VOWELS = frozenset("aeiou")


def matches_criteria(word: str) -> bool:
    """Determins if a word matches the criteria.

    :param word: word to test
    :return: True if it is a match, False otherwise
    """
    letters = frozenset(word)
    # If set of vowels is a proper subset of the letters and has consonants
    return VOWELS < letters and has_correct_consonants(letters, word)


def has_correct_consonants(letters: frozenset[str], word: str):
    """Make sure the word contains exactly two letters that are not vowels.

    :param letters_in_word: set of letters in word
    :param word: word to test
    :return (bool): True if words has exactly two consonants, False otherwise.
    """
    # consonants is the difference between the set of letters and set of vowels
    consonants = letters - VOWELS
    num_unique_consonants = len(consonants)

    return num_unique_consonants == 2 or (
        num_unique_consonants == 1 and word.count(next(iter(consonants))) == 2
    )


def main():
    """Main Execution - Parse through the dictionary file

    :return (list):  List of words which match the criteria
    """
    with open(DICTIONARY_FILE) as cur_file:
        # Read words and filter to those of desired length that match criteria
        matches = []
        for line in cur_file.readlines():
            word = line.strip()
            if len(word) == MAGIC_WORD_LENGTH and matches_criteria(word):
                matches.append(word)
    return matches


if __name__ == "__main__":
    word_matches = main()
    print(word_matches)
