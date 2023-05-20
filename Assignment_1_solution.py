'''
Q1. Create one variable containing following type of data:
(i) string
(ii) list
(iii) float
(iv) tuple
'''
# Ans - 1
string_var = "My name is Akshat Agrawal. I'm an aspiring Data Scientist."
list_variable = ['Akshat', 1, 5.6, True]
float_variable = 99.9
tuple_variable = (1,2,3,4,5)
for i in list_variable:
    print(i)

print("String Variable is :", string_var, "Type is :", type(string_var))
print("List is :", list_variable, "Type is :", type(list_variable))
print("Float is :", float_variable, "Type is :", type(float_variable))
print("Tuple is :", tuple_variable, "Type is :", type(tuple_variable))

'''
Q2. Given are some following variables containing data:
(i) var1 = ''
(ii) var2 = '[ DS , ML , Python]'
(iii) var3 = [ 'DS' , 'ML' , 'Python' ]
(iv) var4 = 1.
What will be the data type of the above given variable.
'''
# Ans - 2
var1 = ''
var2 = '[ DS , ML , Python]'
var3 = [ 'DS' , 'ML' , 'Python' ]
var4 = 1.
# Ans- 2
print(var1, " type is", type(var1))
print(var2, " type is", type(var2))
print(var3, " type is", type(var3))
print(var4, " type is", type(var4))

'''
Q3. Explain the use of the following operators using an example:
(i) /
(ii) %
(iii) //
(iv) **
'''
# Ans - 3
'''
"/" is used to calculate division i.e quotient in a division.
"%" is used to calculate remainder of the division i.e. modulus
"//" is used to calculate floor division
"**" is used to calculate exponential value
'''

a=10
b=3
print(a/b)
print(a%b)
print(a//b)
print(a**b)

# Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the element and its data type.
# Ans - 4
li = ['Akshat', 1, 5.6, True,[1,2,3], (2,3), {6,4,2}, ]
for i in li:
    print(i)

# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many times it can be divisible.
# Ans - 5
x=10
temp = x
y=2
c=0
while(x%y == 0):
    x = x//y
    c = c+1
print(temp," is ", c ," times divisible by ",y)

# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is divisible by 3 or not.
# Ans - 6

for i in range(1,26):
    if (i%3==0):
        print(i, "is divisible by 3")
    else:
        print(i, "is not divisible by 3")

# Q7. What do you understand about mutable and immutable data types? Give examples for both showing this property.
# Ans - 7
set_1 = {1,2,3}
print(set_1)
# set_1.append(4) # will show an error as set is immutable data type
set_1 = {3,4,6}
print(set_1) # we can update set