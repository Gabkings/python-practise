class Fraction:
    def __init__(self,upper,lower):
        self.num = upper
        self.den = lower
    def gcd(m,n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n

    def __add__(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

        

    def show(self):
        print(self.num, '/' , self.den)
a = Fraction(2,3)
b = Fraction(3,4)
c = a + b
print(c.show())