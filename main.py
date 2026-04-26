#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
产品进化机制 MVP 入口文件
基于 transitions 状态机+Celery 的编排引擎
"""

import asyncio
import logging
from config.settings import Config
from state_machine.machine_config import ProductEvolutionMachine
from tasks.celery_app import app as celery_app
from agents.perception_agent import PerceptionAgent
from agents.execution_agent import ExecutionAgent
from agents.learning_agent import LearningAgent
from agents.coordination_agent import CoordinationAgent
from agents.evolution_agent import EvolutionAgent
from agents.decision_agent import DecisionAgent

# 配置日志
logging.basicConfig(
    level=Config.LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ProductEvolutionSystem:
    """产品进化系统主类"""
    
    def __init__(self):
        """初始化系统组件"""
        self.config = Config()
        self.state_machine = ProductEvolutionMachine()
        
        # 初始化所有 Agent
        self.agents = {
            'perception': PerceptionAgent(),
            'execution': ExecutionAgent(),
            'learning': LearningAgent(),
            'coordination': CoordinationAgent(),
            'evolution': EvolutionAgent(),
            'decision': DecisionAgent()
        }
        
        logger.info("Product Evolution System initialized")
    
    async def start(self):
        """启动系统"""
        logger.info("Starting Product Evolution System...")
        
        # 启动状态机
        self.state_machine.start()
        
        # 启动 Celery 任务队列
        celery_app.worker_main(['worker', '--loglevel=info'])
        
        # 启动各 Agent
        for agent_name, agent in self.agents.items():
            logger.info(f"Starting {agent_name} agent...")
            await agent.initialize()
        
        logger.info("All components started successfully")
    
    async def shutdown(self):
        """优雅关闭系统"""
        logger.info("Shutting down Product Evolution System...")
        
        # 关闭各 Agent
        for agent_name, agent in self.agents.items():
            await agent.shutdown()
        
        # 停止状态机
        self.state_machine.stop()
        
        logger.info("System shutdown complete")


async def main():
    """主函数"""
    system = ProductEvolutionSystem()
    
    try:
        await system.start()
        
        # 保持系统运行
        while True:
            await asyncio.sleep(1)
            
    except KeyboardInterrupt:
        logger.info("Received shutdown signal")
    finally:
        await system.shutdown()


if __name__ == '__main__':
    asyncio.run(main())























































































