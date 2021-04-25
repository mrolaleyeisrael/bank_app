import validation
import os

user_db_dir = 'data/user_data/'

def create(regQuest, openingBalance, fullName, password, email):

    if does_acc_exist(regQuest):
        return False

    user_collected_details = str(openingBalance) + ", " + fullName + ", " + password + "," + email

    if does_email_exist(email):
        print('Email already exists')
        return False 

    completion_state = False
    try:
        with open(user_db_dir+str(regQuest)+'.txt', 'x') as file:
            file.write(str(user_collected_details))
            print('Account Created Successfully')
            completion_state = True
            return completion_state

    except FileExistsError:
        print('File already exist')
        does_acc_contain_data = read(user_db_dir+str(regQuest)+'.txt')
        if not does_acc_contain_data:
            delete(regQuest)

    return completion_state


def read(regQuest):
    is_valid_acc = validation.account_number_validation(regQuest)

    try:
        if is_valid_acc:
            with open(user_db_dir+str(regQuest)+'.txt','r') as file_to_read:
                file_already_read = file_to_read.readline()
                return file_already_read
        else:
            with open(user_db_dir+regQuest,'r') as file_to_read:
                file_already_read = file_to_read.readline()
                return file_already_read
    except FileExistsError:
        print('File already exist')
        return False
    except FileNotFoundError:
        print('file was not found')
        return False
    except TypeError:
        print('Invalid account format')

    return False


def update(regQuest):
    print('Update user details')

def delete(regQuest):
    is_delete_successful = True
    print('Delete user details')
    if os.path.exists(user_db_dir+str(regQuest)+'.txt'):
        try:
            os.remove(user_db_dir+str(regQuest)+'.txt')
            print('User data has been deleted successfully')
            return is_delete_successful

        except FileNotFoundError:
            print('User not found')
            is_delete_successful = False
            return is_delete_successful
    else:
        print('No such directory')
        return False
    return is_delete_successful


def does_email_exist(email):
    all_user_available = os.listdir(user_db_dir)
    for each_user in all_user_available:
        user_list = read(each_user).split(',')
        if email in user_list:
            return True
    return False


def does_acc_exist(regQuest):
    all_user_available = os.listdir(user_db_dir) 
    for each_user in all_user_available:
        if each_user == str(regQuest)+'.txt':
            return True
    return False


def authentication(regQuest, passwordx):
    if does_acc_exist(regQuest):
        user = read(regQuest).split(',')
        if passwordx == user[2].strip():
            return user
        else:
            print('Invalid password')
            return False
    return False
        