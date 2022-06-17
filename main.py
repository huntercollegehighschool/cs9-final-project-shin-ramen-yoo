"""
Name(s):
Name of Project:
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
import random

WordList = ["donut", "basin", "sijo" "finals" "telephone", "bestie", "slaying", "pizza", "computer", "latin", "language", "grave", "chaos" "malding", "balding", "seething" "bozo", "success", "college", "doom", "failure", "dead", "teamwork"]

word = random.choice(WordList)
word = list(char for char in word)

GuessesUsed = 1
LettersUsed = []

WordChoice = list(len(word)*"_")

while GuessesUsed < 10:
  if set(LettersUsed).issuperset(word) == True: #if the word they guess is in it it will register, if it's not it will count as a guess.
    print("slay bestie u got the word, the word was",''.join(word)+"!")
    exit()
  def get_index_positions(word, GuessLetter):
      index_pos_list = []
      index_pos = int(0)
      while word.count(GuessLetter) > len(index_pos_list):
        index_pos = word.index(GuessLetter, index_pos)
        index_pos_list.append(index_pos)
        index_pos += 1
      return index_pos_list
      index_pos_list = get_index_positions(word, GuessLetter)

  GuessLetter = input("\nguess a letter or a word: ")
  GuessLetter = GuessLetter.lower() #makes lowercase, easier
  temp2 = ''.join(word)

  if GuessLetter == temp2:
    print("slay bestie u got the word, the word was ",''.join(word)+"!")
    exit()
  elif GuessLetter.isalpha == False:
      print("that is not a letter, please try again smh")

  elif GuessLetter in LettersUsed:
    print("you've already guessed that letter bro, try again")
    print("thus far u have guessed: ", ''.join(WordChoice))
    print("thus far u have guessed:: ", ', '.join(LettersUsed))
    print("you only have",str(10-GuessesUsed),"guess(es) left, hurry up!")

  elif GuessLetter not in word:
    print(GuessLetter,"is not in the word sorry L")
    GuessesUsed += 1
    print("thus far u have guessed: ", ''.join(WordChoice)) 
    LettersUsed.append(GuessLetter)
    print("thus far u have guessed:", ', '.join(LettersUsed))
    print("You have",str(10-GuessesUsed),"guess(es) left, hurry up!")
  
  elif GuessLetter in word and word.count(GuessLetter) > 1: #if the guessed letter is in the word more than once
      print(GuessLetter, "is in the word W based, nice job")
      temp = []
      WordChoice = ''.join(WordChoice)
      for i in range(len(temp2)):
        if temp2[i] == GuessLetter:
          temp.append(i)
      for i in temp:
        WordChoice = WordChoice[:i] + GuessLetter + WordChoice[i+1:] 
      print("thus far u have guessed:", ''.join(WordChoice))
      LettersUsed.append(GuessLetter)
      LettersUsed.sort()
      print("thus far u have guessed the letters or words:", ', '.join(LettersUsed))
      print("you only have",str(10-GuessesUsed),"guess(es) left, move it!")
  elif GuessLetter in word:
    print(GuessLetter, "is in the word W based, nice job")
    LettersUsed.append(GuessLetter)
    letterPosition = int(word.index(GuessLetter))
    WordChoice.pop(letterPosition)
    WordChoice.insert(int(letterPosition), GuessLetter)
    print("thus far u have guessed:", ''.join(WordChoice))
    print("thus far u have guessed the letters or words:", ', '.join(LettersUsed))
    print("you only have",str(10-GuessesUsed),"guess(es) left, move it!")


print("sucks to suck LOL, the word was",''.join(word)+".")
exit()
