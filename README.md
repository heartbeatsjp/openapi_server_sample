# OpenAPI server sample

OpenAPIの定義を出力するためのAPIサーバーのサンプルプログラムです。

FastAPIを用いて実装しています。

対応するフロントエンドのアプリケーションは以下のリポジトリです。
https://github.com/heartbeatsjp/openapi_front_sample

# 使い方

## コンテナの起動

devcontainerを利用しています。VS Codeよりdevcontainerを起動してください。

## アプリケーションの起動

devcontainer起動後、以下のコマンドを実行してください。

```bash
make dev
```

### 動作を確認する場合
アプリケーション起動後 http://127.0.0.1:8081 にアクセスしてください。`hello world`が表示されます。

### OpenAPIスキーマを確認する場合
アプリケーション起動後 http://127.0.0.1:8081/openapi.json にアクセスすると、OpenAPIの定義が表示されます。

### Swagger UIを表示する場合
アプリケーション起動後 http://127.0.0.1:8081/docs にアクセスすると、Swagger UIを用いてAPIを確認できます。

## OpenAPIスキーマファイル出力

http://127.0.0.1:8081/openapi.json にアクセスせずにOpenAPIの定義を表示するには、以下のコマンドを実行してください。`./openapi.json`にOpenAPIの定義が出力されます。

```bash
make generate
```

