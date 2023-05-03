from dataclasses import dataclass
import random
import datetime
import dash_renderer as Dashrender
import pandas as pd
import numpy as np
import time
import asyncio
import pickle
import Network
Numberhouse=14




class Allhourseholds():

    def __init__(self):
        self.name=None;
        self.houses=[];



class CurrenthouseStr:

    def __init__(self, name):
        self.name=name

        self.active=np.zeros(60000,dtype=float)
        self.reactive = np.zeros(60000,dtype=float)
        self.voltage=np.zeros(60000,dtype=float)


    def extract(self,powerlist,length):

        for k in range(self.active.shape[0]):
            if k==length-1:
                self.active[k]=powerlist[0]
                self.reactive[k]=powerlist[1]
                self.voltage[k]=powerlist[2]






class AllStraeamhouse():

    def __init__(self):
        self.houses = [CurrenthouseStr("B{}".format(i+1)) for i in range(Numberhouse )]
        self.time = []
    def extractor(self,streamlist,time):
        self.time.append(time)
        self.houses[0].extract((streamlist[0:2]+streamlist[28:29]),len(self.time))
        self.houses[1].extract((streamlist[2:4]+streamlist[29:30]),len(self.time))
        self.houses[2].extract((streamlist[4:6]+streamlist[30:31]),len(self.time))
        self.houses[3].extract((streamlist[6:8]+streamlist[31:32]),len(self.time))
        self.houses[4].extract((streamlist[8:10]+streamlist[32:33]),len(self.time))
        self.houses[5].extract((streamlist[10:12]+streamlist[33:34]),len(self.time))
        self.houses[6].extract((streamlist[12:14]+streamlist[34:35]),len(self.time))
        self.houses[7].extract((streamlist[14:16]+streamlist[35:36]),len(self.time))
        self.houses[8].extract((streamlist[16:18]+streamlist[36:37]),len(self.time))
        self.houses[9].extract((streamlist[18:20]+streamlist[37:38]),len(self.time))
        self.houses[10].extract((streamlist[20:22]+streamlist[38:39]),len(self.time))
        self.houses[11].extract((streamlist[22:24]+streamlist[39:40]),len(self.time))
        self.houses[12].extract((streamlist[24:26]+streamlist[40:41]),len(self.time))
        self.houses[13].extract((streamlist[26:28]+streamlist[41:42]),len(self.time))
    def findhouse(self,name):
        element=None
        for i in range(len(self.houses)):
            if name==self.houses[i].name:
                element=self.houses[i]
        return element
#









class Currenthouse:

    def __init__(self):
        self.name=None;
        self.reactive=[]
        self.active=[]
        self.time=[]
        self.voltage=None





def addhousele(powerlist, one):

    temp1P = []
    temp2Q = []

    if np.isnan(powerlist[5]):
        temp1P.append(powerlist[2])
        temp2Q.append(powerlist[3])
        one.active.append(powerlist[2])
        one.reactive.append(powerlist[3])
    else:
        temp1P = [powerlist[2], powerlist[5], powerlist[8]]
        temp2Q = [powerlist[3], powerlist[6], powerlist[9]]

        one.active=one.active+ temp1P
        one.reactive=one.reactive+temp2Q










