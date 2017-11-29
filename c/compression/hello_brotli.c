/*
 * Simple example of using Brotli C library for round-trip compress/decompress
 */
#include <stdint.h>     // uint8_t. etc.
#include <stdio.h>     // fprintf, perror, fopen, etc.
#include <stdlib.h>    // malloc, free, exit
#include <string.h>    // strlen, strcat, memset, strerror

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

    const uint8_t* const input_buffer = (uint8_t*)argv[1];

    // Get the size of the input_buffer we wish to compress
    size_t input_size = strlen(argv[1]);

    // Calculate upper bound for size of compressed data given the size of the uncompressed input_buffer
    size_t const maxCompressedSize = BrotliEncoderMaxCompressedSize(input_size);

    // Allocate a buffer to hold the compressed data
    void* const encoded_buffer = malloc_orDie(maxCompressedSize);



    // The higher the quality, the slower the compression (and higher compression ratio). Range is from 0 to 11
    int quality = BROTLI_DEFAULT_QUALITY;

    // Recommended sliding LZ77 window size. Encoder may reduce this value.  Range is from 10 to 24 bits.
    int lgwin = BROTLI_DEFAULT_WINDOW;

    // Compression mode.  Options are: BROTLI_MODE_GENERIC, BROTLI_MODE_TEXT (UTF-8 formatted text), or BROTLI_MODE_FONT
    BrotliEncoderMode mode = BROTLI_DEFAULT_MODE;

    // in: size of @p encoded_buffer;  out: length of compressed data written to  encoded_buffer
    size_t encoded_size = maxCompressedSize;

    // Performs one-shot memory-to-memory compression
    BROTLI_BOOL success = BrotliEncoderCompress(quality, lgwin, mode, input_size, input_buffer, &encoded_size,
                                                encoded_buffer);
    if (success != BROTLI_TRUE || encoded_size == 0)
    {
        fprintf(stderr, "error compressing '%s'\n", input_buffer);
        exit(8);
    }


    // TODO: Calculate the size for the decompressed data in a general way
    size_t maxDecompressedSize = input_size;

    // Allocate a buffer for the reconstructed data
    void* const decoded_buffer = malloc_orDie(maxDecompressedSize);

    // in: size of @p decoded_buffer;  out: length of decompressed data written to decoded_buffer
    size_t decoded_size = maxDecompressedSize;

    // Performs one-shot memory-to-memory decompression
    BrotliDecoderResult result = BrotliDecoderDecompress(encoded_size, encoded_buffer, &decoded_size, decoded_buffer);
    if (BROTLI_DECODER_RESULT_SUCCESS != result)
    {
        fprintf(stderr, "error decompressing\n");
        exit(7);
    }

    printf("Brotli compression ratio: %.3g\n", ((float)decoded_size)/encoded_size);

    free(encoded_buffer);
    free(decoded_buffer);
    return 0;
}
