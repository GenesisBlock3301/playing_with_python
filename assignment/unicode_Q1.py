import sys

UNICODE_CHARACTER = {
    "nul": "U+0000",
    "lf": "U+000A",
    "cr": "U+000D",
    "pad": "U+0080",
    "esc": "U+001B"
}
val = sys.argv[1]
if val in UNICODE_CHARACTER:
    print(UNICODE_CHARACTER[val.lower()])
else:
    print("error")