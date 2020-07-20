#Python refresher
# Enter a number and get an item from a list

# string is made using brackets
stringlst = ["Apple","Orange","Bananna","Blueberry","Grapefruit"]
# val is the integer value of the text entry
val = int(input("Enter a number between 0 and 4:"))
# the value is entered into the list and text is defined as the x entry
txt = stringlst[val]
# text is printed back to the user
print("You picked: ",txt)
