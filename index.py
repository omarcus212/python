import os
import subprocess
import smtplib
from email.message import EmailMessage
from datetime import datetime
from os import listdir
from os.path import isfile, join
import re


path = 'C:\\xampp\\htdocs\\popularbancothales';
os.chdir(path)
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="marcus123",
  database="db_teste"
)


def setinsert(lst,bolsa,inner,outer):
     outer = outer-1
    #  mycursor = mydb.cursor()     
    #  mycursor.executemany('insert into tblkit (Iccid,bolsa_key,inner_key,outer_key) values (%s,1,1,1)', lst)
    #  mydb.commit()
    #  print(mycursor.rowcount, "record inserted.")
    


def readArchive():
 cont = 0;
 bolsa = 0;
 inner = 0;
 outer = 0;
 for fileTXT in os.listdir():
    lst = []
    with open(fileTXT) as ref_arquivo:
      for linha in ref_arquivo.readlines():
        cont = cont+1;
        # print(cont)
        if re.match('[0-9]{20}', linha):
          lst.append((linha.rstrip('\n'),))
          if  cont % 1000 == 0 :
             outer = outer+1;
            #  setinsert(lst,bolsa,inner,outer)
             print('outer',cont,outer)
     
                    
       




readArchive()