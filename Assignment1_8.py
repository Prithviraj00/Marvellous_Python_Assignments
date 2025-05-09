def Number(no1) :
        for i in range(no1) :
            print("*")

def main ():
    print("Enter your number :")
    value1 = int(input())
    
    Number(value1)
    
if __name__ == "__main__" :
     main()