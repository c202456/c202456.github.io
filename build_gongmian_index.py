from pathlib import Path
import re
from urllib.parse import quote

QUARTZ = Path.home() / "Documents" / "quartz"
FOLDER = (
    QUARTZ
    / "content"
    / "我的知識庫"
    / "佛堂"
    / "先生與眾共勉事項"
)
INDEX = FOLDER / "index.md"

pattern = re.compile(
    r"^(?P<number>\d+)-"
    r"(?P<year>\d{4})\."
    r"(?P<month>\d{2})\."
    r"(?P<day>\d{2})\.md$"
)

if not FOLDER.exists():
    raise SystemExit(
        f"❌ 找不到資料夾：\n{FOLDER}"
    )

articles = []

for file in FOLDER.glob("*.md"):
    if file.name == "index.md":
        continue

    match = pattern.match(file.name)
    if not match:
        continue

    articles.append(
        {
            "file": file,
            "stem": file.stem,
            "number": match.group("number"),
            "year": int(match.group("year")),
            "month": int(match.group("month")),
            "day": int(match.group("day")),
        }
    )

articles.sort(
    key=lambda item: (
        item["year"],
        item["month"],
        item["day"],
        int(item["number"]),
    ),
    reverse=True,
)

years = {}

for article in articles:
    years.setdefault(article["year"], []).append(article)

parts = [
    "---",
    "title: 先生與眾共勉事項",
    "---",
    "",
    '<div class="gongmian-header">',
    f'  <div class="gongmian-count">共 {len(articles)} 篇文章</div>',
    '  <div class="gongmian-tip">可使用左上角搜尋功能搜尋文章內容或編號</div>',
    "</div>",
    "",
]

for index, year in enumerate(sorted(years.keys(), reverse=True)):
    year_articles = years[year]
    open_attr = " open" if index == 0 else ""

    parts.append(
        f'<details class="gongmian-year"{open_attr}>'
    )

    parts.append(
        "<summary>"
        f"<span>{year} 年</span>"
        f'<span class="gongmian-year-count">'
        f"{len(year_articles)} 篇"
        "</span>"
        "</summary>"
    )

    parts.append('<div class="gongmian-list">')

    for article in year_articles:
        number = article["number"]
        date = (
            f'{article["year"]}.'
            f'{article["month"]:02d}.'
            f'{article["day"]:02d}'
        )

        href = "./" + quote(article["stem"], safe="-.")

        parts.append(
            f'<a class="gongmian-item" href="{href}">'
            f'<span class="gongmian-number">{number}</span>'
            f'<span class="gongmian-date">{date}</span>'
            f'<span class="gongmian-arrow">→</span>'
            "</a>"
        )

    parts.append("</div>")
    parts.append("</details>")
    parts.append("")

INDEX.write_text(
    "\n".join(parts),
    encoding="utf-8",
)

print(f"✅ 共找到 {len(articles)} 篇文章")

for year in sorted(years.keys(), reverse=True):
    print(f"   • {year} 年：{len(years[year])} 篇")

print("✅ 年份索引頁已重新產生")
