import random as rd

a = []
b = []

list_a_starting_range = int(input("List a starting range: "))
list_a_ending_range = int(input("List a ending range: "))
list_a_range_length = int(input("List a range length: "))
list_b_starting_range = int(input("List b starting range: "))
list_b_ending_range = int(input("List b ending range: "))
list_b_range_length = int(input("List b range length: "))

for z in range(0,list_a_range_length):
    a.append(rd.randint(list_a_starting_range, list_a_ending_range))

for z in range(0,list_b_range_length):
    b.append(rd.randint(list_b_starting_range, list_b_ending_range))

print(a)
print(b)

list = []
for x in a:
    for y in b:
        if x == y not in list:
            list.append(x)

print(list)