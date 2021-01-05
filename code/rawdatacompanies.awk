#get relevent incorporation data for march-oct 2020 and march-oct 2019
#$24 is zipcode of ceo
#12 is zipcode of where it was incorporated
#I did this with both the CEO data and the filing zip code data but the CEO data had more accurate results because it fully matched the correct zipcode
BEGIN{
  FS= "\t"
  
  while ((getline <  "activecorpstxt.tsv") > 0){
      #if the company was encorporated in March-Oct 2020 print the zipcode of the ceo to one file and print the zipcode of the office the company was incorporated in in another file
      if (($1 ~/[0-9]{7}/) && ($3 ~/2020/) && ($3 ~/^(03|04|05|06|07|08|09|10)/) && ($24 ~ /[0-9]{5,}/)){	  
	  print $24 > "2020companiesCeoZip.txt"
	  
      }
      #if the company was encorporated in March-Oct 2019 print the zipcode of the ceo to one file and print the zipcode of the office the company was incorporated in in another file
      else if (($1 ~/[0-9]{7}/) && ($3 ~/2019/) && ($3 ~/^(03|04|05|06|07|08|09|10)/) && ($24 ~ /[0-9]{5,}/)){
	  print $24 > "2019companiesCeoZip.txt"
	  
      }      
      
}

}

	  
      
