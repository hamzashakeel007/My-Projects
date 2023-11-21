#include <cs50.h>
#include <stdio.h>

long checksum(long credit);

int main(void)
{
    // Gets Credit Card Number
    long credit = get_long("Enter Credit Card Number to Check its Validity\n");

    // Calculates Checksum using Luhn's Algorithm
    checksum(credit);

}

long checksum(long credit)
{
    long checksum0 = 0;
    long sum = 0;
    // long i = 0;
    for (i = 0; credit != i; i++)
    {
        checksum0 = credit % 10;
        sum = sum + checksum0;

    }
    printf("%ld\n", sum);
    return sum;
}
