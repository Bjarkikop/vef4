from flask import Flask, render_template, url_for
app = Flask(__name__)

nofn = [
		["Jón Jónsson","1234567890"],
		["Jón Björnsson","1234567891"],
		["Matti Hinriksson","1234567893"],
		["Siggi Hinriksson","1234567894"] 	
		]


@app.route('/')
def index():
	return render_template('index.tpl', nofn=nofn)

@app.errorhandler(404)
def error404(error):
	return '<h1>Þessi síða er ekki til</h1>', 404

@app.route("/<nr>")
def kt(nr):
	# reikna þversummu fyrir nr
	þversumma = 0
	for i in nr:
		þversumma = þversumma + int(i)
	return render_template('dversumma.html', kt=nr, summa=þversumma)
if __name__ == "__main__":
	app.run(debug=True)
	