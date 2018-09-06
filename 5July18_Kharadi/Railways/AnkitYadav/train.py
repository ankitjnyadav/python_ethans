#Train
from random import *
import json


#variable Declaration section
trainsData,usersData,bookingsData = None,None,None
user = {'username':'super','password':'pwd','type':'admin'}
guestUser  = {'username':'ankit','password':'pwd','type':'guest'}
users_list = [user,guestUser,]


dirPath= r'D:\Ethans\Python\8-5\dataFiles'
usersPath = dirPath + r'\user.json'
trainsPath = dirPath + r'\train.json'
bookingsPath = dirPath + r'\booking.json'


def writeUsers(users_list):
	with open(usersPath,'w') as fh:
		json.dump(users_list,fh, indent=4)
def readUsers():
	with open(usersPath,'r') as fh:
		usersData=json.load(fh)
		return usersData




# Schema is - trainNo,src,dest,days{},coachType{},fare{}
trains =  {'trainNo':'1','src':'Pune', 'dest':'Delhi','days':['Mon','Tues'],'coachType':['SL','AC3'],'fare':{'SL':'500','AC3':'900'},'seats':{'SL':'60','AC3':'20'}}
#trains =  {'trainNo':None,'src':None, 'dest':None,'days':[None],'coachType':[None],'fare':{None}}
trains_list = [trains,]


def writeTrains(trains_list):
	with open(trainsPath,'w') as fh:
		json.dump(trains_list,fh, indent=4)
def readTrains():
	with open(trainsPath,'r') as fh:
		trainsData=json.load(fh)
		return trainsData


bookings = {'PNR':'randomNo','src':'Source','dest':'Dest','noOfSeats':'2','coachType':'AC','totalFare':'780','status':'Confirmed'}
bookingsList=[bookings,]
def writeBookings(bookingsList):
	with open(bookingsPath,'w') as fh:
		json.dump(bookingsList,fh, indent=4)
def readBookings():
	with open(bookingsPath,'r') as fh:
		bookingsData=json.load(fh)
		return bookingsData



i=0
count = 0
#temp=3

def init():
	writeTrains(trains_list)
	writeBookings(bookingsList)
	writeUsers(users_list)

def signUp():
	
	flag=1
	usersData = readUsers()
	for x in usersData:#users_list:
		while flag:	
			username = raw_input('Enter the username: ')
			if x['username'].upper()==username.upper():
				print 'Account with username \'%s\' already exits\nTry Again...' %username	
			else:
				flag=0	
				password = raw_input('Enter the password: ')
				#userType = raw_input('Enter the Type (Admin/User): ')
				temp = {'username':username,'password':password,'type':'guest'}
				users_list.append(temp)
				writeUsers(users_list)
				print 'Account Created'
 
def splitIntoList(tempList):
	return tempList.split()	

def addNewTrain():
	trainNo=raw_input('Enter the trainNo: ')
	for i in trains_list:
		if i['trainNo'].upper()==trainNo.upper():
			print 'Train with trainNo %s already exists!' %trainNo
			break
	else:
		src=raw_input('Enter the Source city: ')
		dest=raw_input('Enter the Destination city: ')
		days=raw_input('Enter the Days working: ')
		days=splitIntoList(days)
		coachType=raw_input('Enter the coachTypes: ')
		coachType=splitIntoList(coachType)
		x=0
		fare={}
		seats={}
		while x<len(coachType):
			tempStr = raw_input('Enter the price associated for %s:' %coachType[x]) 
			tempFare = {coachType[x]:tempStr}
			tempStr2 = raw_input('Enter the no. of seats associated for %s:' %coachType[x]) 
			tempSeats = {coachType[x]:tempStr2}
			fare.update(tempFare)
			seats.update(tempSeats)
			x=x+1 

		tempTrain={'trainNo':trainNo,'src':src,'dest':dest,'days':days,'coachType':coachType,'fare':fare,'seats':seats}
		trains_list.append(tempTrain)
		printHash()
		print 'New Train with trainNo: %s Succesfully Added' %trainNo

