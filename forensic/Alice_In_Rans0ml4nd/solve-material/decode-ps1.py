# The following import just contains the encoded payload data in a single list :
# payload_data = [0x13, 0x62, ..., 0x3d]
from payload import payload_data

XOR_KEY = 0x37

decoded = ''
for c_int in payload_data:
    c_dec = c_int ^ XOR_KEY
    decoded += chr(c_dec)

with open("deploy-malware-decoded.ps1", 'w') as f:
    f.write(decoded)

print("Decoded successfully")