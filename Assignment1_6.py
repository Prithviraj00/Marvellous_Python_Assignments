def Number(no1):
    if no1 == 0:
        print("Zero")
    elif (no1>0) :
        print("Postive Number")
    else:
        print("Negative Number") 


def main ():
    print("Enter your number :")
    Number1 = int(input())
    
    Number(Number1)
    
if __name__ == "__main__" :
     main()