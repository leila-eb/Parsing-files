'''
Write a function that reads a pdb file, extracts a selected chain and produces in output a fasta file with the extracted sequence.
The name of the output file should be "pdb_id.fasta" and the file should have exactly two lines: the first with the character '>' followed by the id (without spaces); the second with the whole sequence in one line.

Parameters:
- pdb_id	: string containing the pdb id we want to read
- chain		: string containing the name of the chain to extract
			(we assume that a file called "pdb_id.pdb" exists in the same dir as the program and that it has a chain with the specified name)

Returns:
- None

Bonus - Take in input two additional optional parameters:
- pdb_dir	: string containing a path to a directory where the pdb files are stored
- out_dir	: string containing a path to a directory where we want to store the output fasta files

Optional parameters are parameters with a default value in the function definition. That means that the user can call the function without specifying a value for those parameter, or they can explicitly assign it if they want to change it.
e.g.:	def f(a,b,c=0)
		f(3,4)		-> f will be called with a=3, b=4, c=0
		f(1,2,c=3)	-> f will be called with a=1, b=2, c=3
'''
def extract_chain(pdb_id, chain, pdb_dir='', out_dir=''):
	translate = {	'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C',
					'GLU':'E','GLN':'Q','GLY':'G','HIS':'H','ILE':'I',
					'LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P',
					'SER':'S','THR':'T','TRP':'W','TYR':'Y','VAL':'V'}
					
	residues=[]
	residues_one_letter=[]
	
	pdb_file= pdb_id + '.pdb'
	opener=open(pdb_file,'r')
	line=opener.readline()
	for line in opener:
		if line.startswith('ATOM')==True and line[21] == chain and line[13:15]=='CA':
			residues.append(line[17:20])
	for residue in residues:
		residues_one_letter.append(translate.get(residue))
	#print(residues_one_letter)
	
	output=pdb_id + '.fasta'
	opener2=open(output,'w')
	opener2.write('>'+ pdb_id +'\n')
	for residue in residues_one_letter:
		opener2.write(residue)
  
	return

extract_chain('10GS','A')


