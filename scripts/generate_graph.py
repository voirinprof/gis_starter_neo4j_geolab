from neo4j import GraphDatabase
import geopandas as gpd
from shapely.geometry import Point
import os

# Configuration de connexion
username = os.getenv("NEO4J_USERNAME", "neo4j")
password = os.getenv("NEO4J_PASSWORD", "neo4j_pwd")
uri = os.getenv("NEO4J_URI", "neo4j://neo4j:7687")

# Connexion à Neo4j
driver = GraphDatabase.driver(uri, auth=(username, password))
session = driver.session()

# Créer un noeud avec une géométrie
def create_geospatial_node(lat, lon, label):
    point = Point(lon, lat)
    query = (
        "CREATE (n:GeospatialNode {latitude: $lat, longitude: $lon, label: $label})"
    )
    session.run(query, lat=lat, lon=lon, label=label)

# Exemple d'insertion de données géospatiales
create_geospatial_node(48.8566, 2.3522, "Paris")

# Fermeture de la session
session.close()
