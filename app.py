from flask import Flask, render_template, json, request
import os
import database.db_connector as db

# Configuration
app = Flask(__name__)

# Database connection
db_connection = db.connect_to_database()


def table_insert(table_name, request):
    """
    Wrapper will perform the insert operations on an SQL Table
    :param table_name: name of the table to insert values
    :param request: Request as recieved by Flask App
    :return: None Updates will occur in the Database
    """
    db_connection = db.connect_to_database()

    if table_name == 'customer':
        # Insert Functionality
        name = "'" + request.form['name'] + "'"
        contact_num = "'" + request.form['contact_num'] + "'"
        address = "'" + request.form['address'] + "'"

        query = "INSERT into customer (name, contact_num, address)"
        query += "VALUES (" + name + ',' + contact_num + ',' + address
        query += ');'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'employee':
        # Insert Functionality
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

    elif table_name == 'jet_data':
        # Insert Functionality
        derivative_id = request.form['derivative_id']
        num_engine = request.form['num_engine']
        flight_cycle = request.form['flight_cycle']
        market_value = request.form['market_value']
        payload = request.form['payload']

        query = "INSERT into jet_data (derivative_id, num_engine, flight_cycle, market_value, payload)"
        query += "VALUES (" + derivative_id + ',' + num_engine + ',' + flight_cycle + ',' + market_value + ',' + payload
        query += ');'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'lease':
        customer_id = request.form['customer_id']
        jet_id = request.form['jet_id']
        lease_status = "'" + request.form['lease_status'] + "'"
        start_date = "'" + request.form['start_date'] + "'"
        end_date = "'" + request.form['end_date'] + "'"
        duration = request.form['duration']
        ground_staff_included = request.form['ground_staff_included']
        crew_included = request.form['crew_included']
        lease_value = request.form['lease_value']
        payment_to_date = request.form['payment_to_date']
        payment_remaining = request.form['payment_remaining']


        query = "INSERT into lease (customer_id, jet_id, lease_status, start_date, end_date, duration, ground_staff_included, crew_included, lease_value, payment_to_date, payment_remaining)"
        query += "VALUES (" + customer_id + ',' + jet_id + ',' + lease_status + ',' + start_date + ',' + end_date + ',' + duration + ',' + ground_staff_included + ',' + crew_included + ',' + lease_value + ',' + payment_to_date + ',' + payment_remaining
        query += ');'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'lease_request':
        customer_id = request.form['customer_id']
        derivative_id = request.form['derivative_id']
        need_ground_staff = request.form['need_ground_staff']
        need_crew = request.form['need_crew']

        query = "INSERT into lease_request (customer_id, derivative_id, need_ground_staff, need_crew)"
        query += "VALUES (" + customer_id + ',' + derivative_id + ',' + need_ground_staff + ',' + need_crew
        query += ');'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'aircraft_assignment':
        lease_id = request.form['lease_id']
        employee_id = request.form['employee_id']

        query = "INSERT into aircraft_assignment (lease_id, employee_id)"
        query += "VALUES (" + lease_id + ',' + employee_id
        query += ');'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'derivative_data':
        # Insert Functionality
        model_derivative = "'" + request.form['model_derivative'] + "'"
        body_style = "'" + request.form['body_style'] + "'"
        primary_use = "'" + request.form['primary_use'] + "'"
        flight_range = request.form['flight_range']
        max_seating = request.form['max_seating']
        fuel_efficiency = request.form['fuel_efficiency']
        max_takeoff_weight = request.form['max_takeoff_weight']

        query = "INSERT into derivative_data (model_derivative, body_style, primary_use, flight_range, max_seating, fuel_efficiency, max_takeoff_weight)"
        query += "VALUES (" + model_derivative + ',' + body_style + ',' + primary_use + ',' + flight_range + ',' + max_seating + ',' + fuel_efficiency + ',' + max_takeoff_weight
        query += ');'
        cursor = db.execute_query(db_connection=db_connection, query=query)


