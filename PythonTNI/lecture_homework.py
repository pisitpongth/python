text = input("Enter your text: ")

a = 0
e = 0
i = 0
o = 0
u = 0

for x in range(len(text)):
    if text[x] == "a" or text[x] == "A":
        a = a + 1
    elif text[x] == "e" or text[x] == "E":
        e = e + 1
    elif text[x] == "i" or text[x] == "I":
        i = i + 1
    elif text[x] == "o" or text[x] == "O":
        o = o + 1
    elif text[x] == "u" or text[x] == "U":
        u = u + 1

print("a =", (a), "e =", (e), "i =", (i), "o =", (o), "u =", (u))
