'''
Write a function that reads a dssp file, extracting only a selected chain. The function should then return a dictionary with a key for each residue mapping to the sum of the accessible surface area observed in the chain for that type of residue (reported in the 7th column 'ACC').

Parameters:
- fn		: string containing the name of the dssp file
- chain		: string containing the name of the chain to extract

Returns:
- asa_count	: dictionary storing the total asa for each observed residue (if a residue is not present in the selected chain there is no need to have a corresponding key in the dictionary)
'''

def count_asa(fn, chain):
    import re
    with open(fn,'r') as file:
	    dict_asa={}
		asa=0
		for i,line in enumerate(file):
				pattern=r' # +RESIDUE +AA'
				match=re.search(pattern,line)
				if match:  #matching the pattern in the file
					print(line)
					index=int(i)  #find the index where the pattern is
					
					for i,line in enumerate(file):
						check_chain=line[11:12]
						if int(i) > index and if check_chain==chain:
							res=line[13:14]
							asa=int(line[35:38])
							if res in dict_asa:
								dict_asa[res] += asa
							else:
								dict_asa[res] = asa
                 
         
            
    return dict_asa
        
        
count_asa('5ex1.dssp','D')

asa_count = count_asa('5ex1.dssp','D')
for key,value in asa_count.items():
	print(key,value)
