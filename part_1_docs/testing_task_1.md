### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #The = should be ==. 
      return True
    else #There needs to be a : at the end of else.
      return False
   

  dif highest_card(self, card1 card2): #Def is misspelled. There also needs to be a comma between card1 and card2.
  if card1.value > card2.value: #if needs to be indented.
    return card #Card isn't defined. Card1 needs to be used instead.
  else: #else needs to be indented.
    return card2
  


def cards_total(self, cards): #This whole block of code will be unreachable because it is not indented properly.
  total #total needs to be set to zero.
  for card in cards:
    total += card.value
    return "You have a total of" + total #total will need to be converted into a string.
  
```
