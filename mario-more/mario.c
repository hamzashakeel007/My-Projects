#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Pyramid height input
    int height = get_int("Enter height for mario's pyramid: \n");

    //Algorthm for building pyramid

    label:
    while(true)
    {
        if (height < 1)
        {
            goto label;
        }

        else if (height > 8)
        {
            goto label;
        }

        else
        {
            goto label0;
        }
    }

    label0:
    for (int i = 0, , i++)
    {
        printf("# #");

    }
}