def Readfilesepare():
    data = pd.read_csv('profiles.csv', parse_dates=['t'])
    data_read = data.iloc[:, 2:12]
    count = 0;
    Allrecord = []

    for i in range(data_read.shape[0]):
        # 15 means Numberhouse+1
        if (i + 1) % 15 == 0 or count==0:
            count+=1
            allrecord = Allhourseholds()
            allrecord.houses = [Currenthouse() for i in range(Numberhouse + 1)]
            if i+2>data_read.shape[0]:
                break;

            for j in range(15):

                if data_read.iloc[i + j, 0] == 'B1':
                    allrecord.houses[0].name = 'B1'
                    addhousele(data_read.iloc[i + j, :].tolist(), allrecord.houses[0])
                elif data_read.iloc[i + j, 0] == 'B2':
                    allrecord.houses[1].name = 'B2'
                    addhousele(data_read.iloc[i + j, :].tolist(), allrecord.houses[1])
                elif data_read.iloc[i + j, 0] == 'B3':
                    allrecord.houses[2].name = 'B3'
                    addhousele(data_read.iloc[i + j, :].tolist(), allrecord.houses[2])
                elif data_read.iloc[i + j, 0] == 'B4':
                    allrecord.houses[3].name = 'B4'
                    addhousele(data_read.iloc[i + j, :].tolist(), allrecord.houses[3])
                elif data_read.iloc[i + j, 0] == 'B5':
                    allrecord.houses[4].name = 'B5'
                    addhousele(data_read.iloc[i + j, :].tolist(), allrecord.houses[4])
                elif data_read.iloc[i + j, 0] == 'B6':
                    allrecord.houses[5].name = 'B6'
                    addhousele(data_read.iloc[i + j, :].tolist(), allrecord.houses[5])
                elif data_read.iloc[i + j, 0] == 'B7':
                    allrecord.houses[6].name = 'B7'
                    addhousele(data_read.iloc[i + j, :].tolist(), allrecord.houses[6])
                elif data_read.iloc[i + j, 0] == 'B8':
                    allrecord.houses[7].name = 'B8'
                    addhousele(data_read.iloc[i + j, :].tolist(), allrecord.houses[7])
                elif data_read.iloc[i + j, 0] == 'B9':
                    allrecord.houses[8].name = 'B9'
                    addhousele(data_read.iloc[i + j, :].tolist(), allrecord.houses[8])
                elif data_read.iloc[i + j, 0] == 'B10':
                    allrecord.houses[9].name = 'B10'
                    addhousele(data_read.iloc[i + j, :].tolist(), allrecord.houses[9])
                elif data_read.iloc[i + j, 0] == 'B11':
                    allrecord.houses[10].name = 'B11'
                    addhousele(data_read.iloc[i + j, :].tolist(), allrecord.houses[10])
                elif data_read.iloc[i + j, 0] == 'B12':
                    allrecord.houses[11].name = 'B12'
                    addhousele(data_read.iloc[i + j, :].tolist(), allrecord.houses[11])
                elif data_read.iloc[i + j, 0] == 'B13':
                    allrecord.houses[12].name = 'B13'
                    addhousele(data_read.iloc[i+j,:].tolist(),allrecord.houses[12])
                elif data_read.iloc[i+j,0]=='B14':
                    allrecord.houses[13].name='B14'
                    addhousele(data_read.iloc[i+j,:].tolist(),allrecord.houses[13])
                else:
                    allrecord.houses[14].name='HOF'
                    allrecord.houses[14].voltage=[data_read.iloc[i+j,1],data_read.iloc[i+j,4],data_read.iloc[i+j,7]]

            Allrecord.append(allrecord)
    return Allrecord

def Dssdata(AllElement):

    threelist = ['B1', 'B3', 'B7', 'B9', 'B12']
    onelist=['B2', 'B4','B5' ,'B6','B8', 'B11','B10', 'B13','B14']
    powerlist=[]


    for j in range(15):

        if AllElement.houses[j].name in threelist:
            temp1=[ AllElement.houses[j].active[0], AllElement.houses[j].reactive[0],AllElement.houses[j].active[1],AllElement.houses[j].reactive[1],AllElement.houses[j].active[2],AllElement.houses[j].reactive[2]]
            powerlist = powerlist + temp1
        elif AllElement.houses[j].name in onelist:
            temp2=[AllElement.houses[j].active[0],AllElement.houses[j].reactive[0]]
            powerlist = powerlist + temp2
        elif AllElement.houses[j].name =="HOF":
            temp3=[AllElement.houses[j].voltage[0],AllElement.houses[j].voltage[1],AllElement.houses[j].voltage[2]]
            powerlist = powerlist + temp3

    powerlist[5:27]
    outlist=powerlist[0:6]+powerlist[34:48]+powerlist[6:34]+powerlist[48:51]
    result_dss=Network.calculteDss(outlist)
    return result_dss







def LoadStream(index):
    with open('newopfile.txt', 'r') as file:

        i = 0;

        while True:

            line = file.readline()
            if i == index:

                fe = line.split(",")
                chun = fe[0:42]
                chun = [float(chun[i]) for i in range(len(chun))]
                break
            elif not line:
                break

            i = i + 1;

        return chun

