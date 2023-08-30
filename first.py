# <------------------------------------------------------ List operation ------------------------------------------------------------>

my_list = ["Mijanur",21,'Rahman',True,21.5]
my_list2 = ["Mijanur",21,'Rahman',True,21.5]

                #Add
my_list.append("Sinha")     #for add data in last position
my_list.insert(1,2003)      #add data in spacifc index
my_list.extend(my_list2)     #for add two list

                #Delete

my_list.pop()      #for last number data delete
my_list.pop(1)      #for number 1 index data delete
my_list.remove(21)    # for spacific data delete
my_list.clear()       # for all list clear

my_list.sort() #for sorting data
my_list.reverse()
my_list.min()
my_list.max()


# <---------------------------------------------------------- set for three operation --------------------------------------------------->

my_set = {"Mijaur rahman sinha", 450321}

#op 1 Union
#op 2 intersection



# <----------------------------------------------------- Truple ------------------------------------------------------------->
#truple not support indexing, only readable data, very first and non changeable data
my_tuple = ("Mijanur rahman sinha", "B+", "Male")


# <-------------------------------------------- dictonary ----------------------------------------------------------------->

my_dic = {

    'key':"Value",
    "Name":"Mijanur",
    "Age":"21"
}



# <---------------------------------------------------------- if else ------------------------------------------------------------------->
#Calculator program using ef,elif,else

num1 = float(input("Enter your first number : "))
op = input("Choice operator fron(+,-,/,*,%)")
num2 = float(input("Enter your second number : "))


if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
elif op == "%":
    print(num1%num2)




#leap year

year = int(input("Enter a year: "))

if year%4 == 0:
    print("This year is leap year.")
else:
    print("not leap year.")




#even and odd

n = int(input())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")


#user input copmare

# Define a dictionary with predefined variable values
variable_values = {
    "name": "Mijanur",
    "age": 21,
    "location": "Dhaka"
}

# Get user inputs
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_location = input("Enter your location: ")

# Compare user inputs with predefined variable values
if user_name == variable_values["name"] and user_age == variable_values["age"] and user_location == variable_values["location"]:
    print("All inputs match!")
else:
    print("Inputs do not match.")




# <---------------------------------------------------------------------- While loop ----------------------------------------------------------->

# ----------------------------------- namata -------------------------------------
x = int(input("Enter your value: "))
a = 1
while a<=10:
    print("5","x",a,"=",a*x)
    a = a+1
    
    
x = int(input("Enter your value: "))
for i in range(1,11):
    print("5","*",i,"=",i*x)

#------------------------------ n-n porjonto odd number print -------------------------------

a = int(input("Start Number here : "))
n = int(input("End Number here : "))

while a<=n:
    if a%2 == 0:
        print(a)
        a += 2
    else:
        print(a)
        a += 1 


# ------------------------------- n-n porjonto even number print --------------------------

a = int(input("Start Number here : "))
n = int(input("End Number here : "))

while a<=n:
    if a%2 == 1:
        print(a)
        a += 2
    else:
        print(a)
        a += 1 


#----------------------- user input check even or odd number ---------------------------

a = int(input("Enter a number: "))

while a:
    if a%2 == 0:
        print(a," is a Odd number")
        break
    else:
        print(a,"is a Even number")
        break




















