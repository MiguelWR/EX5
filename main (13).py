#Exercício 5

def S(n):
  if len(n) == 0:
      return False
  if n == 'a' or n == 'b':
      return True
  elif n[0] == 'a':
      return S(n[1:])
  elif n[0] == 'b':
      if len(n) > 1:
          return S(n[1:])
      else:
          return False
  else:
      return False

print(S("a"))
print(S("ab"))
print(S("aba"))
print(S("aaab"))
print(S("bbbbb"))