#include "SoftwareSerial.h"
//SoftwareSerial serial(1,0);
int trigF=2;                    //front sensor trigger pin
int echoF=3;                    //front sensor echo pin
int trigL=4;                    //left sensor trigger pin
int echoL=5;                    //left sensor echo pin
int trigR=6;                    //right sensor trigger pin
int echoR=7;                    //right sensor echo pin
int motor1F=9;                  //motor driver a pin
int motor1B=8;                  //motor driver b pin
int motor2F=11;                 //motor driver c pin
int motor2B=10;                 //motor driver d pin
float sensorReading;            //front sensor reading
int distance;                   //distance calculation variables
int sensorF;                    //distance in front sensor
int sensorR;                    //distance in right sensor
int sensorL;                    //distance in left sensor
int instruction;                //arduino input
bool obstacle;                  //obstacle check variable
int forwardDelay=900;              //delay for forward motor on
int rotationDelay=9*forwardDelay;  //delay for rotation motor on
int forwardLimit=20;               //limit for forward motion
int rotationLimit=30;              //limit for rotation 
void setup() {
  Serial.begin(9600);           //initiallizing serial port 
  pinMode(trigF,OUTPUT);        //trigger front
  pinMode(echoF,INPUT);         //echo front
  pinMode(trigL,OUTPUT);        //trigger front
  pinMode(echoL,INPUT);         //echo front
  pinMode(trigR,OUTPUT);        //trigger front
  pinMode(echoR,INPUT);         //echo front
  pinMode(motor1F,OUTPUT);      //motor driver a
  pinMode(motor1B,OUTPUT);      //motor driver b
  pinMode(motor2F,OUTPUT);      //motor driver c
  pinMode(motor2B,OUTPUT);      //motor driver d
}

void loop(){
  while(Serial.available()==0){}
  instruction=Serial.parseInt();                        //getting input
  switch(instruction){
    case 1:                                             //left rotation
    sensorR=readSensor(trigR,echoR);                    //reading left sensor value
    obstacle=obstacleDetector(sensorR,rotationLimit);   //obstacle check call
    if(not(obstacle)){                                  //checking obstacle
      motorDrive('l');                                  //drive call
    }
    sensorF=readSensor(trigF,echoF);                    //reading front sensor value
    sensorL=readSensor(trigL,echoL);                    //reading front sensor value
    commandGenerator(obstacle,sensorF,sensorR,sensorL); //command generation call
    break;
    case 2:                                             //forward
    sensorF=readSensor(trigF,echoF);                    //reading front sensor value
    obstacle=obstacleDetector(sensorF,forwardLimit);    //obstacle check call
    if(not(obstacle)){                                  //obstacle check
      motorDrive('f');                                  //motor call
    }
    sensorR=readSensor(trigR,echoR);                     //reading right sensor value
    sensorL=readSensor(trigL,echoL);                     //reading left sensor value
    commandGenerator(obstacle,sensorF,sensorR,sensorL);  //command generator call
    break; 
    case 3:                                              //right rotation with sensor read
    sensorL=readSensor(trigL,echoL);                     //reading right sensor value
    obstacle=obstacleDetector(sensorL,rotationLimit);    //obstacle check call
    if(not(obstacle)){                                   //obstacle call
      motorDrive('r');                                   //motor call
    }
    sensorF=readSensor(trigF,echoF);                     //reading front sensor value
    sensorR=readSensor(trigR,echoR);                     //reading front sensor value
    commandGenerator(obstacle,sensorF,sensorR,sensorL);  //command generator call
    break;
    case 4:                                              //left without read
    sensorR=readSensor(trigR,echoR);                     //reading left sensor value
    obstacle=obstacleDetector(sensorL,rotationLimit);    //obstacle check call
    if(not(obstacle)){                                   //obstacle check
      motorDrive('l');                                   //motor call
      automatePrint(1);                                  //printing moved
    }else{
      automatePrint(0);                                  //printing not moved
    }
    
    break;
    case 5:                                              //forward 
    sensorF=readSensor(trigF,echoF);                     //reading front sensor value
    obstacle=obstacleDetector(sensorF,forwardLimit);     //obstacle check call
    if(not(obstacle)){                                   //obstacle check
      motorDrive('f');                                   //motor call
      automatePrint(1);                                  //printing moved
    }else{
      automatePrint(0);                                  //printing not moved
    }
    break;
    case 6:                                              //left 
    sensorL=readSensor(trigL,echoL);                     //reading right sensor value
    obstacle=obstacleDetector(sensorR,rotationLimit);    //obstacle check call
    if(not(obstacle)){                                   //obstacle check
      motorDrive('r');                                   //motor call
      automatePrint(1);                                  //printing moved
    }else{
      automatePrint(0);                                  //printing not moved
    }
    break;
  }
}                              
float readSensor(int trig,int echo){      //calculates and returns sensor distance                              
  digitalWrite(trig,LOW);                 //triggering ultrasonic sensor with pulse
  delayMicroseconds(20);
  digitalWrite(trig,HIGH);
  delayMicroseconds(20);
  digitalWrite(trig,LOW);                              
  sensorReading=pulseIn(echo,HIGH);       //gettting input from ultrasonic sensor
  distance=(0.0451*sensorReading)/2;      //calculating distance
  return distance;
}                           
bool obstacleDetector(int distance,int limit){      //obstacle is near or far check
    if(distance<=limit){                            //checking obstacle distance is danger
      return true;                                  //obstacle is near
    }
    else{
      return false;                                 //obstacle is far
    }
}
void commandGenerator(bool obstacle,int sensorF,int sensorR,int sensorL){      //output to the computer
  if(obstacle == false){                                                       //obstacle check
    Serial.print(sensorL);                                                     //no obstacle
    Serial.print(","); 
    Serial.print(sensorF);
    Serial.print(",");
    Serial.println(sensorR);
   }
   else{
    Serial.print(sensorL);                                                      //no obstacle
    Serial.print(",");
    Serial.print(sensorF);
    Serial.print(",");
    Serial.println(sensorR);
   }
}
void automatePrint(int message){
  Serial.println(message);
}
void motorDrive(char movement){
  switch(movement){
    case 'f':digitalWrite(motor1F,HIGH);   
             digitalWrite(motor2F,HIGH);   
             delay(forwardDelay);
             digitalWrite(motor1F,LOW);   
             digitalWrite(motor2F,LOW);    
             break;
    case 'r':digitalWrite(motor1B,HIGH);
             digitalWrite(motor2F,HIGH);
             delay(rotationDelay);
             digitalWrite(motor1B,LOW);
             digitalWrite(motor2F,LOW);
             break;
    case 'l':digitalWrite(motor1F,HIGH);
             digitalWrite(motor2B,HIGH);
             delay(rotationDelay);
             digitalWrite(motor1F,LOW);
             digitalWrite(motor2B,LOW);
             break;
  }
}
