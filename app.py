from flask import Flask, render_template,request
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    web_title = "Halaman Utama"
    return render_template('home.html', web_title=web_title)

@app.route("/about")
def about():
    web_title = "Halaman About"
    return render_template('about.html', web_title=web_title)

@app.route("/usia", methods=['GET','POST'])
def usia():
    if request.method == 'POST':
        tahun_lahir=int(request.form['tahun_lahir'])
        tahun_sekarang= 2024
        usia = tahun_sekarang - tahun_lahir
        return render_template('usia.html', usia=usia)
    return render_template('usia.html', umur=None)
    


if __name__=="__main__":
    app.run(debug=True)