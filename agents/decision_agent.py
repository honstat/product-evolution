"""
决策 Agent - 负责状态判断和决策

基于感知信息进行状态判断和决策制定
"""

from typing import Any, Dict
from loguru import logger
from .base_agent import BaseAgent


class DecisionAgent(BaseAgent):
    """决策 Agent - 基于感知信息进行状态判断和决策制定"""
    
    def __init__(self, name: str = "DecisionAgent", config: Dict = None):
        super().__init__(name, config)
        self.rules = config.get("rules", []) if config else []
    
    def perceive(self, environment: Dict[str, Any]) -> Dict[str, Any]:
        return {"action": "none"}
    
    def decide(self, perception: Dict[str, Any]) -> Dict[str, Any]:
        """基于感知结果做出决策"""
        logger.info(f"{self.name} making decision...")
        
        decision = {
            "action": "unknown",
            "confidence": 0.0,
            "reasoning": "",
            "next_state": None
        }
        
        try:
            processed_data = perception.get("processed_data", {})
            confidence = perception.get("confidence_score", 0.0)
            
            # 基于置信度做决策
            if confidence < 0.3:
                decision["action"] = "request_more_info"
                decision["reasoning"] = "数据置信度过低"
                decision["confidence"] = confidence
            elif confidence < 0.6:
                decision["action"] = "partial_execution"
                decision["reasoning"] = "数据置信度中等"
                decision["confidence"] = confidence
            else:
                decision["action"] = "full_execution"
                decision["reasoning"] = "数据置信度高"
                decision["confidence"] = confidence
            
            # 确定下一个状态
            decision["next_state"] = self._determine_next_state(decision["action"])
            
            logger.info(f"{self.name} decision: {decision['action']}")
            
        except Exception as e:
            logger.error(f"{self.name} error: {str(e)}")
            decision["error"] = str(e)
        
        return decision
    
    def _determine_next_state(self, action: str) -> str:
        """确定下一个状态"""
        state_map = {
            "request_more_info": "waiting",
            "partial_execution": "processing",
            "full_execution": "executing"
        }
        return state_map.get(action, "idle")
    
    def execute(self, decision: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "no_execution"}
    
    def learn(self, experience: Dict[str, Any]) -> None:
        logger.debug(f"{self.name} learning...")





































































