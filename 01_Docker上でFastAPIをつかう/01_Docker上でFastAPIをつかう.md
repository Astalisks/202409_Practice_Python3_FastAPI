## FastAPIとは
ASGIに対応（Pythonの非同期Webフレームワーク）
特にI/Oバウンドな処理において、同期的なフレームワークよりも効率的に動作
少ないコードでRESTful APIを構築
Pydanticを使用したデータバリデーション
OpenAPI（以前のSwagger）仕様に準拠
単体でHTTPリクエストを処理するHTTPサーバーを持っていない

## uvicornとは
ASGIサーバーの一つ、HTTPサーバー
シングルスレッドの非同期サーバーで、非常に軽量で高速

## Swaggerとは
現OpenAPI仕様に準拠しており、APIのインターフェースや使用方法を自動でドキュメント化
FastAPIに組み込まれているため、FastAPIを使ってAPIを作成すると自動でSwagger UIが生成される



## Docker上でFastAPIをつくる
docker build -t my_fastapi_app .
docker run -d -p 8000:8000 my_fastapi_app
docker ps

http://localhost:8000にアクセスすると、一般的なHTTPサーバの返答が表示される
http://localhost:8000/docsにアクセスすると、Swagger UIが表示される

## 止める
docker stop <CONTAINER ID>