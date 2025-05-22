# The Basics of Cryptography
**Cryptography** is the art and science of keeping information secret and secure by transforming it into an unreadable format.
This script is an introduction to basic cryptography concepts, focusing on Fernet encryption and Base64 encoding.

## Fernet
**Fernet** is a symmetric encryption method that uses a **32-byte key** (256 bits). This key is typically shown as a Base64 string for convenience, but under the hood it is raw binary data. Fernet provides both encryption and decryption, ensuring the authenticity and confidentiality of the data it protects.
Example: `AvcDrS0nkeK2rHi1PsdowPdNWIPkcdA1qbGv3ozkUIM=`
If you're curious about the equals sign at the end, it isn't part of the core key material itself but is a necessary component of the base64 encoding standard to ensure proper decoding.

## Base64
**Base64** is a way to encode binary data in a text-friendly format. It doesn't encrypt the data but rather converts bytes (which may include unprintable characters) into character-encoding-standard, (like ASCII, Unicode, and UTF-8) making it safer to store or transmit in text-based environments.

When working with **Fernet** keys, you'll often see a **32-byte key** represented in Base64 form. Decoding that Base64-encoded string returns the raw 32-byte key used for actual encryption and decryption.

## Bytes
A **byte** consists of 8 bits. For example, `10101010` is one byte (8 bits in binary). Therefore, **32 bytes** equals:

32 bytes * 8 bits/byte = 256 bits

| Bits (8) | Example   |
|----------|-----------|
| 8        | 10101010  |

## Installation

Run the following command to install the required Python package:

`python -m pip install cryptography  `


**Linux:**

`sudo apt-get update`

`sudo apt-get install build-essential libssl-dev libffi-dev python3-dev`

## Sources
**Base64:**
https://en.wikipedia.org/wiki/Base64

**Fernet:**
https://cryptography.io/en/latest/fernet/

**Byte:**
https://en.wikipedia.org/wiki/Byte

**Sample Fernet Key Generator:**
https://fernetkeygen.com/
