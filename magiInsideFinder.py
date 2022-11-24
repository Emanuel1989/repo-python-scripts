#!/usr/bin/python
## MagiInsideFinder version 4.4-desa from office-lenovo
import os
import sys
import traceback

totalResults = 0
totalFilesWithMatchs = 0
oldFileName = ''

def usage():
	print('Usage: python magiInsideFinder.py YOURSTRINGTOSEARCH -php-java-txt-html ' \
		  '[File Filters(default:".txt, .html, .java, .php, .sql")], exceptions are optional.')

def replaceStringInFile(fileName, oldStringToReplace, newString):
	global totalResults
	global totalFilesWithMatchs
	global oldFileName
	if not(os.path.isfile(fileName) and os.access(fileName, os.W_OK)):
		print("WARNING: Skipping... File does not exist or and is not writeable:" + fileName)
		return False

	fileUpdated = False
	showTheLine = ''
	fullLine = ''

	with open(fileName, 'r') as f:
		newlines = []
		lineCounter = 0
		for line in f.readlines():
			lineCounter = lineCounter + 1
			if (oldStringToReplace.lower() in line.lower()) :
			##if (oldStringToReplace in line) :
				fileUpdated = True
				totalResults = totalResults + 1
				showTheLine = line
				fullLine = line
				showTheLine = showTheLine.rstrip("\n\r")
				##positionSubString = showTheLine.lower().find(oldStringToReplace)
				##positionSubString = showTheLine.find(oldStringToReplace)
				positionSubString = showTheLine.lower().find(oldStringToReplace.lower())
			line = line.replace(oldStringToReplace, newString)
			##line = line.replace("Log.", newString)
			newlines.append(line)

			# Write changes to same file
			if fileUpdated :

				if (positionSubString>40):
					showTheLine = "..."+showTheLine[positionSubString-40:]

				positionSubString = showTheLine.lower().find(oldStringToReplace.lower())
				##positionSubString = showTheLine.find(oldStringToReplace)

				if(len(showTheLine)>50):
					showTheLine = showTheLine[:positionSubString+40]+"..."

				showTheLine = showTheLine.replace("\n", "")
				showTheLine = showTheLine.replace("\r", "")
				showTheLine = showTheLine.replace("\t", "")
				
				fullLine = fullLine.replace("\n", "")
				fullLine = fullLine.replace("\r", "")
				fullLine = fullLine.replace("\t", "")
				
				print("File: " + fileName + ":" + str(lineCounter) + " -> "+showTheLine)
				
				if oldFileName != fileName:
					totalFilesWithMatchs = totalFilesWithMatchs + 1
					oldFileName = fileName
			
			fileUpdated = False
			showTheLine = ''
			fullLine = ''
	return fileUpdated

def main():
	successfulResults = False

	try:

		DEFAULT_PATH = '.'
		fileNames = []
		
		print('------------') 
		print('Searching...') 
		print('------------')

		if len(sys.argv) < 2:
			usage()
			# old/new string required parameters, exit if not supplied
			sys.exit(-1)
		else:
			
			if len(sys.argv) > 2:
				otherString = sys.argv[2]
				print('With exceptions')
				
				exceptions = otherString.split("-",3)

				##otherString = otherString.replace('-', '')
				
				try:
					gotdata = exceptions[1]
				except IndexError:
					exceptions.append('dummystring')
					
				try:
					gotdata = exceptions[2]
				except IndexError:
					exceptions.append('dummystring')
					
				try:
					gotdata = exceptions[3]
				except IndexError:
					exceptions.append('dummystring')
				
			else:

				print('Without exceptions')
				otherString = 'none'
			
			oldString = sys.argv[1]
			newString = sys.argv[1]
			
		if len(sys.argv) < 4:
			patterns = ['.txt','.java','.php','.xml','.sql']
		else:
			stringFilter = sys.argv[3]
			patterns = stringFilter.split(',')

		if len(sys.argv) < 5:
			path = DEFAULT_PATH
		else:
			path = sys.argv[4]

		dirpath = os.getcwd()
		##foldername = os.path.basename(dirpath)

		print('[String to find]   : ' + oldString) 
		print('[File filters]      : ' + ', '.join(patterns))
		print('[File exceptions]   : ' + otherString) 
		print('[Directory to check]: ' + dirpath)
		print('------------')

		if not os.path.exists(path):
			raise Exception("Selected path does not exist: " + path)

		# Walks through directory structure looking for files matching patterns
		matchingFileList = \
			[os.path.join(dp, f) \
				for dp, dn, filenames in os.walk(path) \
					for f in filenames \
					
						if os.path.splitext(f)[1] in patterns]

		fileCount = 0
		filesReplaced = 0
		
		for currentFile in matchingFileList:
			
			if(oldString.lower() in currentFile.lower()):
				fileNames.append(currentFile)				
			
			if(otherString is 'none'):
				
				fileCount+=1
				fileReplaced = replaceStringInFile(currentFile, oldString, newString)
				if fileReplaced:
					filesReplaced+=1
					successfulResults = True
			
			else:

					if(exceptions[3] not in currentFile and exceptions[1] not in currentFile and exceptions[2] not in currentFile):
						
						fileCount+=1
						fileReplaced = replaceStringInFile(currentFile, oldString, newString)
						if fileReplaced:
							filesReplaced+=1
							successfulResults = True

		if totalResults == 0:
			print "No results :("
				
		print('------------')
		print("Total files searched: " + str(fileCount))
		print("Total files founded : " + str(totalFilesWithMatchs))
		print("Matches             : " + str(totalResults))
		print('------------')

		if(len(fileNames)>0):
			print(str(len(fileNames)) + ' matches in file names:')
			for i in fileNames:
				print(i)
	
	except Exception as err:
		print(traceback.format_exception_only(type(err), err)[0].rstrip())
		sys.exit(-1)

if __name__ == '__main__':
	main()
