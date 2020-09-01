#FUZZY_SET_CREATION

#Age and genre interestingness measure does not reflect the actual case for human perceptions
#because most human perceptions are fuzzy in nature,therefore age is fuzzified into three fuzzy sets19 
'''young, middle-aged and old'''


#Defining methods to get fuzzy values of given age in three sets i.e. young, middle, and old.

class Age:
    def __int__(self):
        pass
    
    #Get value for young fuzzy set for given age.
    def young(self, age):
        if age < 20.0:
            return 1.0
        elif 20.0 <= age < 35.0:
            return float((35-age)/15.0)
        else:
            return 0.0
    
    #Get value for middle fuzzy set for given age.
    def middle(self, age):  
        if age <= 20 or age > 60:
            return 0.0
        elif 20 < age <= 35:
            return float(age-20)/15
        elif 35 < age <= 45:
            return 1.0
        elif 45 < age <= 60:
            return (60-age)/15.0
        
    #get value for old fuzzy set for given age. 
    def old(self, age):
        
        if age <= 45:
            return 0.0
        elif 45 < age <= 60:
            return (age-45.0)/15
        else:
            return 1.0
        
    #Get fuzzy set values of given age.
    def get_fuzzy_set(self, age):
        return [self.young(age),
                self.middle(age),
                self.old(age)]



#similarly,Genre interestingness measure GIM can be represented naturally by linguistic variables using six fuzzy sets namely 
'''very bad (VB), bad (B), average (AV), good (G), very good (VG), and excellent (E) '''



#Generating fuzzt set for otained GIM- Genre Interestingness Measure

class GIM:

    def __init__(self):
        pass
    
    #Method to get fuzzy set value for very_bad, bad, average, good.
    def gim_a(self, gim, i):
        if gim <= i - 2 or gim > i:
            return 0.0
        elif i - 2 < gim <= i - 1:
            return gim - i + 2.0
        elif i - 1 < gim <= i:
            return float(i - gim)

    def very_bad(self, gim):
        if gim <= 1.0:
            return 1.0
        else:
            return 0.0

    def bad(self, gim):
        return self.gim_a(gim, 2.0)

    def average(self, gim):
        return self.gim_a(gim, 3.0)

    def good(self, gim):
        return self.gim_a(gim, 4.0)

    def very_good(self, gim):
        return self.gim_a(gim, 5.0)

    def excellent(self, gim):
        if gim <=4.0:
            return 0.0
        else:
            return (gim-4.0)
        
    #generates a fuzzy set of gim(list of values) for a given gim value.
    def get_fuzzy_set(self, gim_value):
        return [self.very_bad(gim_value),
                self.bad(gim_value),
                self.average(gim_value),
                self.good(gim_value),
                self.very_good(gim_value),
                self.excellent(gim_value)]

