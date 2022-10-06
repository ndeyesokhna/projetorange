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



# @app.route('/fixe/numd') 
# def numDfix():
#     return render_template('numDfix.html')     

# @app.route('/mobile/numcli') 
# def numclientmob():
#     return render_template('numclientmob.html')


# @app.route('/fixmobile') 
# def fixmobile():
#     return render_template('fixmobile.html')    

















if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=2000)