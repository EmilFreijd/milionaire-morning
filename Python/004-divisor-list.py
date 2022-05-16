__author__ ="Emil Freijd"

number = int(input("Enter the number to be divised: "))

list_of_divised_numbers = []

for i in range(1, number+1):
    if number % i == 0:
        list_of_divised_numbers.append(i)

print(list_of_divised_numbers)


print("New Code Snippet")





#number=int(input("num:"))
#
#list_of_divised_numbers=[]
#
#for num in range(1,number+1):
#    if number % num == 0:
#        list_of_divised_numbers.append(num)
#
#print(list_of_divised_numbers)


__author__ = 'jeffreyhunt'

num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)