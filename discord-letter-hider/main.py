# discord-letter-hider
text = input("$> ")

output = ""
for letter in text:
    output += f"||{letter}||"

print(output)