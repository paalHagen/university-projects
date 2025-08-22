# webapp-flask-neo4j

A web application built with Flask and Neo4j for managing and visualizing graph data.

## Features

- RESTful API for graph operations
- User authentication
- Interactive data visualization
- CRUD operations on nodes and relationships

## Setup

1. **Install dependencies:**

   - Run the following command in your project directory to install all required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Neo4j:**

   - Install/start Neo4j (database server) locally or use a cloud instance.
   - Save your Neo4j credentials (URI, username, password) in a .env file

3. **Set credentials:**

   - Copy the lines from the `.env` file and run them in your terminal to set environment variables:
     ```bash
     export NEO4J_URI=your_neo4j_uri
     export NEO4J_USER=your_neo4j_username
     export NEO4J_PASSWORD=your_neo4j_password
     ```

4. **Run the application:**
   ```bash
   flask run
   ```

## Usage

- Access the web interface at `http://localhost:5000`
- Use the API endpoints for programmatic access

## Contributors

- Pål Hagen Størksen
- Helge Hitland
