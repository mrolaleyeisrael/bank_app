def account_number_validation(regQuest):
    if regQuest:        
        try:
            int(regQuest)
            if len(str(regQuest)) == 10:                
                return True
        except ValueError:
            return False

        except TypeError:
            return False
    return False