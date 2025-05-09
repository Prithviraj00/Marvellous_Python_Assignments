def Number(no1):
   if no1 %5 ==0 :
       print ("True")
   else :
       print("False")


def main ():
    print("Enter your number :")
    Number1 = int(input())
    
    Number(Number1)
    
if __name__ == "__main__" :
     main()