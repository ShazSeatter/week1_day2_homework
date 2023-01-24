stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list

stops.append("Edinburgh Waverley")


#2. Add "Glasgow Queen St" to the start of the list

stops.insert(0, "Glasgow Queen St")


#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")

stops.insert(4, "Polmont")

#4. Print out the index position of "Linlithgow"

index_1 = stops.index("Linlithgow")
print(index_1) 
#  save this into a variable to be able to view it in print 

#5. Remove "Livingston" from the list using its name

stops.remove("Livingston")

#6. Delete "Cumbernauld" from the list by index

stops.pop(2)
print(stops)

#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop


# PythonMethods
# https://docs.python.org/3/tutorial/datastructures.html
# quiz
# https://docs.google.com/forms/d/e/1FAIpQLSc0FNd66FGGdtQMRC6_fx5r3mp6zGA3EP2e1VoImdqS2FcAiA/viewform
