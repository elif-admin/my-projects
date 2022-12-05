from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1 = 1176455, number2 = 2290065340)

@app.route('/sum')
def number():
    var1, var2 = 15215640, 38965430 #buradaki degiskenlere deger atadik.
    return render_template('body.html', value1 = var1, value2 = var2, sum = var1+var2)


if __name__ == '__main__':
    app.run(debug=True) ##devops olarak port bulmak onemli,burasi default olarak 5000 gelir