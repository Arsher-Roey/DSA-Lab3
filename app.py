import math
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', active_page='home')

@app.route('/profile')
def profile():
    return render_template('profile.html', active_page='profile')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)
    
@app.route('/areaofcircle', methods=['GET', 'POST'])
def areaofcircle():
    area = None
    if request.method == 'POST':
        radius = request.form.get('radius', '')
        if radius: 
            try:
                radius = float(radius)
                area = round(math.pi * (radius**2), 2)
            except ValueError:
                area = 'Invalid Input. Please Enter a Number.'
    return render_template('areaofcircle.html', area=area)

@app.route('/areaoftriangle', methods=['GET', 'POST'])
def areaoftriangle():
    area = None
    if request.method == 'POST':
        height = request.form.get('height', '')
        base = request.form.get('base', '')
        if base and height:
            try:
                base = float(base)
                height = float(height)
                area = (base*height)/2
            except ValueError:
                area = 'Invalid Input. Pleae Enter a Number.'
    return render_template('areaoftriangle.html', area=area)

@app.route('/works')
def works():
    return render_template('works.html', active_page='works')

@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

if __name__ == "__main__":
    app.run(debug=True)
