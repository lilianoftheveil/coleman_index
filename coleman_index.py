# -*- coding: utf-8 -*-

x = input("Digit your text: ")

# Number of words
w = 1
for a in x:
    if a == " ":
        w = w + 1

# Number of sentences
s = 0
for b in x:
    if b == "." or b == "!" or b == "?" or b == "...":
        s = s + 1

# Number of letters
l = 0
for c in x:
    # PYTHON Documentation (Utilities for ASCII characters - that check all letters lower and upper -)
    if c.isalpha():
        l = l + 1

# Coleman-Liau index
cl = (l / w * 100)
cs = (s / w * 100)
calcu = round((0.0588 * cl) - (0.296 * cs) - 15.8)

# Print of the Before Grade 1
if calcu < 1:
    print("Before Grade 1")

# Print of the Grade 1
if calcu == 1 or calcu > 1 and calcu <= 16:
    print(f"Grade {calcu}")

# Print of the Grade more than 16
if calcu > 16:
  print("Grade 16+")

print(w)
