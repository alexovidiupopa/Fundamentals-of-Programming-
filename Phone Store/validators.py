def validateAdd(manufacturer,model,price):
    '''
    in - manufacturer, model, price -> strings
    out - False if they are not correct (length<3 for any one of them, respectively price < 100 for the price)
          True otherwise
    '''
    
    if len(manufacturer) < 3 or len(model) < 3 or price < 100:
        return False
    return True

