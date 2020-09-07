#Imports
import numpy as np
import scipy
import csv
from random import randint
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn import linear_model
from sklearn.neighbors import KNeighborsRegressor


#Loading and parsing data
with open("MedEthics_Data No13-16.txt", encoding = "utf8", errors = "ignore") as tsvfile:
    #Binary State Variables
    AlabamaTrain = []
    AlabamaTest = []
    ArizonaTrain = []
    ArizonaTest = []
    CaliforniaTrain = []
    CaliforniaTest = []
    ColoradoTrain = []
    ColoradoTest = []
    FloridaTrain = []
    FloridaTest = []
    GeorgiaTrain = []
    GeorgiaTest = []
    IdahoTrain = []
    IdahoTest = []
    IllinoisTrain = []
    IllinoisTest = []
    IndianaTrain = []
    IndianaTest = []
    IowaTrain = []
    IowaTest = []
    KansasTrain = []
    KansasTest = []
    LouisianaTrain = []
    LouisianaTest = []
    MaineTrain = []
    MaineTest = []
    MarylandTrain = []
    MarylandTest = []
    MassachusettsTrain = []
    MassachusettsTest = []
    MichiganTrain = []
    MichiganTest = []
    MinnesotaTrain = []
    MinnesotaTest = []
    MississippiTrain = []
    MississippiTest = []
    MissouriTrain = []
    MissouriTest = []
    MontanaTrain = []
    MontanaTest = []
    NebraskaTrain = []
    NebraskaTest = []
    NevadaTrain = []
    NevadaTest = []
    NewHampshireTrain = []
    NewHampshireTest = []
    NewJerseyTrain = []
    NewJerseyTest = []
    NewMexicoTrain = []
    NewMexicoTest = []
    NewYorkTrain = []
    NewYorkTest = []
    NorthCarolinaTrain = []
    NorthCarolinaTest = []
    NorthDakotaTrain = []
    NorthDakotaTest = []
    OhioTrain = []
    OhioTest = []
    OklahomaTrain = []
    OklahomaTest = []
    OregonTrain = []
    OregonTest = []
    PennsylvaniaTrain = []
    PennsylvaniaTest = []
    RhodeIslandTrain = []
    RhodeIslandTest = []
    SouthDakotaTrain = []
    SouthDakotaTest = []
    TennesseeTrain = []
    TennesseeTest = []
    UtahTrain = []
    UtahTest = []
    VermontTrain = []
    VermontTest = []
    VirginiaTrain = []
    VirginiaTest = []
    WashingtonTrain = []
    WashingtonTest = []
    WestVirginiaTrain = []
    WestVirginiaTest = []
    WisconsinTrain = []
    WisconsinTest = []
    WyomingTrain = []
    WyomingTest = []
    #Other Variables
    TempTrain = []
    TempTest = []
    IncomeTrain = []
    IncomeTest = []
    UninsuredTrain = []
    UninsuredTest = []
    RatioTrain = []
    RatioTest = []
    CollegeTrain = []
    CollegeTest = []
    DensityTrain = []
    DensityTest = []
    GoogleTrain = []
    GoogleTest = []
    #Response Variable
    ChlamydiaTrain = []
    ChlamydiaTest = []
    reader = csv.DictReader(tsvfile, dialect='excel-tab')
    counter = 1
    for row in reader:
        x = randint(1,5)
        if counter > 348:
            pass
        else: 
            if x % 5 != 0:
                ChlamydiaTrain.append(row["Chlamydia Cases/100k"])
                IncomeTrain.append(row["2017 Median Household Income"])
                TempTrain.append(row["Mean Temp (Monthly Average)"])
                UninsuredTrain.append(row["Uninsured %"])
                RatioTrain.append(row["Pop: Primary Care Physician Ratio"])
                CollegeTrain.append(row["% Some College"])
                DensityTrain.append(row["Population Density"])
                GoogleTrain.append(row["Google Searches (7 day avg)"])
                AlabamaTrain.append(row["Alabama"])
                ArizonaTrain.append(row["Arizona"])
                CaliforniaTrain.append(row["California"])
                ColoradoTrain.append(row["Colorado"])
                FloridaTrain.append(row["Florida"])
                GeorgiaTrain.append(row["Georgia"])
                IdahoTrain.append(row["Idaho"])
                IllinoisTrain.append(row["Illinois"])
                IndianaTrain.append(row["Indiana"])
                IowaTrain.append(row["Iowa"])
                KansasTrain.append(row["Kansas"])
                LouisianaTrain.append(row["Louisiana"])
                MaineTrain.append(row["Maine"])
                MarylandTrain.append(row["Maryland"])
                MassachusettsTrain.append(row["Massachusetts"])
                MichiganTrain.append(row["Michigan"])
                MinnesotaTrain.append(row["Minnesota"])
                MississippiTrain.append(row["Mississippi"])
                MissouriTrain.append(row["Missouri"])
                MontanaTrain.append(row["Montana"])
                NebraskaTrain.append(row["Nebraska"])
                NevadaTrain.append(row["Nevada"])
                NewHampshireTrain.append(row["New Hampshire"])
                NewJerseyTrain.append(row["New Jersey"])
                NewMexicoTrain.append(row["New Mexico"])
                NewYorkTrain.append(row["New York"])
                NorthCarolinaTrain.append(row["North Carolina"])
                NorthDakotaTrain.append(row["North Dakota"])
                OhioTrain.append(row["Ohio"])
                OklahomaTrain.append(row["Oklahoma"])
                OregonTrain.append(row["Oregon"])
                PennsylvaniaTrain.append(row["Pennsylvania"])
                RhodeIslandTrain.append(row["Rhode Island"])
                SouthDakotaTrain.append(row["South Dakota"])
                TennesseeTrain.append(row["Tennessee"])
                UtahTrain.append(row["Utah"])
                VermontTrain.append(row["Vermont"])
                VirginiaTrain.append(row["Virginia"])
                WashingtonTrain.append(row["Washington"])
                WestVirginiaTrain.append(row["West Virginia"])
                WisconsinTrain.append(row["Wisconsin"])
                WyomingTrain.append(row["Wyoming"])
                counter += 1
            else:
                ChlamydiaTest.append(row["Chlamydia Cases/100k"])
                IncomeTest.append(row["2017 Median Household Income"])
                TempTest.append(row["Mean Temp (Monthly Average)"])
                UninsuredTest.append(row["Uninsured %"])
                RatioTest.append(row["Pop: Primary Care Physician Ratio"])
                CollegeTest.append(row["% Some College"])
                DensityTest.append(row["Population Density"])
                GoogleTest.append(row["Google Searches (7 day avg)"])
                AlabamaTest.append(row["Alabama"])
                ArizonaTest.append(row["Arizona"])
                CaliforniaTest.append(row["California"])
                ColoradoTest.append(row["Colorado"])
                FloridaTest.append(row["Florida"])
                GeorgiaTest.append(row["Georgia"])
                IdahoTest.append(row["Idaho"])
                IllinoisTest.append(row["Illinois"])
                IndianaTest.append(row["Indiana"])
                IowaTest.append(row["Iowa"])
                KansasTest.append(row["Kansas"])
                LouisianaTest.append(row["Louisiana"])
                MaineTest.append(row["Maine"])
                MarylandTest.append(row["Maryland"])
                MassachusettsTest.append(row["Massachusetts"])
                MichiganTest.append(row["Michigan"])
                MinnesotaTest.append(row["Minnesota"])
                MississippiTest.append(row["Mississippi"])
                MissouriTest.append(row["Missouri"])
                MontanaTest.append(row["Montana"])
                NebraskaTest.append(row["Nebraska"])
                NevadaTest.append(row["Nevada"])
                NewHampshireTest.append(row["New Hampshire"])
                NewJerseyTest.append(row["New Jersey"])
                NewMexicoTest.append(row["New Mexico"])
                NewYorkTest.append(row["New York"])
                NorthCarolinaTest.append(row["North Carolina"])
                NorthDakotaTest.append(row["North Dakota"])
                OhioTest.append(row["Ohio"])
                OklahomaTest.append(row["Oklahoma"])
                OregonTest.append(row["Oregon"])
                PennsylvaniaTest.append(row["Pennsylvania"])
                RhodeIslandTest.append(row["Rhode Island"])
                SouthDakotaTest.append(row["South Dakota"])
                TennesseeTest.append(row["Tennessee"])
                UtahTest.append(row["Utah"])
                VermontTest.append(row["Vermont"])
                VirginiaTest.append(row["Virginia"])
                WashingtonTest.append(row["Washington"])
                WestVirginiaTest.append(row["West Virginia"])
                WisconsinTest.append(row["Wisconsin"])
                WyomingTest.append(row["Wyoming"])
                counter += 1

