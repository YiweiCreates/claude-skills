# claude-skills · 一套实战沉淀的 Claude 技能合集

> A collection of battle-tested Claude Code skills (in Chinese): humanized writing, code-renovation surgery, safe open-source research & publishing, and Obsidian vault maintenance.

这里的每个技能都不是凭空设计的——都是在真实工作里反复用、踩过坑、修订过多版后固化下来的方法论。装进 Claude Code 后，对 AI 说一句触发词，它就按这套打法干活。

## 技能目录

| 技能 | 一句话 | 什么时候找它 |
|---|---|---|
| [plain-write](plain-write/SKILL.md) 说人话 | 把"给人看的东西"改成真人能一遍看懂的话；文档往多了解释、发消息往少了砍，两套方向相反 | "这太 AI 了""说人话""别每句都括号解释" |
| [code-renew](code-renew/SKILL.md) 代码升级 | 对"能跑但毛病多/死改改不出来"的项目做先诊断后分期的升级手术，绝不盲改 | "全面升级""代码体检""死改改不出来" |
| [oss-research](oss-research/SKILL.md) 开源项目研究 | 安全前提下把开源项目读透：查钩子→保险安装→读透架构→沙箱真机跑通→固定结构报告 | "帮我研究一下 GitHub 上的 XXX" |
| [oss-publish](oss-publish/SKILL.md) 项目开源 | 把项目安全体面地开源：发布前敏感审计到零命中→全新历史发布→发布后远端复扫 | "帮我把这个开源到 GitHub" |
| [vault-audit](vault-audit/SKILL.md) 知识库大阅兵 | 对整个 Obsidian vault 做系统性审计：结构/链接/内容/一致性四查，红黄绿分级报告 | "知识库乱了""帮我做个全库体检" |
| [obsidian-link-guard](obsidian-link-guard/SKILL.md) 链路修复 | 文件改名/迁移后修红链、清 0B 空文件、兼容跳转页、全库断链审计（附脚本） | "改名后链接全炸了""一堆红链" |

几个技能互相衔接：`oss-research` 读懂一个项目 → `code-renew` 动手改造它 → `oss-publish` 把成果开源出去 → 所有对外文字用 `plain-write` 收尾。

## 安装（Claude Code）

```bash
git clone https://github.com/NovaKepler513/claude-skills.git
# 全部安装（用户级，所有项目可用）
cp -r claude-skills/{plain-write,code-renew,oss-research,oss-publish,vault-audit,obsidian-link-guard} ~/.claude/skills/
# 或只装需要的
cp -r claude-skills/plain-write ~/.claude/skills/
```

装好后直接对 Claude 说触发词（如"帮我研究一下 GitHub 上的 XXX"）即可自动命中；也可以显式说"使用 oss-research 研究 XXX"。

不用 Claude Code 的话，把对应 `SKILL.md` 全文贴给任何 AI 助手当操作规范也行。

## 这套技能的共同底色

- **跑起来才算数**：读代码不运行不算研究，改完不实测不算修复，发布了不复查不算完成。
- **结论挂证据**：批判到文件:行号，数字用独立实现对数，"我觉得好了"不算数。
- **安全先行**：陌生代码先查钩子再安装，发布前审计到零命中，push 即永久公开。
- **先看清再动手**：诊断与治疗分离，先确认再修复，绝不盲改。

## 致谢

`plain-write` 的结构雷分类与 5 维自评借鉴了多个开源 anti-slop / humanizer 项目的思路（详见其文末致谢清单）。

## License

MIT
