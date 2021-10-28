import serial                             #importing serial
arduinoSerial=serial.Serial('com4',9600)  #initializing serial listner
arduinoSerial.flushInput()
#READING FROM SERIAL PROCDURE
def readSerial(command):                                
    writeSerial(command)                  #write on serial call
    n=0                                   #initializing n times variable
    while True:                           #infinity loop until reading data from serial
        if(arduinoSerial.inWaiting()>0):  #check for data in serial
            break                         #breaking if data exists
    sensor=arduinoSerial.readline()       #reading sensor data on serial
    return sensor                         #returning sensor
#WRITING FROM SERIAL PROCDURE
def writeSerial(command):
    arduinoSerial.write(command)          #writing the instruction on the serial
#TRACING FUNCTION
def stringToIntConvertor(data):
    length=len(data)
    for i in range(length):
        data[i]=int(data[i])
    return data
def unwantedDataRemover(data):
    data=data[2:len(data)-5]
    return data
def dataSpliter(data):
    data=data.split(',')
    return data
def sensorDataExtractor(data):
    data=unwantedDataRemover(data)
    data=dataSpliter(data)
    data=stringToIntConvertor(data)
    return data
def percieve(instruction):
    data=readSerial(instruction)
    sensorData=sensorDataExtractor(str(data))
    return sensorData
#NAVIGATION WITH PERCEPTION
def rotateLeftP():
    sensorData=percieve(b'1')               #call to trace module
    return sensorData
def moveForwardP():
    sensorData=percieve(b'2')               #call to trace module
    return sensorData
def rotateRightP():
    sensorData=percieve(b'3')               #call to trace module
    return sensorData
#NAVIGATION WITHOUT PERCEPTION
def stop():
    readSerial(b'0')          #readSerial call
def rotateLeft():
    readSerial(b'4')          #readSerial call
def moveForward():
    readSerial(b'5')          #readSerial call
def rotateRight():
    readSerial(b'6')          #readSerial call
