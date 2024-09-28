## Gunicornとは
Pythonアプリケーション向けのWSGI（Web Server Gateway Interface）サーバー、ASGI（Asynchronous Server Gateway Interface）サーバーとしても連携可能
uvicornより推奨されている（公式）
複数のワーカー（プロセス）を立ち上げ並列リクエストを処理→CPUコアを最大限に活用、スレッドセーフが前提
DjangoやFlaskなどのWSGIアプリケーションに対してよく使われる
生産環境での使用を意識して設計、スケーラブル
プロセスベースの並列処理モデル


## Gunicornとuc\vicornの関係
GunicornはWSGIサーバー、uvicornはASGIサーバー
Gunicornはプロセス管理を担当、uvicornは非同期の処理を実行
FastAPIが非同期フレームワークであるのでどちらも使用（連携）が推奨されている



## 02_FastAPIとgunicornを使ってWebアプリケーションを作成する
docker compose up -d
docker ps

http://localhost:8000にアクセスすると、一般的なHTTPサーバの返答が表示される
http://localhost:8000/docsにアクセスすると、Swagger UIが表示される

## 止める
docker stop <CONTAINER ID>