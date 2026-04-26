"""
产品进化机制 - Agent 任务定义模块
基于 Celery 的异步任务定义
"""

from celery import chain, group
from .celery_app import app
from agents.perception_agent import PerceptionAgent
from agents.decision_agent import DecisionAgent
from agents.execution_agent import ExecutionAgent
from agents.learning_agent import LearningAgent
from agents.coordination_agent import CoordinationAgent
from agents.evolution_agent import EvolutionAgent


@app.task(bind=True, max_retries=3)
def run_perception_agent(self, product_id: str, context: dict = None):
    """运行感知 Agent
    
    Args:
        product_id: 产品 ID
        context: 上下文信息
        
    Returns:
        dict: 感知结果
    """
    try:
        agent = PerceptionAgent(product_id=product_id)
        result = agent.run(context=context)
        return {
            'status': 'success',
            'product_id': product_id,
            'agent': 'perception',
            'result': result
        }
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@app.task(bind=True, max_retries=3)
def run_decision_agent(self, product_id: str, perception_result: dict):
    """运行决策 Agent
    
    Args:
        product_id: 产品 ID
        perception_result: 感知结果
        
    Returns:
        dict: 决策结果
    """
    try:
        agent = DecisionAgent(product_id=product_id)
        result = agent.run(perception_result=perception_result)
        return {
            'status': 'success',
            'product_id': product_id,
            'agent': 'decision',
            'result': result
        }
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@app.task(bind=True, max_retries=3)
def run_execution_agent(self, product_id: str, decision_result: dict):
    """运行执行 Agent
    
    Args:
        product_id: 产品 ID
        decision_result: 决策结果
        
    Returns:
        dict: 执行结果
    """
    try:
        agent = ExecutionAgent(product_id=product_id)
        result = agent.run(decision_result=decision_result)
        return {
            'status': 'success',
            'product_id': product_id,
            'agent': 'execution',
            'result': result
        }
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@app.task(bind=True, max_retries=3)
def run_learning_agent(self, product_id: str, execution_result: dict):
    """运行学习 Agent
    
    Args:
        product_id: 产品 ID
        execution_result: 执行结果
        
    Returns:
        dict: 学习结果
    """
    try:
        agent = LearningAgent(product_id=product_id)
        result = agent.run(execution_result=execution_result)
        return {
            'status': 'success',
            'product_id': product_id,
            'agent': 'learning',
            'result': result
        }
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@app.task(bind=True, max_retries=3)
def run_coordination_agent(self, product_id: str, learning_result: dict):
    """运行协调 Agent
    
    Args:
        product_id: 产品 ID
        learning_result: 学习结果
        
    Returns:
        dict: 协调结果
    """
    try:
        agent = CoordinationAgent(product_id=product_id)
        result = agent.run(learning_result=learning_result)
        return {
            'status': 'success',
            'product_id': product_id,
            'agent': 'coordination',
            'result': result
        }
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@app.task(bind=True, max_retries=3)
def run_evolution_agent(self, product_id: str, coordination_result: dict = None):
    """运行进化 Agent
    
    Args:
        product_id: 产品 ID
        coordination_result: 协调结果
        
    Returns:
        dict: 进化结果
    """
    try:
        agent = EvolutionAgent(product_id=product_id)
        result = agent.run(coordination_result=coordination_result)
        return {
            'status': 'success',
            'product_id': product_id,
            'agent': 'evolution',
            'result': result
        }
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@app.task
def run_full_evolution_cycle(product_id: str, initial_context: dict = None):
    """运行完整的进化周期
    
    按顺序执行所有 Agent：感知 -> 决策 -> 执行 -> 学习 -> 协调 -> 进化
    
    Args:
        product_id: 产品 ID
        initial_context: 初始上下文
        
    Returns:
        dict: 完整周期的执行结果
    """
    # 使用 Celery chain 串联所有任务
    workflow = chain(
        run_perception_agent.s(product_id, initial_context),
        run_decision_agent.s(product_id),
        run_execution_agent.s(product_id),
        run_learning_agent.s(product_id),
        run_coordination_agent.s(product_id),
        run_evolution_agent.s(product_id),
    )
    
    result = workflow.apply_async()
    return {
        'status': 'started',
        'product_id': product_id,
        'workflow_id': result.id
    }


@app.task
def run_parallel_agents(product_id: str, context: dict = None):
    """并行运行多个 Agent
    
    Args:
        product_id: 产品 ID
        context: 上下文信息
        
    Returns:
        dict: 并行执行结果
    """
    # 使用 Celery group 并行执行
    parallel_workflow = group(
        run_perception_agent.s(product_id, context),
        run_decision_agent.s(product_id, context),
        run_execution_agent.s(product_id, context),
    )
    
    result = parallel_workflow.apply_async()
    return {
        'status': 'started',
        'product_id': product_id,
        'parallel_workflow_id': result.id
    }





































































































































































































