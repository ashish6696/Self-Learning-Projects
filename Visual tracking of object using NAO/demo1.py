# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 23:17:42 2021

@author: ashis
"""

try:
    import vrep 
except:
    print ('--------------------------------------------------------------')
    print ('"vrep.py" could not be imported. This means very probably that')
    print ('either "vrep.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "vrep.py"')
    print ('--------------------------------------------------------------')
    print ('')
    

import time

print ('Program started')
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19990,True,True,5000,5) # Connect to V-REP

rc,yaw=vrep.simxGetObjectHandle(clientID, 'yaw', vrep.simx_opmode_blocking)
rc,pitch=vrep.simxGetObjectHandle(clientID, 'pitch', vrep.simx_opmode_blocking)
while vrep.simxGetConnectionId(clientID) != -1:
    res,xtarget=vrep.simxGetFloatSignal(clientID,"mySignalNamex",vrep.simx_opmode_blocking)
    res,ytarget=vrep.simxGetFloatSignal(clientID,"mySignalNamey",vrep.simx_opmode_blocking)
    rc=vrep.simxSetJointTargetVelocity(clientID,yaw,1*(0.5-xtarget),vrep.simx_opmode_blocking)
    rc=vrep.simxSetJointTargetVelocity(clientID,pitch,0.5*(0.5-ytarget),vrep.simx_opmode_blocking)
    print([xtarget,ytarget])