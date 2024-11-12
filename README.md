# TODO:

## Rag学習

- [Ragを導入するにあたっての一般知識](https://zenn.dev/spiralai/articles/8af7cbf526c2e1)

<br />
<br />


## 開発手順

FAQボットを構築するために適した技術スタック、プログラミング言語、フレームワーク、インフラを以下にまとめます。

---

### 1. **要件定義**

- **技術**：Google DocsやNotionなどのコラボレーションツール
- **目的**：FAQのリストと回答内容の整理。初期段階の質問と回答のペアの構成。

---

### 2. **データの準備とインデックス化**

- **データ準備**：PythonやNode.jsを使ってJSONやCSV形式でデータを構築。
- **リトリーバルエンジン**：以下の選択肢からインデックス化と検索機能を実装
    - **Pinecone**（Pythonサポート、類似度検索特化）

---

### 3. **リトリーバル（検索）機能の構築**

- **言語**：PythonまたはJavaScript (Node.js)
- **フレームワーク**：
    - **Python**の場合：FastAPIまたはFlaskでAPIを構築し、リトリーバルと生成モデルを接続。
- **ベクトル検索**：より精度が求められる場合は、PineconeやWeaviateを使用し、FAQデータをベクトル埋め込みして類似度検索を行います。

---

### 4. **生成モデルの設定と統合**

- **言語**：PythonまたはJavaScript
- **生成モデル**：
    - **OpenAI GPT API**：自然な応答生成に高い精度を持つため、回答の生成に利用。
    - **Hugging Face Transformers**：ローカルモデルの選択肢として使える。
- **統合**：リトリーバルエンジンで取得した回答候補を生成モデルの入力として使い、ユーザーに自然な回答を提供。

---

### 5. **インターフェースの構築**

- **フロントエンド**：
    - **React**（JavaScriptまたはTypeScript）でチャットUIを構築し、ユーザーが質問を入力・回答を閲覧できるようにします。
    - **Streamlit**や**Gradio**（Pythonのみの実装なら簡単なUI構築に最適）も短期間で構築可能。
- **UIフレームワーク**：Material-UI（Reactのデザインコンポーネント）、Bootstrap
- **チャットボット用ライブラリ**：React Chatbot Kit

---

### 6. **テストと調整**

- **自動テスト**：
    - **APIのテスト**：PostmanやPytest（Python）でリトリーバルや生成部分のAPIのテストを実行。
    - **UIのテスト**：JestやCypress（ReactのUIテストツール）で、ユーザーインターフェースが正しく動作するか確認。
- **フィードバック収集**：
    - **Google Analytics**や**Sentry**でユーザーの利用状況やエラーをトラッキング。

---

### 7. **デプロイと運用**

- **クラウドプロバイダー**：
    - **AWS**（Elastic BeanstalkやEC2、Elasticsearchサービスを利用）
    - **GCP**（App EngineやCloud Run）
    - **Azure**（App ServiceやCognitive Searchサービス）
- **コンテナ化**：
    - **Docker**でAPIや生成モデルのコンテナを作成し、クラウドにデプロイ。
- **CD/CI**：
    - GitHub ActionsまたはGitLab CI/CDで自動デプロイを設定。

---

### 推奨される技術スタックまとめ

- **言語**：Python（データ処理や生成モデル）、JavaScript（フロントエンド）
- **バックエンド**：FastAPI（Python）
- **リトリーバル**：Pinecone
- **生成モデル**：OpenAI GPT APIまたはHugging Face Transformers
- **フロントエンド**：React、Material-UI
- **デプロイ**：AWS（Elastic Beanstalk、Elasticsearch、S3）、またはGCP（App Engine）

このスタックで開発すれば、FAQボットの各ステップに必要な機能を十分にカバーできます。