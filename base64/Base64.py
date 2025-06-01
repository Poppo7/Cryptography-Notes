import base64

# comment when needing to decode
key = b'TYPE-YOUR-32-BYTE-KEY-HERE'
encoded_key = base64.urlsafe_b64encode(key)
print(encoded_key)


# uncomment decode key when needed

'''
encoded_key = b'VERY_LONG_ENCODED_KEY_STRING_HERE'

decoded_key = base64.urlsafe_b64decode(encoded_key)
print(decoded_key)
'''