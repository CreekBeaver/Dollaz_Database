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
	db.execute_query(db_connection=db_connection, query=query)



def select_data(table_name):
	"""
	Performs a query for a given table to return all data.
	:param table_name: String, Consisting of a table name
	:return: Query from an SQL Tble.
	"""
	query = "SELECT * FROM " + table_name + ";"
	cursor = db.execute_query(db_connection=db_connection, query=query)
	results = cursor.fetchall()
	return results


def add_row(field_list, insert_list):
	pass


def update_row(table_name, column_1, new_value, key, id):
	query = "UPDATE " + table_name + " SET " + column_1 + " = " + "'" + new_value + "'" + " "
	query = query + "WHERE " + key + " = " + id + ';'
	db.execute_query(db_connection=db_connection, query=query)


@app.route('/')
def root():
	return render_template("index.j2")


@app.route('/customer')
def customers():
	return render_template("customer.j2", customers=results)


@app.route('/derivative_data')
def derivative_data():
	return render_template('derivative_data.j2', derivatives=results)


@app.route('/update_employee', methods=['GET','POST'])
def update_employees():
	if request.method == "GET":
		results = select_data('employee')
		return render_template('update_employee.j2', employees=results)
	if request.method == "POST":
		print(request.form)
		update_row('employee', request.form['column1'], request.form['value1'], 'employee_id', request.form['employee_id'])
		results = select_data('employee')
		return render_template('update_employee.j2', employees=results)


@app.route('/employee', methods=['GET', 'POST'])
def employees():

	if request.method == "GET":
		results = select_data('employee')
		return render_template('employee.j2', employees=results)
	if request.method == "POST":
		# Handles Adding Rows
		if "add_row" in request.form.keys():
			# Create a list that has all the fields for adding a row
			field_list = ['first_name', 'last_name', 'employment_start_date', 'employment_end_date', 'title', 'salary']
			value_list = []
			for field in field_list:
				if request.form[field] != '':
					value_list.append(request.form[field])

			# Ensures that all the appropriate fields are handled
			if len(field_list) == len(value_list):
				# Make a Call to the Add Row.
				pass

			# Need a way to pass an error message to the user. Right Now there is just a Non Action.

		# Handles Deletion of Rows
		if "delete" in request.form.keys():
			delete('employee', 'employee_id', request.form['delete'])

		results = select_data('employee')
		return render_template('employee.j2', employees=results)


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