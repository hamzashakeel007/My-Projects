#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (image[i][j].rgbtGreen == 0x00 && image[i][j].rgbtBlue == 0x00 && image[i][j].rgbtRed == 0x00)
            {
                image[i][j].rgbtGreen = 0x04;
                image[i][j].rgbtBlue = 0x0a;
                image[i][j].rgbtRed = 0xf4;
            }
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
