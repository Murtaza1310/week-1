#Q7. What do you understand about mutable and immutable data types? Give examples for both showing 
#this property.

#Changing a data on a particular index are called Mutable object like list are mutable
#we cannot change a data on a particular object are called immutable object like strings

# The example of Mutable object

list = [30,20,5,4,9,'Murtaxa','gon']
list[5]='tutorial'

print(list)

#now as u can see we creat a list and write index on it then i will change the index 5 with tutorial and it is not show any error and completely change the index this is mutable

#The example of immutable object

M = 'Murtaza'
M[3]='b'

#But while I try to change the index 3 in the string it show me error and cannot change this is immutable
