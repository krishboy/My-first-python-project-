z=int(input("Enter a number:",))
f=0
for i in range(2,z):
  if z%i==0:
    f=1
    print(i)
    break
if f==1:
  print(z,"is not a Prime number.")
else:
  print(z,"is a Prime number.")
  x=z
  rev=0
  while x>0:
    r=x%10
    rev=rev*10+r
    x=x//10
  print("Reverse of the given number is",rev)
  if rev==z:
    print("Hence",z,"is a palindrome")
  else:
    print("Hence",z,"is not a palindrome")
