from math import factorial
with open('dict.txt', "r") as input_file:
    words = input_file.read().split('\n')
adjectives = 0
nouns = 0
verbs = 0
cool_sentences = 0
for thing in words:
    if thing[len(thing)-2:] == 'yo':
        adjectives += 1
    elif thing[len(thing)-2:] == 'ka':
        nouns += 1
    else:
        verbs += 1
if adjectives == 0 or nouns == 0 or verbs == 0:
    print(0)
elif adjectives == 1 and nouns == 1 and verbs == 1:
    print(1)
elif adjectives <=7:
    for i in range(1,8):
        cool_sentences += factorial(adjectives)*nouns*verbs/factorial(adjectives-i)
else:
    for i in range(1, 8):
        cool_sentences += factorial(adjectives)*nouns*verbs/factorial(adjectives-i)
    cool_sentences 
print(cool_sentences)

           
