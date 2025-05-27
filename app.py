from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

payments = []

@app.route('/')
def index():
    return render_template('index.html', payments=payments)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    amount = request.form['amount']
    month = request.form['month']
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    payments.append({
        'name': name,
        'amount': amount,
        'month': month,
        'date': date
    })
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(payments):
        payments.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=False)

