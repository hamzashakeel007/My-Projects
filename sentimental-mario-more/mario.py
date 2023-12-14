# TODO
import cs50

void pyramid(void)

def main()
    pyramid()



def pyramid(void)

    // Pyramid height input
    height = 0

    while ( (height < 1) or (height > 8) ):
        height = cs50.get_int("Enter height for mario's pyramid: \n")

    for (int i = 0; i < height; ++i):
        for (int j = 0; j < height+i+3; ++j):
            if ( (j == height) or (j == height+1) or (i+j < height-1) ):
                printf(" ")
            else:
                printf("#")
        printf("\n");


main()

