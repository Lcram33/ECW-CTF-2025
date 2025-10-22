import hashlib
import random
import time

# Target SHA256 hash to crack
TARGET_HASH = "3c33e4fcfc797901b77a41febb30d67be4b175bd32d5fd8cf4c03ff7ceb94ca5"

# Syllables with associated frequencies (example normalized frequencies from dataset)
SYLLABLES_FREQ = [
    ("ck", 0.10), ("sp", 0.09), ("th", 0.09), ("ly", 0.08), ("ing", 0.07),
    ("r", 0.06), ("ng", 0.06), ("spr", 0.04), ("thr", 0.03), ("rth", 0.03),
    ("rsp", 0.03), ("ingr", 0.02), ("thly", 0.02), ("ckly", 0.02), ("uck", 0.01),
    ("a", 0.02), ("e", 0.02), ("i", 0.02), ("o", 0.02), ("u", 0.02),
    ("ae", 0.01), ("oo", 0.01), ("ua", 0.01), ("ue", 0.01), ("au", 0.01),
    # Add other syllables and frequencies here
]

SYLLABLES = [x[0] for x in SYLLABLES_FREQ]
WEIGHTS = [x[1] for x in SYLLABLES_FREQ]

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


# Main program - Weighted random search
start = time.time()

count = 0
found = False
max_attempts = 30_000_000  # limit attempts to avoid infinite loops

while count < max_attempts and not found:
    length = random.randint(2, 5)  # number of syllables to combine
    combo = random.choices(SYLLABLES, weights=WEIGHTS, k=length)
    candidate = ''.join(combo)
    if MIN_LEN <= len(candidate) <= MAX_LEN:
        count += 1
        if sha256_hash(candidate) == TARGET_HASH:
            print(f"[!] Found! Original word: {candidate}")
            found = True
            break

stop = time.time()

if not found:
    print("[X] No match found within weighted random attempts.")

formatted_count = f"{count:,}".replace(",", " ")
print(f"[i] Total attempts: {formatted_count}")
print(f"[i] Time taken: ", end="")
print_duration(round(stop - start))
