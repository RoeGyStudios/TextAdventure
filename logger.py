def getLogLevels(printO):
	i = 0
	output = ["DEBUG","Info","Warn","Error"]
	if printO == True:
		while i < len(output):
			print(output[i])
			i =i +1
	elif printO == False:
		return output
	else:
		raise Exception(printO + "is an unknow state. Please use 'True'or 'False'")
def log(prelevel,errorString,printO):
	import time
	outputL = ""
	
	errorlevel = prelevel
	et = getLogLevels(False)
	if errorlevel in et:
		if errorlevel == et[0]:
			outputL = et[0]
		elif errorlevel == et[1]:
			outputL = et[1]
		elif errorlevel == et[2]:
			outputL = et[2]
		elif errorlevel == et[3]:
			outputL = et[3]
		else:
			raise IndexError("Ooops, something went very wrong! Sorry please try again!")
	else:
		raise Exception("Sorry, you used an unknow error Level")
	output = time.strftime("[%H:%M:%S] [" + str(outputL) + "] "+ errorString) 
	if printO == True:
		print(output)
	elif printO == False:
		return output
	else:
		raise Exception(printO + "is an unknow state. Please use 'True'or 'False'")
def configLoad(command):
	index = {}
	mf = open("logger.data","r")
	i = 0
	line = mf.readlines()
	temp1 = line
	run = True
	print(temp1)
	if line[0] != "<START>\n" or line[len(line)-1] != "</START>":
		raise IOError("File starts wrong: " + line[0] + "Or stops wrong:" + line[len(line)-1])
	else:
		print("File OK")
		line.remove('<START>\n')
		line.remove('</START>')
		line = [line.replace('\n','') for line in line]
		print(line)
		#print(len(line))
		while i <= len(line) and run == True:
			if i >= len(line):
				run = False
		#		print("Stop while")
				break
		#	print("RUN")
		#	print('Runde: '),
		#	print(i)
		#	print(line[i])
		#	print(line[i].startswith('#'))
			if line[i].startswith('#'):
				print("Removing:" + line[i])
				line.remove(line[i])
			else:
				print("Don't remove anything")
			if line[i].startswith("version:"):
				index = {line[i].split(':')[0]:line[i].split(':')[1]}
				#print(index)
			
			i = i +1
		print(line)
		print(index)
		try:
			index['version']
		except:
			raise Exception("ERROR: Missing 'version' tag!")
	if command == 'version':
		return index['version']
