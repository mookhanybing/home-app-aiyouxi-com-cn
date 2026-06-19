import json
import sys

SITE_DATA = {
    "title": "爱游戏",
    "url": "https://home-app-aiyouxi.com.cn",
    "keywords": ["爱游戏", "手游", "休闲", "娱乐"],
    "tags": ["游戏平台", "手机游戏", "在线娱乐"],
    "description": "爱游戏是一个提供多种手机游戏与休闲娱乐内容的综合平台。"
}

_EXAMPLE_RECORDS = [
    {"title": "热门推荐", "items": ["连连看", "消消乐", "2048"]},
    {"title": "新游上线", "items": ["梦幻花园", "跑酷高手", "猜歌达人"]}
]

def build_structured_summary(data: dict) -> dict:
    summary = {
        "name": data["title"],
        "url": data["url"],
        "keyword_list": data["keywords"],
        "tag_list": data["tags"],
        "short_intro": data["description"],
    }
    return summary

def format_summary_text(summary: dict) -> str:
    lines = []
    lines.append(f"站点名称: {summary['name']}")
    lines.append(f"网址: {summary['url']}")
    lines.append(f"关键词: {', '.join(summary['keyword_list'])}")
    lines.append(f"标签: {', '.join(summary['tag_list'])}")
    lines.append(f"说明: {summary['short_intro']}")
    return "\n".join(lines)

def format_summary_json(summary: dict) -> str:
    return json.dumps(summary, ensure_ascii=False, indent=2)

def display_categories(records: list) -> list:
    category_output = []
    for record in records:
        header = record["title"]
        items = "; ".join(record["items"])
        category_output.append(f"{header}: {items}")
    return category_output

def run_summary_pipeline():
    structured = build_structured_summary(SITE_DATA)
    print("=== 结构化摘要（文本） ===")
    print(format_summary_text(structured))
    print()
    print("=== 结构化摘要（JSON） ===")
    print(format_summary_json(structured))
    print()
    print("=== 示例分类 ===")
    for line in display_categories(_EXAMPLE_RECORDS):
        print(line)

def main():
    run_summary_pipeline()

if __name__ == "__main__":
    main()