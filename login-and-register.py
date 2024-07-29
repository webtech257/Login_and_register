mail = ["AAABBCCC123@gmail.com","DDDEEEFFF567@gmail.com"]
pas = ["Abcd@123","Efgh@567"]

alpha=0
num =0
sym =0
valid =True
one = False
two = False

while True:
    
    print("-"*50)
    print("Welcome to this page : ")
    print("-"*50)
    print("1. Register \t 2. Login ")
    option = int(input("Enter your option = "))
    print("-"*50)
    if option == 1:
        NewMail = input("Enter your email = ")
        NewPass = input("Enter your password = ")
        host = NewMail[NewMail.find("@"):NewMail.find(".")]
        #print(host)
        domain =NewMail[NewMail.find("."):]
        #print(domain)
        username = NewMail[:NewMail.find("@")]
        #print(username)
        if(domain == ".com"):
            one = True
            if(host == "@gmail"):
                two = True
            
        if username.islower():
            for x in username:
                if x.isalpha()==True:
                    alpha += 1
                    #print(alpha)
                elif x.isdigit()==True:
                    num += 1
                    #print(num)
                elif x.isspace== True:
                    valid = False
                    #print(valid)
                elif x.isalnum()== False:
                    sym += 1
                    #print(sym)
        else:
            print("User name should  in a small letter")
            

        if(alpha>2 and num >0 and sym >0 and valid == True):            
            if(one == True and two == True):
                #print(alpha,num,sym,valid)
                print("valid username")
                
            else:
                print("User name should contain \nMin 3 letters\nmin 1 symbol\nMin 1 number")
                alpha =0
                num=0
                sym=0
                valid=True
        else:
            print("Invalid user name retry to register ......")
        
    
        alpha = 0
        num =0
        sym =0
        upper =0
        valid =True

        for x in NewPass:
          if x.isalpha()==True:
            alpha += 1
            #print(alpha)
            if x.isupper():
                upper += 1
                #print(upper)
          elif x.isdigit()==True:
            num += 1
            #print(num)
          elif x.isspace== True:
            valid = False
            #print(valid)
          elif x.isalnum()== False:
            sym += 1
            #print(sym)
        
        if(len(NewPass) >= 8 and alpha > 0 and num > 0 and sym > 0 and upper > 0 and valid == True):
            print("Password is valid")
            mail.append(NewMail)
            pas.append(NewPass)
            print("Successfully registered your email and password")
        else:
            print("Invalid password. Password must be at least 8 characters long and include upper and lower case letters, digits, and symbols")
        print(mail) 
        print(pas)
    
    
    
    elif(option == 2):
        print("To login Enter your mail id and password")
        RMail = input("Enter your email = ")
        RPass = input("Enter your password = ")
        logged = False
        for x in mail:
            if RMail == x :
                #print(RMail,x)
                logged = True
        for y in pas:
            if RPass == y :
                #print(RPass,y)
                logged = True

        if logged == True:
            print("Successfully logged in ......")
            break
        else:
            print("Retry")
    
    


