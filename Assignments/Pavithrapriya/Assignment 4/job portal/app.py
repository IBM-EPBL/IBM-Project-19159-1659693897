from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'df3asd24sfasd4asd26@45tas0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
