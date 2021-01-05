all: graph.pdf

clean:
	rm 2020companiesCeoZip.txt 2019companiesCeoZip.txt incomeBracketOne.txt incomeBracketTwo.txt incomeBracketThree.txt incomeBracketFour.txt incomeBracketFive.txt incomeBracketSix.txt incomeBracketSeven.txt noMatchZips.txt NumberZipsPerBracket2019.txt NumberZipsPerBracket2020.txt random.txt graph.pdf
#file with zipcodes of ceos of companies founded in 2020
2020companiesCeoZip.txt: activecorpstxt.tsv rawdatacompanies.awk
	gawk -f rawdatacompanies.awk
#same as above, for 2019
2019companiesCeoZip.txt: activecorpstxt.tsv rawdatacompanies.awk
	gawk -f rawdatacompanies.awk
#following files include all the zipcodes for the seven income brackets (from IRS data)
incomeBracketOne.txt: zipIncome.gz getzipcodes.awk
	gawk -f getzipcodes.awk
incomeBracketTwo.txt: zipIncome.gz getzipcodes.awk
	gawk -f getzipcodes.awk
incomeBracketThree.txt: zipIncome.gz getzipcodes.awk
	gawk -f getzipcodes.awk
incomeBracketFour.txt: zipIncome.gz getzipcodes.awk
	gawk -f getzipcodes.awk
incomeBracketFive.txt: zipIncome.gz getzipcodes.awk
	gawk -f getzipcodes.awk
incomeBracketSix.txt: zipIncome.gz getzipcodes.awk
	gawk -f getzipcodes.awk
incomeBracketSeven.txt: zipIncome.gz getzipcodes.awk
	gawk -f getzipcodes.awk
random.txt: zipIncome.gz getzipcodes.awk
	gawk -f getzipcodes.awk
#zipcodes from incorporated data that cant be found in any of the income bracket
noMatchZips.txt: 2020companiesCeoZip.txt 2019companiesCeoZip.txt incomeBracketOne.txt incomeBracketTwo.txt incomeBracketThree.txt incomeBracketFour.txt incomeBracketFive.txt incomeBracketSix.txt incomeBracketSeven.txt splitData.py
	python3 ./splitData.py
#the total number of zipcodes per income bracket from 2019 companies
NumberZipsPerBracket2019.txt: 2020companiesCeoZip.txt 2019companiesCeoZip.txt incomeBracketOne.txt incomeBracketTwo.txt incomeBracketThree.txt incomeBracketFour.txt incomeBracketFive.txt incomeBracketSix.txt incomeBracketSeven.txt splitData.py
	python3 ./splitData.py
#same for 2020
NumberZipsPerBracket2020.txt: 2020companiesCeoZip.txt 2019companiesCeoZip.txt incomeBracketOne.txt incomeBracketTwo.txt incomeBracketThree.txt incomeBracketFour.txt incomeBracketFive.txt incomeBracketSix.txt incomeBracketSeven.txt splitData.py
	python3 ./splitData.py
#graph indicating results
graph.pdf: NumberZipsPerBracket2019.txt NumberZipsPerBracket2020.txt matplot.py
	python3 ./matplot.py


