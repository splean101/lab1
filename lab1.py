import math
import locale

# task 1
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))
d = float(input("Введіть d: "))
f = float(input("Введіть f: "))
result = math.fabs(a - b*c*d**3+(c**5-a**2)/a + f**3*(a-213))
print("result=", result)
print(locale.format_string("%.2f", result))

# task 2
# An arbitrary list containing strings and numbers is given
# Display all odd elements in one line
list1 = ["dfg", 12, 38, "jkl", 67]

for item in list1:
    if not ("str" in str(type(item))):
        if item % 2 != 0:
            print(item)

# task 3
# An arbitrary list containing only numbers is given
# Print the result of multiplying all numbers less than 10
list2 = [13.5, 12, 38, 3, -6, 67, 1]
result = 1
for item in list2:
    if item < 10:
        result *= item
print('result =', result)

# task 4
# An arbitrary list containing only numbers is given
# Output the number in the middle of the array
list3 = [13.5, 12, 38, 3, -6, 67, 1]
length = len(list3)
if length % 2 == 1:
    middle_index = length // 2
    middle_number = list3[middle_index]
else:
    middle_index = length // 2
    middle_number = list3[middle_index]
print('middle number is ', middle_number)
