/**
 * 版本树类型定义
 * 
 * 对照后端契约: backend/core/contracts/version_tree_models.py
 * 对照文档: .kiro/docs/api_contracts.md §3.4
 */

// ==================== 实体类型 ====================

export interface TreeNode {
  node_id: string;
  parent_id?: string;
  version_id: string;
  children: string[];
  decision_point?: string;
  selected_option?: string;
  decision_time?: string;
}

export interface VersionTree {
  tree_id: string;
  user_id: string;
  root_node_id: string;
  current_node_id: string;
  nodes: Record<string, TreeNode>;
  scenario_id: string;
  domain: string;
  created_at: string;
  updated_at: string;
  total_decisions: number;
  max_depth: number;
}

export interface DecisionRecord {
  record_id: string;
  user_id: string;
  tree_id: string;
  node_id: string;
  decision_point: string;
  options_presented: string[];
  option_selected: string;
  context_snapshot: Record<string, unknown>;
  created_at: string;
}

export interface TreePath {
  tree_id: string;
  path: string[];
  decisions: string[];
  total_depth: number;
}

// ==================== 请求类型 ====================

export interface CreateTreeRequest {
  scenario_id: string;
  domain: string;
  initial_versions: LifeVersion[];
}

export interface RecordDecisionRequest {
  node_id: string;
  option: string;
  context?: Record<string, unknown>;
}

export interface CompareParams {
  node_a: string;
  node_b: string;
}

// ==================== 响应类型 ====================

export interface CompareResult {
  node_a: TreeNode;
  node_b: TreeNode;
  common_ancestor: string;
  divergence_point: string;
  differences: Difference[];
}

export interface Difference {
  field: string;
  value_a: unknown;
  value_b: unknown;
}

// ==================== 关联类型 ====================

export interface LifeVersion {
  version_id: string;
  title: string;
  description: string;
  probability: number;
  key_factors: string[];
}
