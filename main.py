from crypt import methods
import csv
import json
from urllib import response
import ftplib
from flask import Flask,redirect, render_template,request
import pysftp 
import paramiko


app = Flask(__name__)

          ####################### mois années ########################
tabs_months = []
tab_years = range(2018, 2023, 1)
for mois in range(1,13,1):
    if mois < 10:
        mois = ' 0' + str(mois)
    tabs_months.append(mois)    
     

################### identifier ftp ####################
Hostname = "127.0.0.1"
Username = "ftpuser"
Password = "ftpuser"
   

                                      #LES ROUTES

##### route home#########
@app.route('/')
def home():
    return render_template('home.html' ) 


###### route mobile
@app.route('/Mobile/<numfacture>') 
def numDmob(numfacture):
    return render_template('mobile.html' ,numfacture = numfacture, tab_months = tabs_months, tab_years = tab_years) 


########## route fixe
@app.route('/Fixe/<numfacture>') 
def numclientfix(numfacture):
    return render_template('fixe.html' ,numfacture=numfacture, tab_months = tabs_months, tab_years = tab_years)  


########### recup chemin ###########
endpoint = None
@app.route('/apis', methods=["POST"]) 
def apis():
    b = request.get_data()
    r = json.loads(b.decode())
    nomfact= r["nomfact"]
    univers = r["univers"]
    print(univers)
    type = r["type"]
    mois = r["mois"]
    year = r["year"]
    numfacture = recupnum(nomfact)
    # print(numfacture)
    if type == "Fact":
        endpoint = f'/ftpuser/fadet/factures/dossier_50877/{univers}/Fact/{year}/{mois}/{numfacture}'
    else:
        endpoint = f'/ftpuser/fadet/factures/dossier_50877/{univers}/Bord/pdf/{year}/{mois}/{numfacture}'
   
    ################# connexion server ftp ############
    svt = pysftp.Connection( host=Hostname, username=Username, password=Password)
    print("Connection succesfully stablished ...  ")

    ####################### telecharger un fichier ###############
    remoteFilePath2 = f"/home/tourediaby/Images/{numfacture}"
    localFilePath2 = "/ftpuser/fadet/factures/dossier_50877/Mobile/Fact/2022/08/770992040P2208097195.pdf"
    print(endpoint)
    svt.get(localFilePath2, remoteFilePath2) 
    return request.url

############## recup numfacture ####################""
def recupnum(nomfact):    
    with open ('Liste_factures_Mobile_202208.csv','r') as f:
        listes = csv.reader(f)
        for ligne in listes:
            splite = ligne[0].split('P')[0]
            if nomfact==splite:
                return  ligne[0]


     

  


   

















if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=2000)