def modifyTrainDetails(modifyTrain):
	for x in trains_list:
		if x['trainNo'].upper()==modifyTrain.upper():
			#trainNo=raw_input('Enter the trainNo: ')
			src=raw_input('Enter the Source city: ')
			dest=raw_input('Enter the Destination city: ')
			days=raw_input('Enter the Days working: ')
			days=splitIntoList(days)
			coachType=raw_input('Enter the coachTypes: ')
			coachType=splitIntoList(coachType)
			z=0
			fare={}
			seats={}
			while z<len(coachType):
				tempStr = raw_input('Enter the price associated for %s:' %coachType[z]) 
				tempFare = {coachType[z]:tempStr}
				tempStr2 = raw_input('Enter the noOfSeats associated for %s:' %coachType[z]) 
				tempSeats = {coachType[z]:tempStr2}
				
				fare.update(tempFare)
				seats.update(tempSeats)
				z=z+1 
				break
			x["src"]=src
			x["dest"]=dest
			x["days"]=days
			x["coachType"]=coachType
			x["fare"]=fare
			x["seats"]=seats
			printHash()
			print'Train Details Succesfully modified'
			print 'Details after Modification:'
			printHash()
			print 'Source: ',x["src"]
			print 'Destination: ',x["dest"]
			print 'Running days: ',x["days"]
			print 'Coaches types: ',x["coachType"]
			print 'Fare:',x["fare"]
			print 'Available Seats: ',x["seats"]
			break
	else:
		print 'no train with trainNo: %s found.' %modifyTrain

def deleteTrainDetails(deleteTrain):
	tempTrainsData = json.load(open(trainsPath))
	size = len(tempTrainsData)
	for x in range(size):	#trains_list:
		if tempTrainsData[x]['trainNo'].upper()==deleteTrain.upper():
			#index = tempTrainsData.index(x)
			tempTrainsData.pop(x)
			writeTrains(tempTrainsData)
			print 'Train with trainNo %s delted!' %deleteTrain
			break
	else:
		print 'no train with trainNo: %s found.' %deleteTrain			
	#showAllTrains()
	return

def setNewPassword():
	tempNewPassword=raw_input('Enter new password: ')
	tempNewConfirmPwd=raw_input('Re-Enter new password: ')
	if(tempNewPassword==tempNewConfirmPwd):
		password=tempNewPassword
		print 'Password Succesfully changes.'
	else:
		print 'Passwords not matching.\nTry again'
		setNewPassword()

def changePassword(currentUser):
	usersData = readUsers()
	for x in usersData:	#users_list:
		#print x
		if x['username']==currentUser:
			password = x['password']
			tempOldPwd = raw_input('Enter current password: ')
			if(tempOldPwd==password):
				setNewPassword()	
			else:
				print 'Incorrect password\nTry Again...'
				changePassword(currentUser)

def login(count):
	username = raw_input('Enter the username: ')
	password = raw_input('Enter the password: ')
	temp = {'username':username,'password':password}

	usersData = readUsers()
	for x in usersData: #users_list:
		#print x
		if x['username'].upper()==username.upper() and x['password'].upper()==password.upper():
			if(x['type'].lower()=='guest'):
				printHash()
				print 'Login Succesfull'
				printHash()
				print 'Welcome %s' %temp['username']
				guestUserMenu(temp['username'])

			elif(x['type'].lower()=='admin'):
				printHash()
				print 'Login Succesfull'
				printHash()
				print 'Welcome %s user' %temp['username']
				adminUserMenu(temp['username'])
			break
	else:
		count=count+1
		temp=3-count
		print 'Account details not matching.\nPlease try again.'
		if(count<3):
			print 'You have got %d more chance left!' %temp 
			login(count)
		elif(count==3):
			print 'Maximum attemps ...\nTry after some time'

