"""
感知 Agent - 负责环境信息收集
"""

from typing import Any, Dict
from loguru import logger
from .base_agent import BaseAgent


class PerceptionAgent(BaseAgent):
    """感知 Agent - 负责从环境中收集和预处理信息"""
    
    def __init__(self, name: str = "PerceptionAgent", config: Dict = None):
        super().__init__(name, config)
        self.data_sources = config.get("data_sources", []) if config else []
    
    def perceive(self, environment: Dict[str, Any]) -> Dict[str, Any]:
        """感知环境信息"""
        logger.info(f"{self.name} starting perception...")
        
        result = {
            "raw_data": {},
            "processed_data": {},
            "confidence_score": 0.0,
            "metadata": {}
        }
        
        try:
            # 收集原始数据
            raw_data = self._collect_raw_data(environment)
            result["raw_data"] = raw_data
            
            # 处理数据
            processed_data = self._process_data(raw_data)
            result["processed_data"] = processed_data
            
            # 计算置信度
            result["confidence_score"] = self._calculate_confidence(processed_data)
            
            # 添加元数据
            from datetime import datetime
            result["metadata"] = {
                "timestamp": datetime.now().isoformat(),
                "sources_used": list(raw_data.keys())
            }
            
            logger.info(f"{self.name} perception completed")
            
        except Exception as e:
            logger.error(f"{self.name} error: {str(e)}")
            result["error"] = str(e)
        
        return result
    
    def _collect_raw_data(self, environment: Dict[str, Any]) -> Dict[str, Any]:
        """收集原始数据"""
        raw_data = {}
        for key in ["user_input", "system_state", "external_data"]:
            if key in environment:
                raw_data[key] = environment[key]
        return raw_data
    
    def _process_data(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """处理数据"""
        processed = {}
        for key, value in raw_data.items():
            if isinstance(value, str):
                processed[key] = value.strip()
            else:
                processed[key] = value
        return processed
    
    def _calculate_confidence(self, data: Dict[str, Any]) -> float:
        """计算置信度"""
        if not data:
            return 0.0
        return min(1.0, len(data) / 3.0)
    
    def decide(self, perception: Dict[str, Any]) -> Dict[str, Any]:
        return {"action": "none"}
    
    def execute(self, decision: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "no_execution"}
    
    def learn(self, experience: Dict[str, Any]) -> None:
        logger.debug(f"{self.name} learning...")

















































































