from flask import Flask, request
# from fil import alle funksjonene i return setningene under

app = Flask(__name__)

# Test:
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# CRUD (Create, Read, Update, Delete) for "Cars" - hver funksjon returnerer et
# funksjonskall til en funksjon som skal ligge i en annen fil. Disse funksjonene skal
# f. eks delete fra databasen
@app.route("/cars", methods=["POST"])
def create_car_route():
    data = request.get_json()
    return create_car(data['make'], data['model'], data['year'], data['location'], data['status'])

@app.route("/cars", methods=["GET"])
def read_cars_route():
    return read_cars()

@app.route("/cars", methods=["PUT"])
def update_car_route():
    data = request.get_json()
    return update_car(data['make'], data['model'], data['year'], data['location'], data['status'])

@app.route("/cars", methods=["DELETE"])
def delete_car_route():
    data = request.get_json()
    delete_car(data['make']) # er dette riktig id/nøkkel?
    return get_all_cars() # skal jeg returnere denne, eller bare utføre slettingen

# CRUD (Create, Read, Update, Delete) for "Customer"
@app.route("/customers", methods=["POST"])
def create_customer_route():
    data = request.get_json()
    return create_customer(data["name"], data["age"], data["address"])

@app.route("/customers", methods=["GET"])
def read_customers_route():
    return read_customers()

@app.route("/customers", methods=["PUT"])
def update_customer_route():
    data = request.get_json()
    return update_customer(data["name"], data["age"], data["address"])

@app.route("/customers", methods=["DELETE"])
def delete_customer_route():
    data = request.get_json()
    delete_customer(data["name"]) # er dette riktig id/nøkkel?
    return get_all_customers() # skal jeg returnere denne, eller bare utføre slettingen

# CRUD (Create, Read, Update, Delete) for "Employees"
@app.route("/employees", methods=["POST"])
def create_employee_route():
    data = request.get_json()
    return create_employee(data["name"], data["address"], data["branch"])

@app.route("/employees", methods=["GET"])
def read_employees_route():
    return read_employees()

@app.route("/employees", methods=["PUT"])
def update_employee_route():
    data = request.get_json()
    return update_employee(data["name"], data["address"], data["branch"])

@app.route("/employees", methods=["DELETE"])
def delete_employee_route():
    data = request.get_json()
    delete_employee(data["name"]) # er dette riktig id/nøkkel?
    return get_all_employees() # skal jeg returnere denne, eller bare utføre slettingen

if __name__ == "__main__":
    app.run(debug=True)