def showAllTrains():
	printHash()
	trainsData = readTrains()
	listLength = len(trainsData)	#trains_list)
	if(listLength==0):
		print 'Sorry!\nNo Trains details available at the moment.'
	else:
		for x in trainsData:	#trains_list:
			print 'TrainNo: ',x['trainNo']
			print 'Source: ',x['src']#trains.get('src')
			print 'Destination: ',x['dest']#trains.get('dest')
			print 'Days: ', x['days']#trains.get('days')
			print 'Coaches Present: ',x['coachType']#trains.get('coachType')
			print 'Fare: ',x['fare']#trains.get('fare')
			print 'Available Seats: ', x['seats']
			print '-'*30

def calculateFare(trainNo,noOfSeats,coachType):
	trainsData = readTrains()
	for x in trainsData: #trains_list:
			if x['trainNo'].upper()==trainNo.upper():
				perPersonFare = x['fare']
				perPersonFare = perPersonFare[coachType]
				totalFare = int(noOfSeats)*int(perPersonFare)
				#print totalFare
	return totalFare

def trainEnquiry(source,dest):
	#train, source, dest,noOfSeats=0,seatType=None
	#showAllTrains()
	printHash()
	trainsData = readTrains()
	listLength = len(trains_list)
	if(listLength==0):
		print 'Sorry!\nNo Trains details available at the moment.'
	else:
		for x in trainsData: #trains_list:
			if x['src'].upper()==source.upper() and x['dest'].upper()==dest.upper():
				printHash()
				print 'TrainNo:',x['trainNo']
				print 'Source:',x['src']#trains.get('src')
				print 'Destination:',x['dest']#trains.get('dest')
				print 'Days:', x['days']#trains.get('days')
				print 'Coaches Present:',x['coachType']#trains.get('coachType')
				print 'Fare:',x['fare']#trains.get('fare')
				print 'Seats available:',x['seats']
				print '-'*30
		else:
			'No Trains available in the selected route...'

def pnrStatus(PNR=None):
	if PNR == None:
		PNR = raw_input('Enter PNR no. : ')
	bookingsData = readBookings()
	for x in bookingsData: #bookingsList:
			if x['PNR']==PNR:
				print 'Current Status: ', x['status']
				print 'noOfSeats: ',x['noOfSeats']
				print 'coachType: ',x['coachType']
	return PNR

def cancelReservation():
	PNR = pnrStatus()
	choice=raw_input('Are you sure you want to cancelReservation? (Yes/No) ')
	bookingsData = readBookings()
	if choice in ['y', 'Y', 'yes', 'Yes', 'YES']:
		for x in bookingsData: #bookingsList:
			if x['PNR'].upper()==PNR.upper():
				x['status']='Cancelled'
	printHash()
	pnrStatus(PNR)

def updateTrainSeats(trainNo,coachType,noOfSeats):
	flag=False
	trainsData = readTrains()
	for x in trainsData: #trains_list:
		if x['trainNo'].upper()==trainNo.upper():
			tempSeats= x['seats']
			if coachType in tempSeats:
				tempNo= tempSeats.get(coachType)	
				if tempNo <= noOfSeats:
					tempNo = int(tempNo) - int(noOfSeats)
					tempSeats[coachType]=str(tempNo)
					#print tempSeats[coachType]
					#print x['seats']
					flag=True
					
				else:
					tempNo = int(tempNo) - int(noOfSeats)
					tempSeats[coachType]=str(tempNo)
					flag=False
					
	print flag
	return flag
	'''
			seats={}
			z=0
			while z<len(x['coachType']):
				print x['coachType']

				print 'CT', coachType
				print coachType[z]
				if coachType.get(z)==coachType:
					print coachType[z]
					#tempSeats = {coachType[z]:tempStr}
				tempStr = 'AA'#raw_input('Enter the price associated for %s:' %coachType[z]) 
				tempSeats = {coachType[z]:tempStr}
				#seats.update(tempSeats)
				print 'S',seats
				print 'T',tempSeats
				z=z+1 
				break
			print 'B',x["seats"]
			x["seats"]=seats
			print 'A',x["seats"]
	'''

