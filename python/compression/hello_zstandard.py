#!/usr/bin/env python3
# coding=utf-8
"""
Uses python-zstandard wrapper around zstandard C library (simplest usage of API for round-trip compress/decompress)
"""
# This module attempts to import and use either the C extension or CFFI implementation for python-zstandard
import zstd


if __name__ == '__main__':
    # bytes data to compress
    data = b"This is a test of the emergency broadcast system. If something bad was really happening, you'd be screwed."

    # The ZstdCompressor class provides an interface for performing compression operations.
    # Each instance is associated with parameters that control compression behavior.
    cctx = zstd.ZstdCompressor()

    # compress(data) compresses and returns data as a one-shot operation
    # The data argument can be any object that implements the buffer protocol.
    compressed = cctx.compress(data)

    # The ZstdDecompressor class provides an interface for performing decompression.
    # Each instance is associated with parameters that control decompression.
    dctx = zstd.ZstdDecompressor()

    # decompress(data) can be used to decompress an entire compressed zstd frame in a single operation.
    # By default, decompress(data) will only work on data written with the content size encoded in its header.
    # If compressed data doesn't have content size embedded, decompress by specifying the max_output_size argument.
    decompressed = dctx.decompress(compressed, max_output_size=1048576)

    assert data == decompressed

    print("Zstandard compression ratio: {0:.3g}".format(len(data) / len(compressed)))
    print("Uncompressed data (length {}): {!r}".format(len(data), data))
    print("Compressed   data (length {}): {!r}".format(len(compressed), compressed))
    print("Decompressed data (length {}): {!r}".format(len(decompressed), decompressed))
