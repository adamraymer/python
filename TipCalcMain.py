import tipCalc

def getBillAmount():
    return float(input('What is the bill amount?: '))
    
def getRating():
    value = float(input('What do you rate the service? (1 to 5 with 5 as the best) '))
    while value < 0 or value > 5:
          value = float(input('What do you rate the service? (1 to 5 with 5 as the best) '))

    return value   




#testing to see if this is okay
tip1 = tipCalc.TipCalc1()
key = input('What is the service? ')

tip1.calculate(tip1.percentVals(key),getRating(),getBillAmount())
