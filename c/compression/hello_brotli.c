/*
 * Simple example of using Brotli C library for round-trip compress/decompress
 */
#include <stdlib.h>    // malloc, free, exit
#include <stdio.h>     // fprintf, perror, fopen, etc.
#include <string.h>    // strlen, strcat, memset, strerror
#include <errno.h>     // errno

// presumes Brotli library (with headers) is installed
#include <brotli/encode.h>
#include <brotli/decode.h>

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
    size_t const cBuffSize = BrotliEncoderMaxCompressedSize(fSize);

    // Allocate a buffer to hold the compressed data
    void* const cBuff = malloc_orDie(cBuffSize);

    // Compress the data
    int quality = BROTLI_DEFAULT_QUALITY;
    int lgwin = BROTLI_DEFAULT_WINDOW;
    BrotliEncoderMode mode = BROTLI_DEFAULT_MODE;
    size_t encoded_size = cBuffSize;

    // Performs one-shot memory-to-memory compression
    BROTLI_BOOL success = BrotliEncoderCompress(quality, lgwin, mode, fSize, data, &encoded_size, cBuff);
    if (success != BROTLI_TRUE || encoded_size == 0)
    {
        printf(stderr, "error compressing '%s'\n", data);
        exit(8);
    }


    // Calculate the size for the decompressed data
    size_t rSize = fSize;

    // Allocate a buffer for the reconstructed data
    void* const rBuff = malloc_orDie(rSize);

    // Performs one-shot memory-to-memory decompression
    size_t decoded_size = rSize;
    BrotliDecoderResult result = BrotliDecoderDecompress(encoded_size, cBuff, decoded_size, rBuff);
    if (BROTLI_DECODER_RESULT_SUCCESS != result)
    {
        fprintf(stderr, "error decompressing\n");
        exit(7);
    }

    printf("Brotli compression ratio: %.3g\n", ((float)decoded_size)/encoded_size);

    free(cBuff);
    free(rBuff);
    return 0;
}
