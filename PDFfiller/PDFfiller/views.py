from django.shortcuts import render
import os
import pdfrw
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
import populate_template
from info import Info
from Info2 import Info2
import pickle
from django.core.files.storage import FileSystemStorage
import datetime


def home(request):
    return render(request, "home.html")

def load(request):
    return render(request, "load.html")

def displaydata(request):
    name = request.POST.get("name", None)
    pin = request.POST.get("pin", None)
    try:
        a1 = open(settings.SAVES_DIRS + 'PDF '+ name + pin, 'r')
        i1 = pickle.load(a1)
        #a2 = open(settings.SAVES_DIRS + 'PDF '+ name + pin + '2', 'r')
        #i2 = pickle.load(a2)
        a1.close()
        #a2.close()
    except:
        return render(request, "notfound.html")
    mydata = {"i1": i1[0], "i2": i1[1]}
    return render(request, "data.html", mydata)

def display(request):
    name = request.POST.get("name", None)
    date = request.POST.get("date", None)
    email = request.POST.get("email", None)
    pin = request.POST.get("pin", None)

    notes = request.POST.get("notes", None)
    Retired = ""
    if "Retired" in request.POST:
        Retired = "X"
    Marriage = ""
    if "Marriage" in request.POST:
        Marriage = "X"
    Div = ""
    if "Div" in request.POST:
        Div = "X"
    SellBus = ""
    if "SellBus" in request.POST:
        SellBus = "X"
    BirthC = ""
    if "BirthC" in request.POST:
        BirthC = "X"
    RefBus = ""
    if "RefBus" in request.POST:
        RefBus = "X"
    BirthGC = ""
    if "BirthGC" in request.POST:
        BirthGC = "X"
    FailBus = ""
    if "FailBus" in request.POST:
        FailBus = "X"
    Remarry = ""
    if "Remarry" in request.POST:
        Remarry = "X"
    JobLoss = ""
    if "JobLoss" in request.POST:
        JobLoss = "X"
    Reloc = ""
    if "Reloc" in request.POST:
        Reloc = "X"
    College = ""
    if "College" in request.POST:
        College = "X"
    LastChild = ""
    if "LastChild" in request.POST:
        LastChild = "X"
    MoveIn = ""
    if "MoveIn" in request.POST:
        MoveIn = "X"
    ChildMarry = ""
    if "ChildMarry" in request.POST:
        ChildMarry = "X"
    DisabilityPar = ""
    if "DisabilityPar" in request.POST:
        DisabilityPar = "X"
    ACDiv = ""
    if "ACDiv" in request.POST:
        ACDiv = "X"
    DisabilityAC = ""
    if "DisabilityAC" in request.POST:
        DisabilityAC = "X"
    ACRemarry = ""
    if "ACRemarry" in request.POST:
        ACRemarry = "X"
    PurHome = ""
    if "PurHome" in request.POST:
        PurHome = "X"
    RelocPar = ""
    if "RelocPar" in request.POST:
        RelocPar = "X"
    DeathPar = ""
    if "DeathPar" in request.POST:
        DeathPar = "X"
    DeathChild = ""
    if "DeathChild" in request.POST:
        DeathChild = "X"
    DeathSpouse = ""
    if "DeathSpouse" in request.POST:
        DeathSpouse = "X"
    SellHome = ""
    if "SellHome" in request.POST:
        SellHome = "X"
    SellProp = ""
    if "SellProp" in request.POST:
        SellProp = "X"
    BuyProp = ""
    if "BuyProp" in request.POST:
        BuyProp = "X"
    Legacy = ""
    if "Legacy" in request.POST:
        Legacy = "X"
    Inherit = ""
    if "Inherit" in request.POST:
        Inherit = "X"
    NewEmp = ""
    if "NewEmp" in request.POST:
        NewEmp = "X"
    SpouseStart = ""
    if "SpouseStart" in request.POST:
        SpouseStart = "X"
    SpouseStop = ""
    if "SpouseStop" in request.POST:
        SpouseStop = "X"
    RelocJob = ""
    if "RelocJob" in request.POST:
        RelocJob = "X"
    StartBus = ""
    if "StartBus" in request.POST:
        StartBus = "X"

    test1 = request.POST.get("FTEstart1", None)
    FTEstart2 = request.POST.get("FTEstart2", None)
    FTEmonth1 = request.POST.get("FTEmonth1", None)
    FTEmonth2 = request.POST.get("FTEmonth2", None)
    FTEend1 = request.POST.get("FTEend1", None)
    FTEend2 = request.POST.get("FTEend2", None)
    FTEbonus1 = request.POST.get("FTEbonus1", None)
    FTEbonus2 = request.POST.get("FTEbonus2", None)
    PTEstart1 = request.POST.get("PTEstart1", None)
    PTEstart2 = request.POST.get("PTEstart2", None)
    PTEmonth1 = request.POST.get("PTEmonth1", None)
    PTEmonth2 = request.POST.get("PTEmonth2", None)
    PTEend1 = request.POST.get("PTEend1", None)
    PTEend2 = request.POST.get("PTEend2", None)
    PTEbonus1 = request.POST.get("PTEbonus1", None)
    PTEbonus2 = request.POST.get("PTEbonus2", None)
    PENstart1 = request.POST.get("PENstart1", None)
    PENstart2 = request.POST.get("PENstart2", None)
    PENmonth1 = request.POST.get("PENmonth1", None)
    PENmonth2 = request.POST.get("PENmonth2", None)
    PENend1 = request.POST.get("PENend1", None)
    PENend2 = request.POST.get("PENend2", None)
    PENbonus1 = request.POST.get("PENbonus1", None)
    PENbonus2 = request.POST.get("PENbonus2", None)
    SSstart1 = request.POST.get("SSstart1", None)
    SSstart2 = request.POST.get("SSstart2", None)
    SSmonth1 = request.POST.get("SSmonth1", None)
    SSmonth2 = request.POST.get("SSmonth2", None)
    SSend1 = request.POST.get("SSend1", None)
    SSend2 = request.POST.get("SSend2", None)
    SSbonus1 = request.POST.get("SSbonus1", None)
    SSbonus2 = request.POST.get("SSbonus2", None)
    RIstart1 = request.POST.get("RIstart1", None)
    RIstart2 = request.POST.get("RIstart2", None)
    RImonth1 = request.POST.get("RImonth1", None)
    RImonth2 = request.POST.get("RImonth2", None)
    RIend1 = request.POST.get("RIend1", None)
    RIend2 = request.POST.get("RIend2", None)
    RIbonus1 = request.POST.get("RIbonus1", None)
    RIbonus2 = request.POST.get("RIbonus2", None)
    EIstart1 = request.POST.get("EIstart1", None)
    EIstart2 = request.POST.get("EIstart2", None)
    EImonth1 = request.POST.get("EImonth1", None)
    EImonth2 = request.POST.get("EImonth2", None)
    EIend1 = request.POST.get("EIend1", None)
    EIend2 = request.POST.get("EIend2", None)
    EIbonus1 = request.POST.get("EIbonus1", None)
    EIbonus2 = request.POST.get("EIbonus2", None)
    SBstart1 = request.POST.get("SBstart1", None)
    SBstart2 = request.POST.get("SBstart2", None)
    SBmonth1 = request.POST.get("SBmonth1", None)
    SBmonth2 = request.POST.get("SBmonth2", None)
    SBend1 = request.POST.get("SBend1", None)
    SBend2 = request.POST.get("SBend2", None)
    SBbonus1 = request.POST.get("SBbonus1", None)
    SBbonus2 = request.POST.get("SBbonus2", None)
    SREstart1 = request.POST.get("SREstart1", None)
    SREstart2 = request.POST.get("SREstart2", None)
    SREmonth1 = request.POST.get("SREmonth1", None)
    SREmonth2 = request.POST.get("SREmonth2", None)
    SREend1 = request.POST.get("SREend1", None)
    SREend2 = request.POST.get("SREend2", None)
    SREbonus1 = request.POST.get("SREbonus1", None)
    SREbonus2 = request.POST.get("SREbonus2", None)
    o1start1 = request.POST.get("o1start1", None)
    o1start2 = request.POST.get("o1start2", None)
    o1month1 = request.POST.get("o1month1", None)
    o1month2 = request.POST.get("o1month2", None)
    o1end1 = request.POST.get("o1end1", None)
    o1end2 = request.POST.get("o1end2", None)
    o1bonus1 = request.POST.get("o1bonus1", None)
    o1bonus2 = request.POST.get("o1bonus2", None)
    o2start1 = request.POST.get("o2start1", None)
    o2start2 = request.POST.get("o2start2", None)
    o2month1 = request.POST.get("o2month1", None)
    o2month2 = request.POST.get("o2month2", None)
    o2end1 = request.POST.get("o2end1", None)
    o2end2 = request.POST.get("o2end2", None)
    o2bonus1 = request.POST.get("o2bonus1", None)
    o2bonus2 = request.POST.get("o2bonus2", None)
    o3start1 = request.POST.get("o3start1", None)
    o3start2 = request.POST.get("o3start2", None)
    o3month1 = request.POST.get("o3month1", None)
    o3month2 = request.POST.get("o3month2", None)
    o3end1 = request.POST.get("o3end1", None)
    o3end2 = request.POST.get("o3end2", None)
    o3bonus1 = request.POST.get("o3bonus1", None)
    o3bonus2 = request.POST.get("o3bonus2", None)
    other11 = request.POST.get("other11", None)
    other21 = request.POST.get("other21", None)
    other31 = request.POST.get("other31", None)
    other12 = request.POST.get("other12", None)
    other22 = request.POST.get("other22", None)
    other32 = request.POST.get("other32", None)

    street1 = request.POST.get("street1", None)
    city1 = request.POST.get("city1", None)
    state1 = request.POST.get("state1", None)
    zip1 = request.POST.get("zip1", None)
    value1 = request.POST.get("value1", None)
    IR1 = request.POST.get("IR1", None)
    MP1 = request.POST.get("MP1", None)
    CBL1 = request.POST.get("CBL1", None)
    ARM1 = request.POST.get("ARM1", None)
    street2 = request.POST.get("street2", None)
    city2 = request.POST.get("city2", None)
    state2 = request.POST.get("state2", None)
    zip2 = request.POST.get("zip2", None)
    value2 = request.POST.get("value2", None)
    IR2 = request.POST.get("IR2", None)
    MP2 = request.POST.get("MP2", None)
    CBL2 = request.POST.get("CBL2", None)
    ARM2 = request.POST.get("ARM2", None)
    street3 = request.POST.get("street3", None)
    city3 = request.POST.get("city3", None)
    state3 = request.POST.get("state3", None)
    zip3 = request.POST.get("zip3", None)
    value3 = request.POST.get("value3", None)
    IR3 = request.POST.get("IR3", None)
    MP3 = request.POST.get("MP3", None)
    CBL3 = request.POST.get("CBL3", None)
    ARM3 = request.POST.get("ARM3", None)
    HomeEquity = request.POST.get("HomeEquity", None)
    TypeLoan1 = request.POST.get("TypeLoan1", None)
    LoanA1 = request.POST.get("LoanA1", None)
    LoanIR1 = request.POST.get("LoanIR1", None)
    LoanMonthly1 = request.POST.get("LoanMonthly1", None)
    LoanCB1 = request.POST.get("LoanCB1", None)
    LoanDate1 = request.POST.get("LoanDate1", None)
    TypeLoan2 = request.POST.get("TypeLoan2", None)
    LoanA2 = request.POST.get("LoanA2", None)
    LoanIR2 = request.POST.get("LoanIR2", None)
    LoanMonthly2 = request.POST.get("LoanMonthly2", None)
    LoanCB2 = request.POST.get("LoanCB2", None)
    LoanDate2 = request.POST.get("LoanDate2", None)
    TypeLoan3 = request.POST.get("TypeLoan3", None)
    LoanA3 = request.POST.get("LoanA3", None)
    LoanIR3 = request.POST.get("LoanIR3", None)
    LoanMonthly3 = request.POST.get("LoanMonthly3", None)
    LoanCB3 = request.POST.get("LoanCB3", None)
    LoanDate3 = request.POST.get("LoanDate3", None)
    ApproxMonth = request.POST.get("ApproxMonth", None)
    notes2 = request.POST.get("notes2", None)


    Risk1 = ""
    if "Risk1" in request.POST:
        Risk1 = "X"
    Risk2 = ""
    if "Risk2" in request.POST:
        Risk2 = "X"
    Risk3 = ""
    if "Risk3" in request.POST:
        Risk3 = "X"
    Risk4 = ""
    if "Risk4" in request.POST:
        Risk4 = "X"
    RateR1 = ""
    if "RateR1" in request.POST:
        RateR1 = "X"
    RateR2 = ""
    if "RateR2" in request.POST:
        RateR2 = "X"
    RateR3 = ""
    if "RateR3" in request.POST:
        RateR3 = "X"
    RateR4 = ""
    if "RateR4" in request.POST:
        RateR4 = "X"
    raise1 = ""
    if "raise1" in request.POST:
        raise1 = "X"
    raise2 = ""
    if "raise2" in request.POST:
        raise2 = "X"
    raise3 = ""
    if "raise3" in request.POST:
        raise3 = "X"
    raise4 = ""
    if "raise4" in request.POST:
        raise4 = "X"
    dropF1 = ""
    if "dropF1" in request.POST:
        dropF1 = "X"
    dropF2 = ""
    if "dropF2" in request.POST:
        dropF2 = "X"
    dropF3 = ""
    if "dropF3" in request.POST:
        dropF3 = "X"
    dropF4 = ""
    if "dropF4" in request.POST:
        dropF4 = "X"
    drop1 = ""
    if "drop1" in request.POST:
        drop1 = "X"
    drop2 = ""
    if "drop2" in request.POST:
        drop2 = "X"
    drop3 = ""
    if "drop3" in request.POST:
        drop3 = "X"
    drop4 = ""
    if "drop4" in request.POST:
        drop4 = "X"
    vol1 = ""
    if "vol1" in request.POST:
        vol1 = "X"
    vol2 = ""
    if "vol2" in request.POST:
        vol2 = "X"
    vol3 = ""
    if "vol3" in request.POST:
        vol3 = "X"
    vol4 = ""
    if "vol4" in request.POST:
        vol4 = "X"
    Current1 = ""
    if "Current1" in request.POST:
        Current1 = "X"
    Current2 = ""
    if "Current2" in request.POST:
        Current2 = "X"
    Current3 = ""
    if "Current3" in request.POST:
        Current3 = "X"
    Current4 = ""
    if "Current4" in request.POST:
        Current4 = "X"
    decline1 = ""
    if "decline1" in request.POST:
        decline1 = "X"
    decline2 = ""
    if "decline2" in request.POST:
        decline2 = "X"
    decline3 = ""
    if "decline3" in request.POST:
        decline3 = "X"
    decline4 = ""
    if "decline4" in request.POST:
        decline4 = "X"
    in1 = ""
    if "in1" in request.POST:
        in1 = "X"
    in2 = ""
    if "in2" in request.POST:
        in2 = "X"
    in3 = ""
    if "in3" in request.POST:
        in3 = "X"
    in4 = ""
    if "in4" in request.POST:
        in4 = "X"
    fly1 = ""
    if "fly1" in request.POST:
        fly1 = "X"
    fly2 = ""
    if "fly2" in request.POST:
        fly2 = "X"
    fly3 = ""
    if "fly3" in request.POST:
        fly3 = "X"
    fly4 = ""
    if "fly4" in request.POST:
        fly4 = "X"
    exp1 = ""
    if "exp1" in request.POST:
        exp1 = "X"
    exp2 = ""
    if "exp2" in request.POST:
        exp2 = "X"
    exp3 = ""
    if "exp3" in request.POST:
        exp3 = "X"
    exp4 = ""
    if "exp4" in request.POST:
        exp4 = "X"
    outlook1 = ""
    if "outlook1" in request.POST:
        outlook1 = "X"
    outlook2 = ""
    if "outlook2" in request.POST:
        outlook2 = "X"
    outlook3 = ""
    if "outlook3" in request.POST:
        outlook3 = "X"
    outlook4 = ""
    if "outlook4" in request.POST:
        outlook4 = "X"
    withdraw1 = ""
    if "withdraw1" in request.POST:
        withdraw1 = "X"
    withdraw2 = ""
    if "withdraw2" in request.POST:
        withdraw2 = "X"
    withdraw3 = ""
    if "withdraw3" in request.POST:
        withdraw3 = "X"
    withdraw4 = ""
    if "withdraw4" in request.POST:
        withdraw4 = "X"
    Income14 = ""
    if "Income14" in request.POST:
        Income14 = "X"
    Growth14 = ""
    if "Growth14" in request.POST:
        Growth14 = "X"
    NDY15 = ""
    if "NDY15" in request.POST:
        NDY15 = "X"
    Market15 = ""
    if "Market15" in request.POST:
        Market15 = "X"
    cons16 = ""
    if "cons16" in request.POST:
        cons16 = "X"
    reward16 = ""
    if "reward16" in request.POST:
        reward16 = "X"
    notes3 = request.POST.get("notes3", None)

    CopiesSS = ""
    if "CopiesSS" in request.POST:
        CopiesSS = "X"
    CopiesMort = ""
    if "CopiesMort" in request.POST:
        CopiesMort = "X"
    Copies401k = ""
    if "Copies401k" in request.POST:
        Copies401k = "X"
    CopiesInvest = ""
    if "CopiesInvest" in request.POST:
        CopiesInvest = "X"
    CopiesInsurance = ""
    if "CopiesInsurance" in request.POST:
        CopiesInsurance = "X"
    CopiesCollege = ""
    if "CopiesCollege" in request.POST:
        CopiesCollege = "X"
    notes4 = request.POST.get("notes4", None)

    Rent1 = request.POST.get("Rent1", None)
    Rent2 = request.POST.get("Rent2", None)
    Rent3 = request.POST.get("Rent3", None)
    Rent4 = request.POST.get("Rent4", None)
    EstateTax1 = request.POST.get("EstateTax1", None)
    EstateTax2 = request.POST.get("EstateTax2", None)
    EstateTax3 = request.POST.get("EstateTax3", None)
    EstateTax4 = request.POST.get("EstateTax4", None)
    PropTax1 = request.POST.get("PropTax1", None)
    PropTax2 = request.POST.get("PropTax2", None)
    HOA1 = request.POST.get("HOA1", None)
    HOA2 = request.POST.get("HOA2", None)
    HOA3 = request.POST.get("HOA3", None)
    HOA4 = request.POST.get("HOA4", None)
    Improv1 = request.POST.get("Improv1", None)
    Improv2 = request.POST.get("Improv2", None)
    Improv3 = request.POST.get("Improv3", None)
    Improv4 = request.POST.get("Improv4", None)
    Fur1 = request.POST.get("Fur1", None)
    Fur2 = request.POST.get("Fur2", None)
    Fur3 = request.POST.get("Fur3", None)
    Fur4 = request.POST.get("Fur4", None)
    Main1 = request.POST.get("Main1", None)
    Main2 = request.POST.get("Main2", None)
    Main3 = request.POST.get("Main3", None)
    Main4 = request.POST.get("Main4", None)
    Lawn1 = request.POST.get("Lawn1", None)
    Lawn2 = request.POST.get("Lawn2", None)
    Lawn3 = request.POST.get("Lawn3", None)
    Lawn4 = request.POST.get("Lawn4", None)
    keep1 = request.POST.get("keep1", None)
    keep2 = request.POST.get("keep2", None)
    keep3 = request.POST.get("keep3", None)
    keep4 = request.POST.get("keep4", None)
    oth1 = request.POST.get("oth1", None)
    oth2 = request.POST.get("oth2", None)
    oth3 = request.POST.get("oth3", None)
    oth4 = request.POST.get("oth4", None)
    CC1 = request.POST.get("CC1", None)
    CC2 = request.POST.get("CC2", None)
    Legal1 = request.POST.get("Legal1", None)
    Legal2 = request.POST.get("Legal2", None)
    Account1 = request.POST.get("Account1", None)
    Account2 = request.POST.get("Account2", None)
    Elec1 = request.POST.get("Elec1", None)
    Elec2 = request.POST.get("Elec2", None)
    gas1 = request.POST.get("gas1", None)
    gas2 = request.POST.get("gas2", None)
    oil1 = request.POST.get("oil1", None)
    oil2 = request.POST.get("oil2", None)
    cell1 = request.POST.get("cell1", None)
    cell2 = request.POST.get("cell2", None)
    trash1 = request.POST.get("trash1", None)
    trash2 = request.POST.get("trash2", None)
    water1 = request.POST.get("water1", None)
    water2 = request.POST.get("water2", None)
    internet1 = request.POST.get("internet1", None)
    internet2 = request.POST.get("internet2", None)
    oth5 = request.POST.get("oth5", None)
    oth6 = request.POST.get("oth6", None)
    groc1 = request.POST.get("groc1", None)
    groc2 = request.POST.get("groc2", None)
    per1 = request.POST.get("per1", None)
    per2 = request.POST.get("per2", None)
    salon1 = request.POST.get("salon1", None)
    salon2 = request.POST.get("salon2", None)
    oth7 = request.POST.get("oth7", None)
    oth8 = request.POST.get("oth8", None)
    Auto11 = request.POST.get("Auto11", None)
    Auto12 = request.POST.get("Auto12", None)
    Auto21 = request.POST.get("Auto21", None)
    Auto22 = request.POST.get("Auto22", None)
    k1 = request.POST.get("401k1", None)
    k2 = request.POST.get("401k2", None)
    Credit11 = request.POST.get("Credit11", None)
    Credit12 = request.POST.get("Credit12", None)
    Credit21 = request.POST.get("Credit21", None)
    Credit22 = request.POST.get("Credit22", None)
    Credit31 = request.POST.get("Credit31", None)
    Credit32 = request.POST.get("Credit32", None)
    StudentLoans1 = request.POST.get("StudentLoans1", None)
    StudentLoans2 = request.POST.get("StudentLoans2", None)
    oth9 = request.POST.get("oth9", None)
    oth10 = request.POST.get("oth10", None)
    Fuel1 = request.POST.get("Fuel1", None)
    Fuel2 = request.POST.get("Fuel2", None)
    serv1 = request.POST.get("serv1", None)
    serv2 = request.POST.get("serv2", None)
    oth11 = request.POST.get("oth11", None)
    oth12 = request.POST.get("oth12", None)
    HomeInsur1 = request.POST.get("HomeInsur1", None)
    HomeInsur2 = request.POST.get("HomeInsur2", None)
    AutoInsur1 = request.POST.get("AutoInsur1", None)
    AutoInsur2 = request.POST.get("AutoInsur2", None)
    health1 = request.POST.get("health1", None)
    health2 = request.POST.get("health2", None)
    OOP1 = request.POST.get("OOP1", None)
    OOP2 = request.POST.get("OOP2", None)
    Pres1 = request.POST.get("Pres1", None)
    Pres2 = request.POST.get("Pres2", None)
    Med1 = request.POST.get("Med1", None)
    Med2 = request.POST.get("Med2", None)
    LTCI1 = request.POST.get("LTCI1", None)
    LTCI2 = request.POST.get("LTCI2", None)
    LI1 = request.POST.get("LI1", None)
    LI2 = request.POST.get("LI2", None)
    DI1 = request.POST.get("DI1", None)
    DI2 = request.POST.get("DI2", None)
    PLUI1 = request.POST.get("PLUI1", None)
    PLUI2 = request.POST.get("PLUI2", None)
    oth13 = request.POST.get("oth13", None)
    oth14 = request.POST.get("oth14", None)
    Club1 = request.POST.get("Club1", None)
    Club2 = request.POST.get("Club2", None)
    GymMem1 = request.POST.get("GymMem1", None)
    GymMem2 = request.POST.get("GymMem2", None)
    News1 = request.POST.get("News1", None)
    News2 = request.POST.get("News2", None)
    oth15 = request.POST.get("oth15", None)
    oth16 = request.POST.get("oth16", None)
    Dining1 = request.POST.get("Dining1", None)
    Dining2 = request.POST.get("Dining2", None)
    Outing1 = request.POST.get("Outing1", None)
    Outing2 = request.POST.get("Outing2", None)
    Hobby1 = request.POST.get("Hobby1", None)
    Hobby2 = request.POST.get("Hobby2", None)
    oth17 = request.POST.get("oth17", None)
    oth18 = request.POST.get("oth18", None)
    Clothes1 = request.POST.get("Clothes1", None)
    Clothes2 = request.POST.get("Clothes2", None)
    Travel1 = request.POST.get("Travel1", None)
    Travel2 = request.POST.get("Travel2", None)
    Gift1 = request.POST.get("Gift1", None)
    Gift2 = request.POST.get("Gift2", None)
    Give1 = request.POST.get("Give1", None)
    Give2 = request.POST.get("Give2", None)
    HomeImprov1 = request.POST.get("HomeImprov1", None)
    HomeImprov2 = request.POST.get("HomeImprov2", None)
    College1 = request.POST.get("College1", None)
    College2 = request.POST.get("College2", None)
    Wedding1 = request.POST.get("Wedding1", None)
    Wedding2 = request.POST.get("Wedding2", None)
    Car1Rep1 = request.POST.get("Car1Rep1", None)
    Car1Rep2 = request.POST.get("Car1Rep2", None)
    Car2Rep1 = request.POST.get("Car2Rep1", None)
    Car2Rep2 = request.POST.get("Car2Rep2", None)
    oth19 = request.POST.get("oth19", None)
    oth20 = request.POST.get("oth20", None)
    HS1 = request.POST.get("HS1", None)
    HS2 = request.POST.get("HS2", None)
    Pest1 = request.POST.get("Pest1", None)
    Pest2 = request.POST.get("Pest2", None)
    AutoR1 = request.POST.get("AutoR1", None)
    AutoR2 = request.POST.get("AutoR2", None)
    Vac1 = request.POST.get("Vac1", None)
    Vac2 = request.POST.get("Vac2", None)
    Misc1 = request.POST.get("Misc1", None)
    Misc2 = request.POST.get("Misc2", None)

    n1 = request.POST.get("n1", None)
    n2 = request.POST.get("n2", None)
    C1 = request.POST.get("C1", None)
    C2  = request.POST.get("C2", None)
    note  = request.POST.get("note", None)

    if request.method == 'POST' and 'FileSS' in request.FILES:
        myfileSS = request.FILES['FileSS']
        filenameSS = myfileSS.name.split(".")
        fsSS = FileSystemStorage()
        filenameSS = fsSS.save(myfileSS.name, myfileSS)
        uploaded_file_urlSS = fsSS.url(filenameSS)
        pathSS = "/" + name + "/" +  myfileSS.name
        populate_template.upload(uploaded_file_urlSS,pathSS)

    if request.method == 'POST' and 'FileMort' in request.FILES:
        myfileMort = request.FILES['FileMort']
        filenameMort = myfileMort.name.split('.')
        fsMort = FileSystemStorage()
        filenameMort = fsMort.save(myfileMort.name, myfileMort)
        uploaded_file_urlMort = fsMort.url(filenameMort)
        pathMort = "/" + name + "/" + myfileMort.name
        populate_template.upload(uploaded_file_urlMort,pathMort)

    if request.method == 'POST' and 'File401k' in request.FILES:
        myfile401k = request.FILES['File401k']
        filename401k = myfile401k.name.split(".")
        fs401k = FileSystemStorage()
        filename401k = fs401k.save(myfile401k.name, myfile401k)
        uploaded_file_url401k = fs401k.url(filename401k)
        path401k = "/" + name + "/" + myfile401k.name
        populate_template.upload(uploaded_file_url401k,path401k)

    if request.method == 'POST' and 'FileInvest' in request.FILES:
        myfileInvest = request.FILES['FileInvest']
        filenameInvest = myfileInvest.name.split(".")
        fsInvest = FileSystemStorage()
        filenameInvest = fsInvest.save(myfileInvest.name, myfileInvest)
        uploaded_file_urlInvest = fsInvest.url(filenameInvest)
        pathInvest = "/" + name + "/" + myfileInvest.name
        populate_template.upload(uploaded_file_urlInvest,pathInvest)

    if request.method == 'POST' and 'FileInsurance' in request.FILES:
        myfileInsurance = request.FILES['FileInsurance']
        filenameInsurance = myfileInsurance.name.split(".")
        fsInsurance = FileSystemStorage()
        filenameInsurance = fsInsurance.save(myfileInsurance.name, myfileInsurance)
        uploaded_file_urlInsurance = fsInsurance.url(filenameInsurance)
        pathInsurance = "/" + name + "/" + myfileInsurance.name
        populate_template.upload(uploaded_file_urlInsurance,pathInsurance)

    if request.method == 'POST' and 'FileCollege' in request.FILES:
        myfileCollege = request.FILES['FileCollege']
        filenameCollege = myfileCollege.name.split(".")
        fsCollege = FileSystemStorage()
        filenameCollege = fsCollege.save(myfileCollege.name, myfileCollege)
        uploaded_file_urlCollege = fsCollege.url(filenameCollege)
        pathCollege = "/" + name + "/" + myfileCollege.name
        populate_template.upload(uploaded_file_urlCollege,pathCollege)

    t1 = [Rent1,EstateTax1,PropTax1,HOA1,Improv1,Fur1,Main1,Lawn1,keep1,CC1,Legal1,Account1,oth1,Rent3,EstateTax3,HOA3,Fur3,Main3,Lawn3,keep3,oth3,Elec1,gas1,oil1,cell1,trash1,water1,internet1,oth5,groc1,salon1,oth7,Auto11,Auto21,k1,Credit11,Credit21,Credit31,StudentLoans1,oth9]
    t2 = [Rent2,EstateTax2,PropTax2,HOA2,Improv2,Fur2,Main2,Lawn2,keep2,CC2,Legal2,Account2,oth2,Rent4,EstateTax4,HOA4,Fur4,Main4,Lawn4,keep4,oth4,Elec2,gas2,oil2,cell2,trash2,water2,internet2,oth6,groc2,salon2,oth8,Auto12,Auto22,k2,Credit12,Credit22,Credit32,StudentLoans2,oth10]
    t3 = [Fuel1,serv1,oth11,HomeInsur1,AutoInsur1,health1,OOP1,Pres1,Med1,LTCI1,LI1,DI1,PLUI1,oth13,Club1,GymMem1,News1,oth15,Dining1,Outing1,Hobby1,oth17,Clothes1,Travel1,Gift1,Give1,HomeImprov1,College1,Wedding1,Car1Rep1,Car2Rep2,oth19,HS1,Pest1,AutoR1,Vac1,Misc1]
    t4 = [Fuel2,serv2,oth12,HomeInsur2,AutoInsur2,health2,OOP2,Pres2,Med2,LTCI2,LI2,DI2,PLUI2,oth14,Club2,GymMem2,News2,oth16,Dining2,Outing2,Hobby2,oth18,Clothes2,Travel2,Gift2,Give2,HomeImprov2,College2,Wedding2,Car1Rep2,Car2Rep2,oth20,HS2,Pest2,AutoR2,Vac2,Misc2]
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    for x in t1:
        if x != '':
            total1 += int(x)
    for x in t2:
        if x != '':
            total2 += int(x)
    for x in t3:
        if x != '':
            total3 += int(x)
    for x in t4:
        if x != '':
            total4 += int(x)
    total4 += total2
    total3 += total1
    i1 = Info(name,pin,Rent1,Rent2,Rent3,Rent4,EstateTax1,EstateTax2,EstateTax3,EstateTax4,PropTax1,PropTax2,HOA1,HOA2,HOA3,HOA4,Improv1,Improv2,Improv3,Improv4,Fur1,Fur2,Fur3,Fur4,Main1,Main2,Main3,Main4,Lawn1,Lawn2,Lawn3,Lawn4,keep1,keep2,keep3,keep4,oth1,oth2,oth3,oth4,CC1,CC2,Legal1,Legal2,Account1,Account2,Elec1,Elec2,gas1,gas2,oil1,oil2,cell1,cell2,trash1,trash2,water1,water2,internet1,internet2,oth5,oth6,groc1,groc2,per1,per2,salon1,salon2,oth7,oth8,Auto11,Auto12,Auto21,Auto22,k1,k2,Credit11,Credit12,Credit21,Credit22,Credit31,Credit32,StudentLoans1,StudentLoans2,oth9,oth10,Fuel1,Fuel2,serv1,serv2,oth11,oth12,HomeInsur1,HomeInsur2,AutoInsur1,AutoInsur2,health1,health2,OOP1,OOP2,Pres1,Pres2,Med1,Med2,LTCI1,LTCI2,LI1,LI2,DI1,DI2,PLUI1,PLUI2,oth13,oth14,Club1,Club2,GymMem1,GymMem2,News1,News2,oth15, oth16,Dining1,Dining2,Outing1,Outing2,Hobby1,Hobby2,oth17,oth18,Clothes1,Clothes2,Travel1,Travel2,Gift1,Gift2,Give1,Give2,HomeImprov1,HomeImprov2,College1,College2,Wedding1,Wedding2,Car1Rep1,Car1Rep2,Car2Rep1,Car2Rep2,oth19,oth20,HS1,HS2,Pest1,Pest2,AutoR1,AutoR2,Vac1,Vac2,Misc1,Misc2, C1, C2, n2, total3, total4)
    i2 = Info2(name,date,pin,email,notes,Retired,Marriage,Div,SellBus,BirthC,RefBus,BirthGC,FailBus,Remarry,JobLoss,Reloc,College,LastChild,MoveIn,ChildMarry,DisabilityPar,DisabilityAC,ACDiv,ACRemarry,PurHome,RelocPar,DeathPar,DeathChild,DeathSpouse,SellHome,SellProp,Legacy,BuyProp,Inherit,NewEmp,SpouseStart,SpouseStop,RelocJob,StartBus,test1,FTEstart2,FTEend1,FTEend2,FTEmonth1,FTEmonth2,FTEbonus1,FTEbonus2,PTEstart1,PTEstart2,PTEend1,PTEend2,PTEmonth1,PTEmonth2,PTEbonus1,PTEbonus2,PENstart1,PENstart2,PENend1,PENend2,PENmonth1,PENmonth2,PENbonus1,PENbonus2,SSstart1,SSstart2,SSend1,SSend2,SSmonth1,SSmonth2,SSbonus1,SSbonus2,RIstart1,RIstart2,RIend1,RIend2,RImonth1,RImonth2,RIbonus1,RIbonus2,EIstart1,EIstart2,EIend1,EIend2,EImonth1,EImonth2,EIbonus1,EIbonus2,SBstart1,SBstart2,SBend1,SBend2,SBmonth1,SBmonth2,SBbonus1,SBbonus2,SREstart1,SREstart2,SREend1,SREend2,SREmonth1,SREmonth2,SREbonus1,SREbonus2,o1start1,o1start2,o1end1,o1end2,o1month1,o1month2,o1bonus1,o1bonus2,o2start1,o2start2,o2end1,o2end2,o2month1,o2month2,o2bonus1,o2bonus2,o3start1,o3start2,o3end1,o3end2,o3month1,o3month2,o3bonus1,o3bonus2,other11,other12,other21,other22,other31,other32,street1,city1,state1,zip1,value1,IR1,MP1,CBL1,ARM1,street2,city2,state2,zip2,value2,IR2,MP2,CBL2,ARM2,street3,city3,state3,zip3,value3,IR3,MP3,CBL3,ARM3,HomeEquity,TypeLoan1,LoanA1,LoanIR1,LoanMonthly1,LoanCB1,LoanDate1,TypeLoan2,LoanA2,LoanIR2,LoanMonthly2,LoanCB2,LoanDate2,TypeLoan3,LoanA3,LoanIR3,LoanMonthly3,LoanCB3,LoanDate3,ApproxMonth,notes2,Risk1,Risk2,Risk3,Risk4,RateR1,RateR2,RateR3,RateR4,raise1,raise2,raise3,raise4,dropF1,dropF2,dropF3,dropF4,drop1,drop2,drop3,drop4,vol1,vol2,vol3,vol4,Current1,Current2,Current3,Current4,decline1,decline2,decline3,decline4,in1,in2,in3,in4,fly1,fly2,fly3,fly4,exp1,exp2,exp3,exp4,outlook1,outlook2,outlook3,outlook4,withdraw1,withdraw2,withdraw3,withdraw4,Income14,Growth14,NDY15,Market15,cons16,reward16,notes3,CopiesSS,CopiesCollege,CopiesMort,Copies401k,CopiesInvest,CopiesInsurance,notes4,n1, note)

    data_dict2 = {
        'C1': C1,
        'C2': C2,
        'Rent1': Rent1,
        'Rent2': Rent2,
        'Rent3': Rent3,
        'Rent4': Rent4,
        'EstateTax1': EstateTax1,
        'EstateTax2': EstateTax2,
        'EstateTax3': EstateTax3,
        'EstateTax4': EstateTax4,
        'PropTax1': PropTax1,
        'PropTax2': PropTax2,
        'HOA1': HOA1,
        'HOA2': HOA2,
        'HOA3': HOA3,
        'HOA4': HOA4,
        'Improv1': Improv1,
        'Improv2': Improv2,
        'Improv3': Improv3,
        'Improv4': Improv4,
        'Fur1': Fur1,
        'Fur2': Fur2,
        'Fur3': Fur3,
        'Fur4': Fur4,
        'Main1': Main1,
        'Main2': Main2,
        'Main3': Main3,
        'Main4': Main4,
        'Lawn1': Lawn1,
        'Lawn2': Lawn2,
        'Lawn3': Lawn3,
        'Lawn4': Lawn4,
        'keep1': keep1,
        'keep2': keep2,
        'keep3': keep3,
        'keep4': keep4,
        'oth1': oth1,
        'oth2': oth2,
        'oth3': oth3,
        'oth4': oth4,
        'CC1': CC1,
        'CC2': CC2,
        'Legal1': Legal1,
        'Legal2': Legal2,
        'Account1': Account1,
        'Account2': Account2,
        'Elec1': Elec1,
        'Elec2': Elec2,
        'gas1': gas1,
        'gas2': gas2,
        'oil1': oil1,
        'oil2': oil2,
        'cell1': cell1,
        'cell2': cell2,
        'trash1': trash1,
        'trash2': trash2,
        'water1': water1,
        'water2': water2,
        'internet1': internet1,
        'internet2': internet2,
        'oth5': oth5,
        'oth6': oth6,
        'groc1': groc1,
        'groc2': groc2,
        'per1': per1,
        'per2': per2,
        'salon1': salon1,
        'salon2': salon2,
        'oth7': oth7,
        'oth8': oth8,
        'Auto11': Auto11,
        'Auto12': Auto12,
        'Auto21': Auto21,
        'Auto22': Auto22,
        'k1': k1,
        'k2': k2,
        'Credit11': Credit11,
        'Credit12': Credit12,
        'Credit21': Credit21,
        'Credit22': Credit22,
        'Credit31': Credit31,
        'Credit32': Credit32,
        'StudentLoans1': StudentLoans1,
        'StudentLoans2': StudentLoans2,
        'oth9': oth9,
        'oth10': oth10,
        'Fuel1': Fuel1,
        'Fuel2': Fuel2,
        'serv1': serv1,
        'serv2': serv2,
        'oth11': oth11,
        'oth12': oth12,
        'HomeInsur1': HomeInsur1,
        'HomeInsur2': HomeInsur2,
        'AutoInsur1': AutoInsur1,
        'AutoInsur2': AutoInsur2,
        'health1': health1,
        'health2': health2,
        'OOP1': OOP1,
        'OOP2': OOP2,
        'Pres1': Pres1,
        'Pres2': Pres2,
        'Med1': Med1,
        'Med2': Med2,
        'LTCI1': LTCI1,
        'LTCI2': LTCI2,
        'LI1': LI1,
        'LI2': LI2,
        'DI1': DI1,
        'DI2': DI2,
        'PLUI1': PLUI1,
        'PLUI2': PLUI2,
        'oth13': oth13,
        'oth14': oth14,
        'Club1': Club1,
        'Club2': Club2,
        'GymMem1': GymMem1,
        'GymMem2': GymMem2,
        'News1': News1,
        'News2': News2,
        'oth15': oth15,
        'oth16': oth16,
        'Dining1': Dining1,
        'Dining2': Dining2,
        'Outing1': Outing1,
        'Outing2': Outing2,
        'Hobby1': Hobby1,
        'Hobby2': Hobby2,
        'oth17': oth17,
        'oth18': oth18,
        'Clothes1': Clothes1,
        'Clothes2': Clothes2,
        'Travel1': Travel1,
        'Travel2': Travel2,
        'Gift1': Gift1,
        'Gift2': Gift2,
        'Give1': Give1,
        'Give2': Give2,
        'HomeImprov1': HomeImprov1,
        'HomeImprov2': HomeImprov2,
        'College1': College1,
        'College2': College2,
        'Wedding1': Wedding1,
        'Wedding2': Wedding2,
        'Car1Rep1': Car1Rep1,
        'Car1Rep2': Car1Rep2,
        'Car2Rep1': Car2Rep1,
        'Car2Rep2': Car2Rep2,
        'oth19': oth19,
        'oth20': oth20,
        'HS1': HS1,
        'HS2': HS2,
        'Pest1': Pest1,
        'Pest2': Pest2,
        'AutoR1': AutoR1,
        'AutoR2': AutoR2,
        'Vac1': Vac1,
        'Vac2': Vac2,
        'Misc1': Misc1,
        'Misc2': Misc2,
        'total1': total1,
        'total2': total2,
        'total3': total3,
        'total4': total4,
        'n2': n2
    }
    data_dict = {
        'note': note,
        'n1': n1,
        'name': name,
       'date': date,
       'email': email,
       'notes': notes,
       'pin': pin,
       'Retired': Retired,
       'Marriage': Marriage,
       'Div': Div,
       'SellBus': SellBus,
       'BirthC': BirthC,
       'RefBus': RefBus,
       'BirthGC': BirthGC,
       'FailBus': FailBus,
       'Remarry': Remarry,
       'JobLoss': JobLoss,
       'Reloc': Reloc,
       'College': College,
       'LastChild': LastChild,
       'MoveIn': MoveIn,
       'ChildMarry': ChildMarry,
       'DisabilityPar': DisabilityPar,
       'DisabilityAC': DisabilityAC,
       'ACDiv': ACDiv,
       'ACRemarry': ACRemarry,
       'PurHome': PurHome,
       'RelocPar': RelocPar,
       'DeathPar': DeathPar,
       'DeathChild': DeathChild,
       'DeathSpouse': DeathSpouse,
       'SellHome': SellHome,
       'SellProp': SellProp,
       'Legacy': Legacy,
       'BuyProp': BuyProp,
       'Inherit': Inherit,
       "NewEmp": NewEmp,
       'SpouseStart': SpouseStart,
       'SpouseStop': SpouseStop,
       'RelocJob': RelocJob,
       'StartBus': StartBus,
       'FTEstarts': test1,
       'FTEstart2': FTEstart2,
       'FTEends': FTEend1,
       'FTEend2': FTEend2,
       'FTEmonths': FTEmonth1,
       'FTEmonth2': FTEmonth2,
       'FTEbonus': FTEbonus1,
       'FTEbonus2': FTEbonus2,
       'PTEstarts': PTEstart1,
       'PTEstart2': PTEstart2,
       'PTEends': PTEend1,
       'PTEend2': PTEend2,
       'PTEmonths': PTEmonth1,
       'PTEmonth2': PTEmonth2,
       'PTEbonus': PTEbonus1,
       'PTEbonus2': PTEbonus2,
       'PENstarts': PENstart1,
       'PENstart2': PENstart2,
       'PENends': PENend1,
       'PENend2': PENend2,
       'PENmonths': PENmonth1,
       'PENmonth2': PENmonth2,
       'PENbonus': PENbonus1,
       'PENbonus2': PENbonus2,
       'SSstarts': SSstart1,
       'SSstart2': SSstart2,
       'SSends': SSend1,
       'SSend2': SSend2,
       'SSmonths': SSmonth1,
       'SSmonth2': SSmonth2,
       'SSbonus': SSbonus1,
       'SSbonus2': SSbonus2,
       'RIstarts': RIstart1,
       'RIstart2': RIstart2,
       'RIends': RIend1,
       'RIend2': RIend2,
       'RImonths': RImonth1,
       'RImonth2': RImonth2,
       'RIbonus': RIbonus1,
       'RIbonus2': RIbonus2,
       'EIstarts': EIstart1,
       'EIstart2': EIstart2,
       'EIends': EIend1,
       'EIend2': EIend2,
       'EImonths': EImonth1,
       'EImonth2': EImonth2,
       'EIbonus': EIbonus1,
       'EIbonus2': EIbonus2,
       'SBstarts': SBstart1,
       'SBstart2': SBstart2,
       'SBends': SBend1,
       'SBend2': SBend2,
       'SBmonths': SBmonth1,
       'SBmonth2': SBmonth2,
       'SBbonus': SBbonus1,
       'SBbonus2': SBbonus2,
       'SREstarts': SREstart1,
       'SREstart2': SREstart2,
       'SREends': SREend1,
       'SREend2': SREend2,
       'SREmonths': SREmonth1,
       'SREmonth2': SREmonth2,
       'SREbonus': SREbonus1,
       'SREbonus2': SREbonus2,
       'o1starts': o1start1,
       'o1start2': o1start2,
       'o1ends': o1end1,
       'o1end2': o1end2,
       'o1months': o1month1,
       'o1month2': o1month2,
       'o1bonus': o1bonus1,
       'o1bonus2': o1bonus2,
       'o2starts': o2start1,
       'o2start2': o2start2,
       'o2ends': o2end1,
       'o2end2': o2end2,
       'o2months': o2month1,
       'o2month2': o2month2,
       'o2bonus': o2bonus1,
       'o2bonus2': o2bonus2,
       'o3starts': o3start1,
       'o3start2': o3start2,
       'o3ends': o3end1,
       'o3end2': o3end2,
       'o3months': o3month1,
       'o3month2': o3month2,
       'o3bonus': o3bonus1,
       'o3bonus2': o3bonus2,
       'other11': other11,
       'other12': other12,
       'other21': other21,
       'other22': other22,
       'other31': other31,
       'other32': other32,
       'street1': street1,
       'city1': city1,
       'state1': state1,
       'zip1': zip1,
       'v1': value1,
       'IR1': IR1,
       'MP1': MP1,
       'CBL1': CBL1,
       'ARM1': ARM1,
       'street2': street2,
       'city2': city2,
       'state2': state2,
       'zip2': zip2,
       'v2': value2,
       'IR2': IR2,
       'MP2': MP2,
       'CBL2': CBL2,
       'ARM2': ARM2,
       'street3': street3,
       'city3': city3,
       'state3': state3,
       'zip3': zip3,
       'v3': value3,
       'IR3': IR3,
       'MP3': MP3,
       'CBL3': CBL3,
       'ARM3': ARM3,
       'HomeEQ': HomeEquity,
       'TL1': TypeLoan1,
       'LA1': LoanA1,
       'IRR1': LoanIR1,
       'MPP1': LoanMonthly1,
       'CL1': LoanCB1,
       'Pay1': LoanDate1,
       'TL2': TypeLoan2,
       'LA2': LoanA2,
       'IRR2': LoanIR2,
       'MPP2': LoanMonthly2,
       'CL2': LoanCB2,
       'Pay2': LoanDate2,
       'TL3': TypeLoan3,
       'LA3': LoanA3,
       'IRR3': LoanIR3,
       'MPP3': LoanMonthly3,
       'CL3': LoanCB3,
       'Pay3': LoanDate3,
       'ApproxM': ApproxMonth,
       'notes2': notes2,
       'Risk1': Risk1,
       'Risk2': Risk2,
       'Risk3': Risk3,
       'Risk4': Risk4,
       'RateR1': RateR1,
       'RateR2': RateR2,
       'RateR3': RateR3,
       'RateR4': RateR4,
       'raise1': raise1,
       'raise2': raise2,
       'raise3': raise3,
       'raise4': raise4,
       'dropF1': dropF1,
       'dropF2': dropF2,
       'dropF3': dropF3,
       'dropF4': dropF4,
       'drop1': drop1,
       'drop2': drop2,
       'drop3': drop3,
       'drop4': drop4,
       'vol1': vol1,
       'vol2': vol2,
       'vol3': vol3,
       'vol4': vol4,
       'Current1': Current1,
       'Current2': Current2,
       'Current3': Current3,
       'Current4': Current4,
       'decline1': decline1,
       'decline2': decline2,
       'decline3': decline3,
       'decline4': decline4,
       'in1': in1,
       'in2': in2,
       'in3': in3,
       'in4': in4,
       'fly1': fly1,
       'fly2': fly2,
       'fly3': fly3,
       'fly4': fly4,
       'exp1': exp1,
       'exp2': exp2,
       'exp3': exp3,
       'exp4': exp4,
       'outlook1': outlook1,
       'outlook2': outlook2,
       'outlook3': outlook3,
       'outlook4': outlook4,
       'withdraw1': withdraw1,
       'withdraw2': withdraw2,
       'withdraw3': withdraw3,
       'withdraw4': withdraw4,
       'Income14': Income14,
       'Growth14': Growth14,
       'NDY15': NDY15,
       'Market15': Market15,
       'cons16': cons16,
       'reward16': reward16,
       'notes3': notes3,
       'CopiesSS': CopiesSS,
       'CopiesCollege': CopiesCollege,
       'CopiesMort': CopiesMort,
       'Copies401k': Copies401k,
       'CopiesInvest': CopiesInvest,
       'CopiesInsurance': CopiesInsurance,
       'notes4': notes4
    }
    BASE = os.path.dirname(os.path.abspath(__file__))
    input = os.path.join(BASE, "template.pdf")
    output = os.path.join(BASE, "Financial Planning Worksheet.pdf")
    input2 = os.path.join(BASE, "template2.pdf")
    output2 = os.path.join(BASE, "Expenses Worksheet.pdf")
    f1 = open(settings.SAVES_DIRS + 'PDF '+ i1.name + i1.pin, 'wb')
    #f2 = open(settings.SAVES_DIRS + 'PDF '+ i1.name + i1.pin + '2', 'w')
    data = [i1,i2]
    pickle.dump(data, f1)
    #pickle.dump(i2, f2)
    f1.close()
    #f2.close()
    populate_template.sendEmail(input, output, data_dict, input2, output2, data_dict2)
    return render(request, "submit.html")

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        filename = myfile.name.split(".")
        name = request.POST.get("name", None)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        path = "/" + name + "/" + filename[0] + str(datetime.datetime.now()) + "." + filename[1]
        populate_template.upload(uploaded_file_url,path)
    return render(request, 'upload.html')
