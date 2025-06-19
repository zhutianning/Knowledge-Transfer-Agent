# Neo4j地理实体建模骨架
# 包含Location节点的建模方法 

from neo4j import GraphDatabase

def create_location(tx, name:str, lat:float, lon:float, terrain:str):
    tx.run(
        "CREATE (l:Location {name: $name, latitude: $lat, longitude: $lon, terrain: $terrain})",
        name=name, lat=lat, lon=lon, terrain=terrain
    )