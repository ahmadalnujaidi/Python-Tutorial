

#first_name = "ahmad"
#last_name = "nujaidi"
#full_name = first_name + " " + last_name
#print(full_name)

##age = 21
##age += 1
##print("your age is "+str(age))
#print(type(age))

##human = False

# MULTIPLE ASSIGNMENT

#a = b = c = d = 30
#f, e, g = "ahmad", 21, False

#print(a)
#print(b)
#print(c)
#print(f)
#print(e)
#print(g)

#name = input("what is your name?: ")

#print("hello "+name)

#age = int(input("how old are you?: "))

#print("wow you are " + str(age) + " years old!")
#height = float(input("how tall are you?: "))
#print("and you're " + str(height) + " cm tall!?")


            #LEARNING MATH
# import math

#pi = 3.14
#x,y,z = 1, 2, 3
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))
#print(min(x,y,z))
#print(max(x,y,z))


            #STRING SLICING         [start: stop: step]  STOPING INDEX IS EXCLUSIVE NOT INCLUSIVE
#name = "Ahmad Alnujaidi"
#first_name= name[0:5]
#print(first_name)

#last_name = name[6:]
#print(last_name)

#funky_name=name[0: :2]
#print(funky_name)

#reversed_name=name[::-1]
#print(reversed_name)


# SLICING
#website="http://google.com"
#slice = slice(7,-4)
#print(website[slice])
#website1="http://wikipedia.com"
#print(website1[slice])


# IF STATEMENTS

#age = int(input("what is your age?: "))
#if age == 100:
   # print("you are a century old")
#elif age >= 18:
    #print("you are an adult")
#elif age == 100:
    #print("you are a century old")  FIRST BLOCK GETS EXECUTED
#elif age <= 0:
    #print("you arent born yet")
#else:
    #print("you are a child")



# LOGICAL OPERATORS

#temp = int(input("temp outside: "))
#if temp >= 0 and temp <= 30:
   # print("temp is good today")
   # print("go outside!")
#elif temp < 0 or temp > 30:
    #print("temp is bad today")
    #print("stay inside")

#if its true it becomes false, vice versa
#if not(temp >= 0 and temp <= 30):
    #print("temp is good today")
    #print("go outside!")
#elif not(temp < 0 or temp > 30):
    #print("temp is bad today")
    #print("stay inside")


# WHILE LOOPS
#while 1==1:
   # print("help im stuck in a loop!")

#name = ""

#while len(name) == 0:
    #name = input("Enter you name: ")

#print("hello "+ name)


# FOR LOOPS

        # FOR LOOP (LIMITED AMT OF TIMES)
        # WHILE LOOP (UNLIMITED AMT OF TIMES)
#for i in range(10):
#    print(i)

#for i in range(50, 100+1, 2):
    #print(i)

#for i in "ahmad alnujaidi":
    #print(i)

            #COUNTDOWN PROGRAM

#import time
#for seconds in range(10, 0, -1):
    #print(seconds)
    #time.sleep(1)
#time.sleep(10)
#print("happy new year")



#             NESTED LOOPS

#rows = int(input("how many rows?: "))
#columns = int(input("how many columns?: "))
#symbol = input("enter a symbol: ")

#for i in range(rows):
#    for j in range(columns):
#        print(symbol, end="") #the end="" will just end the print statement with an empty space "" instead of new line
#    print() #keep empty to start new row



#           BREAK CONTINUE PASS   LOOP CONTROL STATEMENTS
#break = terminate loop entirely
#continue =     skips to next iteration of the loop
#pass = does nothing, acts as a placeholder

#break example for empty name
#while True:
#    name = input("enter name: ")
#    if name != "":
#        break

#phone_number = "123-456-7890"

#for i in phone_number:
    #if i == "-":
        #continue
    #print(i, end="")

#for i in range(1,21):
    #if i == 13:
        #pass
    #else:
        #print(i, end=" ")



#           LISTS

#food = ["pizza", "burger", "hotdog", "pasta"]
#print(food)
#food[0] = "sushi"
#print(food[0])
#for i in food:
    #print(i)

#food.append("ice cream")
#for i in food:
    #print(i)
#food.remove("hotdog")
#for i in food:
    #print(i)
#food.pop()
#for i in food:
    #print(i)
#food.insert(0,"cake")
#for i in food:
    #print(i)
#food.sort()
#for i in food:
    #print(i)
#food.clear()
#for i in food:
    #print(i)






#           2D LISTS : A LIST OF LISTS

#drinks = ["coffee", "sprite", "coke"]
#dinner = ["pizza", "burger", "pasta"]
#dessert = ["cake", "icecream"]
#food = [drinks, dinner, dessert]
#print(food[0][1])


#           TUPLES: collection which is ordered and unchangeable
#                   used to group together related data

#student = ("ahmad", 21, "Male")
#for x in student:
    #print(x)

#if "ahmad" in student:
    #print("ahmad is here")


#           SETS: collection, which is unordered, unindexed, no duplicated values

#utensils = {"fork", "spoon", "knife"}
#dishes = {"bowl", "plate", "cup", "knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)
#dishes.update(utensils)
#dinner_table = utensils.union(dishes)

#print(utensils.difference(dishes))
#print(utensils.intersection(dishes))

#for x in dinner_table:
    #print(x) # it prints in random order each time



#           DICTIONARIES: a changeable, unordered collection of unique key:value pairs
#                           fast because they use hashing, allow us to access a value quickly

#capitals = {'USA':'Washington DC',
#            'India':'new delhi',
#            'China':'bejing',
#            'Russia':'moscow'}

#capitals.update({'Germany':'Berlin'})
#capitals.update({'USA':'Las vegas'})
#capitals.pop('China')
#capitals.clear()

#print(capitals['China'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
#for key, value in capitals.items():
    #print(key,value)






#           INDEX OPERATOR [] = gives access to a sequence's element (str, list, tuples)

#name = "ahmad alnujaidi!"
#if (name[0].islower()):
    #name = name.upper()

#first_name = name[0:5].upper()
#print(first_name)
#last_name = name[6:].upper()
#print(last_name)
#last_char = name[-1]
#print(last_char)

#print(name)





#           FUNCTIONS! = a block of code which is executed only when its called

#def hello(name, lname, age):
#    print("hello! " + name)
#    print("have a nice day " + lname)
#    print("are you " + str(age) + " years old?")

#x = "ahmado"
#hello(x)
#hello("ahmad", "alnujaidi", 21)
#hello('a', 'b', 'c')




#           RETURN STATEMENT = Functions send Python values/objects back to the caller.
#                               these values/objects are known as the function's return value

#def multiply(x,y):
    #result = x * y
    #return result

#def multiply(x,y):
    #return x * y

#x = multiply(6,8)
#print(x)








#           KEYWORD ARGUMENTS = arguments preceded by an identifier when we pass them to a function
#                               the order of the arguments doesn't matter, unlike positional arguments
#                               python knows the names of the arguments that our function receives

#def hello(x,y,z):
    #print("hello "+x+" "+y+" "+z)

#hello(z="alnujaidi",y='ibrahim',x="ahmad")