def bookTrain():
	#train, source, dest,noOfSeats=0,seatType=None
	source = raw_input('Enter the source city: ')
	dest = raw_input('Enter the destination city: ')
	trainEnquiry(source,dest)
	trainNo = raw_input('Enter the trainNo: ')
	noOfSeats = int(raw_input('Enter the no of seats:'))
	coachType = raw_input('Enter the Coach Type: ')
	PNR =  str(randint(1, 999))+'-'+str(randint(1, 9999999))
	totalFare = calculateFare(trainNo,noOfSeats,coachType)
	flag=updateTrainSeats(trainNo,coachType,noOfSeats)
	print flag
	print 'Booking Succesfully Done...'
	printHash()
	print 'PNR: ', PNR
	print 'No Of Passengers: ', noOfSeats
	print 'Coach Type: ', coachType
	print 'Total Fare: ', totalFare
	if flag:
		status='Confirmed'
		temp={'PNR':PNR,'src':source,'dest':dest,'noOfSeats':noOfSeats,'coachType':coachType,'totalFare':totalFare,'status':status}
		bookingsList.append(temp)
		writeBookings(bookingsList)
		printHash()
	else:
		status='Waiting'
		temp={'PNR':PNR,'src':source,'dest':dest,'noOfSeats':noOfSeats,'coachType':coachType,'totalFare':totalFare,'status':status}
		bookingsList.append(temp)
		printHash()
		
		
	#print bookingsList
	#'PNR':'randomNo','src':'Source','dest':'Dest','noOfSeats':'2','coachType':'AC','totalFare':'780'}

def printHash():
	print '#'*35

def guestUserMenu(currentGuest):	
	i=0
	while(i!=6):
		print '#'*35
		print '1. Train Enquiry'
		print '2. PNR Status'
		print '3. Book A Train'
		print '4. Cancel Reservation'
		print '5. Change password'
		print '6. Log Out'
		printHash()
		i = int(raw_input('Please enter your choice: '))
		printHash()
		if(i==1):
			source = raw_input('Enter the source city: ')
			dest = raw_input('Enter the destination city: ')
			trainEnquiry(source,dest)
			print
		elif(i==2):
			pnrStatus()
		elif(i==3):
			bookTrain()
		elif(i==4):
			cancelReservation()

		elif(i==5):
			changePassword(currentGuest)
		elif(i==6):
			break
		else:
			i = int(raw_input('Thats an incorrect choice...\nPlease try again'))
			continue

def adminUserMenu(currentAdminUser):
	i=0
	while(i!=5):
		print '#'*35
		print '1. Add a new Train'
		print '2. Modify Train details'
		print '3. Delete specific Train'
		print '4. Change password'
		print '5. Log Out'
		printHash()
		i = int(raw_input('Please enter your choice: '))
		printHash()
		if(i==1):
			addNewTrain()
		elif(i==2):
			modifyTrain=raw_input('Enter the trainNo you want to modify details of: ')
			modifyTrainDetails(modifyTrain)
		elif(i==3):
			deleteTrain=raw_input('Enter the trainNo you want to delete details of: ')
			deleteTrainDetails(deleteTrain)
		elif(i==4):
			changePassword(currentAdminUser)
		elif(i==5):
			print 'Logging Out...\n'
			break
		else:
			i = int(raw_input('Thats an incorrect choice...\nPlease try again'))
			continue

def checkUserType():
	return user.get('username')

def exit():
	print '\n'
	printHash()
	print '     Visit Again. Thank You!'
	printHash()
	print '\n'

def main():
	i=0
	while(i!=3):
		print '\n'
		print '#'*35
		print 'Welcome to Train Reservation Center'
		print '#'*35
		print '1. Log in'
		print '2. Sign Up'
		print '3. Exit'
		init()
		printHash()
		i = int(raw_input('Please enter your choice: '))
		printHash()
		if(i==1):
			count=0
			login(count)	
		elif(i==2):
			signUp()
		elif(i==3):
			exit()
			break
		else:
			i = int(raw_input('Thats an incorrect choice...\nPlease try again'))
		
main()	
