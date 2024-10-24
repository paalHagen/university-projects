from flask import Flask, request
from neo4j_folder.DB import create_car, read_cars, update_car, delete_car
from neo4j_folder.DB import create_customer, read_customers, update_customer, delete_customer
from neo4j_folder.DB import create_employee, read_employees, update_employee, delete_employee
from neo4j_folder.DB import order_car, cancel_order_car, rent_car, return_car

app = Flask(__name__)

# --------------------------------------------------------------------------------------------------------------------------------------
#             Endpoints -> Cars:

@app.route("/cars", methods=["POST"])
def create_car_route():
    data = request.get_json()
    return create_car(data["car_id"],data["make"], data["model"], data["year"], data["location"], data["status"])

@app.route("/cars", methods=["GET"])
def read_cars_route():
    return read_cars()

@app.route("/cars", methods=["PUT"])
def update_car_route():
    data = request.get_json()
    return update_car(data["car_id"], data["make"], data["model"], data["year"], data["location"], data["status"])

@app.route("/cars", methods=["DELETE"])
def delete_car_route():
    data = request.get_json()
    delete_car(data["car_id"])
    return read_cars()

# --------------------------------------------------------------------------------------------------------------------------------------
#             Endpoints -> Customers:

@app.route("/customers", methods=["POST"])
def create_customer_route():
    data = request.get_json()
    return create_customer(data["customer_id"],data["name"], data["age"], data["address"])

@app.route("/customers", methods=["GET"])
def read_customers_route():
    return read_customers()

@app.route("/customers", methods=["PUT"])
def update_customer_route():
    data = request.get_json()
    return update_customer(data["customer_id"],data["name"], data["age"], data["address"])

@app.route("/customers", methods=["DELETE"])
def delete_customer_route():
    data = request.get_json()
    delete_customer(data["customer_id"])
    return read_customers()

# --------------------------------------------------------------------------------------------------------------------------------------
#             Endpoints -> Employees:

@app.route("/employees", methods=["POST"])
def create_employee_route():
    data = request.get_json()
    return create_employee(data["employee_id"],data["name"], data["address"], data["branch"])

@app.route("/employees", methods=["GET"])
def read_employees_route():
    return read_employees()

@app.route("/employees", methods=["PUT"])
def update_employee_route():
    data = request.get_json()
    return update_employee(data["employee_id"],data["name"], data["address"], data["branch"])

@app.route("/employees", methods=["DELETE"])
def delete_employee_route():
    data = request.get_json()
    delete_employee(data["employee_id"])
    return read_employees()

# --------------------------------------------------------------------------------------------------------------------------------------
#             Endpoints -> order-car, cancel-order-car, rent-car, return-car:

@app.route("/order-car", methods=["POST"])
def order_car_route():
    data = request.get_json()
    return order_car(data["customer_id"], data["car_id"])

@app.route("/cancel-order-car", methods=["POST"])
def cancel_order_car_route():
    data = request.get_json()
    return cancel_order_car(data["customer_id"], data["car_id"])

@app.route("/rent-car", methods=["POST"])
def rent_car_route():
    data = request.get_json()
    return rent_car(data["customer_id"], data["car_id"])

@app.route("/return-car", methods=["POST"])
def return_car_route():
    data = request.get_json()
    return return_car(data["customer_id"], data["car_id"], data["status"])

if __name__ == "__main__":
    app.run(debug=True)