class TipCalc1:

   def __init__(self):
       self.key = 'Default'
       self.rating = 3
       self.billAmount = 0
       
   def percentVals(self,key):
       tipPerc = {'Default':.15}
       
       return float(tipPerc.get(key) / 3)
       
   def calculate(self, percVal, rating, billAmount):
        print('Tip should be: $',float((percVal * rating) * billAmount))




       
