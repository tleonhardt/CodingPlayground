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


def find_matches(filtered_words: list[str]) -> list[str]:
    """Accepts a list of filtered words that are all of the correct length.

    :param filtered_words: list of words that are all the desired length
    :return: List of words matching our criteria
    """
    match_list = []
    for word in filtered_words:
        letters = frozenset(word)
        # If set of vowels is a proper subset of the letters in word
        if VOWELS < letters:
            # If the word has two consonants
            if has_correct_consonants(letters, word):
                match_list.append(word)
    return match_list


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
        # Read words and filter to those of the desired length
        words = [
            line.strip()
            for line in cur_file.readlines()
            if len(line.strip()) == MAGIC_WORD_LENGTH
        ]
        matches = find_matches(words)
    return matches


if __name__ == "__main__":
    word_matches = main()
    print(word_matches)
