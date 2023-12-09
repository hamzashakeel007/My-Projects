#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Invalid commmand line argument. Must only be 2 line argument\n Usage: ./recover IMAGE\n");
        return;
    }

    FILE *file = fopen(argv[1], "r");

    if (file == NULL)
    {
        printf("File not opened due do insufficient memory\n");
        return;
    }

    
}
