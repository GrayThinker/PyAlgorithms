"""
Triple DES, RSA, blowfish, twofish, AES, IDEA, MD5, HMAC
"""

def pad(text):
    length = 16 - (len(text)%16)
    