#Building Combined Training Array (turning lists to arrays)
CombinedTrainArray = []

ChlamydiaTrainArray = np.asarray(ChlamydiaTrain).astype(float)

IncomeTrainArray = np.asarray(IncomeTrain).astype(float)
TempTrainArray = np.asarray(TempTrain).astype(float)
UninsuredTrainArray = np.asarray(UninsuredTrain).astype(float)
RatioTrainArray = np.asarray(RatioTrain).astype(float)
CollegeTrainArray = np.asarray(CollegeTrain).astype(float)
DensityTrainArray = np.asarray(DensityTrain).astype(float)
GoogleTrainArray = np.asarray(GoogleTrain).astype(float)
AlabamaTrainArray = np.asarray(ArizonaTrain).astype(int)
ArizonaTrainArray = np.asarray(ArizonaTrain).astype(int)
CaliforniaTrainArray = np.asarray(CaliforniaTrain).astype(int)
ColoradoTrainArray = np.asarray(ColoradoTrain).astype(int)
FloridaTrainArray = np.asarray(FloridaTrain).astype(int)
GeorgiaTrainArray = np.asarray(GeorgiaTrain).astype(int)
IdahoTrainArray = np.asarray(IdahoTrain).astype(int)
IllinoisTrainArray = np.asarray(IllinoisTrain).astype(int)
IndianaTrainArray = np.asarray(IndianaTrain).astype(int)
IowaTrainArray = np.asarray(IowaTrain).astype(int)
KansasTrainArray = np.asarray(KansasTrain).astype(int)
LouisianaTrainArray = np.asarray(LouisianaTrain).astype(int)
MaineTrainArray = np.asarray(MaineTrain).astype(int)
MarylandTrainArray = np.asarray(MarylandTrain).astype(int)
MassachusettsTrainArray = np.asarray(MassachusettsTrain).astype(int)
MichiganTrainArray = np.asarray(MichiganTrain).astype(int)
MinnesotaTrainArray = np.asarray(MinnesotaTrain).astype(int)
MississippiTrainArray = np.asarray(MississippiTrain).astype(int)
MissouriTrainArray = np.asarray(MissouriTrain).astype(int)
MontanaTrainArray = np.asarray(MontanaTrain).astype(int)
NebraskaTrainArray = np.asarray(NebraskaTrain).astype(int)
NevadaTrainArray = np.asarray(NevadaTrain).astype(int)
NewHampshireTrainArray = np.asarray(NewHampshireTrain).astype(int)
NewJerseyTrainArray = np.asarray(NewJerseyTrain).astype(int)
NewMexicoTrainArray = np.asarray(NewMexicoTrain).astype(int)
NewYorkTrainArray = np.asarray(NewYorkTrain).astype(int)
NorthCarolinaTrainArray = np.asarray(NorthCarolinaTrain).astype(int)
NorthDakotaTrainArray = np.asarray(NorthDakotaTrain).astype(int)
OhioTrainArray = np.asarray(OhioTrain).astype(int)
OklahomaTrainArray = np.asarray(OklahomaTrain).astype(int)
OregonTrainArray = np.asarray(OregonTrain).astype(int)
PennsylvaniaTrainArray = np.asarray(PennsylvaniaTrain).astype(int)
RhodeIslandTrainArray = np.asarray(RhodeIslandTrain).astype(int)
SouthDakotaTrainArray = np.asarray(SouthDakotaTrain).astype(int)
TennesseeTrainArray = np.asarray(TennesseeTrain).astype(int)
UtahTrainArray = np.asarray(UtahTrain).astype(int)
VermontTrainArray = np.asarray(UtahTrain).astype(int)
VirginiaTrainArray = np.asarray(VirginiaTrain).astype(int)
WashingtonTrainArray = np.asarray(WashingtonTrain).astype(int)
WestVirginiaTrainArray = np.asarray(WestVirginiaTrain).astype(int)
WisconsinTrainArray = np.asarray(WisconsinTrain).astype(int)
WyomingTrainArray = np.asarray(WyomingTrain).astype(int)

