#include <cs50.h>
#include <stdio.h>

void pyramid(void);

int main(void)
{
    //Algorthm for building pyramid
    pyramid();
}



void pyramid(void)
{
    // Pyramid height input
    int height = 0;

    while ( (height < 1) || (height > 8) )
    {
        height = get_int("Enter height for mario's pyramid: \n");
    }

    for (int i = 0; i < height; ++i)
    {
        for (int j = 0; j < height+i+3; ++j)
        {
            if ( (j == height) || (j == height+1) || (i+j < height-1) )
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("\n");
    }
}
