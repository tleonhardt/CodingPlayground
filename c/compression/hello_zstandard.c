/*
 * Simple example of using Zstandard C library for round-trip compress/decompress
 */
#include <stdlib.h>    // malloc, free, exit
#include <stdio.h>     // fprintf, perror, fopen, etc.
#include <string.h>    // strlen, strcat, memset, strerror
#include <errno.h>     // errno
#include <zstd.h>      // presumes zstd library is installed

static void* malloc_orDie(size_t size)
{
    void* const buff = malloc(size);
    if (buff) return buff;
    /* error */
    perror(NULL);
    exit(3);
}

int main(int argc, const char** argv)
{
    const char* const exeName = argv[0];

    if (argc!=2) {
        printf("wrong arguments\n");
        printf("usage:\n");
        printf("%s DATA_TO_COMPRESS\n", exeName);
        return 1;
    }

    const char* const data = argv[1];

    // Get the size of the data we wish to compress
    size_t fSize = strlen(data);

    // Calculate upper bound for size of compressed data
    size_t const cBuffSize = ZSTD_compressBound(fSize);

    // Allocate a buffer to hold the compressed data
    void* const cBuff = malloc_orDie(cBuffSize);

    // Compress the data
    size_t const cSize = ZSTD_compress(cBuff, cBuffSize, data, fSize, 1);
    if (ZSTD_isError(cSize))
    {
        fprintf(stderr, "error compressing '%s' : %s \n", data, ZSTD_getErrorName(cSize));
        exit(8);
    }


    // Calculate the size for the decompressed data
    // WArNING: In newer versions of zstd, ZSTD_getDecompressedSize() -> ZSTD_findDecompressedSize()
    unsigned long long const rSize = ZSTD_getDecompressedSize(cBuff, cSize);
    if (rSize==0)
    {
        fprintf(stderr, "Compressed data was not compressed by zstd (or compressed using streaming mode)\n");
        exit(5);
    }

    // Allocate a buffer for the reconstructed data
    void* const rBuff = malloc_orDie((size_t)rSize);

    // Decompress the data
    size_t const dSize = ZSTD_decompress(rBuff, rSize, cBuff, cSize);
    if (dSize != rSize)
    {
        fprintf(stderr, "error decoding: %s \n", ZSTD_getErrorName(dSize));
        exit(7);
    }

    printf("Zstandard compression ratio: %.3g\n", ((float)dSize)/cSize);

    free(cBuff);
    free(rBuff);
    return 0;
}