#           NESTED FUNCTION CALLS = function calls inside other function calls
#                                   innermost function calls are resolved first
#                                   returned value is used as argument for the next outer function

#example
#num = input("enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)
#print(round(abs(float(input("enter a whole positive number: ")))))







#           VARIABLE SCOPE = the region that a variable is recognized
#                             a variable is only available from inside the region it is created
#                              a global and locally scoped variable versions of a variable can be created
#           LEGB rule, Local, Enclosing, Global, Built-in

#name = "alnujaidi" # GLOBAL SCOPE (available inside & outside functions)

#def display_name():
    #name = "ahmad"  # LOCAL SCOPE (only available inside function)
    #print(name)
#display_name()









#           ARGS = parameter that will pack all arguments into a tuple
#                   useful so that a function can accept a varying amount of arguments

#example
#def add(num1,num2):
    #sum = num1+num2
    #return sum
#print(add(1,2,3)) #3 args were given you get error

#def add(*args):
    #sum = 0
    #args = list(args)
    #args[0] = 0         # turn the tuple into a list to change a certain index
    #for i in args:
        #sum += i
    #return sum
#print(add(1,2,3,4,5,6))






#           **kwargs = parameter that will pack all arguments into a dictionary
#                      useful so that a function can accept a varying amount of keyword arguments

#example
#def hello(first,last):
    #print("hello "+first+" "+last)

#hello(first="ahmad",middle="ibrahim",last="alnujaidi") # will get error cause 1 extra argument

#def hello(**kwargs):
    #print("hello "+kwargs['first']+" "+kwargs['last'])
    #print("hello ",end="")
    #for key,value in kwargs.items():
        #print(value,end=" ")

#hello(title="Mr.",first="ahmad",middle="ibrahim",last="alnujaidi")







#           str.format() = optional method that gives users more control when displaying output

#animal = "cow"
#item = "moon"

#print("the " + animal + " jumped over the " + item) EXAMPLE without format
#print("The {} jumped over the {}".format(animal,item))
#print("The {1} jumped over the {0}".format(animal,item)) #positional argument (animal is index 0, item is index 1)
#print("The {item} jumped over the {animal}".format(animal="cat",item="moon")) #keyword argument
#text = "the {} jumped over the {}"
#print(text.format(animal,item))
                                                #padding
#name = "ahmad"
#print("hello, my name is {:10} nice to meet you".format(name))
#print("hello, my name is {:<10} nice to meet you".format(name))
#print("hello, my name is {:>10} nice to meet you".format(name))
#print("hello, my name is {:^10} nice to meet you".format(name))

                                                #number formating
#num = 3.14159
#num2 = 1000
#print("the number pi is {:.2f}".format(num))
#print("the number pi is {:,}".format(num2))
#print("the number pi is {:b}".format(num2))
#print("the number pi is {:o}".format(num2))
#print("the number pi is {:x}".format(num2))




#           RANDOM MODULE

#import random
#x = random.randint(1,6)
#y = random.random()
#myList = ['rock','paper','scissors']
#z = random.choice(myList)
#cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
#random.shuffle(cards)

#print(x)
#print(y)
#print(z)
#print(cards)



#           EXCEPTION HANDLING  = events detected  during execution that interrupt the flow of the program

# try:
#     numerator = int(input("enter a number to divide: "))
#     denomenator = int(input("enter a number to divide by: "))
#     result = numerator / denomenator
#
# except ZeroDivisionError as e:
#     print(e)
#     print("you cant divide by zero")
# except ValueError as e:
#     print(e)
#     print("enter only numbers please")
# except Exception as e:
#     print(e)
#     print("something went wrong :(")
# else:
#     print(result)
# finally:
#     print("this will always execute")





#           FILE DETECTION
import os
#
# path = "C:\\Users\\a\\Desktop\\text"
#
# if os.path.exists(path):
#     print("that location exists")
#     if os.path.isfile(path):
#         print("that is a file")
#     elif os.path.isdir(path):
#         print("that is a directory!")
# else:
#     print("that location doesnt exist")





#           READ A FILE
import os
# try:
#     with open('test.tx') as file:  #put file path. since its inside project folder just put name
#         print(file.read())
# except FileNotFoundError as e:
#     print(e)
#     print("file not found")

#print(file.closed) #it will print true since after reading the file it will automatically close



#           WRITING FILES

# text = "\nhave a nice day! see you"
# with open('test.txt', 'a') as file:
#     file.write(text)





#           COPY A FILE

# copyfile() = copies contents of file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)
#
# import shutil
#
# shutil.copyfile('test.txt','copy.txt') #src,dst





#           MOVE A FILE
# import os
# source = "folder"
# destination = "C:\\Users\\a\\Desktop\\folder"
#
# try:
#     if os.path.exists(destination):
#         print("there is already a file there ")
#     else:
#         os.replace(source,destination)
#         print(source+" was moved")
#
# except FileNotFoundError:
#     print(source+ " not found")





#                   DELETE FILES
# import os
# import shutil
# path = "folder"
# try:
#     os.remove(path)         #delete a file
#     os.rmdir(path)          #Delete empty directory
#     shutil.rmtree(path)     #removes folder and all files within "DANGEROUS"
# except FileNotFoundError:
#     print("file not found")
# except PermissionError:
#     print("you do not have permission to delete that")
# except OSError:
#     print("you cannot delete that using that function")
# else:
#     print(path+ " was deleted")



                    # MODULE = a file containing python code. may contain functions, classes, etc...
                    # used with modular programming, which is to seperate a program into parts
# import messages as msg
# from messages import hello,bye      #could also do import *
# hello()
# bye()
# # msg.hello()
# # msg.bye()
# help("modules")




                    # ROCK PAPER SCISSORS GAME
# import random
#
# while True:
#     choices = ["rock", "paper", "scissors"]
#     computer = random.choice(choices)
#     player = None
#     while player not in choices:
#         player = input("rock, paper, or scissors?: ").lower()
#
#     if player == computer:
#         print("computer: ", computer)
#         print("player: ", player)
#         print("TIE!")
#     elif player == "rock":
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("you lose")
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("you win")
#     elif player == "scissors":
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("you win")
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("you lose")
#     elif player == "paper":
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("you win")
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("you lose")
#     play_again = input("player again? (yes/no): ").lower()
#     if play_again != "yes":
#         break
# print("Bye!")





#                   QUIZ GAME

