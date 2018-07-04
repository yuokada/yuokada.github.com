===============
職務経歴 その2
===============

2016年01-09月
=============

仕事としてエンジニアっぽくない期間だった。
ドキュメント書いたりOJTの業務したりと自分でコード書く期間では無かったように思う。
フラストレーションが溜まりやすい環境だったけど、思うに業務と評価の関連性が薄いから
ガンバっても評価されないというのが直接の原因だったようにきがする。


Pull Requests
-------------

仕事関連で出したPRがほとんど。

- `Fix the markdown syntax error. by yuokada · Pull Request #296 · prestodb/presto-admin <https://github.com/prestodb/presto-admin/pull/296>`_
- `enable timeout when https by yuokada · Pull Request #2 · marant/goloris <https://github.com/marant/goloris/pull/2>`_
- `Use time.Duration by yuokada · Pull Request #1 · marant/goloris <https://github.com/marant/goloris/pull/1>`_
- `Fix ineffassign error by yuokada · Pull Request #3 · sony/sonyflake <https://github.com/sony/sonyflake/pull/3>`_
- `Add pp parameter by yuokada · Pull Request #12 · fukata/golang-stats-api-handler <https://github.com/fukata/golang-stats-api-handler/pull/12>`_
- | `[WIP] Add function to to shorten and format numbers by yuokada · Pull Request #6437 · prestodb/presto <https://github.com/prestodb/presto/pull/6437>`_
  | マージされてないけど。

2016年10月-2017年9月
====================

新しいチームに異動。 運用業務を中心に

`Presto | Distributed SQL Query Engine for Big Data <https://prestodb.io/>`_

- Prestoの導入調査と環境構築
- CentOS7上での運用のためのパッケージ開発・環境構築

- 利用技術

  - systemd
  - firewalld
  - rpm/fpm

2017年10月-現在
====================

継続してPrestoの開発・運用を主な業務として実施している。
開発の比率が徐々にだが上がって来ている。


`Platform as a Service` としてPrestoを提供するための技術調査を実施。

- Apache Mesos と Marathonを中心に調査
- Kubernetesも少しだけ調査

  - PoCとなるデモ環境の開発・構築を担当


利用技術
--------

- Mesos / Marathon
- Python3.6 / Django
- traefik : `containous/traefik: The Cloud Native Edge Router<https://github.com/containous/traefik>`_
