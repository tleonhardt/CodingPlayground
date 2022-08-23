# Dictionary Search Challenge

Searching for a word or phrase which meets certain criteria is a common need in many applications. An effective search should correctly identify every candidate either as a match or not a match. Moreover, an effective search should be efficient.

Given an English dictionary to search, create a program that will find all words in the dictionary which match the following criteria:

1. The target word is exactly 7 letters long.
2. The target word contains all the vowels [aeiou] exactly once.
3. Two of the letters in the target word are not vowels.

So if '.' represents any single non-vowel character, possible matched words would be:

- aeiou..
- aeio.u.
- aei.ou.
- ae.iou.
- a.eiou.
- .aeiou.
- aeio..u
- aei.o.u
- ae.io.u
- etc.

## Your Assignment

Find a good English dictionary online which you can download and which has at least 150,000 words. Then write a program to parse every word in this dictionary and determine if it meets the above criteria. Finally, use your program to find at least 5 English words which match this criteria.

You may write your program in any programming language you choose. You can also use any design methodology you feel suits the problem: object-oriented, procedural, scripting, functional, etc.

Your code should should contain good naming, appropriate comments, and display good design. Efficiency of your algorithm should be one consideration. If there are two different solutions which both produce correct answers, but one of them runs in one tenth the time, then the faster solution is a better one.
