---
name: obsidian-link-guard
description: |
  Obsidian 链接防断裂技能。用于文件重命名/迁移后，批量修复 wikilink、保留兼容入口、扫描全库断链并输出修复结果。

  MANDATORY TRIGGERS: 改名后链接失效、红链、索引不到、空文件、404、断链、wikilink 修复、知识库链接体检、rename migration。
---

# Obsidian Link Guard

你要做的事情：在 Obsidian 知识库文件改名、迁移、目录重构后，确保"旧入口不断、全库可索引、跨平台可访问"。

---

## 适用场景

1. 文件重命名后，索引页出现红链。
2. Obsidian 因旧链接自动创建了 0B 空文件。
3. 新平台/新会话使用旧路径导致 GitHub 404。
4. 做了目录重构后，需要一次全库链接健康检查。

---

## 标准流程（6步）

### 1) 确认"新旧映射"

先明确：
- 新的官方文件名（canonical）
- 旧文件名（legacy）及其历史用途（启动词、runbook、外链）

示例：
- `frontend-runbook.md` → `前端运维手册.md`
- `frontend-spec.md` → `前端交互规格.md`

### 2) 排查空壳文件

重点找 0B 的 `.md` 文件（常见于 Obsidian 自动补文件）：

```bash
bash scripts/find_zero_byte_files.sh "<vault-root>"
```

（脚本随本 skill 附带于 `scripts/` 目录）

### 3) 建立兼容入口（不要留空）

旧文件名不要删除成空白；改为"兼容跳转页"：
- 标题写"已迁移"
- 一个 wikilink 指向新文件
- 可附绝对路径，方便跨平台排错

### 4) 批量改索引入口

优先改这些文档：
1. 总入口（HOME / _START_HERE / 总索引）
2. 产品索引和运行手册
3. 启动词模板与 GitHub 链接

### 5) 运行全库坏链审计

```bash
python3 scripts/audit_wikilinks.py "<vault-root>"
```

输出 `MISSING_PATH` 就继续修，直到输出为空。

### 6) 收尾与同步

1. 输出"旧→新映射表"
2. 列出变更文件
3. 给出"剩余风险/未修复项（如有）"
4. 提交并推送（如果是 Git 仓库且用户要求）

---

## 改名防断链规则（长期）

1. 先建新文件，再改旧链接，最后处理旧文件。
2. 旧文件名保留为兼容跳转页至少一段时间，不直接硬删。
3. 对外/跨平台启动词优先使用 ASCII 文件名入口（兼容更高）。
4. 每次重构后必须跑一次脚本审计，不能只靠人工抽查。

---

## 输出模板（修复完成后）

```markdown
已完成链接修复：
1) 旧→新映射：
- old-a.md -> new-a.md
- old-b.md -> new-b.md

2) 本次改动：
- 更新索引：...
- 新增兼容入口：...
- 修复坏链：... 条

3) 审计结果：
- audit_wikilinks: 0 条 MISSING_PATH
- zero-byte md: 0 个（或列出例外）
```

---

## 附带脚本

- `scripts/audit_wikilinks.py`——全库 wikilink 断链审计（只审路径式链接，跳过代码块与 http 链接；有断链时退出码 1，可接 CI）
- `scripts/find_zero_byte_files.sh`——找出 0 字节的 .md 空壳文件
