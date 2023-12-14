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
    float L = (float) letters / words * 100
    float S = (float) sentences / words * 100
    float index = 0.0588 * L - 0.296 * S - 15.8

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }

    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }

    else
    {
        printf("Grade %i\n", (int) round(index));
    }
}

int count_letters(string text)
{
    int countl = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            countl++;
        }

        else
        {
            continue;
        }
    }

    return countl;
}

int count_words(string text)
{
    int countw = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[i]))
        {
            countw++;
        }

        else
        {
            continue;
        }
    }

    return countw + 1;
}

int count_sentences(string text)
{
    int counts = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            counts++;
        }

        else
        {
            continue;
        }
    }
    return counts;
}
