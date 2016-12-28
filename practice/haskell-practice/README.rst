==============================
ふつうのHaskellプログラミング
==============================

`ふつうのHaskellプログラミング ふつうのプログラマのための関数型言語入門 | 青木 峰郎, 山下 伸夫`__

.. __: https://www.amazon.co.jp/dp/4797336021/


これの写経的なディレクトリ。


.. ::

    Python_ は、
    `私のお気に入りのプログラム言語`__ です。
    .. _Python: http://www.python.org/

    __ Python_


ChangeLog
=========

2016/12/05
----------

- | 最新のコンパイラに合わせたコードのリポジトリ
  | https://github.com/qtamaki/stdhaskell-samples.git

.. code-block:: bash

    $ git clone https://github.com/qtamaki/stdhaskell-samples.git

2016/12/03
----------

- 3,4章完了
- パターンマッチ周りすっかり忘れてた。
  factorial関数を書いてみた。

  .. code-block:: haskell

      factorial :: Int -> Int
      factorial 1 = 1
      factorial n = n * factorial  (n - 1)

2016/11/13
----------

- 2章まで読了。
- 3章のパターンマッチのところで中断中

links
=====

- http://d.hatena.ne.jp/kk_Ataka/20111202/1322839748
