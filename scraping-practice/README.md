

# スクレイピング練習用プロジェクト

このリポジトリは、PythonとFlaskを使って構築した「スクレイピング練習用サイト」と、それを学ぶための「解説ページ」で構成されています。


scraping-practice/
├── README.md
├── requirements.txt
├── docs/
│ ├── index.html # 解説ページ（リンクつき）
│ └── style.css # 解説用CSS
├── scraping_demo/
│ ├── app.py # Flaskアプリ本体
│ ├── data_generator.py # （未使用なら削除OK）
│ ├── static/
│ │ └── style.css # サイト用CSS
│ └── templates/
│ ├── index.html # トップページ
│ ├── products.html # 商品一覧
│ ├── article.html # 記事ページ
│ └── reviews.html # レビュー一覧