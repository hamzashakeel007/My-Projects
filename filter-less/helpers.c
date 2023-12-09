#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float green = image[i][j].rgbtGreen;
            float red = image[i][j].rgbtRed;
            float blue = image[i][j].rgbtBlue;

            // Averaging for gray filter
            int grayfilter = round(green + red + blue) / 3);
            // int gf = round(grayfilter);
            image[i][j].rgbtGreen = grayfilter;
            image[i][j].rgbtRed = grayfilter;
            image[i][j].rgbtGreen = grayfilter;
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
