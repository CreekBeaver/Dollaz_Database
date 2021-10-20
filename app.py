from flask import Flask, render_template, json, request
import os
import database.db_connector as db

# Configuration
app = Flask(__name__)

# Database connection
db_connection = db.connect_to_database()

# Routes

'''
Very Important notes and thoughts:

- Create a dictionary so you can map input columns to their data types for data correction and validation
- Create individual functions taht can perform the "Insert", "Update" and "Delete" Options so you dont
need to continually re-iterate them in your code. This will also reduce Hard coding. 
'''
def delete(table_id, primary_key, value):
	query = 'DELETE FROM ' + table_id + ' '
	query += 'WHERE '
	query = query + primary_key + '=' + value + ";"

	return query


@app.route('/')
def root():
	return render_template("index.j2")


@app.route('/customers')
def customers():
	return render_template("customer.j2", customers=results)


@app.route('/derivative_data')
def derivative_data():
	return render_template('derivative_data.j2', derivatives=results)

@app.route('/update_employees', methods=['GET','POST'])
def update_employees():
	return render_template('update_employee.j2', employees=results)

@app.route('/employees', methods=['GET', 'POST'])
def employees():
	return render_template('employees.j2', employees=results)


@app.route('/jet_data')
def jet_data():
	return render_template('jet_data.j2', jets=results)


@app.route('/lease_requests')
def lease_requests():
	return render_template('lease_requests.j2')


@app.route('/lease')
def lease():
	return render_template('lease.j2')



# Listener
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 9112))
	app.run(port=port, debug=True)