from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = """
あなたはSVGデザイナーです。
以下の条件でシンプルなポスター風SVGを生成してください。
- サイズ: 300x250
- 背景色: #FF6600
- 見出し: 秋のセール開催！
- サブコピー: 最大50%OFF、今だけ
- CTA: 今すぐチェック

注意:
- <svg>タグを必ず含める
- テキストは<text>タグで残す
- 出力はSVGコードのみ
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

svg_code = response.choices[0].message.content

# 1. コードブロックを削除
svg_code = svg_code.strip()
if svg_code.startswith("```"):
    svg_code = "\n".join(line for line in svg_code.splitlines() if not line.startswith("```"))

# 2. xmlnsが無ければ追加
if "<svg" in svg_code and "xmlns" not in svg_code:
    svg_code = svg_code.replace(
        "<svg",
        '<svg xmlns="http://www.w3.org/2000/svg"',
        1
    )

with open("output.svg", "w", encoding="utf-8") as f:
    f.write(svg_code)

print("✅ output.svg を生成しました！")
