# The decoder is just the same Solitaire process as encoding, but you subtract the keystream from the cipher
# instead of the adding you do when encoding.
import encoder
import sys

if __name__ == "__main__":
    message = sys.argv[1]
    key = sys.argv[2]

    print(encoder.encode(message, key, decode=True))