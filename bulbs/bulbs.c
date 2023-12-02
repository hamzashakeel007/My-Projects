#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    int arr[BITS_IN_BYTE];
    string message = get_string("Message: ");
    for (int i = 0, n = strlen(message); i < n; i++)
    {
        //Converting into decimal
        int decimal = message[i];

        //Converting into binary
        do
        {
            int divide = decimal = decimal / 10;

        } while (decimal > 0);
        if (decimal % 2 == 0)
        {
            arr[BITS_IN_BYTE] = 0;
        }

        else
        {
            arr[BITS_IN_BYTE] = 1;
        }
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
