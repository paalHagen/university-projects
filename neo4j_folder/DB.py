from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import json

URI = "neo4j+s://b729d323.databases.neo4j.io"
AUTH = ("neo4j", "passord")

def _get_connection() -> Driver:
    driver =GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties

# --------------------------------------------------------------------------------------------------------------------------------------
#             CAR METODENE:

def create_car(car_id,make,model,year,location,status):
     
    cars = _get_connection().execute_query("MERGE (a:Car{id:$id, make:$make, model:$model, reg:$reg, year:$year,location:$location, status:$status})RETURN a;", 
    id=id, make=make, model=model, year=year,location=location,status=status)

    nodes_json = [node_to_json(record["a"])for record in cars]
    print(nodes_json)
    return nodes_json

def read_cars():
    with _get_connection()._session() as session:
        cars = session.run("MATCH (a:Car) RETURN a;")
        nodes_json = [node_to_json(record["a"])for record in cars]
        print(nodes_json)
        return nodes_json

def update_car(id,make,model,year,location,status):
    with _get_connection()._session() as session:
        cars = session.run("MATCH (a:Car{id:$id}) set a.make=$make, a.model=$model, a.year=$year,a.location=$location,a.status=$status RETURN a;",
        id=id, make=make, model=model, year=year, location=location,status=status)

        print(cars)

        nodes_json = [node_to_json(record["a"])for record in cars]
        print(nodes_json)

        return nodes_json

def delete_car(id):

    _get_connection().execute_query("MATCH (a:Car{id:$id}) delete a;", id=id)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                   CUSTOMER METODENE

def create_customer(customer_id, name, age, address):

    customers = _get_connection().execute_query("MERGE (a:Customer{customer_id:$customer_id, name:$name, age:$age, address:$address})RETURN a;",
    customer_id=customer_id, name=name,age=age,address=address)

    nodes_json = [node_to_json(record["a"])for record in customers]
    print(nodes_json)
    return nodes_json

def read_customers():
    with _get_connection()._session() as session:
        customers = session.run("MATCH (a:Customers) RETURN a;")
        nodes_json = [node_to_json(record["a"])for record in customers]
        print(nodes_json)
        return nodes_json

def update_customer(customer_id, name, age, address):
    with _get_connection()._session() as session:
        customers = session.run("MATCH (a:Customer{customer_id:$customer_id}) set a.name=$name, a.age=$age, a.address=$address RETURN a;",
        customer_id=customer_id, name=name, age=age, address=address)

        print(customers)
        
        nodes_json = [node_to_json(record["a"])for record in customers]
        print(nodes_json)
        return nodes_json

def delete_customer(customer_id):
    _get_connection().execute_query("MATCH (a:Customer{customer_id:$customer_id}) delete a;", customer_id=customer_id)


# ---------------------------------------------------------------------------------------------------------------------------------------------------
#                   EMPLOYEE METODENE

def create_employee(employee_id, name, address, branch):

    employees = _get_connection().execute_query("MERGE (a:Employee{employee_id:$employee_id, name:$name, address:$address, branch:$branch})RETURN a;",
    employee_id=employee_id, name=name, address=address, branch=branch)

    nodes_json = [node_to_json(record["a"])for record in employees]
    print(nodes_json)
    return nodes_json

def read_employees():
    with _get_connection()._session() as session:
        employees = session.run("MATCH (a:Employees) RETURN a;")
        nodes_json = [node_to_json(record["a"])for record in employees]
        print(nodes_json)
        return nodes_json

def update_employee(employee_id, name, address, branch):
    with _get_connection()._session() as session:
        employees = session.run("MATCH (a:Employee{employee_id:$employee_id}) set a.name=$name, a.address=$address, a.branch=$branch RETURN a;",
        employee_id, name, address, branch)

        print(employees)

        nodes_json = [node_to_json(record["a"])for record in employees]
        print(nodes_json)
        
        return nodes_json

def delete_employee(employee_id):
    _get_connection().execute_query("MATCH (a:Employee{employee_id:Semployee_id}) delete a;", employee_id=employee_id)