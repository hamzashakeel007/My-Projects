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
        int binary[BITS_IN_BYTE];
        //Converting into binary
        for (int j = 0; j < BITS_IN_BYTE; i++)
        {
            int divide = decimal = decimal / 10;
            binary[j] = binary[j] % 2;

            if (divide % 2 == 0)
            {
                print_bulb(bit);
            }

            else
            {
                print_bulb(bit);
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