# def new_game():
#
#     guesses = []
#     correct_guesses = 0
#     question_num = 1
#
#     for key in questions:
#         print("-----------------------------")
#         print(key)
#         for i in options[question_num-1]:
#             print(i)
#         guess = input("enter (A,B,C,D): ")
#         guess = guess.upper()
#         guesses.append(guess)
#
#         correct_guesses += check_answer(questions.get(key),guess)
#         question_num += 1
#     displayer_score(correct_guesses, guesses)
#
# def check_answer(answer,guess):
#     if answer == guess:
#         print("correct!")
#         return 1
#     else:
#         print("wrong!")
#         return 0
#
# def displayer_score(correct_guesses, guesses):
#     print("-----------------------------")
#     print("RESULTS")
#     print("-----------------------------")
#
#     print("answers: ",end=" ")
#     for i in questions:
#         print(questions.get(i), end=' ')
#     print()
#     print("guesses: ", end=" ")
#     for i in guesses:
#         print(i, end=' ')
#     print()
#
#     score = int((correct_guesses/len(questions))*100)
#     print("your score is: "+str(score)+"%")
#
# def play_again():
#     response = input("do you want to play again? (yes/no): ")
#     response = response.upper()
#     if response == "YES":
#         return True
#     else:
#         return False
#
# questions = {"who created python?": "A",
#              "what year was python created?":"B",
#              "python is tributed to which comedy group":"C",
#              "is the earth round":"A",
#              "is my name ahmad?: ":"D"
# }
#
# options = [["A. guido","B. yousif","C. khaled","D ibrahim"],
#            ["A. 1999","B. 1991","C. 2002","D. 2024"],
#            ["A. lonely island", "B. smosh", "C. monty python","D. SNL"],
#            ["A. yes", "B. no"],
#            ["A. sometimes", "B. no", "C. its khaled", "D. yes"]
#            ]
# new_game()
#
# while play_again():
#     new_game()
# print("Thanks for playing! BYE")




#                   OBJECT ORIENTED PROGRAMMING
# from carclass import Car
# car_1 = Car("chevy", "corvette",2021,"blue")
# car_2 = Car("ford","mustang",2024,"red")
# # print(car_1.make)
# # print(car_1.model)
# # print(car_1.year)
# # print(car_1.color)
# # car_1.drive()
# # car_1.stop()
#
# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)
# car_2.drive()
# car_2.stop()





#                   Class Variables
# from carclass import Car
# car_1 = Car("chevy", "corvette",2021,"blue")
# car_2 = Car("ford","mustang",2024,"red")
#
# Car.wheels = 2
# print(car_1.wheels)
# print(car_2.wheels)
# print(Car.wheels)











#                   INHERITANCE
# class Animal:
#
#     alive = True
#
#     def eat(self):
#         print("this animal is eating")
#
#     def sleep(self):
#         print("this animal is sleeping")
#
# class Rabbit(Animal):
#     def run(self):
#         print("this rabbit is running")
#
# class Fish(Animal):
#     def swim(self):
#         print("this fish is swim")
#
#
# class Hawk(Animal):
#     def fly(self):
#         print("this hawk is flying")
#
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# print(hawk.alive)
# fish.eat()
# rabbit.sleep()
# rabbit.run()
# fish.swim()
# hawk.fly()








#                   MULTI LEVEL INHERITANCE = when a derived (child) class inherits from another derived (child)
                                                # class

# class Organism:
#
#     alive = True
#
# class Animal(Organism):
#
#     def eat(self):
#         print("this animal is eating")
#
# class Dog(Animal):
#
#     def bark(self):
#         print("this dog is barking")
#
# doggy = Dog()
# print(doggy.alive)
# doggy.eat()
# doggy.eat()










#                   multiple inheritance = when a child class is derived from more than one parent class

# class Prey:
#
#     fde flee(self):
#         print("this animal flees")
#
# class Predator:
#
#     def hunt(self):
#         print("this animal hunts")
#
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey,Predator):
#     pass
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()




#                   METHOD OVERRIDING

# class Animal:
#     def eat(self):
#         print("this animal is eating")
#
# class Rabbit(Animal):
#
#     def eat(self):
#         print("This rabbit is eating a carrot")
#
# rabbit = Rabbit()
# rabbit.eat()








#                   METHOD CHAINING = calling multiple methods sequentially
#                                       each call performs an action on the same object and returns self


# class Car:
#     def turn_on(self):
#         print("you start the engine")
#         return self
#     def drive(self):
#         print("You drive the car")
#         return self
#
#     def brake(self):
#         print("You step on the brake")
#         return self
#
#     def turn_off(self):
#         print("You turn off the engine")
#         return self
#
# car = Car()
# # car.turn_on()
# # car.drive()
# # car.turn_on().drive()
# # car.brake().turn_off()
# (car.turn_on()
#  .drive()
#  .brake()
#  .turn_off())







#                   Super Function = function used to give access to the methods of a parent class
#                                       returns a temporary object of a parent class when used

# class Rectangle:
#
#     def __init__(self,length, width):
#         self.length = length
#         self.width = width
#
#
# class Square(Rectangle):
#
#     def __init__(self,length, width):
#         super().__init__(length,width)
#
#     def area(self):
#         return self.length * self.width
#
# class Cube(Rectangle):
#
#     def __init__(self,length, width, height):
#         super().__init__(length,width)
#         self.height = height
#
#     def volume(self):
#         return self.length * self.width * self.height
#
# square = Square(3,3)
# cube = Cube(3,3,3)
#
# print(square.area())
# print(cube.volume())






#                   ABSTRACT CLASSES
# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
# class Car(Vehicle):
#
#     def go(self):
#         print("You drive the car")
#
#     def stop(self):
#         print("this car has stopped")
#
# class Motorcycle(Vehicle):
#
#     def go(self):
#         print("You drive the motorcycle")
#
#     def stop(self):
#         print("this motorcycle has stopped")
#
# # vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()
#
# # vehicle.go()
# car.go()
# motorcycle.go()
# car.stop()
# motorcycle.stop()







#                   OBJECTS AS ARGUMENTS

# class Car:
#
#     color = None
#
# class Motorcyle:
#
#     color = None
# def change_color(vehicle,color):
#     vehicle.color = color
#
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
#
# bike_1 = Motorcyle()
#
# change_color(car_1, "blue")
# change_color(car_2, "red")
# change_color(car_3, "green")
# change_color(bike_1,"black")
#
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(bike_1.color)







#                   DUCK TYPING = concept where the class of an object is less important than the methods/attributes
#                                   class type is not checked if minimum methods/attributes are present
#                                   "if it walks like a duck, and it quacks like a duck, then it must be a duck"

# class Duck:
#     def walk(self):
#         print("this duck is walking")
#     def talk(self):
#         print("this duck is quacking")
#
# class Chicken:
#     def walk(self):
#         print("this chicken is walking")
#     def talk(self):
#         print("this chicken is clucking")
#
# class Person():
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("you caught the critter!")
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(chicken)













#                   WALRUS OPERATOR :=

# new to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)
# print(happy := True)

# foods = list()
# while True:
#     food = input("what food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# foods = list()
# while food := input("what food do you like?: ") != "quit":
#     foods.append(food)









#                   FUNCTIONS TO VARIABLES

# def hello():
#     print("hello")

# print(hello)
# hi = hello
# print(hi)

# hi = hello
# hi()

# say = print
# say("whoa i cant believe this works :O")






#                   HIGHER ORDER FUNCTIONS = a function that either:
#                                              1. accepts a function as an argument
#                                                   OR
#                                              2. returns a function
#                                               (in python, functions are also treated as objects)


# def loud(text):
#     return text.upper()
#
# def quiet(text):
#     return text.lower()
#
# def hello(func):
#     text = func("Hello")
#     print(text)
#
# hello(quiet)



