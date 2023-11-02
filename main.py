import random
def choice1():
    user=input("enter scissor,paper,rock:")
    comp=["scissor","paper","rock"]
    computer=random.choice(comp)
    print(f'your choice {user} and computer {computer}')
    def main():
        if user == computer:
            return "it tie"
        elif user=="rock":
            if computer=="scissor":
                print("you win!")
            else:
                print("you lose")
        elif user=="scissor":
            if computer=="paper":
                 print("you win!")
            else:
                print("you lose")
        elif user=="paper":
            if computer=="rock":
                print("you win!")
            else:
                print("you lose")
    main()
choice1()

