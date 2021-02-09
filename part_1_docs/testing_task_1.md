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
    if card.value = 1: # Should use == is to assign value
      return True
    else # : Expected for body of else statement
      return False


  dif highest_card(self, card1 card2): # dif if a typo. should
  if card1.value > card2.value:
    return card # Card is not defined
  else:
    return card2
  # Line 28-31 need to be indented to be a body of the function


def cards_total(self, cards):
  total # defined but never given value
  for card in cards:
    total += card.value
    return "You have a total of" + total
```
