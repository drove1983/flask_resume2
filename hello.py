from flask import Flask, render_template

app = Flask(__name__)

# Create Index Page
@app.route('/')
def index():
    ime = "Vedran"
    omiljena_pica = ["gljive", "sir", "kecap", "salama"]
    return render_template("index.html", ime=ime,
                           omiljena_pica=omiljena_pica)

# Create About page
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(port=8080, debug=True)


