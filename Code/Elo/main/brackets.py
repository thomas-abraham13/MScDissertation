import csv
#import pandas as pd
import re
import numpy as np
import collections
import csv
import time

def elo(r1,r2,k,s1,s2,Team1,Team2):
    R1=pow(10,r1/400)
    R2=pow(10,r2/400)
    #R2=10^(r2/400)
    E1=R1/(R1+R2)
    E2=R2/(R1+R2)
    print(Team1,"has ",int(E1*100),"% to win")
    print(Team2,"has ",int(E2*100),"% to win")
    if s1==1:
        print(Team1 , "won")
        g=0
    else:
        g=1
        print(Team2,"won")
    r1_cap=r1+k*(s1-E1)
    r2_cap=r2+k*(s2-E2)
    return r1_cap,r2_cap

dataFile=open('TeamMatchups.csv','r')
reader=csv.reader(dataFile)
j=0
Teams=['ATL','BOS','BKN','CHA','CHI','CLE','DAL','DEL','DEN','DET','EST','FCB','GSW','HOU','IND','LAC','LAL','MAC','MEM','MIA','MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHX','POR','RMD','SAC','SAS','SDS','SLA','TOR','USA','UTA','WAS','WLD','WST']
#prior=[1000,1010,1020,1030,1040,1050,'D,'DEL','DEN','DET','EST','FCB','GSW','HOU','IND','LAC','LAL','MAC','MEM','MIA','MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHX','POR','RMD','SAC','SAS','SDS','SLA','TOR','USA','UTA','WAS','WLD','WST']
teams_rating = collections.OrderedDict()
accuracy=0
k=0
check=[]
match=0
for i in range(0,40):
    teams_rating[Teams[i]]=1000
for row1 in reader:
    if j!=0:
        print("\n")
        s = re.split('\W+', row1[2])
        print(s)
        if len(s) == 2:
            match+=1
            print("Match", match)
            #time.sleep(2)
            Team1 = s[0]
            Team2 = s[1]
            flag = 1
            c = Team1 + Team2
            if row1[3]=='W':
                s1=1
                s2=0
            else:
                s1=0
                s2=1
            if (s1 == 1 and teams_rating[Team1] > (teams_rating[Team2] + 100)) or (s2 == 1 and (100 + teams_rating[Team2]) > teams_rating[Team1]):
                accuracy+=1
            teams_rating[Team1],teams_rating[Team2]=elo(teams_rating[Team1],teams_rating[Team2],30,s1,s2,Team1,Team2)
            print(Team1,"rating",teams_rating[Team1],Team2,"rating",teams_rating[Team2])
    j=j+1
print(accuracy)
dataFile.close()
for Team in teams_rating:
    print(Team,teams_rating[Team])
#Bracket Formation