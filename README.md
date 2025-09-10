# Banner Generation AI (MVP)

AIを利用して、シンプルな **バナー / ポスター形式のSVGファイル** を自動生成するツールです。  
生成されたSVGは **Figma / Illustrator / Webブラウザ** で編集・プレビュー可能です。  

---

## ✨ 特徴
- **OpenAI API** を利用してテキストからSVGを生成
- SVG形式で保存するため、拡大縮小しても劣化なし
- 出力ファイルはそのまま **Illustrator / Figma** で編集可能
- 将来的に **デザイナーテンプレート × AI差し込み** のワークフローを想定

---

## 🛠️ セットアップ

### 1. リポジトリをクローン
```bash
git clone https://github.com/yourname/banner-ai.git
cd banner-ai
```

### 2. 仮想環境を作成 & 有効化
```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
### 3. 必要ライブラリをインストール
```bash
pip install -r requirements.txt
```

### 4. OpenAI APIキーを設定
```bash
export OPENAI_API_KEY="sk-xxxx..."   # macOS/Linux
$env:OPENAI_API_KEY="sk-xxxx..."    # Windows PowerShell
```

---

## 🚀 使い方

### 1. サンプルコードを実行
```bash
python main.py
```

### 2. 出力
- output.svg が生成されます
- ブラウザで開くとプレビュー可能
- Illustrator / Figma に読み込んで編集可能

---

## 📄 サンプル出力（SVG抜粋）
```xml
<svg xmlns="http://www.w3.org/2000/svg" width="300" height="250">
  <rect width="300" height="250" fill="#FF6600"/>
  <text x="150" y="120" font-size="24" text-anchor="middle" fill="#ffffff">
    秋のセール開催！
  </text>
  <text x="150" y="160" font-size="16" text-anchor="middle" fill="#ffffff">
    最大50%OFF、今だけ
  </text>
</svg>
```

---

## 🧩 今後の展望
- **テンプレート対応**
  - デザイナーが作成したSVGテンプレートにプレースホルダーを埋め込み
  - Python側でテキスト・画像を差し替え可能にする

- **画像生成連携**
  - Adobe Firefly等で生成した背景画像をSVG内に挿入

- **GUI化**
   - CLIベースからWeb UI / Figma Plugin への拡張

---

## 📚 技術メモ
- SVGは XMLベースのベクター形式 なので編集・検索・バージョン管理が容易
- ```xmlns="http://www.w3.org/2000/svg"``` を必ず含める必要あり
- AI出力には余分なコードブロックが混ざる場合があるため、保存時にクリーンアップ処理を実施

---

## 👥 想定ユーザー
- デザイナー : テンプレートを作成し、生成結果をFigmaやIllustratorで調整
- マーケター / ディレクター : 叩き台としてAI出力を利用し、コピーやレイアウトのバリエーションを確認
- エンジニア : ワークフロー自動化やAPI連携を実装

---

📌 ライセンス
MIT

---
