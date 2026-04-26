"""
产品进化机制 - 适配器模块

第二期开发（Week 5-6, 9-10）
包含 Git、CI/CD、通知等外部系统集成适配器
"""

from .git_adapter import GitAdapter, GitHubAdapter, GitLabAdapter
from .cicd_adapter import CICDAdapter, GitHubActionsAdapter, JenkinsAdapter
from .notification import NotificationService, FeishuNotifier, EmailNotifier, WebhookNotifier

__all__ = [
    # Git 适配器
    'GitAdapter',
    'GitHubAdapter',
    'GitLabAdapter',
    
    # CI/CD 适配器
    'CICDAdapter',
    'GitHubActionsAdapter',
    'JenkinsAdapter',
    
    # 通知服务
    'NotificationService',
    'FeishuNotifier',
    'EmailNotifier',
    'WebhookNotifier',
]























