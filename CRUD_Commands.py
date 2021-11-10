def table_insert(table_name, request):

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
        max_takeoff_weight = request.form['make_takeoff_weight']


        query = "INSERT into derivative_data (model_derivative, body_style, primary_use, flight_range, max_seating, fuel_efficiency, max_takeoff_weight)"
        query += "VALUES (" + model_derivative + ',' + body_style + ',' + primary_use + ',' + flight_range + ',' + max_seating + ',' + fuel_efficiency + ',' + max_takeoff_weight
        query += ');'
        cursor = db.execute_query(db_connection=db_connection, query=query)

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


def table_delete(table_name, request):
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


def table_update(table_name, request):
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
        print('lease')

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
        max_takeoff_weight = request.form['make_takeoff_weight']


        query = "INSERT into derivative_data (model_derivative, body_style, primary_use, flight_range, max_seating, fuel_efficiency, max_takeoff_weight)"
        query += "VALUES (" + model_derivative + ',' + body_style + ',' + primary_use + ',' + flight_range + ',' + max_seating + ',' + fuel_efficiency + ',' + max_takeoff_weight
        query += ');'
        cursor = db.execute_query(db_connection=db_connection, query=query)