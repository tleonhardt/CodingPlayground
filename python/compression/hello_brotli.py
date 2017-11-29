#!/usr/bin/env python3
# coding=utf-8
"""
Uses brotli module wrapper around Brotli C library (simplest usage of API for round-trip compress/decompress)
"""
import brotli


if __name__ == '__main__':
    # bytes data to compress
    data = b"This is a test of the emergency broadcast system. If something bad was really happening, you'd be screwed."

    # Compress a byte string
    compressed = brotli.compress(data)

    # Decompress a compressed byte string
    decompressed = brotli.decompress(compressed)

    assert data == decompressed

    print("Brotli compression ratio: {0:.3g}".format(len(data)/len(compressed)))
    print("Uncompressed data (length {}): {!r}".format(len(data), data))
    print("Compressed   data (length {}): {!r}".format(len(compressed), compressed))
    print("Decompressed data (length {}): {!r}".format(len(decompressed), decompressed))
