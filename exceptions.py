class customexception(Exception):
    pass

class valuetoosmallexception(customexception):
    pass

class valuetoobigexception(customexception):
    pass

cnumber = 20

while True:
    try:
        input_number = int(input("Enter a number: "))
        if input_number < cnumber:
            raise valuetoosmallexception
        elif input_number > cnumber:
            raise valuetoobigexception
        break    
    except valuetoosmallexception as _:
        print("value is too small") 
    except valuetoobigexception as _:
        print("value is too big")
    except Exception as _:
        pass                   
        
