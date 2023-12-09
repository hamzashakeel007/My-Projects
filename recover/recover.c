#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Invalid commmand line argument. Must only be 2 line argument\n Usage: ./recover IMAGE\n");
        return;
    }

    FILE *infile = fopen(argv[1], "r");

    if (infile == NULL)
    {
        printf("File not opened due do insufficient memory\n");
        return;
    }

    char *buffer[512];
    int count;

    FILE *outfile = NULL;

    char *filename = malloc(8 * sizeof(char));

    while (fread(buffer, sizeof(char), 512, infile))
    {

    }
}
