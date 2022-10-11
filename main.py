from crypt import methods
import json
from urllib import response
from flask import Flask,redirect, render_template, template_rendered,request

app = Flask(__name__)


tabs_months = range(1,13,1)
tab_years = range(2018, 2023, 1)



                                      #LES ROUTES

@app.route('/')
def home():
    return render_template('home.html' ) 



@app.route('/mobile/<numfacture>') 
def numDmob(numfacture):
    return render_template('mobile.html' ,numfacture = numfacture, tab_months = tabs_months, tab_years = tab_years) 



@app.route('/fixe/<numfacture>') 
def numclientfix(numfacture):
    return render_template('fixe.html' ,numfacture=numfacture, tab_months = tabs_months, tab_years = tab_years) 



@app.route('/apis', methods=["POST"]) 
def apis():
    b = request.get_data()
    r = json.loads(b.decode())
    univers = r["univers"]
    type = r["type"]
    mois = r["mois"]
    year = r["year"]
    Factures = f'/fadet/factures/dossier_50877/{univers}/{type}/{year}/{mois}/'
    print(Factures)
    return request.url


# Factures = f'/fadet/factures/dossier_50877/{univers}/Fact/{annee}/{mois}/'

 

# Bordereau = f'/fadet/factures/dossier_50877/{univers}/Bord/pdf/{annee}/{mois}/'
# @app.route('/login',methods=['get','post']) 
# def login():
#         print(request.form)
#         return 'page de traitement'     

  


   

















if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=2000)