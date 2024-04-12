import random

words = ["찍", "찍찍", "찍찍찍", "ㅉㅣㄱ", "ㅉ", "쮝", "쭈ㅣㄱ", " ", "!", "?", ",", "?!", "...", "ㅋ"]
said = []
rNum = random.randint(1, 30)

for i in range(rNum):
    dice = random.randint(0, len(words) - 1)
    said.append(words[dice])
print("".join(said))