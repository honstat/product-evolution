"""
Git Adapter - 第二期开发 (Week 5-6)

实现 GitHub/GitLab API 封装，支持：
- 仓库确认
- 分支创建
- 代码提交
- MR/PR 创建
- 状态同步
"""

import logging
from abc import ABC, abstractmethod
from typing import Optional, Dict, List, Any
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class Repository:
    """仓库信息数据类"""
    name: str
    owner: str
    url: str
    default_branch: str
    is_private: bool


@dataclass
class Branch:
    """分支信息数据类"""
    name: str
    commit_sha: str
    protected: bool


@dataclass
class PullRequest:
    """Pull Request/Merge Request 数据类"""
    id: int
    number: int
    title: str
    source_branch: str
    target_branch: str
    state: str  # open, closed, merged
    url: str


class GitAdapter(ABC):
    """Git 适配器抽象基类
    
    定义 Git 操作的统一接口，支持不同 Git 平台的适配
    """
    
    def __init__(self, token: str, base_url: Optional[str] = None):
        """初始化 Git 适配器
        
        Args:
            token: API 访问令牌
            base_url: API 基础 URL（用于自托管实例）
        """
        self.token = token
        self.base_url = base_url
        self.session = self._create_session()
    
    @abstractmethod
    def _create_session(self):
        """创建 HTTP 会话"""
        pass
    
    @abstractmethod
    def get_repository(self, owner: str, repo: str) -> Repository:
        """获取仓库信息
        
        Args:
            owner: 仓库所有者
            repo: 仓库名称
            
        Returns:
            Repository 对象
        """
        pass
    
    @abstractmethod
    def create_branch(self, owner: str, repo: str, branch_name: str, 
                     from_branch: Optional[str] = None) -> Branch:
        """创建新分支
        
        Args:
            owner: 仓库所有者
            repo: 仓库名称
            branch_name: 新分支名称
            from_branch: 源分支名称（默认为默认分支）
            
        Returns:
            Branch 对象
        """
        pass
    
    @abstractmethod
    def commit_files(self, owner: str, repo: str, branch: str, 
                    files: List[Dict[str, Any]], message: str) -> str:
        """提交文件到指定分支
        
        Args:
            owner: 仓库所有者
            repo: 仓库名称
            branch: 目标分支
            files: 文件列表，每个文件包含 path 和 content
            message: 提交信息
            
        Returns:
            提交 SHA
        """
        pass
    
    @abstractmethod
    def create_pull_request(self, owner: str, repo: str, 
                          title: str, body: str,
                          source_branch: str, target_branch: str) -> PullRequest:
        """创建 Pull Request / Merge Request
        
        Args:
            owner: 仓库所有者
            repo: 仓库名称
            title: PR 标题
            body: PR 描述
            source_branch: 源分支
            target_branch: 目标分支
            
        Returns:
            PullRequest 对象
        """
        pass
    
    @abstractmethod
    def get_pull_request_status(self, owner: str, repo: str, pr_number: int) -> Dict[str, Any]:
        """获取 PR 状态
        
        Args:
            owner: 仓库所有者
            repo: 仓库名称
            pr_number: PR 编号
            
        Returns:
            PR 状态字典（包含 CI 状态、审查状态等）
        """
        pass


class GitHubAdapter(GitAdapter):
    """GitHub API 适配器
    
    实现 GitHub REST API v3 的封装
    """
    
    def __init__(self, token: str, base_url: Optional[str] = None):
        """初始化 GitHub 适配器
        
        Args:
            token: GitHub Personal Access Token
            base_url: GitHub Enterprise API URL（可选）
        """
        super().__init__(token, base_url or "https://api.github.com")
    
    def _create_session(self):
        import requests
        session = requests.Session()
        session.headers.update({
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        })
        return session
    
    def get_repository(self, owner: str, repo: str) -> Repository:
        """获取 GitHub 仓库信息"""
     



































































































































































