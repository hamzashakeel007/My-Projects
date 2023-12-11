#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Invalid commmand line argument. Must only be 2 line argument\n Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *infile = fopen(argv[1], "r");

    if (infile == NULL)
    {
        printf("File not opened due do insufficient memory\n");
        return 1;
    }

    unsigned char buffer[512];
    FILE *outfile = NULL;
    char *filename = malloc(8 * sizeof(char));
    int count = 0;

    while (fread(buffer, sizeof(char), 512, infile) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            sprintf(filename, "%03i.jpg", count);
            outfile = fopen(filename, "w");
            count++;
        }

        if (outfile != NULL)
        {
            fwrite(buffer, sizeof(char), 512, outfile);
        }
    }


    return 0;
}
