# Product Evolution - 产品进化机制 MVP

基于 transitions 状态机 + Celery 编排引擎的产品进化系统，包含 6 个 Agent。

## 技术架构

- **状态机引擎**: transitions (Python 轻量级有限状态机)
- **任务编排**: Celery (分布式任务队列)
- **Agent 数量**: 6 个核心 Agent

## 项目结构

```
product-evolution/
├── agents/                 # 6 个 Agent 实现
│   ├── __init__.py
│   ├── base_agent.py      # Agent 基类
│   ├── perception_agent.py    # 感知 Agent
│   ├── decision_agent.py      # 决策 Agent
│   ├── execution_agent.py     # 执行 Agent
│   ├── learning_agent.py      # 学习 Agent
│   ├── coordination_agent.py  # 协调 Agent
│   ── evolution_agent.py     # 进化 Agent
├── state_machine/          # 状态机定义
│   ├── __init__.py
│   ├── machine_config.py   # transitions 配置
│   └── states.py           # 状态定义
├── tasks/                  # Celery 任务
│   ├── __init__.py
│   ├── celery_app.py       # Celery 应用配置
│   └── agent_tasks.py      # Agent 任务定义
├── config/                 # 配置文件
│   └── settings.py
├── requirements.txt        # 依赖包
└── README.md
```

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行

```bash
# 启动 Celery Worker
celery -A tasks.celery_app worker --loglevel=info

# 运行主程序
python main.py
```

## License

MIT











































