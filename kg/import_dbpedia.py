# DBpedia历史事件抽取骨架
# 未来将实现SPARQL查询与数据导入 
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("https://dbpedia.org/sparql")
sparql.setQuery("""
SELECT ?event ?label ?lat ?long WHERE {
  ?event dbo:wikiPageWikiLink dbr:History .
  ?event rdfs:label ?label .
  ?event geo:lat ?lat .
  ?event geo:long ?long .
  FILTER (lang(?label) = 'zh')
} LIMIT 100
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert() 