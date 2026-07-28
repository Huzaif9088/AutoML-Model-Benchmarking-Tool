print("Hello..Welcome to our MarshResto\n")

name = input("May I know your name..?")

if name == "Ben" or name == "Dell":
    evil_status = input("Are you evil..?")
    good_deeds = int(input("How many good deeds you did today..?\n"))
    if evil_status == "No" and good_deeds < 4:
        print("Oh, You are one of those good\n\n",name)
        print("Great",name,"You did nice today\n\n")
        print("Welcome",name,"..!!")
        
    else:
        print("You're not welcome here you evil",name,"..!!","Get out...!!!!")
        exit()
        
        
        
else:
    print("Hey",name,"thanks for the coming in our resto...!!\n\n\n")

print(" Today we have this special menu Just coffee, Black Coffee, Tea, Juice")


order = input("What would you like to have.?")

price = None


if order == "Just coffee":
    price = 5
elif order == "Black Coffee":
    price = 8
elif order == "Tea":
    price = 10
elif order == "Juice":
     price = 15
else:
    print("Sorry we dont serve this")
    exit()

count = input("How much quantity you want..?")

print("Sure, your total amount is",price * int(count))
print("Your order will come in a moment")




