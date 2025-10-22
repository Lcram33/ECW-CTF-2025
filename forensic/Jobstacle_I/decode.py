import base64
import codecs

def is_ascii(s):
    try:
        s.decode('ascii')
        return True
    except UnicodeDecodeError:
        return False

with open("strings.txt", "r", encoding="utf-8", errors="ignore") as f:
    data = f.read().splitlines()

for line in data:
    line = line.strip()
    if not line:
        continue

    # Try direct Base64
    try:
        decoded = base64.b64decode(line, validate=True)
        if is_ascii(decoded):
            print(f"[BASE64] {line} => {decoded.decode('ascii')}")
            continue  # skip ROT13 if direct Base64 worked
    except (base64.binascii.Error, ValueError):
        pass

    # Try ROT13 then Base64
    try:
        rot13_line = codecs.decode(line, 'rot_13')
        decoded = base64.b64decode(rot13_line, validate=True)
        if is_ascii(decoded):
            print(f"[ROT13+BASE64] {line} => {decoded.decode('ascii')}")
    except (base64.binascii.Error, ValueError):
        continue
