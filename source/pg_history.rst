==================
プログラミング履歴
==================

大学時代
========

- 大学に入ったのが2005年でプログラミングに興味を持てたのは授業かな？
- | それと株やってた影響。 OmegaChartっていうオープンソースのソフトを使っていたのでそれを自分で拡張してみたかった。
  | 実際にやったのはXMLの設定ファイルをいじる程度だったｗ
- 授業のfortran, C言語、Javaを一応触ったぐらい。
- 橋本先生のバイトで始めたPerl

----
Perl
----

- | これが本格的に手を付けたはじめの言語。
  | 大学時代に作った地震データ解析プログラム。

  - 今にすればヒドイものだ
  - データベースなんてものは一切知らなかったので
    強引にCSVファイルの解析をしてたっけ
  - まだコードがあるけど１０００行超えるものだった。
  - sprintf の存在を知らなくて何百業もおんなじようなコード書いてしまった。
  - 正規表現もいまいち理解してなかったからその辺も原因かな。

- 今ならデータベースとSQLを使って１００行かそこらで書ききれると思う。
- あと、O/Rマッパー使うと思うからへたしたら１００行も切るかもね。
- エラー処理もやってないし

------
Python
------

- Perlのあとに他の言語やりたいなと思って学生生協ぶらついてたら
  PythonとRubyの本に出会った。
- 某新聞によればグーグル独自言語のパイソンっていうものがあるらしいwww
  もちろん、その独自言語とは違うよ
- 当時はGoogle万歳の時代だったので日本人が作った言語のRubyと迷ったけど
  Pythonを選んだ
- Rubyの作者・まつもとゆきひろと下の名前が一緒っだので多少の親近感はあったけど
  Googleのほうが勝った。
- pythonの入門書にはみんなのpythonを使った
- オブジェクト指向なにそれ？美味しいの？状態だった自分には途中から難しかったけど
  一応ひと通り読みきってわかったつもりになっていた。
- 今読んだらモジュールとかChees Shopとか古い部分があるけど言語の説明のところは今読んでもいい本だと思う。
- 2版が去年辺りに出てるのでそれだと修正はいってるはず。
- pythonはインデントが嫌いっていう人が多いけど、
  僕はあれのお陰で綺麗にプログラミングするっていうことを覚えた人間なのであれには一切抵抗がない
- self は確かにめんどくさい。 これは何とかならないかな？
  関数からクラスメソッドに移す際にそのままカットアンドペーストだとダメでselfを追加する手間がある

-------
R言語
-------
- あと、研究で得られたデータをグラフで表示するときに使ってたぐらい。
- CSVを食わせて強引にデータをグラフにしてたかな。
- 今ではすっかり忘れてしまった。

入社後
======

---
PHP
---
- 入った時に使ってたのが5.2だった。
  5.3はリリースされたけど単体テストや結合テストが揃ってなかったので移行できなかった。
- コードが全般的に汚いのでPHP使う仕事はあまり好きじゃない。
- WEBツールのソース読んでたら配列と連想配列の使い方を全く知らないような人間が書いたコード見つけたり、
  いろいろイケてないコード見続けたのが原因。
- コーディング規約が無かったのが痛かった。
- 名前空間なにそれ状態を続けてる。

-----
MySQL
-----

- 会社に入って初めて知って会社に入ってから一番好きになったプロダクト
- SQLの書き方を位置から学んでいまはビューも普通に書けるようになった。
- UDFとNative Function を作る経験もした。
- MySQLでログを一定期間保存するようなシステムを作ったときに、
  RANGEパーティションなんかを覚えた。
- スケジューラもレプリケーションの遅延監視でちょびっと触った。
- ストアドは触ったけどプロダクトで使う前に離れたのでそこまで詳しくなれなかった。
- Spidrストレージエンジン使ってみるという経験もした。
  スパイダーは最近は更新が殆ど無いのでどうなってるんだろうか？

----
Perl
----

- Mooseはいいけどテスト駆動開発したり単体テスト走らせるにはちょっと重いんだよね。

  頻繁に走らせないならいいんだけどコード書くのがヘタでテストいっぱい走らせたい人にはしんどい。

- オブジェクト指向開発
- WebService::SimpleやPararell::Prefork使って並行処理するソースを動かしてたりしたこともあった。


-------
Python
-------

- 本格化
- モジュール書いたよ!
  githubに上がってるコードから判断して。
- 1人プロジェクトでFlask使ってWebAPI作ったり、そのドキュメントをSphinxで書いていたのが2013年の10月-2013年3月ぐらい。
- 社内のPython利用者支援(数が少ないので二、三人で支援できてたｗ)とかそんな状態。

-----------------
Javascript&jQuery
-----------------

- grease monkeyの拡張書いたりしたときにちょっとだけ。
- 最近は Coffee Scriptに興味がある。
- キレイなJS書くのは結構な手間なのでCoffee ScriptでJS書けるならなるべくそっちがいいなと。
  githubも新しいJSはCoffee Scriptで書くといってるしベストプラクティスではないかもしれないけど
  ベタープラクティスだと考えている。
- Firebug使ってブラウザからデータ抜くような使い方がほとんど。

-----
Go
-----

- Goconとか行き始めたのが2013年秋口から。
- 最初はPerlスクリプトの置き換えで主に活躍
- 管理するサーバー台数が増えるにつれて並列処理が必要になってきてgoroutine活用のスクリプトを書き始めた。
- 業務で書く簡単なサーバーは徐々にGoで作る流れが出来てきた。

2016/10
=======

- | 最近、prestoとそのエコシステムを触ってる。
  | `Presto | Distributed SQL Query Engine for Big Data <https://prestodb.io/>`_
- CentOS7の上に環境を構築してるので `systemd` とかも合わせて触ってる

Future
======

- not PF as a Servisce but PF is a service
