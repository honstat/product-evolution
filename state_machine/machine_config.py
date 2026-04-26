"""
产品进化机制 - 状态机配置模块
基于 transitions 库的状态机配置和转换定义
"""

from transitions import Machine, State
from .states import ProductState


class ProductEvolutionMachine(Machine):
    """产品进化状态机类
    
    定义产品从需求收集到最终部署的完整生命周期状态转换
    """
    
    # 状态转换定义
    transitions = [
        # 需求阶段转换
        {
            'trigger': 'collect_requirement',
            'source': ProductState.INITIAL.value,
            'dest': ProductState.REQUIREMENT_COLLECTED.value
        },
        {
            'trigger': 'analyze_requirement',
            'source': ProductState.REQUIREMENT_COLLECTED.value,
            'dest': ProductState.REQUIREMENT_ANALYZED.value
        },
        
        # 技术方案阶段转换
        {
            'trigger': 'create_tech_doc',
            'source': ProductState.REQUIREMENT_ANALYZED.value,
            'dest': ProductState.TECH_DOC_CREATED.value
        },
        {
            'trigger': 'review_tech_doc',
            'source': ProductState.TECH_DOC_CREATED.value,
            'dest': ProductState.TECH_DOC_REVIEWED.value
        },
        {
            'trigger': 'reject_tech_doc',
            'source': ProductState.TECH_DOC_CREATED.value,
            'dest': ProductState.REQUIREMENT_ANALYZED.value
        },
        
        # 开发阶段转换
        {
            'trigger': 'start_development',
            'source': ProductState.TECH_DOC_REVIEWED.value,
            'dest': ProductState.DEVELOPMENT_STARTED.value
        },
        {
            'trigger': 'progress_development',
            'source': ProductState.DEVELOPMENT_STARTED.value,
            'dest': ProductState.DEVELOPMENT_IN_PROGRESS.value
        },
        {
            'trigger': 'complete_development',
            'source': ProductState.DEVELOPMENT_IN_PROGRESS.value,
            'dest': ProductState.DEVELOPMENT_COMPLETED.value
        },
        
        # 测试阶段转换
        {
            'trigger': 'start_testing',
            'source': ProductState.DEVELOPMENT_COMPLETED.value,
            'dest': ProductState.TESTING_STARTED.value
        },
        {
            'trigger': 'progress_testing',
            'source': ProductState.TESTING_STARTED.value,
            'dest': ProductState.TESTING_IN_PROGRESS.value
        },
        {
            'trigger': 'pass_testing',
            'source': ProductState.TESTING_IN_PROGRESS.value,
            'dest': ProductState.TESTING_PASSED.value
        },
        {
            'trigger': 'fail_testing',
            'source': ProductState.TESTING_IN_PROGRESS.value,
            'dest': ProductState.TESTING_FAILED.value
        },
        {
            'trigger': 'retry_development',
            'source': [ProductState.TESTING_FAILED.value, ProductState.TESTING_IN_PROGRESS.value],
            'dest': ProductState.DEVELOPMENT_IN_PROGRESS.value
        },
        
        # 部署阶段转换
        {
            'trigger': 'prepare_deployment',
            'source': ProductState.TESTING_PASSED.value,
            'dest': ProductState.DEPLOYMENT_READY.value
        },
        {
            'trigger': 'deploy',
            'source': ProductState.DEPLOYMENT_READY.value,
            'dest': ProductState.DEPLOYED.value
        },
        
        # 监控与优化阶段转换
        {
            'trigger': 'start_monitoring',
            'source': ProductState.DEPLOYED.value,
            'dest': ProductState.MONITORING.value
        },
        {
            'trigger': 'need_optimization',
            'source': ProductState.MONITORING.value,
            'dest': ProductState.OPTIMIZATION_NEEDED.value
        },
        {
            'trigger': 'complete_optimization',
            'source': ProductState.OPTIMIZATION_NEEDED.value,
            'dest': ProductState.OPTIMIZATION_COMPLETED.value
        },
        {
            'trigger': 'return_to_monitoring',
            'source': ProductState.OPTIMIZATION_COMPL




















































































































