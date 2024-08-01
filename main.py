print("Welcome to the Love Calculator!\n")
name1 = input("What is your name? \n")
name2 = input("What is your name? \n")


combined_string = name1 + name2 
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e 

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e 

love_score = str(true) + str(love)
final = int(love_score)

if final <= 10 or final >= 90:
    print(f"Your score is {final}, you go together like coke and mentos.")
elif final >= 40 and final <= 50:
    print(f"Your score is {final}, you are alright together.")
else:
    print(f"Your score is {final}.") 