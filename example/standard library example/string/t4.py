

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

fruits = ("apple", "banana", "cherry")
for x in fruits:
  print(x)

fruits = {"apple", "banana", "cherry"}
for x in fruits:
  print(x)

fruits = {"apple":1, "banana":2, "cherry":3}
for x in fruits:
  print(x, fruits[x])

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)