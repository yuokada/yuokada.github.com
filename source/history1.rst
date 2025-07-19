===========
職務経歴
===========

2009年4月 ~ 2013年3月
=========================

- 2009年4月 入社
- 2009年7月 コメントシステムのWebAPI開発・保守チームに配属

業務内容
--------

- PHP でのWebAPI保守
- カスタマーサポート(CS)ツールへの機能追加

  - Role / 権限管理機能の導入
  - データベースの冗長化構成への切り替え

- コメント削除バッチ開発

  表示期間が終了したコメントをDBと検索インデックスから削除するためのバッチ開発

- WebAPIの設計・開発

  - Python2.7/Flask製 Restful WebAPIサーバー - MySQL - Redis.
  - MySQL スキーマ設計
  - Redis Key設計

2013年4月 ~ 2016年9月
=========================

Webビーコン、リダイレクター を運用するチームに異動。

業務内容
--------

- OSの乗せ換え: FreeBSD6 -> CentOS6への移行作業
- Webビーコンのキャパシティ管理、モニタリング周りの改善

  - サーバーのパフォーマンス検証
  - モニタリング情報の精査
  - リクエストの可視化のために `Influxdb/Grafana` の導入

- デプロイ作業の短縮 - 1000台超のサーバーへのデプロイ作業の簡素化
- 高負荷でのサーバーの運用とnagiosによる監視業務
- ユーザーの行動履歴を取るためのブラウザの新機能の調査と参考実装
- `Golang` によって周辺ツールのパフォーマンス改善

  - デプロイ時にリダイレクターが期待した動作をするかの動作確認ツールがあり
    HTTPリクエストを投げてレスポンスを確認をしていた箇所を並列化して高速化。

- `nginx`, `Appache Trafic Server(ATS)` によるSSL証明書の運用

  - SSL証明書の監視
  - SANオプションつきSSL証明書の導入

- レガシーシステムの統廃合の調整

  機能が似通ったビーコンを廃止するための社内調整

その他の業務
---------------

- OJTトレーナー
- 外向けのイベント運営

Pull Request
------------

- `enable timeout when https by yuokada · Pull Request #2 · marant/goloris <https://github.com/marant/goloris/pull/2>`_
- `Use time.Duration by yuokada · Pull Request #1 · marant/goloris <https://github.com/marant/goloris/pull/1>`_
- `Fix ineffassign error by yuokada · Pull Request #3 · sony/sonyflake <https://github.com/sony/sonyflake/pull/3>`_
- `Add pp parameter by yuokada · Pull Request #12 · fukata/golang-stats-api-handler <https://github.com/fukata/golang-stats-api-handler/pull/12>`_

2016年10月-2017年9月
====================
分散クエリ処理エンジン `Presto` を開発・運用するチームに異動。

`Presto | Distributed SQL Query Engine for Big Data <https://prestodb.io/>`_

業務内容
--------

- Prestoの導入と構成の調査・パフォーマンスなど検証

  - トラフィックが出るところでインフラを担当する部署とNW周りの調整業務を担当

- 運用のためのchef クックブックなど環境構築周りを中心に担当
- CentOS7上での運用のためのパッケージ開発・環境構築

利用技術
--------

- CentOS7
- Java8
- Prestodb
- Object Storage
- chef / chef server
- systemd
- firewalld
- rpm/fpm


その他の業務
------------

- OJT: チーム開発でのプロダクト・オーナーとしてチューター的な役割を担当
- インターンシップ: チーム内でのインターンシップ担当としてコードレビューを主に担当

2017年10月-2019年3月
====================

継続してPrestoの開発・運用を主な業務として実施している。前期よりも開発の比率が徐々にだが上がって来ている。

`Platform as a Service` としてPrestoを提供するための技術調査を実施。

- `Apache Mesos` と そのフレームワークの `Marathon` を中心に調査
- `Kubernetes` も少しだけ調査

  - PoCとなるデモ環境の開発・構築を担当
  - 社内認証基盤 `Athenz` を利用するためのプラグイン開発

利用技術
--------

- Mesos / Marathon
- Python3.6 / Django
- traefik : `containous/traefik: The Cloud Native Edge Router <https://github.com/containous/traefik>`_
