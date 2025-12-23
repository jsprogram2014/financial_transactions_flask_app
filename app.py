# Import libraries
from flask import Flask, request, url_for, render_template, redirect

# Instantiate Flask functionality
app=Flask(__name__)

# Sample data   
TRANSACTIONS = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route('/')
def get_transactions():
    return render_template("transactions.html",transactions=TRANSACTIONS)

# Create operation
@app.route('/add',methods=['GET','POST'])
def add_transaction():

    if request.method == 'POST':

        FORM_DATA={'id':len(TRANSACTIONS) + 1,
                   'date':request.form['date'],
                   'amount':int(request.form['amount'])}
        
        TRANSACTIONS.append(FORM_DATA)

        return redirect(url_for('get_transactions'))

    return render_template('form.html')


# Update operation
@app.route('/edit/<int:transaction_id>', methods=['POST','GET'])
def edit_transaction(transaction_id):

    for trans in TRANSACTIONS:
        if trans['id']==transaction_id:
            DATA_TO_BE_EDITED=trans

    if request.method=='POST':
        FORM_DATA=request.form

        for trans in TRANSACTIONS:
            if trans['id']==transaction_id:
                trans['date']=request.form['date']
                trans['amount']=int(request.form['amount'])
        
        return redirect(url_for('get_transactions'))

    return render_template('edit.html',transaction=DATA_TO_BE_EDITED)


# Delete operation
@app.route('/delete/<int:transaction_id>',methods=['GET'])
def delete_transaction(transaction_id):
    for i,trans in enumerate(TRANSACTIONS):
        if trans['id']==transaction_id:
            TRANSACTIONS.pop(i)
    
    return redirect(url_for('get_transactions'))

# Run the Flask app
    