#Actually Building Combined Train Array
counter2 = 0
for row in IncomeTrainArray:
    if counter2 > len(IncomeTrainArray):
        pass
    else:
        CombinedTrainArray.append([IncomeTrainArray[counter2],
                                   TempTrainArray[counter2],
                                   UninsuredTrainArray[counter2],
                                   RatioTrainArray[counter2],
                                   CollegeTrainArray[counter2],
                                   DensityTrainArray[counter2],
                                   GoogleTrainArray[counter2],
                                   AlabamaTrainArray[counter2],
                                   ArizonaTrainArray[counter2],
                                   CaliforniaTrainArray[counter2],
                                   ColoradoTrainArray[counter2],
                                   FloridaTrainArray[counter2],
                                   GeorgiaTrainArray[counter2],
                                   IdahoTrainArray[counter2],
                                   IllinoisTrainArray[counter2],
                                   IndianaTrainArray[counter2],
                                   IowaTrainArray[counter2],
                                   KansasTrainArray[counter2],
                                   LouisianaTrainArray[counter2],
                                   MaineTrainArray[counter2],
                                   MarylandTrainArray[counter2],
                                   MassachusettsTrainArray[counter2],
                                   MichiganTrainArray[counter2],
                                   MinnesotaTrainArray[counter2],
                                   MississippiTrainArray[counter2],
                                   MissouriTrainArray[counter2],
                                   MontanaTrainArray[counter2],
                                   NebraskaTrainArray[counter2],
                                   NevadaTrainArray[counter2],
                                   NewHampshireTrainArray[counter2],
                                   NewJerseyTrainArray[counter2],
                                   NewMexicoTrainArray[counter2],
                                   NewYorkTrainArray[counter2],
                                   NorthCarolinaTrainArray[counter2],
                                   NorthDakotaTrainArray[counter2],
                                   OhioTrainArray[counter2],
                                   OklahomaTrainArray[counter2],
                                   OregonTrainArray[counter2],
                                   PennsylvaniaTrainArray[counter2],
                                   RhodeIslandTrainArray[counter2],
                                   SouthDakotaTrainArray[counter2],
                                   TennesseeTrainArray[counter2],
                                   UtahTrainArray[counter2],
                                   VermontTrainArray[counter2],
                                   VirginiaTrainArray[counter2],
                                   WashingtonTrainArray[counter2],
                                   WestVirginiaTrainArray[counter2],
                                   WisconsinTrainArray[counter2],
                                   WyomingTrainArray[counter2]
                           ])
        counter2 += 1
    
