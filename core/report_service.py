def render_markdown(report: dict) -> str:
    """Render the LLM JSON result into a friendly Chinese Markdown report."""
    lines = []
    lines.append("## 📈 本期热销 TOP5")
    for i, item in enumerate(report.get('current_hot', []), 1):
        lines.append(f"**{i}.** [{item.get('title','')}]({item.get('url','')}) - 得分: {item.get('score',0):.1f}")
    lines.append("\n## 🔮 未来 3 个月潜力关键词")
    for kw in report.get('future_hot', []):
        lines.append(f"- **{kw.get('keyword','')}**（增长率 {kw.get('growth_3m',0)*100:.1f}%）: {kw.get('reason','')}")
    lines.append("\n## 📝 小结")
    lines.append(report.get('summary',''))
    lines.append("\n### 行动建议")
    lines.append("- 在 TikTok / Instagram Reels 投放 **厨房小配件** 短视频，利用已出现的热度标签。")
    return "\n".join(lines)
