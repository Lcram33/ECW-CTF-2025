from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import unhexlify

# Given data
ct_hex = "d2373cdd6d999679668b0d4587abbeb325bda0343841f3cdb1e4ec8f7b597f75ddde462a9bbefb828318f3bc16af0f52dce3ffbfa34670557bf89ee98ce45da82eb45abd320c4b0a143e2569a6bd8a8f8d7c0e52a76ff4b4505e82df2c204632"
key_hex = "3de090e7059fb1d7f77dec50078405c855e3f1a46589e72db2602c7d7e8403b8"

# Convert hex to bytes
ciphertext = unhexlify(ct_hex)
key = unhexlify(key_hex)

# no success with these modes
# def try_decrypt_aes_modes(ciphertext, key):
#     results = {}

#     # AES-ECB
#     cipher = AES.new(key, AES.MODE_ECB)
#     results['ECB'] = cipher.decrypt(ciphertext)

#     # AES-CBC (first 16 bytes as IV)
#     iv = ciphertext[:16]
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     results['CBC'] = cipher.decrypt(ciphertext[16:])

#     # AES-CTR (first 8 bytes as nonce)
#     nonce = ciphertext[:8]
#     ctr = Counter.new(64, prefix=nonce, initial_value=0)
#     cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
#     results['CTR'] = cipher.decrypt(ciphertext[8:])

#     return results

def try_more_modes(ciphertext, key):
    results = {}
    iv = ciphertext[:16]

    # AES-OFB
    cipher = AES.new(key, AES.MODE_OFB, iv)
    results["OFB"] = cipher.decrypt(ciphertext[16:])

    # AES-CFB
    cipher = AES.new(key, AES.MODE_CFB, iv)
    results["CFB"] = cipher.decrypt(ciphertext[16:])

    # AES-GCM (use first 12 bytes as nonce, last 16 as tag)
    if len(ciphertext) > 28:
        nonce = ciphertext[:12]
        tag = ciphertext[-16:]
        body = ciphertext[12:-16]
        try:
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
            results["GCM"] = cipher.decrypt_and_verify(body, tag)
        except Exception as e:
            results["GCM"] = str(e)

    return results

results = try_more_modes(ciphertext, key)

for mode, data in results.items():
    try:
        print(f"{mode}:", data.decode('utf-8', errors='ignore'))
    except Exception:
        print(f"{mode} raw:", data)
