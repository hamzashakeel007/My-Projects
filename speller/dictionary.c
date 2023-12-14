// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include <stdio.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

unsigned int word_count;
unsigned int hash_val;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    hash_val = hash(word);
    node *traverse = table[hash_val];

    while( traverse != 0)
    {
        if (strcasecmp(word, traverse->word) == 0)
        {
            return true;
        }
        traverse = traverse->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0] - 'Á');
    // unsigned long upper = 0;
    // int length = strlen(word);
    // for (int i = 0; i < length; i++)
    // {
    //     upper += toupper(word[i]);
    // }

    // return upper % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");

    if (file == NULL)
    {
        return false;
    }

    char word[LENGTH + 1];

    // read file till the end
    while (fscanf(file, "%s", word) != EOF)
    {
        node *new = malloc(sizeof(node));

        if (new == NULL)
        {
            return false;
        }

        strcpy (new->word, word);
        hash_val = hash(word);
        new->next = table[hash_val];
        table[hash_val] = new;
        word_count++;

    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if (word_count > 0)
    {
        return word_count;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *traverse = table[i];
        while (traverse)
        {
            node *tmp = traverse;
            traverse = traverse->next;
            free(tmp);
        }
        if (traverse == NULL)
        {
            return true;
        }
    }
    return false;
}
