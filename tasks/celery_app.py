"""
产品进化机制 - Celery 应用配置模块
"""

from celery import Celery
from kombu import Exchange, Queue


# 创建 Celery 应用实例
app = Celery(
    'product_evolution',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/1',
    include=['tasks.agent_tasks']
)

# Celery 配置
app.conf.update(
    # 任务序列化格式
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    
    # 时区设置
    timezone='Asia/Shanghai',
    enable_utc=True,
    
    # 任务过期时间（秒）
    task_expires=3600,
    
    # 任务重试配置
    task_acks_late=True,
    task_reject_on_worker_lost=True,
    
    # 结果过期时间（秒）
    result_expires=7200,
    
    # 并发数
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=1000,
    
    # 任务路由配置
    task_routes={
        'tasks.agent_tasks.run_perception_agent': {'queue': 'perception'},
        'tasks.agent_tasks.run_decision_agent': {'queue': 'decision'},
        'tasks.agent_tasks.run_execution_agent': {'queue': 'execution'},
        'tasks.agent_tasks.run_learning_agent': {'queue': 'learning'},
        'tasks.agent_tasks.run_coordination_agent': {'queue': 'coordination'},
        'tasks.agent_tasks.run_evolution_agent': {'queue': 'evolution'},
    },
    
    # 队列配置
    task_queues=(
        Queue('perception', Exchange('perception'), routing_key='perception'),
        Queue('decision', Exchange('decision'), routing_key='decision'),
        Queue('execution', Exchange('execution'), routing_key='execution'),
        Queue('learning', Exchange('learning'), routing_key='learning'),
        Queue('coordination', Exchange('coordination'), routing_key='coordination'),
        Queue('evolution', Exchange('evolution'), routing_key='evolution'),
    ),
    
    # Beat 调度器配置（定时任务）
    beat_scheduler='celery.beat:PersistentScheduler',
    beat_schedule_filename='celerybeat-schedule',
    
    # 定时任务配置
    beat_schedule={
        'run-evolution-cycle': {
            'task': 'tasks.agent_tasks.run_evolution_agent',
            'schedule': 3600.0,  # 每小时运行一次
            'args': (),
        },
    },
)


# 自动发现任务
app.autodiscover_tasks(['tasks'])


@app.task(bind=True)
def debug_task(self):
    """调试任务"""
    print(f'Request: {self.request!r}')
    return 'Debug task completed'


if __name__ == '__main__':
    app.start()















































































