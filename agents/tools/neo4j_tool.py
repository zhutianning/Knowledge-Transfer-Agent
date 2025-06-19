# Neo4j工具骨架
# 未来将实现自然语言转Cypher查询 
   
from langchain.tools import BaseTool
from neo4j import GraphDatabase

class Neo4jTool(BaseTool):
    name = "Neo4j查询工具"
    description = "用于查询地理和历史知识图谱"

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def _run(self, query:str):
        with self.driver.session() as session:
            result = session.run(query)
            return [record.data() for record in result]