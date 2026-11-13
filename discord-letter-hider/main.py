# discord-letter-hider
import time
text = input("$> ")

output = ""
for letter in text:
    output += f"||{letter}||"

print(output)
print("Closing in 10 seconds...")
time.sleep(10)