# def divisor(x):
#     def dividend(y):
#         return y / x
#     return dividend
#
# divide = divisor(2)
# print(divide(10))






#                   LAMBDA FUNCTION = function written in 1 line using lambda keyword
#                                       accepts any number of arguments, but only has one expression
#                                       (think of it as a shortcut)
#                                       (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

# def double(x):
#     return x * 2
#
# print(double(5))
#
# double = lambda x: x * 2
# multiply = lambda x,y: x * y
# add = lambda x,y,z: x+y+z
# full_name = lambda first_name, last_name: first_name+ " "+last_name
# age_check = lambda age: True if age >=18 else False
#
# print(age_check(18))
# print(full_name("ahmad","alnujaidi"))
# print(add(5,6,7))
# print(multiply(5,6))
# print(double(5))










# sort() method = used with lists
# sort() function = used with iterables

# students = ["squidward", "sandy", "patrick", "spongebob", "mr.krabs", "ahmad"] # list
# students_tuple = ("squidward", "sandy", "patrick", "spongebob", "mr.krabs", "ahmad") #tuple
#
# students.sort(reverse=True)
# sorted_students = sorted(students_tuple)
#
# for i in sorted_students:
#     print(i)
#
# students = [("squidward","F",60),          # a list of tuples
#             ("sandy","A",33),
#             ("patrick","D",36),
#             ("spongebob","B",20),
#             ("Mr.Krabs","C",78)]
#
# age = lambda ages:ages[2]
# students.sort(key=age)
# for i in students:
#     print(i)












#                   MAP         map() = applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

# store = [("shirt",20.00),
#          ("pants",25.00),
#          ("jacket",50.00),
#          ("socks",10.00)]
#
# to_euros = lambda data: (data[0], data[1]*0.82)
# to_dollars = lambda data: (data[0], data[1]/0.82)
#
# store_euros = list(map(to_euros,store))
# store_dollars = list(map(to_dollars,store_euros))
#
# for i in store_euros:
#     print(i)
#
# for i in store_dollars:
#     print(i)







# filter() = creates a collection of elements from an iterable for which a function returns true
#
# filter(function, iterable)

# friends = [("rachel",19),
#            ("monica",18),
#            ("phoebe",17),
#            ("joey",16),
#            ("chandler",21),
#            ("ross",20)]
#
# age = lambda data:data[1] >= 18
#
# drinking_buddies = list(filter(age,friends))
#
# for i in drinking_buddies:
#     print(i)







#                   reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#                               performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

# import functools
#
# # letters = ["h","e","l","l","o"]
# #
# # word = functools.reduce(lambda x, y:x+y ,letters)
# #
# # print(word)
#
# factorial = [5,4,3,2,1]
#
# result = functools.reduce(lambda x,y: x * y, factorial)
#
# print(result)








# list comprehensions = a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression (if/else) for item in iterable]

# squares = []            # create an empty list
# for i in range(1,11):   # create a for loop
#     squares.append(i*i) # define what each loop iteration should do
# print(squares)

# squares = [i*i for i in range(1,11)]
# print(squares)

# students = [100,90,80,70,60,50,40,30,0]

# passed_students = list(filter(lambda x: x >=60, students))
# passed_students = [i for i in students if i >= 60]
# passed_students = [i if i >= 60 else "failed" for i in students]
#
# print(passed_students)










#                   DICTIONARY COMPREHENSIONS = create dictionaries using an expression
#                                               can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
# ----------------------------------------------------------------------------

# cities_in_F = {'New York': 32, 'Boston': 75, "Los Angeles": 100, 'Chicago': 50}
#
# cities_in_C = {key: round((value - 32) * (5/9)) for (key,value) in cities_in_F.items()}
#
# print(cities_in_C)
#
# ----------------------------------------------------------------------------
# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)

# ----------------------------------------------------------------------------
# cities = {'New York': 32, 'Boston': 75, "Los Angeles": 100, 'Chicago': 50}
# # desc_cities = {key: ("WARM" if value >= 40 else "COLD" ) for (key,value) in cities.items()}
# # print(desc_cities)
#
# def check_temp(value):
#     if value >=70:
#         return "HOT"
#     elif 69>= value >=40:
#         return "WARM"
#     else:
#         return "COLD"
#
# desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
# print(desc_cities)








#                   zip(*iterables) = aggregate elements from two or more iterables (list,tuples, sets, etc.)
#                                       creates a zip object with paired elements stored in tuples for each element

# usernames = ["ahmad", "ibrahim", "yousif"]
# passwords = ("p@ssword", "abc123", "guest")
# login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]
#
# users = zip(usernames,passwords,login_date)
#
# for i in users:
#     print(i)

# print(type(users))
#
# for key,value in users.items():
#     print(key+" "+value)











# **************************************************
#                   if __name__ == '__main__':
# **************************************************

# module can be run as a standalone program
# module can be imported and used by other modules

# python interpreter sets "special variables", one of which is __name__
# python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run

# then python will execute the code found within __main__














#                   TIME MODULE

# import time

#print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                           epoch = when your computer thinks time began (reference point)

# print(time.time())      # return current seconds since epoch

# print(time.ctime(time.time()))

# time_object = time.localtime()
# # print(time_object)
# local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)
# print(local_time)


# time_string = "20 April, 2024"
# time_object = time.strptime(time_string, "%d %B, %Y")
#
# print(time_object)

#
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)












#                   THREADING

# thread = a flow of execution. like a separate order of instructions
#                               however each thread takes a turn running to achieve concurrency
#                               GIL = (global interpreter lock),
#                               allows only one thread to hold the control of the python interpreter at any one time
#
# cpu bounds = program/task spends most of it's time waiting for internal events (cpu intensive)
#               use multiprocessing
#
# io bound = program/task spends mos tof it's time waiting for external events (user input, web scraping)
#               use multithreading

# import threading
# import time
#
# def eat_breakfest():
#     time.sleep(3)
#     print("you ate breakfest")
#
# def drink_coffee():
#     time.sleep(4)
#     print("you drank coffee")
#
# def study():
#     time.sleep(5)
#     print("you finish studying")
#
# x = threading.Thread(target=eat_breakfest(),args=())
# x.start()
#
# y = threading.Thread(target=drink_coffee(),args=())
# y.start()
#
# z = threading.Thread(target=study(),args=())
# z.start()
#
# # eat_breakfest()
# # drink_coffee()
# # study()
#
# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())







#                   DAEMON THREAD = a thread that runs in the background, not important for program to run
#                                   your program will not wait for daemon threads to complete before exiting
#                                   non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                                   ex. background tasks, garbage collection, waiting ro input, long-running processes
#
# import threading
# import time
#
# answer = input("do you wish to exit?")
# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("logged in for: ",count," seconds")
#
#
# x = threading.Thread(target=timer(), daemon=True)
# x.start()
#
# answer = input("do you wish to exit?")











#                   MULTIPROCESSING

#***********************************************************
# python multiprocessing
#***********************************************************

