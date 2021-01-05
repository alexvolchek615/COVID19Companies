#middle class income in nyc is 55138-165413
#(zipIncome.gz: f 1: zipcode f 3: average income)
#seven different files
#0-14100
#14101-53700
#53701-85500
#85501-163300
#163301-207350
#207351-518400
#518401+

BEGIN{
path= "zipIncome"
command= "zcat " path ".gz"
#the file has zip codes for all of the USA but it doesnt matter bc only the zip codes matching the NY incorporation data (CEO zipcode) will be used
    
    FS="|"
    #if average income in certain zipcode is X then put in file based on income bracket
    while ((command | getline) > 0){
	if (($3 >= 0) && ($3 <= 14100)){
	    print $1 > "incomeBracketOne.txt"
	    
	}
	else if (($3 >= 14101) && ($3 <= 53700)){
	    print $1 > "incomeBracketTwo.txt"
	    
	}
	else if (($3 >= 53701) && ($3 <= 85500)){
	    print $1 > "incomeBracketThree.txt"
	}
	else if (($3 >= 85501) && ($3 <= 163300)){
	    print $1 > "incomeBracketFour.txt"
	}
	else if (($3 >= 163301) && ($3 <= 207350)){
	    print $1 > "incomeBracketFive.txt"
	}
	else if (($3 >= 207351) && ($3 <= 518400)){
	    print $1 > "incomeBracketSix.txt"
	}
	else if ($3 >= 518401){
	    print $1 > "incomeBracketSeven.txt"
	}
	#weird zipcodes not in IRS data 
	else{
	    print $1 > "random.txt"
	}
    }
}
	    
		
