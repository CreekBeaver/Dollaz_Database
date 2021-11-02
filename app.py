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
	if request.method == "GET":
		results = select_data('customer')
		return render_template('customer.j2', customers=results)
	if request.method == "POST":
		results = select_data('customer')
		return render_template("customer.j2", customers=results)

@app.route('/update_customer', methods=['GET','POST'])
def update_customer():
	if request.method == "GET":
		results = select_data('customer')
		return render_template('update_customer.j2', customers=results)


@app.route('/update_employee', methods=['GET','POST'])
def update_employee():
	# Obtain the Update Employee Page
	if request.method == "GET":
		employee_id = request.args['update']
		query = "SELECT * FROM employee WHERE employee_id = " + employee_id + ";"
		cursor = db.execute_query(db_connection=db_connection, query=query)
		results = cursor.fetchall()
		return render_template('update_employee.j2', data=results)


@app.route('/employee', methods=['GET', 'POST'])
def employee():

	if request.method == "GET":
		results = select_data('employee')
		return render_template('employee.j2', data=results)
	if request.method == "POST":

		# Insert Functionality
		if 'add_row' in request.form.keys():
			first_name = "'" + request.form['first_name'] + "'"
			last_name = "'" + request.form['last_name'] + "'"
			start_date = "'" + request.form['employment_start_date'] + "'"

			# Need to handle the Null Entry
			if request.form['employment_end_date'].lower() == 'null':
				end_date = "NULL"
			else:

				end_date = "'" + request.form['employment_end_date'] + "'"
			title = "'" + request.form['title'] + "'"
			salary = request.form['salary']

			query = "INSERT into employee (first_name, last_name, employment_start_date, employment_end_date, title, salary)"
			query += "VALUES (" + first_name + ',' + last_name + ',' + start_date + ',' + end_date + ',' + title + ',' + salary
			query += ');'
			cursor = db.execute_query(db_connection=db_connection, query=query)

		# Delete Functionality
		if 'delete' in request.form.keys():
			query = "DELETE FROM employee WHERE employee_id="
			query += request.form['delete'] + ';'
			cursor = db.execute_query(db_connection=db_connection, query=query)


		# Update Functionality
		if 'update' in request.form.keys():
			employee_id = request.form['update']
			first_name = "'" + request.form['first_name'] + "'"
			last_name = "'" + request.form['last_name'] + "'"
			start_date = "'" + request.form['employment_start_date'] + "'"

			# Need to handle the Null Entry
			if request.form['employment_end_date'].lower() == 'none' or request.form['employment_end_date'].lower() == 'null':
				end_date = "NULL"
			else:

				end_date = "'" + request.form['employment_end_date'] + "'"
			title = "'" + request.form['title'] + "'"
			salary = request.form['salary']

			query = "UPDATE employee SET first_name=" + first_name +","
			query += 'last_name=' + last_name + ","
			query += 'employment_start_date=' + start_date + ','
			query += 'employment_end_date=' + end_date + ','
			query += 'title=' + title + ','
			query += 'salary=' + salary
			query += 'WHERE employee_id=' + employee_id + ';'
			cursor = db.execute_query(db_connection=db_connection, query=query)

		results = select_data('employee')
		return render_template('employee.j2', data=results)

@app.route('/update_jet_data')
def update_jet_data():
	if request.method == "GET":
		results = select_data('jet_data')
		return render_template('update_jet_data.j2', jets=results)

@app.route('/jet_data')
def jet_data():
	if request.method == "GET":
		results = select_data('jet_data')
		return render_template('jet_data.j2', jets=results)

@app.route('/derivative_data')
def derivative_data():
	if request.method == "GET":
		results = select_data('derivative_data')
		return render_template('derivative_data.j2', data=results)

@app.route('/update_derivative_data')
def update_derivative_data():
	if request.method == "GET":
		results = select_data('derivative_data')
		return render_template('update_derivative_data.j2', data=results)

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