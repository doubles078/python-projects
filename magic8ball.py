import random

def getAnswer(answerNumber):
     if answerNumber == 1:
          return 'It is certain'
     elif answerNumber == 2:
          return 'Probably not'
     else:
          return 'LOLOL'

r = random.randint(1,3)
fortune = getAnswer(r)
print(fortune)
