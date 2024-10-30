import random
def display(n):
  ls =['-----\n |  |\n O  |\n/|\ |\n/ \ |','-----\n |  |\n O  |\n/|\ |\n/   |','-----\n |  |\n O  |\n/|\ |\n    |','-----\n |  |\n O  |\n/|  |\n    |','-----\n |  |\n O  |\n |  |\n    |','-----\n |  |\n O  |\n    |\n    |','-----\n |  |\n    |\n    |\n    |']
  print(ls[n])
def choice():
  choice_list=['apple','python','cricket','balls','football']
  return random.choice(choice_list)
def gameplay(wordchoice):
  n =6
  letters=[]
  correct =False
  display(n)
  print('\n\n')
  temp_word ='_'*len(wordchoice)
  print(temp_word,'\n\n')
  while correct==False and n!=0:
    t = input('Enter the letter which you guess\n')
    if t in temp_word or t in letters:
      print('You have already guessed this word try another\n')
    elif t in wordchoice:
      for i in range(len(wordchoice)):
        if wordchoice[i]==t:
          temp_word=temp_word[0:i]+t+temp_word[i+1:]
    else:
      n-=1
      print('\n\nYou have guessed the wrong letter.\nThink you should try again')
      letters.append(t)
    display(n)
    print('\n\nLetters entered :',*letters)
    print(temp_word)
    if temp_word==wordchoice:
      correct =True
  if correct==True:
    print('You won')
  else:
    display(n)
    print('You have run out of guesses')
    print('wrong guesses---->',6)
    print('right guesses---->',len(temp_word)-temp_word.count('_'))
    print('The word was',wordchoice)
w = choice()
gameplay(w)