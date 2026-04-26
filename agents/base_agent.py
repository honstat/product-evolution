"""
Agent 基类 - 所有 Agent 的父类

提供通用的 Agent 接口和基础功能
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from pydantic import BaseModel
from loguru import logger


class AgentState(BaseModel):
    """Agent 状态模型"""
    name: str
    status: str = "idle"  # idle, running, completed, error
    current_task: Optional[str] = None
    metadata: Dict[str, Any] = {}


class BaseAgent(ABC):
    """
    Agent 基类
    
    所有 Agent 都需要继承此类并实现以下抽象方法：
    - perceive(): 感知环境信息
    - decide(): 做出决策
    - execute(): 执行任务
    - learn(): 学习优化
    """
    
    def __init__(self, name: str, config: Optional[Dict] = None):
        """
        初始化 Agent
        
        Args:
            name: Agent 名称
            config: 配置字典
        """
        self.name = name
        self.config = config or {}
        self.state = AgentState(name=name)
        logger.info(f"Agent {name} initialized")
    
    @abstractmethod
    def perceive(self, environment: Dict[str, Any]) -> Dict[str, Any]:
        """
        感知环境信息
        
        Args:
            environment: 环境信息字典
            
        Returns:
            感知结果字典
        """
        pass
    
    @abstractmethod
    def decide(self, perception: Dict[str, Any]) -> Dict[str, Any]:
        """
        基于感知结果做出决策
        
        Args:
            perception: 感知结果
            
        Returns:
            决策结果字典
        """
        pass
    
    @abstractmethod
    def execute(self, decision: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行决策
        
        Args:
            decision: 决策结果
            
        Returns:
            执行结果字典
        """
        pass
    
    @abstractmethod
    def learn(self, experience: Dict[str, Any]) -> None:
        """
        从经验中学习优化
        
        Args:
            experience: 经验数据
        """
        pass
    
    def run(self, environment: Dict[str, Any]) -> Dict[str, Any]:
        """
        运行 Agent 完整流程：感知 -> 决策 -> 执行
        
        Args:
            environment: 环境信息
            
        Returns:
            最终执行结果
        """
        try:
            self.state.status = "running"
            
            # 感知
            perception = self.perceive(environment)
            logger.debug(f"{self.name} perception: {perception}")
            
            # 决策
            decision = self.decide(perception)
            logger.debug(f"{self.name} decision: {decision}")
  










































































































