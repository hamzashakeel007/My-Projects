#include <cs50.h>
#include <stdio.h>
int get_ssize(void);
int get_esize(int startsize);
int calculation(int startsize, int endsize);

int main(void)
{
    // TODO: Prompt for start size
    int startsize = get_ssize();
    // TODO: Prompt for end size
    int endsize = get_esize(startsize);
    // TODO: Calculate number of years until we reach threshold
    int calc = calculation(startsize, endsize);
    // TODO: Print number of years
    printf("Years: %i \n", calc);
}

int get_ssize(void)
{
    int n = 0;

label:
    n = get_int("Minimun start size should be greater or equal to 9: ");
    if (n < 9)
    {
        goto label;
    }
    return n;
}

int get_esize(int startsize)
{
    int n = 0;

label1:
    n = get_int("End size should be greater or equal to start size: ");
    if (n < startsize)
    {
        goto label1;
    }
    return n;
}

int calculation(int startsize, int endsize)
{
    int years = 0;

    while (startsize < endsize)
    {
        // population born each year(s)
        startsize = startsize + (startsize / 3) - (startsize / 4);
        years++;
    }
    return years;
}
