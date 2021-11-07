-- These are the Database Manipulation Queries for Group 75 - Dollaz & Databases

-- -----------
-- customer --
-- -----------

-- get all customers and attributes
SELECT * FROM customer;

-- add a new customer
INSERT INTO customer (name, contact_num, address) 
VALUES (:name_input, :contact_num_input, :address_input);

-- update an existing customer
UPDATE customer
SET name = :name_input, contact_num = :contact_num_input, address = :address_input
WHERE customer_id = :customer_id_selected;

-- delete a customer
DELETE FROM customer WHERE customer_id = :customer_id_selected;

-- ------------------
-- derivative_data --
-- ------------------

-- get all jet derivatives and attributes
SELECT * FROM derivative_data;

-- add a new derivative
INSERT INTO derivative_data (model_derivative, body_style, primary_use, 
            flight_range, max_seating, fuel_efficiency, max_takeoff_weight)
VALUES (:model_derivative_input, :body_style_input, :primary_use_input, :flight_range_input, 
        :max_seating_input, :fuel_efficiency_input, :max_takeoff_weight_input);

-- update an existing derivative
UPDATE derivative_data
SET model_derivative = :model_derivative_input, body_style = :body_style_input, 
    primary_use = :primary_use_input, flight_range = :flight_range_input, max_seating = :max_seating_input, 
    fuel_efficiency = :fuel_efficiency_input, max_takeoff_weight = :max_takeoff_weight_input 
WHERE derivative_id = :derivative_id_selected;

-- delete a derivative
DELETE FROM derivative_data WHERE derivative_id = :derivative_id_selected;

-- -----------
-- employee --
-- -----------

-- get all employees and attributes
SELECT * FROM employee;

-- add a new employee
INSERT INTO employee (first_name, last_name, employment_start_date, employment_end_date, title, salary)
VALUES (:first_name_input, :last_name_input, :employment_start_date_input, :employment_end_date_input,
        :titleInput, :salary_input);

-- update an existing employee
UPDATE employee
SET first_name = :first_name_input, last_name = :last_name_input, employment_start_date = :employment_start_date_input, 
    employment_end_date = :employment_end_date_input, title = :title_input, salary =:salary_input
WHERE employee_id = :employee_id_selected;

-- delete an employee
DELETE FROM employee WHERE employee_id_input = :employee_id_selected;

-- filter employees
-- filter by employee id
SELECT * FROM employee WHERE employee_id = :employee_id_input;
-- filter by first_name
SELECT * FROM employee WHERE first_name = :first_name_input;
-- filter by last_name
SELECT * FROM employee where last_name = :last_name_input;
-- filter by employment start date
SELECT * FROM employee where employment_start_date = :employment_start_date_input;
-- filter by employment end date
SELECT * FROM employee WHERE employment_end_date = :employment_end_date_input;
-- filter by title
SELECT * FROM employee WHERE title = :title_input;
-- filter by salary
SELECT * FROM employee WHERE salary = :salary_input;

-- -----------
-- jet_data --
-- -----------

-- get all jets and attributes
SELECT * FROM jet_data;

-- add a new jet
INSERT INTO jet_data (derivative_id, num_engine, flight_cycle, market_value, payload)
VALUES (:derivative_id_input, :num_engine_input, :flight_cycle_input, :market_value, 
        :payload_input);

-- update jet
UPDATE jet_data
SET derivative_id = :derivative_id_input, num_engine = :num_engine_input, flight_cycle = :flight_cycle_input, 
    market_value = :market_value, payload = :payload_input
WHERE jet_id = :jet_id_selected;

-- delete a jet
DELETE FROM jet_data WHERE jet_id = :jet_id_selected;

-- --------
-- lease --
-- --------

-- get all leases and attributes
SELECT * FROM lease;

-- add a new lease
INSERT INTO lease (customer_id, jet_id, lease_status, start_date, end_date, duration, 
            ground_staff_included, crew_included, lease_value, payment_to_date, payment_remaining)
VALUES (:customer_id_input, :jet_id_input, :lease_status_input, :start_date_input, :end_date_input,
        :duration_input, :ground_staff_included_input, :crew_included_input, :lease_value_input, 
        :payment_to_date_input, :payment_remaining_input);

-- update lease
UPDATE lease
SET customer_id = :customer_id_input, jet_id = :jet_id_input, lease_status = :lease_status_input, 
    start_date = :start_date_input, end_date = :end_date_input, duration = :duration_input, 
    ground_staff_included = :ground_staff_included_input, crew_included = :crew_included_input, 
    lease_value = :lease_value_input, payment_to_date = :payment_to_date_input, 
    payment_remaining = :payment_remaining_input
WHERE lease_id = lease_id_selected;

-- delete a lease
DELETE FROM lease WHERE lease_id = :lease_id_selected;

-- ----------------
-- lease_request --
-- ----------------

-- get all lease requests and attributes
SELECT * FROM lease_request;

-- add a new lease request
INSERT INTO lease_request (customer_id, derivative_id, need_ground_staff, need_crew)
VALUES (:customer_id_input, :derivative_id_input, :need_ground_staff_input, :need_crew_input)

-- update lease request
UPDATE lease_request
SET customer_id = :customer_id_input, derivative_id = :derivative_id_input, 
    need_ground_staff = :need_ground_staff_input, need_crew :need_crew_input
WHERE request_id = :request_id_selected

-- delete a request
DELETE FROM lease_request WHERE request_id = :request_id_selected;

-- ----------------------
-- aircraft_assignment --
-- ----------------------

-- get all aircraft assignments
SELECT * FROM aircraft_assignment;

-- associate an employee to a lease (M-to-M relationship addition)
INSERT INTO aircraft_assignment (lease_id, employee_id)
VALUES (:lease_id_input, :employee_id_input) -- or _selected?

-- update aircraft assignment
UPDATE aircraft_assignment
SET lease_id = :lease_id_input, employee_id = employee_id_input -- or selected?
WHERE lease_id = :lease_id_selected AND employee_id = :employee_id_selected

-- delete aircraft assignment
DELETE FROM aircraft_assignment WHERE lease_id = :lease_id_selected AND employee_id = :employee_id_selected;

-- -----------------------
-- Project Spec queries --
-- -----------------------

-- get all currently leased aircraft
SELECT jet_id FROM lease WHERE lease_status = "active";
-- get lease end dates
SELECT jet_id, end_date FROM lease where lease_status = "active";
-- get all lease request id's and lease end dates for the same derivative (shows upcoming lease opportunity)
SELECT request_id, model_derivative, lease_id, end_date FROM lease_request
INNER JOIN derivative_data ON lease_request.derivative_id = derivative_data.derivative_id
INNER JOIN jet_data ON derivative_data.derivative_id = jet_data.derivative_id
INNER JOIN lease ON jet_data.jet_id = lease.jet_id;