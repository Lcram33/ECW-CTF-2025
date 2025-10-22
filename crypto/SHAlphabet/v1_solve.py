import hashlib
import itertools
import time



# Target SHA256 hash to crack
TARGET_HASH = "3c33e4fcfc797901b77a41febb30d67be4b175bd32d5fd8cf4c03ff7ceb94ca5"


# Syllables observed in the database
SYLLABLES = [
    # Core consonant clusters
    "ck", "sp", "th", "ly", "r", "ng", "spr", "thr", "rth", "rsp",
    "ckr", "rly", "sth", "sps", "rck", "nck",

    # Common endings and transitions
    "ing", "ingr", "ingth", "ingck", "ring", "thing", "cking", "sping",

    # Frequent vowel & diphthong cores
    "a", "e", "i", "o", "u", "ae", "ea", "eo", "oo", "ua", "ue", "au", "ou", "io",

    # Combined stems and hybrids
    "lyth", "thly", "ckly", "uck", "uckly", "ack", "ackly", "uth", "uthly",
    "ark", "ork", "erk", "irk", "urk", "ra", "ro", "ru", "re", "ri",

    # Prefix-like units
    "spu", "spa", "spo", "spe", "spi", "spl", "spr", "spaing", "spuing",
    "cku", "cka", "cko", "cke", "cki",

    # Suffix-like units
    "ly", "lyly", "ing", "ingly", "ring", "rly", "thly", "ckly", "inglyck",

    # Bridge segments within words
    "rth", "nth", "rck", "ckth", "spth", "thsp", "cksp", "spck",

    # Extended complex segments
    "ckingr", "spingr", "thring", "ckspth", "ingsp", "ingth", "ingck", "ingr",
    
    # Repetitions and echo clusters
    "lyly", "ckck", "thth", "spsp", "rlyr", "ngng",
]


# Minimum and maximum lengths for generated candidates
MIN_LEN = 8
MAX_LEN = 30


def sha256_hash(s: str) -> str:
    """Return the hexadecimal SHA256 hash of a string."""
    return hashlib.sha256(s.encode()).hexdigest()


def print_duration(seconds):
    one_minute = 60
    one_hour = one_minute * 60
    one_day = one_hour * 24
    one_month = one_day * 30
    one_year = round(one_day * 365.25)

    duration_string = ""
    years = seconds // one_year
    if years > 0:
        seconds %= one_year

    months = seconds // one_month
    if months > 0:
        seconds %= one_month

    days = seconds // one_day
    if days > 0:
        seconds %= one_day

    hours = seconds // one_hour
    if hours > 0:
        seconds %= one_hour

    minutes = seconds // one_minute
    if minutes > 0:
        seconds %= one_minute

    year_string = f" year{'' if years <= 1 else 's'} "
    month_string = f" month{'' if months <= 1 else 's'} "
    day_string = f" day{'' if days <= 1 else 's'} "
    hour_string = f" hour{'' if hours <= 1 else 's'} "
    minute_string = f" minute{'' if minutes <= 1 else 's'} "
    second_string = f" second{'' if seconds <= 1 else 's'}"

    if years > 0:
        duration_string += f"{years}{year_string}"
    if months > 0:
        duration_string += f"{months}{month_string}"
    if days > 0:
        duration_string += f"{days}{day_string}"
    if hours > 0:
        duration_string += f"{hours}{hour_string}"
    if minutes > 0:
        duration_string += f"{minutes}{minute_string}"
    if seconds > 0:
        duration_string += f"{seconds}{second_string}"

    if duration_string == "":
        duration_string = "instantly"

    print(duration_string.strip())


# Main program - Brute-force search
start = time.time()

count = 0
found = False
for r in range(2, 6):  # combinations of 2 to 5 syllables
    for combo in itertools.product(SYLLABLES, repeat=r):
        candidate = ''.join(combo)
        if MIN_LEN <= len(candidate) <= MAX_LEN:
            count += 1
            if sha256_hash(candidate) == TARGET_HASH:
                print(f"[!] Found! Original word: {candidate}")
                found = True
                break
    if found:
        break

stop = time.time()

if not found:
    print("[X] No match found within these combinations.")

formatted_count = f"{count:,}".replace(",", " ")
print(f"[i] Total attempts: {formatted_count}")
print(f"[i] Time taken: ", end="")
print_duration(round(stop - start))
