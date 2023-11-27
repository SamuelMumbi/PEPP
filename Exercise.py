#Q1 Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
# Initialize an empty list
list1 = []
# Accept user input to create a list of integers
for list1 in range(5):
    try:
        num = int(input("Enter an integer: "))
        list1.append(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")
# Compute the sum of all integers in the list
list_sum = sum(list1)

# Print the list and its sum
print("List:", list1)
print("Sum:", list_sum)
  
#Q2 Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
favourite_books = ("Holy_Bible", "RichDadPoorDad", "WinFriends&InfluencePeple","PurposeDrivenLife","ArtOfWar")
for b in favourite_books:
  print(b)
  if b=="ArtOfWar":
    break
  
# Q3 Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

#innitialize an empty dictionary
d={} 
#accept user input(name,age,color)
name=input("what is your name? \n")
Age=input("how old are you? \n")
color=input("what is your favourite colour? \n")
#print results
print(d)

#Q4 Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

#innitialize an empty set
s1=set()
#accept values of integers and print results
for s1 in range(8):
        num = int(input("Enter integers:"))
s1={1,2,3,4,5}
s2={4,5,6,7,1}
s3=set(s1).intersection(s1)
print(s3)

#Q5 Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters
strings = []
strings=["good","nice ","love","band"]
results=[i.lower()+"y" for i in strings]
print("results!!", results)



