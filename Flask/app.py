from flask import Flask, request
from neo4j_folder.DB import create_car, read_cars, update_car, delete_car
from neo4j_folder.DB import create_customer, read_customers, update_customer, delete_customer
from neo4j_folder.DB import create_employee, read_employees, update_employee, delete_employee
from neo4j_folder.DB import order_car, cancel_order_car, rent_car, return_car

app = Flask(__name__)

# return i DB.py: enten boolean eller status code. Hvis boolean så kan jeg skrive if result i app.py,
# hvis status code så kan jeg skrive if result == 201 i app.py.

# --------------------------------------------------------------------------------------------------------------------------------------
#             Endpoints -> Cars:

@app.route("/cars", methods=["POST"])
def create_car_route():
    data = request.get_json()
    create_car(data["car_id"],data["make"], data["model"], data["year"], data["location"], data["status"])
    return "Car was created", 201

@app.route("/cars", methods=["GET"])
def read_cars_route():
    return read_cars(), 200

@app.route("/cars", methods=["PUT"])
def update_car_route():
    data = request.get_json()
    update_car(data["car_id"], data["make"], data["model"], data["year"], data["location"], data["status"])
    return "Car was updated", 200

@app.route("/cars", methods=["DELETE"])
def delete_car_route():
    data = request.get_json()
    delete_car(data["car_id"])
    return "Car deleted", 200

# --------------------------------------------------------------------------------------------------------------------------------------
#             Endpoints -> Customers:

@app.route("/customers", methods=["POST"])
def create_customer_route():
    data = request.get_json()
    create_customer(data["customer_id"],data["name"], data["age"], data["address"])
    return "Customer was created", 201

@app.route("/customers", methods=["GET"])
def read_customers_route():
    return read_customers(), 200

@app.route("/customers", methods=["PUT"])
def update_customer_route():
    data = request.get_json()
    update_customer(data["customer_id"],data["name"], data["age"], data["address"])
    return "Customer was updated", 200

@app.route("/customers", methods=["DELETE"])
def delete_customer_route():
    data = request.get_json()
    delete_customer(data["customer_id"])
    return "Customer was deleted", 200

# --------------------------------------------------------------------------------------------------------------------------------------
#             Endpoints -> Employees:

@app.route("/employees", methods=["POST"])
def create_employee_route():
    data = request.get_json()
    create_employee(data["employee_id"],data["name"], data["address"], data["branch"])
    return "Employee was created", 201

@app.route("/employees", methods=["GET"])
def read_employees_route():
    return read_employees(), 200

@app.route("/employees", methods=["PUT"])
def update_employee_route():
    data = request.get_json()
    update_employee(data["employee_id"],data["name"], data["address"], data["branch"])
    return "Employee was created", 200

@app.route("/employees", methods=["DELETE"])
def delete_employee_route():
    data = request.get_json()
    delete_employee(data["employee_id"])
    return "Employee was deleted", 200

# --------------------------------------------------------------------------------------------------------------------------------------
#             Endpoints -> order-car, cancel-order-car, rent-car, return-car:

@app.route("/order-car", methods=["POST"])
def order_car_route():
    data = request.get_json()
    var = order_car(data["customer_id"], data["car_id"])
    return var, 200

@app.route("/cancel-order-car", methods=["POST"])
def cancel_order_car_route():
    data = request.get_json()
    var = cancel_order_car(data["customer_id"], data["car_id"])
    return var, 200

@app.route("/rent-car", methods=["POST"])
def rent_car_route():
    data = request.get_json()
    var = rent_car(data["customer_id"], data["car_id"])
    return var, 200

@app.route("/return-car", methods=["POST"])
def return_car_route():
    data = request.get_json()
    var = return_car(data["customer_id"], data["car_id"], data["status"])
    return var, 200

if __name__ == "__main__":
    app.run(debug=True)