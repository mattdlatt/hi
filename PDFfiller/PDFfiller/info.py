class Info:
    def __init__(self,name,pin,Rent1,Rent2,Rent3,Rent4,EstateTax1,EstateTax2,EstateTax3,EstateTax4,PropTax1,PropTax2,HOA1,HOA2,HOA3,HOA4,Improv1,Improv2,Improv3,Improv4,Fur1,Fur2,Fur3,Fur4,Main1,Main2,Main3,Main4,Lawn1,Lawn2,Lawn3,Lawn4,keep1,keep2,keep3,keep4,oth1,oth2,oth3,oth4,CC1,CC2,Legal1,Legal2,Account1,Account2,Elec1,Elec2,gas1,gas2,oil1,oil2,cell1,cell2,trash1,trash2,water1,water2,internet1,internet2,oth5,oth6,groc1,groc2,per1,per2,salon1,salon2,oth7,oth8,Auto11,Auto12,Auto21,Auto22,k1,k2,Credit11,Credit12,Credit21,Credit22,Credit31,Credit32,StudentLoans1,StudentLoans2,oth9,oth10,Fuel1,Fuel2,serv1,serv2,oth11,oth12,HomeInsur1,HomeInsur2,AutoInsur1,AutoInsur2,health1,health2,OOP1,OOP2,Pres1,Pres2,Med1,Med2,LTCI1,LTCI2,LI1,LI2,DI1,DI2,PLUI1,PLUI2,oth13,oth14,Club1,Club2,GymMem1,GymMem2,News1,News2,oth15, oth16,Dining1,Dining2,Outing1,Outing2,Hobby1,Hobby2,oth17,oth18,Clothes1,Clothes2,Travel1,Travel2,Gift1,Gift2,Give1,Give2,HomeImprov1,HomeImprov2,College1,College2,Wedding1,Wedding2,Car1Rep1,Car1Rep2,Car2Rep1,Car2Rep2,oth19,oth20,HS1,HS2,Pest1,Pest2,AutoR1,AutoR2,Vac1,Vac2,Misc1,Misc2, C1, C2, n2, total3, total4):
        self.name = name
        self.pin = pin
        self.Rent1 = Rent1
        self.Rent2 = Rent2
        self.Rent3 = Rent3
        self.Rent4 = Rent4
        self.EstateTax1 = EstateTax1
        self.EstateTax2 = EstateTax2
        self.EstateTax3 = EstateTax3
        self.EstateTax4 = EstateTax4
        self.PropTax1 = PropTax1
        self.PropTax2 = PropTax2
        self.HOA1 = HOA1
        self.HOA2 = HOA2
        self.HOA3 = HOA3
        self.HOA4 = HOA4
        self.Improv1 = Improv1
        self.Improv2 = Improv2
        self.Improv3 = Improv3
        self.Improv4 = Improv4
        self.Fur1 = Fur1
        self.Fur2 = Fur2
        self.Fur3 = Fur3
        self.Fur4 = Fur4
        self.Main1 = Main1
        self.Main2 = Main2
        self.Main3 = Main3
        self.Main4 = Main4
        self.Lawn1 = Lawn1
        self.Lawn2 = Lawn2
        self.Lawn3 = Lawn3
        self.Lawn4 = Lawn4
        self.keep1 = keep1
        self.keep2 = keep2
        self.keep3 = keep3
        self.keep4 = keep4
        self.oth1 = oth1
        self.oth2 = oth2
        self.oth3 = oth3
        self.oth4 = oth4
        self.CC1 = CC1
        self.CC2 = CC2
        self.Legal1 = Legal1
        self.Legal2 = Legal2
        self.Account1 = Account1
        self.Account2 = Account2
        self.Elec1 = Elec1
        self.Elec2 = Elec2
        self.gas1 = gas1
        self.gas2 = gas2
        self.oil1 = oil1
        self.oil2 = oil2
        self.cell1 = cell1
        self.cell2 = cell2
        self.trash1 = trash1
        self.trash2 = trash2
        self.water1 = water1
        self.water2 = water2
        self.internet1 = internet1
        self.internet2 = internet2
        self.oth5 = oth5
        self.oth6 = oth6
        self.groc1 = groc1
        self.groc2 = groc2
        self.per1 = per1
        self.per2 = per2
        self.salon1 = salon1
        self.salon2 = salon2
        self.oth7 = oth7
        self.oth8 = oth8
        self.Auto11 = Auto11
        self.Auto12 = Auto12
        self.Auto21 = Auto21
        self.Auto22 = Auto22
        self.k1 = k1
        self.k2 = k2
        self.Credit11 = Credit11
        self.Credit12 = Credit12
        self.Credit21 = Credit21
        self.Credit22 = Credit22
        self.Credit31 = Credit31
        self.Credit32 = Credit32
        self.StudentLoans1 = StudentLoans1
        self.StudentLoans2 = StudentLoans2
        self.oth9 = oth9
        self.oth10 = oth10
        self.Fuel1 = Fuel1
        self.Fuel2 = Fuel2
        self.serv1 = serv1
        self.serv2 = serv2
        self.oth11 = oth11
        self.oth12 = oth12
        self.HomeInsur1 = HomeInsur1
        self.HomeInsur2 = HomeInsur2
        self.AutoInsur1 = AutoInsur1
        self.AutoInsur2 = AutoInsur2
        self.health1 = health1
        self.health2 = health2
        self.OOP1 = OOP1
        self.OOP2 = OOP2
        self.Pres1 = Pres1
        self.Pres2 = Pres2
        self.Med1 = Med1
        self.Med2 = Med2
        self.LTCI1 = LTCI1
        self.LTCI2 = LTCI2
        self.LI1 = LI1
        self.LI2 = LI2
        self.DI1 = DI1
        self.DI2 = DI2
        self.PLUI1 = PLUI1
        self.PLUI2 = PLUI2
        self.oth13 = oth13
        self.oth14 = oth14
        self.Club1 = Club1
        self.Club2 = Club2
        self.GymMem1 = GymMem1
        self.GymMem2 = GymMem2
        self.News1 = News1
        self.News2 = News2
        self.oth15 = oth15
        self.oth16 = oth16
        self.Dining1 = Dining1
        self.Dining2 = Dining2
        self.Outing1 = Outing1
        self.Outing2 = Outing2
        self.Hobby1 = Hobby1
        self.Hobby2 = Hobby2
        self.oth17 = oth17
        self.oth18 = oth18
        self.Clothes1 = Clothes1
        self.Clothes2 = Clothes2
        self.Travel1 = Travel1
        self.Travel2 = Travel2
        self.Gift1 = Gift1
        self.Gift2 = Gift2
        self.Give1 = Give1
        self.Give2 = Give2
        self.HomeImprov1 = HomeImprov1
        self.HomeImprov2 = HomeImprov2
        self.College1 = College1
        self.College2 = College2
        self.Wedding1 = Wedding1
        self.Wedding2 = Wedding2
        self.Car1Rep1 = Car1Rep1
        self.Car1Rep2 = Car1Rep2
        self.Car2Rep1 = Car2Rep1
        self.Car2Rep2 = Car2Rep2
        self.oth19 = oth19
        self.oth20 = oth20
        self.HS1 = HS1
        self.HS2 = HS2
        self.Pest1 = Pest1
        self.Pest2 = Pest2
        self.AutoR1 = AutoR1
        self.AutoR2 = AutoR2
        self.Vac1 = Vac1
        self.Vac2 = Vac2
        self.Misc1 = Misc1
        self.Misc2 = Misc2
        self.C1 = C1
        self.C2 = C2
        self.n2 = n2
        #self.total1 = total1
        #self.total2 = total2
        self.total3 = total3
        self.total4 = total4
