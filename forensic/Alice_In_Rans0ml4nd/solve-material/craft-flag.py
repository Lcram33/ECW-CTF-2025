import hashlib


def sha_256_str(input_str):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_str.encode('utf-8'))
    return sha256_hash.hexdigest()


flag_data = {
    "The email address used by the attacker": 'it-support@alices.corp',
    "The email address targeted within the company": 'natacha.routi@alice.corp',
    "The MD5 hash of the first malware": '8d8b36683ed095a7eebe4e8c70141bfc',
    "The domain name contacted to download a script": 'ykfqaqa.ru',
    "The password used to connect to the server": 'admin123sY*-+',
    "The name of the scheduled task that was executed": 'DontTouchMe',
    "The domain name contacted by the script to download the second malware": 'susqouh.ru',
    "The MD5 hash of the malware present on the server": '5d820e7bbb4e4bc266629cadfa474365',
    "The domain name used for data exfiltration": 'yinxuqab.ru',
    "The name of the ransomware gang (in lowercase)": 'sphinxlock',
    "The cryptocurrency wallet address used by the attackers": '84N2hXaVqgS5DzA1FpkGuD98Ex2cVXH6k8RwZ7PmUz1oBY9X6GZYMT3WJYkfY9AdELNH2tsBrxJZcdkLkJxYH5RZ73XKbPq',
    "The final flag contained in a file exfiltrated by the malware": 'DNS_TUNNEL_SUCCESS_C0MPLETE'
}

flag_to_hash = ':'.join(flag_data.values())
flag = "ECW{" + sha_256_str(flag_to_hash) + "}"

# Debug / print as in the challenge header
# print("=== Flag data used to generate the hash ===")
# for i, f_tuple in enumerate(flag_data.items()):
#     i += 1
#     key, value = f_tuple
#     print(f"{i}. {key}: `{value}`")
# print()
# print()

print("Generated flag:")
print(flag_to_hash)
print()
print()
print("Final Flag:", flag)