ChlamydiaTrainArray = ChlamydiaTrainArray.reshape(-1,1)

#Building Chlamydia Testing and Combined Array (basically just copy above)
CombinedTestArray = []

ChlamydiaTestArray = np.asarray(ChlamydiaTest).astype(float)

IncomeTestArray = np.asarray(IncomeTest).astype(float)
TempTestArray = np.asarray(TempTest).astype(float)
UninsuredTestArray = np.asarray(UninsuredTest).astype(float)
RatioTestArray = np.asarray(RatioTest).astype(float)
CollegeTestArray = np.asarray(CollegeTest).astype(float)
DensityTestArray = np.asarray(DensityTest).astype(float)
GoogleTestArray = np.asarray(GoogleTest).astype(float)
AlabamaTestArray = np.asarray(ArizonaTest).astype(int)
ArizonaTestArray = np.asarray(ArizonaTest).astype(int)
CaliforniaTestArray = np.asarray(CaliforniaTest).astype(int)
ColoradoTestArray = np.asarray(ColoradoTest).astype(int)
FloridaTestArray = np.asarray(FloridaTest).astype(int)
GeorgiaTestArray = np.asarray(GeorgiaTest).astype(int)
IdahoTestArray = np.asarray(IdahoTest).astype(int)
IllinoisTestArray = np.asarray(IllinoisTest).astype(int)
IndianaTestArray = np.asarray(IndianaTest).astype(int)
IowaTestArray = np.asarray(IowaTest).astype(int)
KansasTestArray = np.asarray(KansasTest).astype(int)
LouisianaTestArray = np.asarray(LouisianaTest).astype(int)
MaineTestArray = np.asarray(MaineTest).astype(int)
MarylandTestArray = np.asarray(MarylandTest).astype(int)
MassachusettsTestArray = np.asarray(MassachusettsTest).astype(int)
MichiganTestArray = np.asarray(MichiganTest).astype(int)
MinnesotaTestArray = np.asarray(MinnesotaTest).astype(int)
MississippiTestArray = np.asarray(MississippiTest).astype(int)
MissouriTestArray = np.asarray(MissouriTest).astype(int)
MontanaTestArray = np.asarray(MontanaTest).astype(int)
NebraskaTestArray = np.asarray(NebraskaTest).astype(int)
NevadaTestArray = np.asarray(NevadaTest).astype(int)
NewHampshireTestArray = np.asarray(NewHampshireTest).astype(int)
NewJerseyTestArray = np.asarray(NewJerseyTest).astype(int)
NewMexicoTestArray = np.asarray(NewMexicoTest).astype(int)
NewYorkTestArray = np.asarray(NewYorkTest).astype(int)
NorthCarolinaTestArray = np.asarray(NorthCarolinaTest).astype(int)
NorthDakotaTestArray = np.asarray(NorthDakotaTest).astype(int)
OhioTestArray = np.asarray(OhioTest).astype(int)
OklahomaTestArray = np.asarray(OklahomaTest).astype(int)
OregonTestArray = np.asarray(OregonTest).astype(int)
PennsylvaniaTestArray = np.asarray(PennsylvaniaTest).astype(int)
RhodeIslandTestArray = np.asarray(RhodeIslandTest).astype(int)
SouthDakotaTestArray = np.asarray(SouthDakotaTest).astype(int)
TennesseeTestArray = np.asarray(TennesseeTest).astype(int)
UtahTestArray = np.asarray(UtahTest).astype(int)
VermontTestArray = np.asarray(UtahTest).astype(int)
VirginiaTestArray = np.asarray(VirginiaTest).astype(int)
WashingtonTestArray = np.asarray(WashingtonTest).astype(int)
WestVirginiaTestArray = np.asarray(WestVirginiaTest).astype(int)
WisconsinTestArray = np.asarray(WisconsinTest).astype(int)
WyomingTestArray = np.asarray(WyomingTest).astype(int)

