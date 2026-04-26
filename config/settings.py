"""
产品进化机制 - 配置文件模块
包含系统运行所需的所有配置项
"""

import os
from datetime import timedelta


# ==================== 基础配置 ====================

# 项目名称
PROJECT_NAME = "product-evolution"

# 项目版本
PROJECT_VERSION = "1.0.0"

# 调试模式
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 'yes')

# 时区设置
TIMEZONE = 'Asia/Shanghai'


# ==================== Celery 配置 ====================

# Celery Broker (消息队列)
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')

# Celery Backend (结果存储)
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/1')

# Celery 任务序列化格式
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']

# Celery 时区
CELERY_TIMEZONE = TIMEZONE

# Celery 任务过期时间（秒）
CELERY_TASK_EXPIRES = int(os.getenv('CELERY_TASK_EXPIRES', 3600))

# Celery 结果过期时间（秒）
CELERY_RESULT_EXPIRES = int(os.getenv('CELERY_RESULT_EXPIRES', 7200))

# Celery 任务重试配置
CELERY_TASK_ACKS_LATE = True
CELERY_TASK_REJECT_ON_WORKER_LOST = True

# Celery Worker 配置
CELERY_WORKER_PREFETCH_MULTIPLIER = 1
CELERY_WORKER_MAX_TASKS_PER_CHILD = 1000

# Celery 队列路由
CELERY_ROUTES = {
    'tasks.agent_tasks.run_perception_agent': {'queue': 'perception'},
    'tasks.agent_tasks.run_decision_agent': {'queue': 'decision'},
    'tasks.agent_tasks.run_execution_agent': {'queue': 'execution'},
    'tasks.agent_tasks.run_learning_agent': {'queue': 'learning'},
    'tasks.agent_tasks.run_coordination_agent': {'queue': 'coordination'},
    'tasks.agent_tasks.run_evolution_agent': {'queue': 'evolution'},
}


# ==================== 状态机配置 ====================

# 状态机初始状态
MACHINE_INITIAL_STATE = 'initial'

# 状态机自动转换
MACHINE_AUTO_TRANSITIONS = True

# 状态历史记录
MACHINE_ENABLE_HISTORY = True

# 最大状态历史长度
MACHINE_MAX_HISTORY_LENGTH = 100


# ==================== Agent 配置 ====================

# Agent 超时时间（秒）
AGENT_TIMEOUT = int(os.getenv('AGENT_TIMEOUT', 300))

# Agent 最大重试次数
AGENT_MAX_RETRIES = int(os.getenv('AGENT_MAX_RETRIES', 3))

# Agent 重试延迟（秒）
AGENT_RETRY_DELAY = int(os.getenv('AGENT_RETRY_DELAY', 60))

# Agent 并发数限制
AGENT_CONCURRENCY_LIMIT = int(os.getenv('AGENT_CONCURRENCY_LIMIT', 10))


# ==================== 感知 Agent 配置 ====================

PERCEPTION_AGENT_CONFIG = {
    # 数据源配置
    'data_sources': ['api', 'database', 'file'],
    
    # 数据采集间隔（秒）
    'collection_interval': 60,
    
    # 数据缓存时间（秒）
    'cache_ttl': 300,
    
    # 数据验证规则
    'validation_rules': {
        'required_fields': ['product_id', 'timestamp', 'data_type'],
        'max_data_size': 10 * 1024 * 1024,  # 10MB
    },
}


# ==================== 决策 Agent 配置 ====================

DECISION_AGENT_CONFIG = {
   

















































































