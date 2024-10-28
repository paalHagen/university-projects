from neo4j import GraphDatabase, Driver

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
     with _get_connection().session() as session:
        cars = session.run(
            "MERGE (a:Car{car_id:$car_id, make:$make, model:$model, year:$year,location:$location, status:$status})RETURN a;", 
            car_id=car_id, make=make, model=model, year=year,location=location,status=status
        )
        nodes_json = [node_to_json(record["a"])for record in cars]
        return nodes_json

def read_cars():
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Car) RETURN a;")
        nodes_json = [node_to_json(record["a"])for record in cars]
        return nodes_json

def update_car(car_id,make,model,year,location,status):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Car{car_id:$car_id}) set a.make=$make, a.model=$model, a.year=$year,a.location=$location,a.status=$status RETURN a;",
        car_id=car_id, make=make, model=model, year=year, location=location,status=status)
        nodes_json = [node_to_json(record["a"])for record in cars]
        return nodes_json

def delete_car(car_id):

    _get_connection().execute_query("MATCH (a:Car{car_id:$car_id}) delete a;", car_id=car_id)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                   CUSTOMER METODENE

def create_customer(customer_id, name, age, address):
    with _get_connection().session() as session:
        customer = session.run(
            "MERGE (a:Customer{customer_id:$customer_id, name:$name, age:$age, address:$address})RETURN a;",
            customer_id=customer_id, name=name,age=age,address=address
        )
        nodes_json = [node_to_json(record["a"])for record in customer]
        return nodes_json

def read_customers():
    with _get_connection().session() as session:
        customers = session.run("MATCH (a:Customer) RETURN a;")
        nodes_json = [node_to_json(record["a"])for record in customers]
        return nodes_json

def update_customer(customer_id, name, age, address):
    with _get_connection().session() as session:
        customers = session.run("MATCH (a:Customer{customer_id:$customer_id}) set a.name=$name, a.age=$age, a.address=$address RETURN a;",
        customer_id=customer_id, name=name, age=age, address=address)
        nodes_json = [node_to_json(record["a"])for record in customers]
        return nodes_json

def delete_customer(customer_id):
    _get_connection().execute_query("MATCH (a:Customer{customer_id:$customer_id}) delete a;", customer_id=customer_id)


# ---------------------------------------------------------------------------------------------------------------------------------------------------
#                   EMPLOYEE METODENE

def create_employee(employee_id, name, address, branch):

    employees = _get_connection().execute_query("MERGE (a:Employee{employee_id:$employee_id, name:$name, address:$address, branch:$branch})RETURN a;",
    employee_id=employee_id, name=name, address=address, branch=branch)
    nodes_json = [node_to_json(record["a"])for record in employees]
    return nodes_json

def read_employees():
    with _get_connection().session() as session:
        employees = session.run("MATCH (a:Employee) RETURN a;")
        nodes_json = [node_to_json(record["a"])for record in employees]
        return nodes_json

def update_employee(employee_id, name, address, branch):
    with _get_connection().session() as session:
        employees = session.run("MATCH (a:Employee{employee_id:$employee_id}) set a.name=$name, a.address=$address, a.branch=$branch RETURN a;",
        employee_id, name, address, branch)
        nodes_json = [node_to_json(record["a"])for record in employees]
        return nodes_json

def delete_employee(employee_id):
    _get_connection().execute_query("MATCH (a:Employee{employee_id:$employee_id}) delete a;", employee_id=employee_id)

#  ORDER CAR METODENE
# ---------------------------------------------------------------

# ORDER a car
def order_car(customer_id, car_id):
    with _get_connection().session() as session:
        # sjekker om bilen er tilgjengelig
        car = session.run(
            "MATCH (a:Car {car_id: $car_id}) "
            "RETURN a.status AS status;",
            car_id=car_id).single()

        if car and car["status"] != 'available':
            return {"error": "This car is not available"}, 400
        
        # sjekker om customer allerede har bestilt en bil
        previous_order = session.run(
            "MATCH (c:Customer {customer_id: $customer_id})-[:ORDERED]->(a:Car) "
            "RETURN a LIMIT 1;",
            customer_id=customer_id).single()

        if previous_order:
            return {"error": "Customer has already ordered a car"}, 400
        
        # Hvis bilen er tilgjengelig og kunden ikke har bestilt en annen bil. Så vil bestillingen gå igjennom. 
        session.run(
            "MATCH (c:Customer {customer_id: $customer_id}), (a:Car {car_id: $car_id}) "
            "MERGE (c)-[:ORDERED]->(a) "
            "SET a.status = 'booked' "
            "RETURN c, a;",
            customer_id=customer_id, car_id=car_id)

        return {"status": "Car ordered and status updated to booked"}

# Cancel order

def cancel_order_car(customer_id, car_id):
    with _get_connection().session() as session:
        # Sjekker om kunden har bestilt en bil
        order = session.run(
            "MATCH (c:Customer {customer_id: $customer_id})-[r:ORDERED]->(a:Car {car_id: $car_id}) "
            "RETURN r;",
            customer_id=customer_id, car_id=car_id).single()

        if not order:
            return {"error": "No order found for this customer and car"}, 400

        # Om det er en bestilling mellom kunden til den bilen, blir det forholdet fjernet.
        session.run(
            "MATCH (c:Customer {customer_id: $customer_id})-[r:ORDERED]->(a:Car {car_id: $car_id}) "
            "DELETE r "
            "SET a.status = 'available' "
            "RETURN c, a;",
            customer_id=customer_id, car_id=car_id)

        return {"status": "Order canceled and car status updated to available"}


# Renting the car

def rent_car(customer_id, car_id):
    with _get_connection().session() as session:
        # Sjekker om kunden har booket bilen
        booking = session.run(
            "MATCH (c:Customer {customer_id: $customer_id})-[:ORDERED]->(a:Car {car_id: $car_id}) "
            "RETURN a;",
            customer_id=customer_id, car_id=car_id).single()

        if not booking:
            return {"error": "Customer does not have a booking for this car"}, 400
        
        # Hvis kunden har booket bilen, blir bilens status endret.
        session.run(
            "MATCH (c:Customer {customer_id: $customer_id})-[:ORDERED]->(a:Car {car_id: $car_id}) "
            "SET a.status = 'rented' "
            "RETURN a;",
            customer_id=customer_id, car_id=car_id)

        return {"status": "Car rented successfully, status updated to rented"}

#Return car

def return_car(customer_id, car_id, return_status):
    with _get_connection().session() as session:
        # Sjekker om kunden har leid bilen.
        rental = session.run(
            "MATCH (c:Customer {customer_id: $customer_id})-[:ORDERED|RENTED]->(a:Car {car_id: $car_id}) "
            "RETURN a;",
            customer_id=customer_id, car_id=car_id).single()

        if not rental:
            return {"error": "Customer has not rented this car"}, 400
        
        # Endrer statusen til bilen basert på tilstanden
        if return_status == 'ok':
            new_status = 'available'
        elif return_status == 'damaged':
            new_status = 'damaged'
        else:
            return {"error": "Invalid return status"}, 400

        # Oppdaterer bilens status på bilen og fjerner forholdet. 
        session.run(
            "MATCH (c:Customer {customer_id: $customer_id})-[r:ORDERED|RENTED]->(a:Car {car_id: $car_id}) "
            "DELETE r "
            "SET a.status = $new_status "
            "RETURN a;",
            customer_id=customer_id, car_id=car_id, new_status=new_status)

        return {"status": f"Car returned successfully, status updated to {new_status}"}