#Actually Building Combined Test Array
counter3 = 0
for row in IncomeTestArray:
    if counter3 > len(IncomeTestArray):
        pass
    else:
        CombinedTestArray.append([IncomeTestArray[counter3],
                                   TempTestArray[counter3],
                                   UninsuredTestArray[counter3],
                                   RatioTestArray[counter3],
                                   CollegeTestArray[counter3],
                                   DensityTestArray[counter3],
                                   GoogleTestArray[counter3],
                                   AlabamaTestArray[counter3],
                                   ArizonaTestArray[counter3],
                                   CaliforniaTestArray[counter3],
                                   ColoradoTestArray[counter3],
                                   FloridaTestArray[counter3],
                                   GeorgiaTestArray[counter3],
                                   IdahoTestArray[counter3],
                                   IllinoisTestArray[counter3],
                                   IndianaTestArray[counter3],
                                   IowaTestArray[counter3],
                                   KansasTestArray[counter3],
                                   LouisianaTestArray[counter3],
                                   MaineTestArray[counter3],
                                   MarylandTestArray[counter3],
                                   MassachusettsTestArray[counter3],
                                   MichiganTestArray[counter3],
                                   MinnesotaTestArray[counter3],
                                   MississippiTestArray[counter3],
                                   MissouriTestArray[counter3],
                                   MontanaTestArray[counter3],
                                   NebraskaTestArray[counter3],
                                   NevadaTestArray[counter3],
                                   NewHampshireTestArray[counter3],
                                   NewJerseyTestArray[counter3],
                                   NewMexicoTestArray[counter3],
                                   NewYorkTestArray[counter3],
                                   NorthCarolinaTestArray[counter3],
                                   NorthDakotaTestArray[counter3],
                                   OhioTestArray[counter3],
                                   OklahomaTestArray[counter3],
                                   OregonTestArray[counter3],
                                   PennsylvaniaTestArray[counter3],
                                   RhodeIslandTestArray[counter3],
                                   SouthDakotaTestArray[counter3],
                                   TennesseeTestArray[counter3],
                                   UtahTestArray[counter3],
                                   VermontTestArray[counter3],
                                   VirginiaTestArray[counter3],
                                   WashingtonTestArray[counter3],
                                   WestVirginiaTestArray[counter3],
                                   WisconsinTestArray[counter3],
                                   WyomingTestArray[counter3]
                           ])
        counter3 += 1
    
