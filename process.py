import os
from flask import Flask, render_template, request, jsonify, current_app
from flask import send_from_directory, send_file

app = Flask(__name__)

array = [1, 2, 3, 4, 5,6,7, 8]
txtArray = """this is line  1\n
THis is line2\n
This is line 3"""


@app.route('/')
def index():
	return render_template('sqlproc.html')

@app.route('/SQLProcessor')
def sqlProcessor():
	return render_template('sqlproc.html')

@app.route('/sqlproc', methods=['POST'])
def sqlproc():
	print ("sqlproc is called")
	input = request.form['input']
	sqltype = request.form['sqltype']

	print ("input = ", input)
	print ("sqltype = ", sqltype)
	reverseInput = input[::-1]
	return jsonify({'output' : reverseInput})

@app.route('/getExample', methods=['POST'])
def getExample():
	value = request.form['input']
	print ("current  working directory = ", os.getcwd())
	print ("getExample  called", value)
	file_name = "example/example" + str(value).strip()
	# print ("file_name =", file_name)
	s = open(file_name, "r").read()
	return jsonify({'output' : s})

@app.route('/excelSQLConverter', methods=['GET', 'POST'])
def get_excelSQLConverter():
	print ("download called")
	print ("current  working directory = ", os.getcwd())
	return send_file(r"templates/sqlproc.html", attachment_filename = "osf", as_attachment = True)

@app.route('/getArray/<int:value>', methods=['GET', 'POST'])
def getArray(value):
	print ("getArray called")
	return  txtArray


if __name__ == '__main__':
	app.run(debug=True)