import random 

repeat = True
while repeat == True:
  words = ['Niners', 'Garoppolo', 'Rice', 'Bosa', 'Kittle', 'Williams']
word = (random.choice(words)) 
print("Your word has", len(word), "letters.")

if word in words:
    print("Your word is a 49er.Guess the characters.")
    
    
guesses = ''
turns = 12
 
while turns > 0:
     failed = 0
     for char in word:
         if char in guesses:
            print(char)
         else:
            print("_")
            failed += 1
             
         if failed == 0:
           print("You Win")
           print("The word is: ", word)
           break
     guess = input("guess a character:")
     guesses += guess
     if guess not in word:
         turns -= 1
         print("Wrong")
         print("You have", + turns, 'more guesses')
     if turns == 0:
            print("You Lose")

   


