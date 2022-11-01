import random 
quotes=["All our dreams can come true, if we have the courage to pursue them.","The secret of getting ahead is getting started.","I've missed more than 9,000 shots in my career. I’ve lost almost 300 games. 26 times I’ve been trusted to take the game winning shot and missed. I’ve failed over and over and over again in my life and that is why I succeed. – Michael Jordan","The best time to plant a tree was 20 years ago. The second best time is now.","We need to accept that we won’t always make the right decisions, that we’ll screw up royally sometimes – understanding that failure is not the opposite of success, it’s part of success."]
answer = input ("Do you want to play games or quotes?(Type joke or quote, all in smaller case)")

if answer == 'joke': 
  print("Welcome to the Jokes Corner! What\'s your name?",end= ' ')
  name = input()
  print('Hey '+ name+' try to guess the answers for these jokes!')
  print()
  print('What do you get when you put three ducks in a box?')
  guess = input()
  answerFirst= 'A box of quackers.' 
  if guess == answerFirst: 
    print('WOW! Good job you did it!')
  else: 
    print('Oops!The correct answer is '+answerFirst)
  print ()
  print("What did the pecan say to walnut?")
  guess= input()
  answerSec= "We're friends because we are nuts"

  if guess == answerSec:
      print('Correct!, the right answer is '+ answerSec)
      
  else:
      print("Good try, but the right answer answer is "+ answerSec)
  print()
  print("Why did the student eat his homework? ")
  guess= input()
  answerThird='The teacher told him it was a piece of cake.'

  if guess == answerThird:
      print("Correct!, the right answer is "+ answerThird)
      
  else:
      print("Good try, but the right answer answer is "+ answerThird)
  print()
  print('What do you call a sad coffee?')#print()adds a newline character to the end of the string it prints
  guess= input()
  answerFourth= 'A Depresso'

  if guess == answerFourth:
      print('Correct!, the right answer is ',answerFourth)
      
      
  else:
      print('Good try, but the right answer answer is '+ answerFourth)

elif answer == 'quote': 
  name = input ("Hello, what\'s your name?")
  print ("Hi "+ name + "! Welcome to Quotemania!\n")
  print(random.choice(quotes))
  print ("\n")
  i = str(input("Press 'a' for another quote or presss 'b' to quit\n "))
  if i == 'a': 
    print(random.choice(quotes))
    print ("\n")
    i = str(input("Press 'a' for another quote or press 'b' to quit \n"))

  elif i == 'b': 
    quit()

  
