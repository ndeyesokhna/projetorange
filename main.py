from crypt import methods
import csv
import email
from http import client
import json
from urllib import response
import ftplib
from flask import Flask,redirect, render_template, send_file, request
import pysftp 
import paramiko
import os
import zipfile
import requests
from flask import Flask
from flask_mail import Mail , Message
from Onedrive import OneDrive


app = Flask(__name__)


          ####################### mois années ########################770992040
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


###### route mobile #############""
@app.route('/Mobile/<numfacture>') 
def numDmob(numfacture):
    return render_template('mobile.html' ,numfacture = numfacture, tab_months = tabs_months, tab_years = tab_years) 


########## route fixe
@app.route('/Fixe/<numfacture>') 
def numclientfix(numfacture):
    return render_template('fixe.html' ,numfacture=numfacture, tab_months = tabs_months, tab_years = tab_years)  


########### recup chemin ###########

@app.route('/apis', methods=["POST"]) 
def apis():
    b = request.get_data()
    r = json.loads(b.decode())
    nomfact= r["nomfact"]
    univers = r["univers"]
    type = r["type"]
    mois = r["mois"]
    year = r["year"]
    numfacture = recupnum(nomfact)
    nomclient=r["nomduclient"]
   
    if type == "Fact":
        endpoint = f'/ftpuser/fadet/factures/dossier_50877/{univers}/Fact/{year}/{mois}/{numfacture}'
    else:
        endpoint = f'/ftpuser/fadet/factures/dossier_50877/{univers}/Bord/pdf/{year}/{mois}/{numfacture}'
   
    
    ################# connexion server ftp ############
    svt = pysftp.Connection( host=Hostname, username=Username, password=Password)
    print("Connection succesfully stablished ...  ")

    ####################### telecharger un fichier ###############
    if not os.path.exists(f"{nomclient}"):
        os.makedirs(f"{nomclient}")
    remote = f"./{nomclient}/{numfacture}"
    re =f"./{nomclient}"
    # print(re)
    svt.get(endpoint, remote)
    file_zip =  f'{re}.zip'
    zip_directory(re, file_zip)  
    return {'value':nomclient}


############## recup numfacture ####################""
def recupnum(nomfact):    
    with open ('Liste_factures_Mobile_202208.csv','r') as f:
        listes = csv.reader(f)
        for ligne in listes:
            splite = ligne[0].split('P')[0]
            if nomfact==splite:
                return  ligne[0]

################### zip le folder ###################
def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, mode='w') as zipf:
        len_dir_path = len(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path:])
                
     
################## route envoyer ############   
@app.route('/envoyer/') 
def envoyer():
    return render_template('envoyer.html')
  

##################### telecharger #############
@app.route('/downloads/<type>' ) 
def downloads(type):
    file_zip =   f'{type}.zip'
    return send_file(file_zip,as_attachment=True)

################ onedrive ################"
@app.route('/onedrive' , methods = ["POST"])
def onedrive():
    dataone = request.get_data()
    datadrive = json.loads(dataone.decode())
    email= datadrive["email"]
    password= datadrive["password"]
    url_user= datadrive["url"]
    nomclient=datadrive["client"]
    # print(nomclient)
    path_folder_name_local = f'./{nomclient}'
    # print(entry_point)


    # session = OneDrive(email = email, password = password, url_user = entry_point)
    # session.create_folder_on_onedrive(nomclient)
   

    # session.upload_files_to_onedrive(path_folder_name_local, nomclient)

    return "ytty"

















if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=2000)