'''
Write a function that reads from two fasta files and produces three files containing respectively: the list of ids that are present only in the first file; the list of ids that are present only in the second file; the list of ids that are shared between the two files. All three lists should be sorted alphabetically.
The names of the three files that you need to create should be constructed from the names of the input files. e.g.: f1.fasta , f2.fasta -> f1_only.txt , f2_only.txt , f1_f2.txt

Parameters:
- fn1	: string containing the name of the 1st fasta file
- fn2	: string containing the name of the 2nd fasta file
		(we assume both to be in the same dir as the program and to have an extension '.fasta')

Returns:
- None
'''
def extract_ids(fn1, fn2):
	#part 1: read the files and extract the ids
	
	list1 = []
	reader=open(fn1,'r')
	for line in reader:
		if line[0]== '>':
			id=line.strip().split('|')[1]
			list1.append(id)
	
	list2 = []
	reader=open(fn2,'r')
	for line in reader:
		if line[0]== '>':
			id=line.strip().split('|')[1]
			list2.append(id)
	print(list1)

extract_ids('f1.fasta','f2.fasta')



'''
Write a function that reads from a file a list of ids and that extracts from a second file in fasta format the corresponding chains. The function should then return a dictionary in the form {id:chain} containing all of the found chains and a list containing the ids of the chains that were not in the fasta file.

Parameters:
- fn_ids	: string containing the name of the file with the ids
- fn_fasta	: string containing the name of the fasta file

Returns:
- found		: dictionary that associates the chain to each id that was present in the fasta file
- not_found	: list containing all the ids that were not present in the fasta file
# '''
# def extract_fastas(fn_ids, fn_fasta):
	# return {} , []

# found, not_found = extract_fastas('ids.txt','f1.fasta')
# for i,(key,value) in enumerate(found.items(),1):
	# print(i,key,value)
# print(not_found)


