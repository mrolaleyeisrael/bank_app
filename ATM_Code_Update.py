from datetime import datetime as dt
from random import randrange
import validation
import database
from getpass import getpass


print('\nWelcome to BTech Bank...')


def intake():

    """ This function accepts the custome account number and 
        password then validates them against 
        those in the database after which it returns both 
        the account number and the welcome message
    """

    while True:
        regQuest = input('Please Enter your account Number :\n')
        is_acc_number_valid = validation.account_number_validation(regQuest)

        if is_acc_number_valid:
            
            userPassword = getpass('Please Enter your secret password :\n')
            user_auth = database.authentication(regQuest,userPassword)
            
            
            WelcomeMessage = 'Welcome back '
            if user_auth:
                return regQuest,WelcomeMessage
        else:
            print('This user does not exist, please check and try again')
            intake()

    return False


def login():
    
    """ This is the login functionality that checks whether a user wants to 
    perform some transactions or will like to register if he or she is new 
    """

    print('''\nDo you have an account with us?, If Yes, press 1, If No press 2''')
    prompt = int(input('Select Option:\n'))

    if prompt ==1:

        print("*"*50)

        p = intake()   

        # p is now an object that store the tuple of 
        # regQuest and Welcome Message from the intake function
        print(p[1])

        # x stores the current time the user was logged in
        x=str(dt.now()) 

        print('You Logged in to your account at: {}'.format(x.split('.')[0]))
        print('''\nWhat Operation do you want to perform \n\t
            Press 1 for cash withdrawal\n\t
            Press 2 for  deposit\n\t
            Press 3 to contact Customer Support Center\n\t
            Press 4 to Logout of your account.''')

        Option_Chosen = int(input("\nEnter You Preferred Option : \n"))

        if Option_Chosen == 1:
            print("*"*50)
            cashWithdrawal()

        elif Option_Chosen == 2:
            print("*"*50)
            cashDeposit()

        elif Option_Chosen == 3:
            print("*"*50)
            customerSupport()

        elif Option_Chosen == 4:
            print("*"*50)
            logout()
        
        else:
            print('Invalid Input, Please try again.')
            login()

    elif prompt == 2:
        print("*"*50)
        print('Will you like to register?')
        userOption = int(input('If yes press 1, if No press 2 to exist\n'))

        if userOption ==1:
            register()

        elif userOption ==2:
            print("*"*50)
            print('Thank you for your interest...')
            exit()

        else:
            exit()


def register():
    
    print('Welcome to the registration room')

    firstName = input('Enter your first name:\n').capitalize()
    lasttName = input('Enter your last name:\n').capitalize()
    email = input('Enter your email address:\n')
    password = input('Enter your password:\n')
    openingBalance = float(input('Enter your Opening Balance:\n'))
    gender = input('What is your gender:\n').strip().title()
    fullName = firstName.strip() +' '+lasttName.strip()

    try:
        acc = accGeneration()

        # create account from the validate module
        is_acc_created = database.create(acc,str(openingBalance), fullName, password, email)
        
    except:
        print('Account generation failed, please try again later...')
        register()

    if gender == 'Male' or gender[0]=='M':
        print("*"*50)
        accMessage = 'Dear Mr. '+fullName+' your account number is ' + acc

    elif gender == 'Female' or gender[0]=='F':
        print("*"*50)
        accMessage = 'Dear Mrs./Ms. '+fullName+' your account number is ' + acc

    else:
        print("*"*70)
        accMessage = "Dear customer, kindly enter a 'Male' or 'Female' as your gender input"
        register()

    print(accMessage)
    login()


def logout():
    goodbyeMessage = 'Thank you for banking with us... '
    print(goodbyeMessage)
    print("*"*50)
    login()


def cashDeposit(): 

    amtDeposit =  int(input("Enter Amount to deposit :\n"))
    print("Your Current Balance is {}".format(amtDeposit))


def cashWithdrawal():
    
    amtToWithdraw =  int(input("Enter Amount to deposit :\n"))
    print("Your Current Balance is {}".format(amtToWithdraw))


def customerSupport():

    print('''To speak with our customer service :\n\t
        Choose 1 to be transferred to a customer service agent\n
        Choose 2 to sent a mail compalaint\n''')

    custServOption = int(input('Enter your preferred option\n'))

    if custServOption == 1:

        print('Please wait while we transfer your call to our customer service agent...')

    elif custServOption == 2:

        try:

            emptyList = []
            email = input('Please Enter your e-mail address: \n')

            for eachChar in email:
                emptyList.append(eachChar)

            if '@' not in emptyList or '.' not in emptyList:

                print("Invalid Email")

            else:
                print('You will receive an email in ',email)

        except:
            print('Invalid Input')

    else:
        print('You have entered the wrong option')


def accGeneration():
    # Generate random account number for every user
    # Account number must be 10 digits

    accNumber = randrange(1000000000,9999999999)
    return str(accNumber)



login()