# multiproceesing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)
#
#
# from multiprocessing import Process, cpu_count
# import time
#
# def counter(num):
#     count = 0
#     while count < num:
#         count += 1
#
# def main():                                     #14667.2339798  seconds
#
#     # print(cpu_count)
#
#
#     a = Process(target=counter, args=(125000000,))
#     b = Process(target=counter, args=(125000000,))
#     c = Process(target=counter, args=(125000000,))
#     d = Process(target=counter, args=(125000000,))
#     e = Process(target=counter, args=(125000000,))
#     f = Process(target=counter, args=(125000000,))
#     g = Process(target=counter, args=(125000000,))
#     h = Process(target=counter, args=(125000000,))
#
#
#     a.start()
#     b.start()
#     c.start()
#     d.start()
#     e.start()
#     f.start()
#     g.start()
#     h.start()
#
#     a.join()
#     b.join()
#     c.join()
#     d.join()
#     e.join()
#     f.join()
#     g.join()
#     h.join()
#
#     print("finished in: ",time.perf_counter()," seconds")
#
#
# if __name__ == '__main__':
#     main()
#
#
#







#                   GUI Windows

# from tkinter import *
#
# # widgets = GUI elements: buttons, textboxes, labels, images
# # windows = serves as a container to hold or contain these widgets
#
# window = Tk() # instantiate an instance of a window
# window.geometry("1280x720")
# window.title("Ahmad Alnujaidi first GUI program")
#
# icon = PhotoImage(file='hacker.png')        #changes icon bar but i got error
# window.iconphoto(True,icon)
#
# window.config(background="#279c36")
#
# window.mainloop() # place window on computer screen, listen for events









#                   LABELS

# from tkinter import *
#
# # label = an area widget that holds text and/or an image within a window
#
# window = Tk()
# window.geometry("1280x720")
#
# photo = PhotoImage(file='hacker.png')
#
# label = Label(window,
#               text="Hello World, this is Ahmad Ibrahim Alnujaidi",
#               font=('Arial',40,'bold'),
#               fg='#00FF00',
#               bg='black',
#               relief=RAISED,    # border
#               bd=10,            #border width
#               padx=20,
#               pady=50,
#               image=photo,
#               compound='top')
# label.pack()
# #label.place(x=0,y=0)    #places label top left
# # label.place(x=100,y=100)
#
#
# window.mainloop()









#                   BUTTONS
# from tkinter import *
#
# # button = you click them then do stuff
#
# count = 0
# def click():
#     global count
#     count += 1
#     print("you clicked the button")
#     print(count)
#
#
# window = Tk()
# window.geometry("1280x720")
#
# photo = PhotoImage(file='hacker.png')
#
# button = Button(window,
#                 text="CLICK ME",
#                 command=click,
#                 font=("Comic Sans",30),
#                 fg="#00FF00",
#                 bg="black",
#                 activeforeground="#00FF00",
#                 activebackground="gray",
#                 state=ACTIVE,
#                 image=photo,
#                 compound='bottom'
#                 )
# button.pack()
#
# window.mainloop()
#
#







#                   ENTRY BOX

# from tkinter import *
# # entry widget = textbox that accept a single line of user input
#
# def submit():
#     username = entry.get()
#     print("Hello "+username)
#     entry.config(state=DISABLED)
# def delete():
#     entry.delete(0,END)
#
# def backspace():
#     entry.delete(len(entry.get())-1,END)
#
# window = Tk()
# window.geometry("1280x720")
# window.title("entry lesson")
#
#
#
# entry = Entry(window,
#               font=("Arial",50),
#               fg="#00FF00",
#               bg="black",
#               show="*")
# # entry.insert(0,'Spongebob')
# entry.pack(side=LEFT)
#
# submit_button = Button(window, text="submit", command=submit)
# submit_button.pack(side=RIGHT)
#
# delete_button = Button(window, text="delete", command=delete)
# delete_button.pack(side=RIGHT)
#
# backspace_button = Button(window, text="backspace", command=backspace)
# backspace_button.pack(side=RIGHT)
#
#
# window.mainloop()









#                   CHECK BOX
#
# from tkinter import *
#
# def display():
#     if (x.get() == 1):
#         print("you agree")
#     else:
#         print("you dont agree")
#
#
#
# window = Tk()
# window.geometry("1280x720")
#
# icon = PhotoImage(file='hacker.png')
# x = IntVar()
#
# check_button = Checkbutton(window,
#                            text="i agree to this",
#                            variable=x,
#                            onvalue=1,
#                            offvalue=0,
#                            command=display,
#                            font=("Arial",20),
#                            fg="#00FF00",
#                            bg="black",
#                            activeforeground="#00FF00",
#                            activebackground="black",
#                            padx=25,
#                            pady=10,
#                            image=icon,
#                            compound='left'
#                            )
# check_button.pack()
#
#
# window.mainloop()










#                   RADIO BUTTONS
# radio button = similar to checkbox, but you can only select one from a group

# from tkinter import *
#
# food = ["pizza", "burger", "hotdog"]
#
# def order():
#     if(x.get()==0):
#         print("you ordered pizza")
#     elif(x.get()==1):
#         print("you ordered burger")
#     else:
#         print("you ordered a hotdog")
#
# window = Tk()
# window.geometry("1280x720")
#
# hacker1 = PhotoImage(file='hacker.png')
# hacker2 = PhotoImage(file='hacker.png')
# hacker3 = PhotoImage(file='hacker.png')
#
# food_images = [hacker1, hacker2, hacker3]
#
# x = IntVar()
# for index in range(len(food)):
#     radio_button = Radiobutton(window,
#                                text=food[index],    # adds text to radio  buttons
#                                variable=x,          # groups radiobuttons together if they share same variable
#                                value=index,         # this assigns each radiobutton a different value
#                                padx=25,             # adds padding on x-axis
#                                font=("Impact",50),
#                                image=food_images[index],
#                                compound='left',
#                                indicatoron=0,       # eliminate circle indicators
#                                width=750,           # sets width of radio buttons
#                                command=order,
#                                )
#     radio_button.pack(anchor=W)
#
# window.mainloop()










#                   SCALE
# from tkinter import *
#
# def submit():
#     print("The hacker expertise is: "+str(scale.get()))
#
#
# window = Tk()
#
# hacker = PhotoImage(file='hacker.png')
# hackerLabel = Label(image=hacker)
# hackerLabel.pack()
#
# scale = Scale(window,
#               from_=100,
#               to=0,
#               length=600,
#               orient=VERTICAL,          # orientation of scale vert / horz
#               font=("Consolas,",20),
#               tickinterval=10,
#               #showvalue=0               # hide current value
#               resolution=10,             # increments of scale
#               troughcolor='#69EAFF',
#               fg='#FF1C00',
#               bg='black'
#
#               )
# scale.set((scale['from']-scale['to'])/2)    # or could just put 50
# scale.pack()
#
# button = Button(window,text="submit",command=submit)
# button.pack()
#
# window.mainloop()








#                   LIST BOXES = a listing of selectable text items with in its own container

