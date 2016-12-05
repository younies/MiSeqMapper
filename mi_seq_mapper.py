#!/usr/bin/python

mapper = {
	"cereus" : 1053231,
	"freundii" : 1173724,
	"cloacae": 1870957,
	"pneumoniae" : 1455604,
	"abscessus" :1001740,
	"vulgaris" :1173773,
	"sphaeroides" : 272943,
	"aureus" :1075083,
	"enterica": 1868170,
	"cholerae" : 991923,
}



def getUID(dna):
	for ( key,  uid) in mapper.items():
		if( dna.find(key) > -1 ):
			return uid
		
	print "error"
	print dna
	return -1

Hi_file = open("/Users/youniesmahmoud/Desktop/test_kraken/accuracy/MiSeq_accuracy.fa");

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


write_Hi = open("/Users/youniesmahmoud/Desktop/mi2.txt" , 'w')


for DNA in DNAS:
	write_Hi.write(str(DNA))
	write_Hi.write('\n')