def table_delete(table_name, request):
    """
    Deletes a row in a table given the table name and Flask Requeest
    :param table_name: string containing target table for row delete
    :param request: Request as recieved from Webpage
    :return: None: Deletes the row in the table
    """
    if table_name == 'customer':
        query = "DELETE FROM customer WHERE customer_id="
        query += request.form['delete'] + ';'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'employee':
        query = "DELETE FROM employee WHERE employee_id="
        query += request.form['delete'] + ';'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'jet_data':
        query = "DELETE FROM jet_data WHERE jet_id="
        query += request.form['delete'] + ';'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'lease':
        query = "DELETE FROM lease WHERE lease_id="
        query += request.form['delete'] + ';'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'lease_request':
        query = "DELETE FROM lease_request WHERE request_id="
        query += request.form['delete'] + ';'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'aircraft_assignment':
        query = "DELETE FROM aircraft_assignment WHERE lease_id="
        # Note; Might also need to delete the matching entity! That will require form change
        query += request.form['delete'] + ';'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'derivative_data':
        query = "DELETE FROM derivative_data WHERE derivative_id="
        query += request.form['delete'] + ';'
        cursor = db.execute_query(db_connection=db_connection, query=query)


def select_data(table_name):
    """
    Performs a query for a given table to return all data.
    :param table_name: String, Consisting of a table name
    :return: Query from an SQL Tble.
    """
    db_connection = db.connect_to_database()
    query = "SELECT * FROM " + table_name + ";"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return results


def table_update(table_name, request):
    """
    Performs an upate of a table in SQL
    :param table_name: Name of the table
    :param request: Request from the form
    :return:  Updates the table.
    """
    if table_name == 'customer':
        customer_id = request.form['update']
        name = "'" + request.form['name'] + "'"

        contact_num = "'" + request.form['contact_num'] + "'"
        address = "'" + request.form['address'] + "'"
        print('after address before query')
        query = "UPDATE customer SET name=" + name + ","
        query += 'contact_num=' + contact_num + ","
        query += 'address=' + address
        query += ' WHERE customer_id=' + customer_id + ';'
        print('here is the query!\n', query)
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'employee':
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
        query = "UPDATE employee SET first_name=" + first_name + ","
        query += 'last_name=' + last_name + ","
        query += 'employment_start_date=' + start_date + ','
        query += 'employment_end_date=' + end_date + ','
        query += 'title=' + title + ','
        query += 'salary=' + salary
        query += ' WHERE employee_id=' + employee_id + ';'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'jet_data':
        jet_id = request.form['update']
        derivative_id = request.form['derivative_id']
        num_engine = request.form['num_engine']
        flight_cycle = request.form['flight_cycle']
        market_value = request.form['market_value']
        payload = request.form['payload']

        query = "UPDATE jet_data SET derivative_id=" + derivative_id + ","
        query += 'num_engine=' + num_engine + ","
        query += 'flight_cycle=' + flight_cycle + ','
        query += 'market_value=' + market_value + ','
        query += 'payload=' + payload
        query += ' WHERE jet_id=' + jet_id + ';'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'lease':
        lease_id = request.form['update']
        customer_id = request.form['customer_id']
        jet_id = request.form['jet_id']
        lease_status = "'" + request.form['lease_status'] + "'"
        start_date = "'" + request.form['start_date'] + "'"
        end_date = "'" + request.form['end_date'] + "'"
        duration = request.form['duration']
        ground_staff_included = request.form['ground_staff_included']
        crew_included = request.form['crew_included']
        lease_value = request.form['lease_value']
        payment_to_date = request.form['payment_to_date']
        payment_remaining = request.form['payment_remaining']

        query = "UPDATE lease SET customer_id=" + customer_id + ","
        query += 'jet_id=' + jet_id + ","
        query += 'lease_status=' + lease_status + ','
        query += 'start_date=' + start_date + ','
        query += 'end_date=' + end_date + ","
        query += 'duration=' + duration + ','
        query += 'ground_staff_included=' + ground_staff_included + ','
        query += 'crew_included=' + crew_included + ','
        query += 'lease_value=' + lease_value + ','
        query += 'payment_to_date=' + payment_to_date + ','
        query += 'payment_remaining=' + payment_remaining
        query += ' WHERE lease_id=' + lease_id + ';'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'lease_request':
        request_id = request.form['update']
        customer_id = request.form['customer_id']
        derivative_id = request.form['derivative_id']
        need_ground_staff = request.form['need_ground_staff']
        need_crew = request.form['need_crew']

        query = "UPDATE lease_request SET customer_id=" + customer_id + ","
        query += 'derivative_id=' + derivative_id + ","
        query += 'need_ground_staff=' + need_ground_staff + ','
        query += 'need_crew=' + need_crew
        query += ' WHERE request_id=' + request_id + ';'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    # *** Note: This one is going to need some SERIOUS Re-work to actually work ***
    elif table_name == 'aircraft_assignment':
        lease_id = request.form['lease_id']
        employee_id = request.form['employee_id']

        query = "UPDATE aircraft_assignment SET lease_id=" + lease_id + ","
        query += 'employee_id=' + employee_id
        query += ' WHERE lease_id=' + lease_id + ';'
        cursor = db.execute_query(db_connection=db_connection, query=query)

    elif table_name == 'derivative_data':
        derivative_id = request.form['update']
        model_derivative = "'" + request.form['model_derivative'] + "'"
        body_style = "'" + request.form['body_style'] + "'"
        primary_use = "'" + request.form['primary_use'] + "'"
        flight_range = request.form['flight_range']
        max_seating = request.form['max_seating']
        fuel_efficiency = request.form['fuel_efficiency']
        max_takeoff_weight = request.form['max_takeoff_weight']

        query = "UPDATE derivative_data SET model_derivative=" + model_derivative + ","
        query += 'body_style=' + body_style + ","
        query += 'primary_use=' + primary_use + ','
        query += 'flight_range=' + flight_range + ','
        query += 'max_seating=' + max_seating + ','
        query += 'fuel_efficiency=' + fuel_efficiency + ','
        query += 'max_takeoff_weight=' + max_takeoff_weight
        query += ' WHERE derivative_id=' + derivative_id + ';'
        cursor = db.execute_query(db_connection=db_connection, query=query)

