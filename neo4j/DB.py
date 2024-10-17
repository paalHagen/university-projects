from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver

URI = "neo4j+s://b729d323.databases.neo4j.io"
AUTH = ("neo4j", "passord")

def _get_connection():
    driver =GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

