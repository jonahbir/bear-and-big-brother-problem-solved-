class bear:
    # a= weight of limack 
    # b= weight of bob
    def __init__(self,a:int,b:int,years=0):
        # initialize the attributes 
        self.a=a
        self.b=b
        self.years=years
        # validate the attributes 
        assert self.a>=1 and self.a<=self.b ,f"the weight of limack {self.a} must be greater than 1 and less than bob's weight "
        assert self.a<=10 and self.b<=10,f"weight cannot be greater than 10"

    def how_many_years(self):
        while self.a<=self.b:
            self.a*=3
            self.b*=2
            self.years+=1
        return self.years 
a,b=tuple(map(int,input().split()))
count_no_of_years=bear(a,b)
print(count_no_of_years.how_many_years())


