'''
Write a function that reads a pssm file and extracts either the Position Specific Scoring Matrix or the Sequence Profile. The function should then return a list of dictionaries such that for each position of the sequence you have a value corresponding to each residue type.

Parameters:
- fn		: string containing the name of the pssm file
- choice	: integer, either 0 or 1. If 0 you need to extract the pssm, if 1 you need to extract the profile
			(we assume that choice will always have a valid value when the function is called)

Returns:
- extracted	: list containing one dictionary for each position in the sequence. Each dictionary should have a pair key:value for each of the 20 residue types
			(mind that the order in wich the values corresponding to the residues are listed is specified in the third line of the file and that it may differ for each file)
'''
#reg 1h35

def extract_pssm(fn,modality):
	extracted=[]
	reader=open(fn,'r')
	reader.readline()
	reader.readline()
	line=reader.readline().strip().split()
	order=line[:20] #stores the order of the residues
	
	for line in reader:
		line=line.strip()
		if line=='': #if line is empty
			break
		line=line.split()
		position={} #dic where we are going to store everything
		if modality == 'pssm':
			line=line[2:22]
		else:
			line=line[22:42]
		#input(line)
		for res,value in zip(order,line):
			position[res]=int(value)
		extracted.append(position)
	
	
	return extracted

# extract_pssm('5ex1_A.pssm','profile')
# extract_pssm('5ex1_A.pssm','profile')
	
pssm=extract_pssm('5ex1_A.pssm','pssm')
profile = extract_pssm('5ex1_A.pssm','profile')
print(pssm[11]['A'] , profile[11]['A'])

'''
Write a function that extracts a profile from a pssm file and reads from a dssp file of the same protein chain. The function should then return a single number, obtained by summing for each position in the sequence the solvent accessibility multiplied by the frequency in the profile of the observed residue. Your function should call the one you defined in the previous exercise.

Parameters:
- pdb_id	: string containing the pdb id we want to read
- chain		: string containing the name of the chain to extract
			(we assume that in the same directory of the script there are two files called "<pdb_id>_<chain>.pssm" and "<pdb_id>.dssp"

Returns:
- value		: floating point value defined like above
			(mind that the values you read in the profile are percentages. For this exercise you should also ignore the difference made by dssp between lowercase and capital letters.)
'''

# def exercise(pdb_id, chain):
	# return 0.0

# print(exercise('5ex1','A'))
