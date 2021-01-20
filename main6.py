#ValueError
class BaseValidationError(ValueError):
     pass

class NameTooLongError(BaseValidationError):
     pass

class NameTooShortError(BaseValidationError):
     pass

def validate(name):
    if len(name) < 5:
        raise ValueError
 
    try:
        validate(name)
    except BaseValidationError:
        print(f'You entered wrong name, try again')

    
    

