# Q1
grades = [85, 92, 78, 95, 88]
grades.append(90)
grades.sort()
print(f"Sorted grades: {grades}")
print(f"Sorted grades:", grades)
print(f"Highest grade: {grades[-1]}")
print(f"Lowest grade: {grades[0]}")
print(f"Total number of grades: {len(grades)}")


# Q2
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print(f"Number of apples: {apple_count}")
milk_position = cart.index("milk")
print(f"Position of milk: {milk_position}")
cart.remove("apple") #using remove
removed_item = cart.pop() #remove last item of the array
print(f"remove item using pop: {removed_item}")
print("Is banana in cart?", "banana" in cart)


# Q3
point1 = (3, 5)
point2 = (7, 2)
x1, y1 = point1
x2, y2 = point2
print(f"X1={x1}, Y1={y1}")
print(f"X2={x2}, Y2={y2}")
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 
print("Distance between points:", distance)


# Q4
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
Wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace") # add a person
print(f"Monday class: {monday_class}")
print(f"Wednesday class: {Wednesday_class}")
print(f"Attended both classes: {monday_class & Wednesday_class}") # shift 7 (find duplicate)
print(f"Attended either classes: {monday_class | Wednesday_class}") # shift \ (union)
print(f"Only Monday: {monday_class - Wednesday_class}") # specific one.
print(f"Only One Class: {monday_class ^ Wednesday_class}") #, ^ = caret, shift 6
allStudents = monday_class | Wednesday_class
print("Is Monday subset of all students?", monday_class <= allStudents) # True


# Q5
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
print(f"Alice phone number: {contacts['Alice']}")
contacts["Diana"]= "555-4321"
print(f"Contact after adding Diana: {contacts}")
contacts["Bob"]= "555-0000"
print(f"Contact after update Bob: {contacts}")
del contacts["Charlie"] # delete Charlie
print(f"Contact after delete Charlie: {contacts}")
print(f"All names {contacts.keys()}")
print(f"All numbers {contacts.values()}")
print(f"Total contacts {len(contacts)}")
