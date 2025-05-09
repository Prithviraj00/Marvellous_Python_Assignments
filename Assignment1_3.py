def Add(number1,number2) :
    ans=0
    ans= number1 + number2
    return ans

def main ():
    
    print("Enter your 1st number :")
    value1 = int(input())
    
    print ("Enter you 2nd number :")
    value2 = int(input())
    
    result = Add(value1,value2)
    print("Addition is :",result)
    
   
if __name__ == "__main__" :
     main()