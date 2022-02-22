#1)Write a python program to find the longest word.
# my_file=open("homework_file.txt","r")
# print(my_file.read())
#1)
# with open("homework_file.txt","r") as my_file:
# 	x = my_file.read().split()
# 	my_list = sorted([(word, len(word)) for word in x], key=lambda i: i[1], reverse=True)
# print("The longest word in my file is",my_list[0][0])
# my_file.close()

# with open("homework_file.txt","r") as my_file:
# 	words= my_file.read().split()
# 	print("The longest word in my file is",max(words,key=len))

#2)Write a Python program to count the frequency of words in a file.
# with open("homework_file.txt","r") as my_file:
# 	words=my_file.read()
# 	my_dict={}
# 	for i in words.split():
# 		key=my_dict.keys()
# 		if i in my_dict:
# 			my_dict[i]+=1
# 		else:
# 			my_dict[i]=1
# 	print(my_dict)

#3)Write a Python program to read a random line from a file.

# import random
# with open ("homework_file.txt","r") as my_file:
# 	x=my_file.read().splitlines()
# 	y=random.choice(x)
# 	print(y)

#using function

# import random
# def my_function(name):
# 	with open(name,"r") as my_file:
# 		x=my_file.read().splitlines()
# 		return random.choice(x)
# print(my_function("homework_file.txt"))

#4)You have two list convert it in dictionary and add
# in (mydict.txt) and show result:
# for example: input :
# first = [‘Ani’, ‘Jessy’, ‘Ben’]
# second = [1,2,3]
# my_dict = {1 : “Ani” , 2: “Jessy”, 3: “Ben”}

# first_list=["Ani", "Jessy", "Ben"]
# second_list=[1,2,3]
# my_dict={}
# for i in second_list:
# 	for j in first_list:
# 		my_dict[i]=j
# 		first_list.remove(j) 
# 		break
# print(my_dict)
# with open ("my_dict.txt","a") as my_file:
# 	my_file.write(str(my_dict))


# first_list=["Ani", "Jessy", "Ben"]
# second_list=[1,2,3]
# my_dict={}
# for i in first_list:
# 	for j in second_list:
# 		my_dict[i]=j
# 		second_list.remove(j) 
# 		break
# print(my_dict)
# with open ("my_dict.txt","a") as my_file:
# 	my_file.write(str(my_dict))

#5)Write a program that takes in a string as input,
# counts and outputs the number of vowels.
# And add result in json file.
# for example:
# input: test
# output: 1

# my_string=input("Enter a string ")
# count_vowels=0
# my_string.lower()
# for i in my_string:
#     if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
#            count_vowels=count_vowels+1
# print(count_vowels)
# with open ("mynew_file.txt","w") as my_file:
# 	my_file.write(my_string)
# 	my_file.write("-")
# 	my_file.write(str(count_vowels))
# 	my_file=open("mynew_file.txt","r")
# print(my_file.readlines())

#using "a"
# my_string=input("Enter a string ")
# count_vowels=0
# my_string.lower()
# for i in my_string:
#     if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
#            count_vowels=count_vowels+1
# print(count_vowels)
# with open ("homework_file.txt","a") as my_file:
# 	my_file.write(my_string)
# 	my_file.write("-")
# 	my_file.write(str(count_vowels))