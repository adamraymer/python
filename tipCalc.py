class TipCalc1:

   def __init__(self):
       self.key = 'Default'
       self.rating = 3
       self.billAmount = 0
       
   def percentVals(self):
       tipPerc = {'Default':.15}

       key = input('What is the service? ')
       
       return float(tipPerc.get(key) / 3)


   def getBillAmount(self):
        return float(input('What is the bill amount?: '))

   def getRating(self):
        value = float(input('What do you rate the service? (1 to 5 with 5 as the best) '))
        while value < 0 or value > 5:
            value = float(input('What do you rate the service? (1 to 5 with 5 as the best) '))

        return value   
       
   def calculate(self, percVal, rating, billAmount):
        print(float((percVal * rating) * billAmount))




       
