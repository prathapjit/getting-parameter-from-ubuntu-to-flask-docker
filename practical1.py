from flask import Flask,url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'manickam!'



@app.route('/sum/<int:a_value>')
def addtion(a_value):
    add=a_value+5
    return "%d" % add

@app.route('/sub/<int:s_value>')
def subtraction(s_value):
    sub=s_value-5
    return "%d" % sub

@app.route('/mul/<int:m_value>')
def multiply(m_value):
    mul=m_value*5
    return "%d" % mul
   
    
    
  
@app.route('/name')
def hello_world1():
    return 'prathap!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

#methods=['POST''GET']
#<int:value>',methods=['POST''GET']