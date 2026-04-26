"""
产品进化机制 - 状态定义模块
基于 transitions 库的状态机状态定义
"""

from enum import Enum


class ProductState(Enum):
    """产品进化状态枚举"""
    
    # 初始状态
    INITIAL = "initial"
    
    # 需求阶段
    REQUIREMENT_COLLECTED = "requirement_collected"
    REQUIREMENT_ANALYZED = "requirement_analyzed"
    
    # 技术方案阶段
    TECH_DOC_CREATED = "tech_doc_created"
    TECH_DOC_REVIEWED = "tech_doc_reviewed"
    
    # 开发阶段
    DEVELOPMENT_STARTED = "development_started"
    DEVELOPMENT_IN_PROGRESS = "development_in_progress"
    DEVELOPMENT_COMPLETED = "development_completed"
    
    # 测试阶段
    TESTING_STARTED = "testing_started"
    TESTING_IN_PROGRESS = "testing_in_progress"
    TESTING_PASSED = "testing_passed"
    TESTING_FAILED = "testing_failed"
    
    # 部署阶段
    DEPLOYMENT_READY = "deployment_ready"
    DEPLOYED = "deployed"
    
    # 监控与优化阶段
    MONITORING = "monitoring"
    OPTIMIZATION_NEEDED = "optimization_needed"
    OPTIMIZATION_COMPLETED = "optimization_completed"
    
    # 终态
    COMPLETED = "completed"
    ARCHIVED = "archived"


# 状态分组定义
REQUIREMENT_STATES = [
    ProductState.INITIAL,
    ProductState.REQUIREMENT_COLLECTED,
    ProductState.REQUIREMENT_ANALYZED,
]

DEVELOPMENT_STATES = [
    ProductState.DEVELOPMENT_STARTED,
    ProductState.DEVELOPMENT_IN_PROGRESS,
    ProductState.DEVELOPMENT_COMPLETED,
]

TESTING_STATES = [
    ProductState.TESTING_STARTED,
    ProductState.TESTING_IN_PROGRESS,
    ProductState.TESTING_PASSED,
    ProductState.TESTING_FAILED,
]

PRODUCTION_STATES = [
    ProductState.DEPLOYED,
    ProductState.MONITORING,
    ProductState.OPTIMIZATION_NEEDED,
    ProductState.OPTIMIZATION_COMPLETED,
]

TERMINAL_STATES = [
    ProductState.COMPLETED,
    ProductState.ARCHIVED,
]





































































