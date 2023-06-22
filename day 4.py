age = 4

if age > 17:
  print("adult")
elif age > 13:
  print("teen")
else:
  print("child")

age1 = 9
if age1 < 13:
  print("child")
elif age1 < 18:
  print("teen")
else:
  print("adult")

#Print statement for every score range along with score

score = 99

if score > 100:
  print("Wow")
  print(score)
elif score > 90:
  print("Great")
  print(score)
elif score > 80:
  print("Good")
elif score > 70:
  print("pass")
  print (score)
else: 
  print(ok)
  print (score)
print("bye")

While loop

counter = 0

while counter <= 3:
  print("I love learning Python!")
  counter += 1
  #counter = counter +1 
  #counter (0-4) <= 3? Yes, so print
  
#List
#create list of numbers
#loop through list
# square list and update

numbers = [1,2,3,4,5,6,7,8]

count = 0
for num in numbers:
  numbers[count] = num**2
  count += 1

#print(numbers)
#print(numbers)

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print("Oysha likes")

Dictionary
carDict = {
  "brand": "mercedes", "model": "s class", "year": 2023
}

print(carDict["brand"])

#List

response = input("What is your name?")

print("Thank you" + ' Oysha')

#Text enter
while True:
  reply = input("Enter Text: ")
  if reply == "stop" : break
  print(reply) 