# from tkinter import *
#
# def submit():
#     #print("you have ordered: " + listbox.get(listbox.curselection()))
#     food = []
#     for index in listbox.curselection():
#         food.insert(index,listbox.get(index))
#     print("You have ordered: ")
#     for index in food:
#         print(index)
#
# def add():
#     listbox.insert(listbox.size(),entrybox.get())
#     listbox.config(height=listbox.size())
#
# def delete():
#     #listbox.delete(listbox.curselection())
#     for index in reversed(listbox.curselection()):
#         listbox.delete(index)
#     listbox.config(height=listbox.size())
#
#
#
# window = Tk()
#
# listbox = Listbox(window,
#                   bg='#f7ffde',
#                   font=("Constantia",35),
#                   width=12,
#                   selectmode=MULTIPLE
#                   )
# listbox.pack()
# listbox.insert(1,"pizza")
# listbox.insert(2,"pasta")
# listbox.insert(3,"lasagna")
# listbox.insert(4,"garlic bread")
# listbox.insert(5,"soup")
#
# listbox.config(height=listbox.size())
#
# entrybox = Entry(window)
# entrybox.pack()
#
# add_button = Button(window,
#                        text="add",
#                        command=add)
# add_button.pack()
#
# delete_button = Button(window,
#                        text="delete",
#                        command=delete)
# delete_button.pack()
#
# submit_button = Button(window,
#                        text="submit",
#                        command=submit)
# submit_button.pack()
# window.mainloop()
#







#                   MESSAGE BOXES

# from tkinter import *
# from tkinter import messagebox
#
# def click():
#     #messagebox.showinfo(title="info box TITLE", message="you are retarded")
#     #messagebox.showwarning(title="WARNING", message="YOU ARE ACTUALLY RETARDED")
#     #messagebox.showerror(title="ERROR!", message="its not you its the other retard")
#
#     # if messagebox.askokcancel(title="ask ok cancel", message="do you want to do the thing?"):
#     #     print("you did a thing")
#     # else:
#     #     print("you canceled")
#
#     # if messagebox.askretrycancel(title='ask retry cnacel', message="you want to retry?"):
#     #     print("you retried")
#     # else:
#     #     print("you canceled")
#     # if messagebox.askyesno(title='yes or no', message='do you like cake?'):
#     #     print("you like cake")
#     # else:
#     #     print("ur on a diet")
#     # answer = messagebox.askquestion(title='ask question', message='do you like pie?')
#     # if answer == 'yes':
#     #     print("i like pie too")
#     # else:
#     #     print("i prefer cake")
#     answer = messagebox.askyesnocancel(title='ask yes no cancel', message='do you like to code',icon='info')
#     if (answer == True):
#         print("you like to code")
#     elif (answer == False):
#         print("why not")
#     else:
#         print("you have dodged the question")
#
#
# window = Tk()
#
# button = Button(window, command=click, text="click me")
# button.pack()
#
# window.mainloop()









#                   COLOR CHOOSER
#
# from tkinter import *
# from tkinter import colorchooser    # sub module
#
# def click():
#     color = colorchooser.askcolor()
#     # print(color)
#     # colorHex = color[1]       # condense the code and just assign bg to color[1]
#     # print(colorHex)
#     window.config(bg=color[1])
#
# window = Tk()
# window.geometry("1280x720")
#
#
#
# button = Button(window,
#                 text='click me',
#                 command=click)
# button.pack()
#
# window.mainloop()









#                   TEXT AREA
# text widget = functions like a text area, you can enter multiple lines of text
# from tkinter import *
#
# def submit():
#     input = text.get("1.0",END)
#     print(input)
#
# window = Tk()
# window.geometry("1280x720")
#
# text = Text(window,
#             bg="light yellow",
#             font=("Ink Free",25),
#             height=8,
#             width=20,
#             padx=20,
#             pady=20,
#             fg='purple')
# text.pack()
#
# button = Button(window,text="Submit",command=submit)
# button.pack()
#
# window.mainloop()









#                   OPEN A FILE
# from tkinter import *
# from tkinter import filedialog
#
# def openFile():
#     filepath = filedialog.askopenfilename(initialdir="C:\\Users\\a\\PycharmProjects\\pythonProject1",
#                                           title='Open File OKAY?',)
#     file = open(filepath,'r')
#     print(file.read())
#     file.close()
#
# window = Tk()
#
# button = Button(text='Open',
#                 command=openFile,
#                 )
# button.pack()
#
#
# window.mainloop()













#                   Save a file
# from tkinter import *
# from tkinter import filedialog
#
# def saveFile():
#     file = filedialog.asksaveasfile(defaultextension='.txt')
#     if file is None:
#         return
#     filetext = str(text.get(1.0,END))
#     file.write(filetext)
#     file.close()
#
# window = Tk()
#
# button = Button(text='save',command=saveFile)
# button.pack()
#
# text = Text(window)
# text.pack()
#
# window.mainloop()









#                   MENU BAR
# from tkinter import *
#
# def openFile():
#     print("file has been opened")
#
# def saveFile():
#     print("file has been saved")
#
# def cut():
#     print("you cut some text")
#
# def copy():
#     print("you copied some text")
#
# def paste():
#     print("you pasted some text")
#
# window = Tk()
# window.geometry("1280x720")
#
# menubar = Menu(window)
# window.config(menu=menubar)
#
# fileMenu = Menu(menubar, tearoff=0, font=('MV Boli',8))
# menubar.add_cascade(label='File',menu=fileMenu)
# fileMenu.add_command(label='Open', command=openFile)
# fileMenu.add_command(label='Save', command=saveFile)
# fileMenu.add_separator()
# fileMenu.add_command(label='Exit', command=quit)
#
# editMenu = Menu(menubar, tearoff=0,font=('MV Boli',8))
# menubar.add_cascade(label='Edit',menu=editMenu)
# editMenu.add_command(label='Cut',command=cut)
# editMenu.add_command(label='Copy',command=copy)
# editMenu.add_command(label='Paste',command=paste)
#
# window.mainloop()










#                   # FRAMES
# frame = a rectangular container to group and hold widgets

# from tkinter import *
#
# window = Tk()
#
# frame = Frame(window, bg='pink',bd=5,relief=RAISED)
# frame.pack(side=BOTTOM)
#
# Button(frame,text='W',font=("Consolas",25),width=3).pack(side=TOP)
# Button(frame,text='A',font=("Consolas",25),width=3).pack(side=LEFT)
# Button(frame,text='S',font=("Consolas",25),width=3).pack(side=LEFT)
# Button(frame,text='D',font=("Consolas",25),width=3).pack(side=LEFT)
#
#
# window.mainloop()









#                   NEW WINDOWS

# from tkinter import *
#
# def create_window():
#     # new_window = Toplevel() # a new window 'on top' of other windows, linked to a 'bottom' window
#     new_window = Tk()         # new independent window
#     old_window.destroy()      # close out of old window
#
#
# old_window = Tk()
#
# Button(old_window,text='Create new window',command=create_window).pack()
#
# old_window.mainloop()








