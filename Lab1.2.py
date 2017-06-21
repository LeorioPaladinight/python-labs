import time

# masochism
print('Write the word')
word = input().lower()
key = input().lower()
if len(word) != len(key):
    print('Error')
    time.sleep(15)
bfp = 0
brain = []
while bfp < len(word):
    brain.append(key[bfp])
    anb = ord(brain[bfp])
    anb -= anb - bfp - 1  # Делает порядок числа с 97-122 до 1-26
    bfw = ord(word[bfp])
    brain[bfp] = chr(anb + bfw)
    print (brain[bfp])
    bfp += 1



# word - your word
# key - no comment
# bfp - buffer for power, before it is i
# anb - another buffer
