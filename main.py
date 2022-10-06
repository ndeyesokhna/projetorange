from flask import Flask,redirect, render_template, template_rendered,request

app = Flask(__name__)



                                      #LES ROUTES

@app.route('/')
def home():
    return render_template('home.html' ) 


@app.route('/mobile') 
def mobile():
    return render_template('mobile.html')   




@app.route('/fix') 
def fix():
    return render_template('fix.html') 

@app.route('/fixmobile') 
def fixmobile():
    return render_template('fixmobile.html')    








































if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=2000)