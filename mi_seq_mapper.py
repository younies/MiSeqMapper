#!/usr/bin/python

mapper = {
	 "hydrophila": 1321367,
   "cereus" :  1441464,
  "fragilis" : 1422847,
   "abscessus" : 1335417,
   "fermentans" : 1149860,
   "sphaeroides" : 272943,
   "aureus" :  1675528 ,
   "pneumoniae" : 1449971,
   "cholerae" :  1420885,
   "axonopodis" : 1437877,
}



def getUID(dna):
	for ( key,  uid) in mapper.items():
		if( dna.find(key) > -1 ):
			return uid
		
	print "error"
	print dna
	return -1

Hi_file = open("HiSeq_accuracy.fa");

lines = Hi_file.read()
lines = lines.split("\n")

for line in lines:
	line = line.strip()


DNAS = []

for line 	in lines:
	if(not line):
		continue
	if(line[0] == '>'):
		DNAS.append(line)
	else:
		if(DNAS[-1][0] == '>'):
			DNAS.append(line)
		else:
			DNAS[-1] += line



for i in range(len(DNAS)):
	if(DNAS[i][0] == '>'):
		DNAS[i] = getUID(DNAS[i])


write_Hi = open("/Users/youniesmahmoud/Desktop/hi2.txt" , 'w')


for DNA in DNAS:
	write_Hi.write(str(DNA))
	write_Hi.write('\n')
