"""
产品进化机制 - Celery 任务模块
"""

from .celery_app import app
from .agent_tasks import (
    run_perception_agent,
    run_decision_agent,
    run_execution_agent,
    run_learning_agent,
    run_coordination_agent,
    run_evolution_agent,
)

__all__ = [
    'app',
    'run_perception_agent',
    'run_decision_agent',
    'run_execution_agent',
    'run_learning_agent',
    'run_coordination_agent',
    'run_evolution_agent',
]





