# --- Routes ---


@app.route('/')
def root():
    db_connection = db.connect_to_database()
    return render_template("index.j2")


@app.route('/employee', methods=['GET', 'POST'])
def employee():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        results = select_data('employee')
        return render_template('employee.j2', data=results)
    if request.method == "POST":
        # Insert Functionality
        if 'add_row' in request.form.keys():
            table_insert('employee', request)
        # Delete Functionality
        if 'delete' in request.form.keys():
            table_delete('employee', request)
        # Update Functionality
        if 'update' in request.form.keys():
            table_update('employee', request)

        results = select_data('employee')
        return render_template('employee.j2', data=results)


@app.route('/update_employee', methods=['GET','POST'])
def update_employee():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        employee_id = request.args['update']
        query = "SELECT * FROM employee WHERE employee_id = " + employee_id + ";"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template('update_employee.j2', data=results)


@app.route('/customer', methods=['GET', 'POST'])
def customers():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        results = select_data('customer')
        return render_template('customer.j2', customers=results)
    if request.method == "POST":
        if 'add_row' in request.form.keys():
            table_insert('customer', request)
        if 'delete' in request.form.keys():
            table_delete('customer', request)
        if 'update' in request.form.keys():
            table_update('customer', request)
        results = select_data('customer')
        return render_template("customer.j2", customers=results)


@app.route('/update_customer', methods=['GET','POST'])
def update_customer():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        customer_id = request.args['update']
        query = "SELECT * FROM customer WHERE customer_id = " + customer_id + ";"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template('update_customer.j2', customers=results)


@app.route('/jet_data', methods=["GET", "POST"])
def jet_data():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        results = select_data('jet_data')
        return render_template('jet_data.j2', jets=results)
    if request.method == "POST":
        if 'add_row' in request.form.keys():
            table_insert('jet_data', request)
        if 'delete' in request.form.keys():
            table_delete('jet_data', request)
        if 'update' in request.form.keys():
            table_update('jet_data', request)
        results = select_data('jet_data')
        return render_template('jet_data.j2', jets=results)


