'''recursively search a directory for a file, and update a line of text. can be used with txt, HTML, or XML files instead of BeautifulSoup'''

import os

user_dir = input(' ')  #prompt for user 
root_dir = os.path.join(user_dir)

match_file = input('') #prompt for user to pass in 
replace_file = '' #assign a generic file name here

wordReplacements1 = input('Find word: ')
wordReplacements2 = input('Replace with word: ')

wordReplacements = {wordReplacements1 : wordReplacements2} #dictionary creation of text to find and replace

def updateSCM(line):
    for key, value in wordReplacements.items(): #instructing the wordReplacement/what to find
        line = line.replace(key, value)
    return line

def setPath(dirpath, filename):
    org_name = os.path.join(dirpath, filename) 
    new_name = os.path.join(dirpath, filename.replace(match_file, replace_file)) #assignment of where to save and replace file
    with open(new_name, 'w') as output_file, open(org_name) as input_file: 
        for line in input_file:
            output_file.write(updateSCM(line))
	
	input_file.close()
	os.remove(match_file)
	os.rename(new_name, org_name)
  
			
for dirpath, dirs, files in os.walk(root_dir): #walk the directory
    for filename in files:
        if (filename == match_file):
            setPath(dirpath, filename) 