#                   window tabs
# from tkinter import *
# from tkinter import ttk
#
# window = Tk()
# window.geometry("1280x720")
#
# notebook = ttk.Notebook(window)     # widget that manages a collection of windows/displays
#
# tab1 = Frame(notebook)  # new frame for tab 1
# tab2 = Frame(notebook)  # new frame for tab 2
#
# notebook.add(tab1,text='Tab 1')
# notebook.add(tab2,text='Tab 2')
# notebook.pack(expand=True, fill='both') #expand = expand to fill any space not otherwise used
#                                         #fill = fill space on x and y axis
#
# Label(tab1,text='Hello this is tab#1',width=50,height=25).pack()
# Label(tab2,text='goodbye this is tab#2',width=50,height=25).pack()
#
# window.mainloop()










#                   Grid
# grid() = geometry manager that organizes widgets in a table-like structure in a parent
# from tkinter import *
# 
# window = Tk()
#
# titleLabel = Label(window,text='Enter your info',font=("Arial",25)).grid(row=0,column=0,columnspan=2)
#
# firstNameLabel = Label(window,text='first name: ',width=20,bg="red").grid(row=1,column=0)
# firstNameEntry = Entry(window).grid(row=1,column=1)
#
# LastNameLabel = Label(window,text='Last name: ',bg='green').grid(row=2,column=0)
# LastNameEntry = Entry(window).grid(row=2,column=1)
#
# emailLabel = Label(window,text='Email: ',bg="blue",width=30).grid(row=3,column=0)
# emailEntry = Entry(window).grid(row=3,column=1)
#
# submitButton = Button(window,text='submit').grid(row=4,column=0,columnspan=2)
#
# window.mainloop()










#                   PROGRESS BAR
# from tkinter import *
# from tkinter.ttk import *
# import time
#
# def start():
#     GB = 100
#     download = 0
#     speed =1
#     while (download<GB):
#         time.sleep(0.05)
#         bar['value']+=(speed/GB)*100
#         download += speed
#         percent.set(str(int((download/GB)*100))+"%")
#         text.set(str(download)+"/"+str(GB)+ " GB completed")
#         window.update_idletasks()
#
#
# window = Tk()
#
# percent = StringVar()
# text = StringVar()
#
#
# bar = Progressbar(window,orient=HORIZONTAL, length=300,)
# bar.pack(pady=10,padx=10)
#
# Label(window,textvariable=percent).pack()   #percent label
#
# Label(window,textvariable=text).pack()
#
# Button(window,text="download",command=start).pack()
#
# window.mainloop()









#                   CANVAS
# canvas = widget that is used to draw graphs, plots, images in a window
# from tkinter import *
#
# window = Tk()
#
# canvas = Canvas(window,height=500, width=500)
# # canvas.create_line(0,0,500,500, fill="blue",width=5)
# # canvas.create_line(0,500,500,0, fill="red",width=5)
# # canvas.create_rectangle(50,50,250,250,fill='#00ff00')
# # points = [250,0,500,500,0,500]
# # canvas.create_polygon(points,fill='purple',outline='blue',width=5)
# # canvas.create_arc(0,0,500,500,fill='yellow',style=PIESLICE,start=270,extent=180)
# canvas.create_arc(0,0,500,500,fill='red',extent=180,width=10)
# canvas.create_arc(0,0,500,500,fill='white',extent=180,width=10,start=180)
# canvas.create_oval(190,190,310,310,fill='white',width=10)
# canvas.pack()
#
# window.mainloop()







#                   KEYBOARD EVENTS
# from tkinter import *
#
# def doSomething(event):
#     #print("you pressed: "+event.keysym)
#     label.config(text=event.keysym)
#
# window = Tk()
#
# window.bind("<Key>",doSomething)
#
# label = Label(window,font=("Helvetica",100))
# label.pack()
#
# window.mainloop()









#                   mouse events
# from tkinter import *
#
# def doSomething(event):
#     print("mouse coords"+ str(event.x)+" "+str(event.y))
#
# window = Tk()
#
# # window.bind("<Button-1>",doSomething)   #left click
# # window.bind("<Button-2>",doSomething)   #scroll wheel click
# # window.bind("<Button-3>",doSomething)   #right click
# #window.bind("<ButtonRelease>",doSomething)
# #window.bind("<Enter>",doSomething)       #enter the window
# #window.bind("<Leave>",doSomething)       #leave the window
# window.bind("<Motion>",doSomething)     #where to mouse moved
#
# window.mainloop()











#                   drag & drop
# from tkinter import *
#
# def drag_start(event):
#     widget = event.widget
#     widget.startX = event.x
#     widget.startY = event.y
#
# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x,y=y)
#
#
# window = Tk()
# window.geometry("1280x720")
#
# label = Label(window,bg="red",width=10,height=5)
# label.place(x=0,y=0)
#
# label2 = Label(window,bg="blue",width=10,height=5)
# label2.place(x=100,y=100)
#
# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_motion)
#
# label2.bind("<Button-1>",drag_start)
# label2.bind("<B1-Motion>",drag_motion)
#
# window.mainloop()









#                   move images w/ keys
# from tkinter import *
#
# def move_up(event):
#     label.place(x=label.winfo_x(),y=label.winfo_y()-10)
#
# def move_down(event):
#     label.place(x=label.winfo_x(),y=label.winfo_y()+10)
#
# def move_left(event):
#     label.place(x=label.winfo_x()-10,y=label.winfo_y())
#
# def move_right(event):
#     label.place(x=label.winfo_x()+10,y=label.winfo_y())
#
# window = Tk()
# window.geometry("1280x720")
#
# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)
#
# window.bind("<Up>",move_up)
# window.bind("<Down>",move_down)
# window.bind("<Left>",move_left)
# window.bind("<Right>",move_right)
#
# hacker = PhotoImage(file='hacker.png')
# label = Label(window,image=hacker)
# label.place(x=0,y=0)


# window.mainloop()


# from tkinter import *
#
# def move_up(event):
#     canvas.move(hackerimage,0,-10)
# def move_down(event):
#     canvas.move(hackerimage, 0, +10)
# def move_left(event):
#     canvas.move(hackerimage, -10, 0)
# def move_right(event):
#     canvas.move(hackerimage, +10, 0)
#
#
# window = Tk()
#
# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)
#
#
# hacker = PhotoImage(file='hacker.png')
#
# canvas = Canvas(window,width=500,height=500)
# canvas.pack()
# hackerimage = canvas.create_image(0,0,image=hacker,anchor=NW)
#
# window.mainloop()







#                   ANIMATIONS
# from tkinter import *
# import time
#
# WIDTH = 700
# HEIGHT = 600
# velocityX = 3
# velocityY = 2
#
# window = Tk()
#
#
#
# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()
#
#
# hacker = PhotoImage(file='hacker.png')
# hackerbg = PhotoImage(file='hackerbgpng.png')
#
# background = canvas.create_image(0,0,image=hackerbg,anchor=NW)
# my_image = canvas.create_image(0,0,image=hacker,anchor=NW)
#
# image_width = hacker.width()
# image_height = hacker.height()
#
# while True:
#     coords = canvas.coords(my_image)
#     print(coords)
#     if (coords[0]>=(WIDTH-image_width) or coords[0]<0):
#         velocityX = -velocityX
#     if (coords[1]>=(HEIGHT-image_height) or coords[1]<0):
#         velocityY = -velocityY
#     canvas.move(my_image,velocityX,velocityY)
#
#     window.update()
#     time.sleep(0.01)
#
#
# window.mainloop()