@app.route('/update_jet_data', methods=["GET", "POST"])
def update_jet_data():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        jet_id = request.args['update']
        query = "SELECT * FROM jet_data WHERE jet_id = " + jet_id + ";"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template('update_jet_data.j2', jets=results)


@app.route('/derivative_data', methods=["GET", "POST"])
def derivative_data():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        results = select_data('derivative_data')
        return render_template('derivative_data.j2', data=results)
    if request.method =="POST":
        if 'add_row' in request.form.keys():
            table_insert('derivative_data', request)
        if 'delete' in request.form.keys():
            table_delete('derivative_data', request)
        if 'update' in request.form.keys():
            table_update('derivative_data', request)
        results = select_data('derivative_data')
        return render_template('derivative_data.j2', data=results)


@app.route('/update_derivative_data')
def update_derivative_data():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        derivative_id = request.args['update']
        query = "SELECT * FROM derivative_data WHERE derivative_id = " + derivative_id + ";"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template('update_derivative_data.j2', data=results)


@app.route('/lease', methods=["GET", "POST"])
def lease():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        results = select_data('lease')
        return render_template('lease.j2', data=results)
    if request.method == "POST":
        if 'add_row' in request.form.keys():
            table_insert('lease', request)
        if 'delete' in request.form.keys():
            table_delete('lease', request)
        if 'update' in request.form.keys():
            table_update('lease', request)
        results = select_data('lease')
        return render_template('lease.j2', data=results)


@app.route('/update_lease', methods=["GET", "POST"])
def update_lease():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        lease_id = request.args['update']
        query = "SELECT * FROM lease WHERE lease_id = " + lease_id + ";"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template('update_lease.j2', data=results)


@app.route('/lease_request', methods=["GET", "POST"])
def lease_request():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        results = select_data('lease_request')
        return render_template('lease_request.j2', data=results)
    if request.method == "POST":
        if 'add_row' in request.form.keys():
            table_insert('lease_request', request)
        if 'delete' in request.form.keys():
            table_delete('lease_request', request)
        if 'update' in request.form.keys():
            table_update('lease_request', request)
        results = select_data('lease_request')
        return render_template('lease_request.j2', data=results)


@app.route('/update_lease_request', methods=["GET", "POST"])
def update_lease_request():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        request_id = request.args['update']
        query = "SELECT * FROM lease_request WHERE request_id = " + request_id + ";"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template('update_lease_request.j2', data=results)


@app.route('/aircraft_assignment', methods=["GET", "POST"])
def aircraft_assignment():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        results = select_data('aircraft_assignment')
        return render_template('aircraft_assignment.j2', data=results)
    if request.method == "POST":
        if 'add_row' in request.form.keys():
            table_insert('aircraft_assignment', request)
        if 'delete' in request.form.keys():
            table_delete('aircraft_assignment', request)
        if 'update' in request.form.keys():
            table_update('aircraft_assignment', request)
        results = select_data('aircraft_assignment')
        return render_template('aircraft_assignment.j2', data=results)


@app.route('/update_aircraft_assignment', methods=["GET", "POST"])
def update_aircraft_assignment():
    db_connection = db.connect_to_database()
    if request.method == "POST":
        lease_id = request.form['update'][1]
        employee_id = request.form['update'][4]
        query = "SELECT * FROM aircraft_assignment WHERE (lease_id = " + lease_id
        query += "AND employee_id = " + employee_id + ");"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template('update_aircraft_assignment.j2', data=results)

# Filter employees by last name


@app.route("/filter_employee", methods =["GET", "POST"])
def filter_employees():
    db_connection = db.connect_to_database()
    if request.method == "POST":
        employee_id = request.form['employee_filter']
        query = "SELECT * FROM employee WHERE employee_id = " + employee_id + ";"
        # Filter employees by last name
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template('employee.j2', data=results)

# Listener


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4520))
    app.run(port=port, debug=True)
    #app.run(host="flip1.engr.oregonstate.edu", port=4518, debug=True)