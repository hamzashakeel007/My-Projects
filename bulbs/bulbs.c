#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string message = get_string("Message: ");
    for (int i = 0, n = strlen(message); i < n; i++)
    {
        //Converting into decimal
        int decimal = message[i];
        int bit = 0;
        //Converting into binary
        for (int j = 0; j < BITS_IN_BYTE; i++)
        {
            int binary[] = {0, 0, 0, 0, 0, 0, 0, 0};
            bit = decimal % 2;
            decimal = decimal / 10;

            for (int j = 0; j < 8; j++)
            {
                binary[i] = bit[i];
            }

            for (int k = 7; k < BITS_IN_BYTE - 1; k--)
            {
                printf("%i\n", binary[i]);
            }
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
