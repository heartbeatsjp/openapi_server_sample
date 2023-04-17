# OpenAPI server sample

OpenAPIの定義を出力するためのAPIサーバーのサンプルプログラムです。

FastAPIを用いて実装しています。

# 使い方

## コンテナの起動

devcontainerを利用しています。VSCodeよりdevcontainerを起動してください。

## アプリケーションの起動

devcontainer起動後、以下のコマンドを実行してください。

```bash
make dev
```

アプリケーション起動後 http://127.0.0.1:8081 にアクセスすると`hello world`が表示されます。

http://127.0.0.1:8081/openapi.json にアクセスすると、OpenAPIの定義が表示されます。

http://127.0.0.1:8081/docs にアクセスすると、Swagger UIが表示されます。


## OpenAPI

http://127.0.0.1:8081/openapi.json にアクセスせずにOpenAPIの定義を表示するには、以下のコマンドを実行してください。`./openapi.json`にOpenAPIの定義が出力されます。

```bash
make generate
```

