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

        //Converting into binary
        int binary[] = {0, 0, 0, 0, 0, 0, 0, 0};
        for (int j = 0; decimal > 0; j++)
        {

            binary[j] = decimal % 2;
            decimal = decimal / 2;
        }

        for (int k = BITS_IN_BYTE - 1; k > - 1; k--)
        {
            print_bulb(binary[k]);
        }
        printf("\n");
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
