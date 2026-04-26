"""
产品进化机制 - Agent 模块

包含 6 个核心 Agent：
- PerceptionAgent: 感知 Agent，负责环境信息收集
- DecisionAgent: 决策 Agent，负责状态判断和决策
- ExecutionAgent: 执行 Agent，负责任务执行
- LearningAgent: 学习 Agent，负责经验学习和优化
- CoordinationAgent: 协调 Agent，负责多 Agent 协作
- EvolutionAgent: 进化 Agent，负责系统自我进化
"""

from .base_agent import BaseAgent
from .perception_agent import PerceptionAgent
from .decision_agent import DecisionAgent
from .execution_agent import ExecutionAgent
from .learning_agent import LearningAgent
from .coordination_agent import CoordinationAgent
from .evolution_agent import EvolutionAgent

__all__ = [
    'BaseAgent',
    'PerceptionAgent',
    'DecisionAgent',
    'ExecutionAgent',
    'LearningAgent',
    'CoordinationAgent',
    'EvolutionAgent',
]
