#                       ANIMATE MULTIPLE OBJECTS
# from tkinter import *
# from Ball import *
# import time
#
# window = Tk()
#
# WIDTH = 500
# HEIGHT = 500
#
#
# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()
#
# volley_ball = Ball(canvas,0,0,100,1,1,"white")
# tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
# basket_ball = Ball(canvas,0,0,125,8,7,"orange")
#
# while True:
#     volley_ball.move()
#     tennis_ball.move()
#     basket_ball.move()
#     window.update()
#     time.sleep(0.01)
#
# window.mainloop()









#                   CLOCK PROGRAM
from tkinter import *
from time import *

# def update():
#     time_string = strftime("%I:%M:%S %p")
#     time_label.config(text=time_string)
#
#     day_string = strftime("%A")
#     day_label.config(text=day_string)
#
#     date_string = strftime("%B %d, %Y")
#     date_label.config(text=date_string)
#
#     window.after(1000,update)
#
# window = Tk()
#
# time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
# time_label.pack()
#
# day_label = Label(window,font=("Ink Free",25))
# day_label.pack()
#
# date_label = Label(window,font=("Ink Free",30))
# date_label.pack()
#
# update()
#
# window.mainloop()













#                   SEND AN EMAIL
# import smtplib
#
# sender = "ahmadalnujaidi02@gmail.com"
# receiver =  "ahmadalnujaidi02@gmail.com"
# password = "Nujaidi8592025"
# subject = "python email test"
# body = "I wrote an email! :D"
#
# #header
# message = f"""From: {sender}
# To: {receiver}
# Subject: {subject}\n
# {body}
#
# """
#
# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
# try:
#     server.login(sender,password)
#     print("Logged in...")
#     server.sendmail(sender,receiver,message)
#     print("Email has been sent")
#
# except smtplib.SMTPAuthenticationError:
#     print("unable to sign in")
#
#   NEED TO ENABLE LESS SECURE APP ACCESS







#*******************************************
# run .py file with cmd
#*******************************************
# save file as .py (python file)
# go to command prompt
# navigate to directory w/ your file: cd C:\Users\A\Deskptop
# invoke python to interpreter + script: python hello_world.py

# print("Hello World!")
#
# name = input("whats your name?: ")
#
# print("Hello, ",name)










#                   PIP
#*************************************************************************************
# Python pip
#*************************************************************************************
# pip = package manager for packages and modules from Python Package Index
#
#       included for python version 3.4+
#       open command prompt

#       help:                       pip
#       check:                      pip --version
#       update:                     pip install --upgrade pip
#       installed packages:         pip list
#       check outdated packages:    pip list --outdated
#       install a package:          pip install "package name"
#*************************************************************************************









#                   .py to exe

# (windows defender may prevent you from running)
# (make sure pip and pyinstaller are installed/updated)

# cd to directory that contains your .py file
# pyinstaller ...
#                   -F              (all in 1 file)
#                   -w              (removes terminal window)
#                   -i icon.ico     (adds custom icon to .exe)
#                   clock.py        (name of your main python file)

# .exe is located in the dist folder












#                   CALCULATOR PROGRAM

# from tkinter import *
#
#
# def button_press(num):
#     global equation_text
#
#     equation_text = equation_text + str(num)
#     equation_label.set(equation_text)
#
# def equals():
#     global equation_text
#
#     try:
#
#         total = str(eval(equation_text))
#
#         equation_label.set(total)
#
#         equation_text = total
#
#     except SyntaxError:
#         equation_label.set("Syntax Error")
#         equation_text = ""
#
#
#     except ZeroDivisionError:
#         equation_label.set("arithmetic error")
#         equation_text = ""
#
# def clear():
#
#     global equation_text
#
#     equation_label.set("")
#
#     equation_text = ""
#
# window = Tk()
# window.title("Calculator program")
# window.geometry("500x500")
#
# equation_text = ""
#
# equation_label = StringVar()
#
# label = Label(window,textvariable=equation_label, font=("consolas",20),bg="white",width=24,height=2)
# label.pack()
#
# frame = Frame(window)
# frame.pack()
#
# button1 = Button(frame, text=1, height=4, width=9, font=35,
#                  command= lambda: button_press(1))
# button1.grid(row=0,column=0)
#
# button2 = Button(frame, text=2, height=4, width=9, font=35,
#                  command= lambda: button_press(2))
# button2.grid(row=0,column=1)
#
# button3 = Button(frame, text=3, height=4, width=9, font=35,
#                  command= lambda: button_press(3))
# button3.grid(row=0,column=2)
#
# button4 = Button(frame, text=4, height=4, width=9, font=35,
#                  command= lambda: button_press(4))
# button4.grid(row=1,column=0)
#
# button5 = Button(frame, text=5, height=4, width=9, font=35,
#                  command= lambda: button_press(5))
# button5.grid(row=1,column=1)
#
# button6 = Button(frame, text=6, height=4, width=9, font=35,
#                  command= lambda: button_press(6))
# button6.grid(row=1,column=2)
#
# button7 = Button(frame, text=7, height=4, width=9, font=35,
#                  command= lambda: button_press(7))
# button7.grid(row=2,column=0)
#
# button8 = Button(frame, text=8, height=4, width=9, font=35,
#                  command= lambda: button_press(8))
# button8.grid(row=2,column=1)
#
# button9 = Button(frame, text=9, height=4, width=9, font=35,
#                  command= lambda: button_press(9))
# button9.grid(row=2,column=2)
#
# button0 = Button(frame, text=0, height=4, width=9, font=35,
#                  command= lambda: button_press(0))
# button0.grid(row=3,column=1)
#
# plus = Button(frame, text="+", height=4, width=9, font=35,
#                  command= lambda: button_press('+'))
# plus.grid(row=0,column=3)
#
# minus = Button(frame, text="-", height=4, width=9, font=35,
#                  command= lambda: button_press('-'))
# minus.grid(row=1,column=3)
#
# multiply = Button(frame, text="*", height=4, width=9, font=35,
#                  command= lambda: button_press('*'))
# multiply.grid(row=2,column=3)
#
# divide = Button(frame, text="/", height=4, width=9, font=35,
#                  command= lambda: button_press('/'))
# divide.grid(row=3,column=3)
#
# equal = Button(frame, text="=", height=4, width=9, font=35,
#                  command= equals)
# equal.grid(row=3,column=2)
#
# decimal = Button(frame, text=".", height=4, width=9, font=35,
#                  command= lambda: button_press('.'))
# decimal.grid(row=3,column=0)
#
# clear = Button(window, text="clear", height=4, width=12, font=35,
#                  command=clear)
# clear.pack()
#
# window.mainloop()











