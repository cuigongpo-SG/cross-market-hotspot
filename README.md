# cross-market-hotspot

跨境电商热卖商品抓取、分析与推荐平台。

- 支持 Amazon API / Playwright 抓取
- 支持 TikTok Shop API 抓取
- 可选 Google Trends 辅助预测
- LLM（OpenRouter 免费模型）生成中文报告
- Docker + FastAPI 部署
- GitHub Actions + Codex CLI 自动审查

## 项目结构
```
cross-market-hotspot/
├─ core/                # 业务核心代码
│   ├─ models.py        # Pydantic 数据模型
│   ├─ loop.py          # Loop Skill（已内置）
│   ├─ pipeline.py      # 抓取 → 汇总 → LLM → 报告
│   ├─ fetch_amazon.py  # Amazon 抓取占位
│   ├─ fetch_tiktok.py  # TikTok 抓取占位
│   ├─ fetch_trends.py  # 可选趋势抓取
│   ├─ llm_service.py   # LLM 调用封装
│   └─ report_service.py# Markdown 渲染
├─ gateway/             # FastAPI 接口
│   └─ main.py
├─ Dockerfile           # 多阶段构建
├─ docker-compose.yml   # 本地调试
├─ .github/workflows/ci.yml  # CI + Codex 审查
├─ ops/ci_review.sh    # Codex CLI 审查脚本
└─ .gitignore
```