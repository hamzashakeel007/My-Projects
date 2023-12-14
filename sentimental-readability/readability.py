# TODO
import cs50
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

def main():
    text = cs50.get_string("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    #Coleman-Liau Index formula
    L = float (letters / words * 100)
    S = float (sentences / words * 100)
    index = 0.0588 * L - 0.296 * S - 15.8

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        printf("Grade ", int (round(index)))


def count_letters(text):
    countl = 0
    for i in range(0, len(text), 1):
        if (isalpha(text[i])):
            countl += 1
        else:
            continue
    return countl

def count_words(text):
    countw = 0
    for i in range(0, len(text), 1):
        if (isspace(text[i])):
            countw += 1
        else:
            continue
    return countw + 1


def count_sentences(text):
    counts = 0
    for i in range(0, len(text), 1):
        if (text[i] == '.' or text[i] == '?' or text[i] == '!'):
            counts += 1
        else:
            continue
    return counts


main()
