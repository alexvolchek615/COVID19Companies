
incomeBracketFiles = ["incomeBracketOne.txt", "incomeBracketTwo.txt", "incomeBracketThree.txt", "incomeBracketFour.txt", "incomeBracketFive.txt","incomeBracketSix.txt", "incomeBracketSeven.txt"]
#create dictionary (hashmap) with zipcode: incomebracket
zipToIncomeBracket = {}
bracketIndex = 0
for incomeFile in incomeBracketFiles:
    bracketFile = open(incomeFile)
    for zipCode in bracketFile:
        zipToIncomeBracket[zipCode.strip()] = bracketIndex
    bracketIndex += 1

#find zipcode of ceo in the dictionary (using key) to then match to income bracket
CeoZipCodes2019 = open("2019companiesCeoZip.txt")
count2019 = [0] * 7
#zipcodes that dont match any income bracket (not in IRS data)
f= open("noMatchZips.txt", "w")
final2019= open("NumberZipsPerBracket2019.txt", "w")
final2020= open("NumberZipsPerBracket2020.txt", "w")
#print(count2019)
for ceoZipCode in CeoZipCodes2019:
    if ceoZipCode[:5].strip() in zipToIncomeBracket:
        count2019[zipToIncomeBracket[ceoZipCode[:5].strip()]] += 1
    else:
        print(ceoZipCode, file= f)
#same thing for 2020 zipcodes
CeoZipCodes2020 = open("2020companiesCeoZip.txt")
count2020 = [0] * 7
for ceoZipCode in CeoZipCodes2020:
    if ceoZipCode[:5].strip() in zipToIncomeBracket:
        count2020[zipToIncomeBracket[ceoZipCode[:5].strip()]] += 1
    else:
        print(ceoZipCode, file= f)
for item in count2019:
    print(item, file=final2019)
for item in count2020:
    print(item, file=final2020)
#print(count2019, file= final2019)
#print(count2020, file= final2020)
#print(count2019)
#print(count2020)
