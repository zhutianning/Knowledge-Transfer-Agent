# Knowledge-Transfer-Agent
```
Knowledge-Transfer-Agent/
│
├── agents/                # Agent与Tools开发
│   ├── history_qa_agent.py
│   └── tools/
│       └── neo4j_tool.py
│
├── kg/                    # KG相关
│   ├── neo4j_schema.py    # 地理实体建模
│   ├── import_conceptnet.py
│   └── import_dbpedia.py
│
├── llm/                   # LLM相关
│   └── llm_integration.py
│
├── data/                  # 数据存放
│   ├── conceptnet/
│   └── dbpedia/
├── configs/
│   └── config.yaml
│
├── main.py                # 项目入口
└── requirements.txt
```
