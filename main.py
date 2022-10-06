from flask import Flask,redirect, render_template, template_rendered,request

app = Flask(__name__)



                                      #LES ROUTES

@app.route('/')
def home():
    return render_template('home.html' ) 



@app.route('/mobile/<numfacture>') 
def numDmob(numfacture):
    return render_template('mobile.html' ,numfacture=numfacture) 



@app.route('/fixe/<numfacture>') 
def numclientfix(numfacture):
    return render_template('fixe.html' ,numfacture=numfacture) 



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