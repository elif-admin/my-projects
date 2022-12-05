from flask import Flask

app = Flask(__name__)

@app.route('/') #anasayfa demektir.
def hello():
    return "Hello World from Flask!!!"

@app.route('/second')
def second():
    return 'Bize Her Yer Trabzon!!!!'

@app.route('/third/subthird')
def third():
    return 'This is the subpage of third page'

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'




if __name__ == '__main__':
    app.run(debug=True) #true dan sonra port ekleyebilirsin.port kisminda bisey yazmazsa browsera localhost:5000 yazip enterlayinca web sayfasi acilir.
#debug mode : hata ayiklama modudur, eger; yukaridaki komutlarda syntax hatasi yaparsak(: koymayi unutmak gibi) terminalde bu hatayi syntax hatasi olarak verir.