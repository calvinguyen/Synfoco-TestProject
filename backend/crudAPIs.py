import flask
from flask import jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import URL
from mssql import create_cnxn, execute_query, execute_read_query, execute_read_dic

connection_string = "DRIVER={SQL Server};SERVER=172.26.54.133;DATABASE=Synfoco_Logistic_Management_System;UID=synfoco;PWD=synfoco16;Trusted_Connection=no;"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

#setting up an application name
app = flask.Flask(__name__) #sets up the application
app.config['SQLALCHEMY_DATABASE_URI'] = connection_url
app.config["DEBUG"] = True #allow to show errors in browser

# setting up home page to test connection
@app.route('/', methods=['GET'])
def home():
    return "<h1>Test Connection</h1>"

#(DONE) returns Customers table
@app.route('/api/customers', methods=['GET'])
def getcustomers():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    query = 'SELECT * FROM Customers'
    #execute sql return statement and get customer records
    customers = execute_read_query(cnxn, query)
    return jsonify(customers)

#(DONE) returns Companies tables
@app.route('/api/companies', methods=['GET'])
def getcompanies():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    query = 'SELECT * FROM Companies'
    #execute sql return statement and get companies records
    companies = execute_read_query(cnxn, query)
    return jsonify(companies)

#(DONE) returns Drivers tables
@app.route('/api/drivers', methods=['GET'])
def getdrivers():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    query = 'SELECT * FROM Drivers'
    #execute sql return statement and get drivers records
    drivers = execute_read_query(cnxn, query)
    return jsonify(drivers)

#DONE returns Employees tables
@app.route('/api/employees', methods=['GET'])
def getemployees():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    query = 'SELECT * FROM Employees'
    #execute sql return statement and get employees records
    employees = execute_read_query(cnxn, query)
    return jsonify(employees)

#DONE returns Orders tables
@app.route('/api/orders', methods=['GET'])
def getorders():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    query = 'SELECT * FROM Orders'
    #execute sql return statement and get orders records
    orders = execute_read_query(cnxn, query)
    return jsonify(orders)

#DONE DELETE record in Companies table
@app.route('/api/companies/<int:id>', methods=['DELETE'])
def deletecompany():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    query = 'SELECT * FROM Orders'
    #execute sql return statement and get customer records
    orders = execute_read_query(cnxn, query)
    return jsonify(orders)



@app.route('/api/testpost', methods=['POST'])
def testpost():
    req_data = request.get_json()
    newid = req_data['id']
    newfn = req_data['firstname']
    return 'ID: {}, Name: {}'.format(newid, newfn)





app.run()