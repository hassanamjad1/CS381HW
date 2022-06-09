'''
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''

phone_key = {
  "2" : "abc",
  "3" : "def",
  "4" : "ghi",
  "5" : "jkl",
  "6" : "mno",
  "7" : "pqrs",
  "8" : "tuv",
  "9" : "wxyz"
}
def letterCombinations(digits):
  res = []
  a = digits[0]
  b = digits[1]
  for i in range(len(phone_key[a])):
    for j in range(len(phone_key[b])):
      str = phone_key[a][i] + phone_key[b][j]
      res.append(str)
  return res
      

  
print(letterCombinations("23"))

