# 

def chknum(value):
    
    if value %2 == 0 :
     print ("Number is Even")
    else :
        print ("Number is odd")
    

def main():
    
    print ("Enter your number :")
    number = int (input())
    chknum(number)

if __name__ =="__main__" :
    main()