ChlamydiaTestArray = ChlamydiaTestArray.reshape(-1,1)

"""
__________________________________________________________________________________________
"""

#KNN regression
neigh = KNeighborsRegressor(n_neighbors=5)
neigh.fit(CombinedTrainArray, ChlamydiaTrainArray)
KNNpred = neigh.predict(CombinedTestArray)

#Determining % error of KNN function
Errors = []
counter4 = 0
for x in KNNpred:
    Error = abs(x-ChlamydiaTestArray[counter4])/ChlamydiaTestArray[counter4]*100
    Errors.append(Error)
    counter4 += 1

print("KNN Mean % Error with Outliers is: ")
print(sum(Errors)/len(Errors))

#Removing Outliers (<LQ-1.5IQR or >UQ+1.5IQR), Determining % Error
Second = np.percentile(Errors,25)
Fourth = np.percentile(Errors,75)
IQR = Fourth-Second
Errors_No_Outliers = []
for x in Errors:
    if x <Second-1.5*IQR or x > Fourth+1.5*IQR:
        pass
    else:
        Errors_No_Outliers.append(x)

print("KNN Mean % Error without Outliers is: ")
print(sum(Errors_No_Outliers)/len(Errors_No_Outliers))

#Determining KNN Rsquared
print("KNN R Squared is: ")
print(neigh.score(CombinedTestArray, ChlamydiaTestArray))
print("")

"""
__________________________________________________________________________________________
"""


#SVM regression... oof this is terrible
svm = SVR()
svm.fit(CombinedTrainArray,ChlamydiaTrainArray.ravel())
SVMpred = svm.predict(CombinedTestArray)

#Determining % error of SVM function
Errors2 = []
counter5 = 0
for x in SVMpred:
    Error = abs(x-ChlamydiaTestArray[counter5])/ChlamydiaTestArray[counter5]*100
    Errors2.append(Error)
    counter5 += 1

print("SVM Mean % Error with Outliers is: ")
print(sum(Errors2)/len(Errors2))

#Removing Outliers (<LQ-1.5IQR or >UQ+1.5IQR), Determining % Error
Second2 = np.percentile(Errors2,25)
Fourth2 = np.percentile(Errors2,75)
IQR2 = Fourth2-Second2
Errors_No_Outliers2 = []
for x in Errors2:
    if x <Second2-1.5*IQR2 or x > Fourth2+1.5*IQR2:
        pass
    else:
        Errors_No_Outliers2.append(x)

print("SVM Mean % Error without Outliers is: ")
print(sum(Errors_No_Outliers2)/len(Errors_No_Outliers2))

#Determining SVM Rsquared
print("SVM R Squared is: ")
print(svm.score(CombinedTestArray, ChlamydiaTestArray))
print("")

"""
__________________________________________________________________________________________
"""

#Decision Tree regression
tree = DecisionTreeRegressor()
tree.fit(CombinedTrainArray,ChlamydiaTrainArray.ravel())
Treepred = tree.predict(CombinedTestArray)

#Determining % error of Tree function
Errors3 = []
counter6 = 0
for x in Treepred:
    Error = abs(x-ChlamydiaTestArray[counter6])/ChlamydiaTestArray[counter6]*100
    Errors3.append(Error)
    counter6 += 1

print("Tree Mean % Error with Outliers is: ")
print(sum(Errors3)/len(Errors3))

#Removing Outliers (<LQ-1.5IQR or >UQ+1.5IQR), Determining % Error
Second3 = np.percentile(Errors3,25)
Fourth3 = np.percentile(Errors3,75)
IQR3 = Fourth3-Second3
Errors_No_Outliers3 = []
for x in Errors3:
    if x <Second3-1.5*IQR3 or x > Fourth3+1.5*IQR3:
        pass
    else:
        Errors_No_Outliers3.append(x)

print("Tree Mean % Error without Outliers is: ")
print(sum(Errors_No_Outliers3)/len(Errors_No_Outliers3))

#Determining Tree Rsquared
print("Tree R Squared is: ")
print(tree.score(CombinedTestArray, ChlamydiaTestArray))
print("")




