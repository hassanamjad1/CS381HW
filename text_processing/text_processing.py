import re

text = "555-1239Dr. Bernard Lander(636) 555-0113Hollingdorp, Donnatella555-6542Fitzgerald, F. Sco\
tt555 8904Rev. Martin Luther King636-555-3226Snodgrass, Theodore5553642Carlamina Scarfoni"
#1
numbers = re.findall( '[0-9]+' , text)
print('Extracting numbers : ' + str(numbers))

#2
names = re.sub( '[0-9]+',";", text )
print('Extracting names : '+ str(names))

#3
standard = re.findall( '[\w. \w \w|\w, \w|\w, A-Z. \w|\w. \w \w|\w \w]+'  , names)
standard = [i for i in standard if i != " "]

for i in range(len(standard)):
  if ',' in standard[i]:
    curr = standard[i].split(',')
    standard[i] = curr[1][1:]+' '+curr[0]

print('standard form with proper order ' + str(standard))

#4
hasTitle = []
for name in standard:
  curr = re.match( '\w{2,3}. ' , name)
  if curr:
    hasTitle.append(True)
  else:
    hasTitle.append(False)
print('Logical Vector to indicate the titles for names : ' + str(hasTitle))


#5
hasMidSecondName = []
for name in standard:
  curr = re.match('\w{1}. \w+ \w+|\w+. \w+ \w+ \w+|\w+ {3,}', name)
  if curr:
    hasMidSecondName.append(True)
  else:
    hasMidSecondName.append(False)
print('Logical Vector to indicate the mid/second for names : ' + str(hasMidSecondName))

#6
string = '<title>+++BREAKING NEWS+++<title>'
# firstTag = re.findall( "<.+>" , string)
firstTag = re.match( "<.{5}>" , string)
# this fails because the re will extract all the character between < and > as + indicates  1 or many occurences and . indicates any character
print('Correctly Extracting first html tag : ' + str(firstTag[0]))

#7
string = '(5-3)^2=5^2-2*5*3+3^2'
# equation = re.findall( "[^1]+" , string)
equation = re.findall( "[^-]+" , string)
print(equation)




