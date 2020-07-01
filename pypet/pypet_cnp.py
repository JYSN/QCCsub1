
# Declare vars

"""
print('give this a second go!')
name = 'Charlie Sheen'
bloodtype = 'tiger'
years = 40
age = 'a Benjamin Button'
requires_more_cocaine = True
kilos_left = 5.4
lives_left = 9
photo_healthy = '(╯°□°）╯︵ ┻━┻'
photo_low_on_coke = '┬─┬ ノ( ゜-゜ノ)'

martin_photo = '( ͡° ͜ʖ ͡°)'
martin_sober = '(-_-)#'
"""

# Dictionaries & Lists

adonis = {
  'name': 'Charlie Sheen',
  'requires_more_cocaine' : True,
  'charisma' : 3,
  'photo_coked' : '(╯°□°）╯︵ ┻━┻',
  'photo_sober' : '┬─┬ ノ( ゜-゜ノ)',
  'lives_left' : 9,
  'kilos_left' : 10.4,
   'quote' : "I am on a drug. It's called Charlie Sheen. It's not available. If you try it once, you will die. Your face will melt off and your children will weep over your exploded body."
}

coach = {
  'name' : 'Emilio Estevez',
  'requires_more_cocaine' : False,
  'charisma' : 2,
  'photo_coked' : '(ﾉﾟ0ﾟ)ﾉ~',
  'photo_sober' : '(－‸ლ)',
  'lives_left' : 3,
  'kilos_left' : 4.2,
  'quote' : 'QUAAAAAACCCK!!! QUAACCCCKK!!!'
}

celebs = [adonis, coach]

# Functions
def checkpoint(celebrity):
  if celebrity['requires_more_cocaine'] == True:
    print(celebrity['photo_sober'])
  else:
    print(celebrity['photo_coked'])

def vitals(celebrity):
  print(celebrity['name'], 'now has', celebrity['charisma'], 'CHA,', 'and has', celebrity['kilos_left'], 'kilos', ' and ', celebrity['lives_left'], ' lives left.')

def deal(celebrity):
  if celebrity['requires_more_cocaine'] == True:
    celebrity['requires_more_cocaine'] = False
    celebrity['kilos_left'] = celebrity['kilos_left'] - 0.5
    celebrity['lives_left'] = celebrity['lives_left'] - 0.1
    print(celebrity['name'], 'sneaks off to the bathroom for five minutes...\n')
    print(celebrity['name'] + ':', celebrity['quote'])
    elipsis()
    checkpoint(celebrity)
  else:
    print('The celebrity already IS a golden god!')
    checkpoint(celebrity)

def party(on_wayne):
  checkpoint(on_wayne)
  deal(on_wayne)

  # output format cheats
    # newline
def div() :
  print('\n')
    # boxy style divider
def cage() :
  print('|_|_|_|_|_|_|_|_|_|_|_|_|_|')

def elipsis() :
  print('.......')




# Printing statements
for celeb in celebs:
  print('hello ', celeb['name'])
  print(celeb['photo_coked'])

#print ('hello, ' + celebs['name'])
#print (celebs['photo_coked'])

# Conditionals


# Tests





# Results
  # formatting
div()
elipsis()
div()
cage()
print(' C E L E B R I G O T C H I !')
cage()
div()
"""vitals(adonis)
#print(adonis['requires_more_cocaine' 'charisma' 'lives_left' 'kilos_left'])
div()
deal(adonis)
div()
vitals(adonis)
div()
deal(adonis)
div()
vitals(adonis)
cage()
print('Charm:', adonis['charisma'], ', Lives:', adonis['lives_left'])"""
cage()
for celeb in celebs:
  party(celeb)


# A history of bad decisions:
"""Feed = deal()
  hungry = requires_more_cocaine
  weight = charisma, INVERSE: lives_left, kilos_left
  species ("cat") = "adonis"

  Get input from the user with raw_input()
  \n for newline
"""