#!/usr/bin/env python3
"""
あなたはデータベースの再設計を任されており、インデックス設計のため、
まずデータのカーディナリティ（cardinality）を調査するよう依頼されました。

カーディナリティとは列内に含まれるデータの一意性を示すもので、
性別のように反復データが多い場合は「低く」、一方名前のように一意のデータが多い場合は「高く」なります。

今回はまず列ごとにどれだけユニークな（一意な）項目の数があるか、
元データであるCSVファイルから計測することにしました。



本設問で求められるプログラムの前提条件は、以下の通りとなります。

    標準入力から、CSV形式のASCII文字のみで構成された行列データが送られる
    CSVの先頭行はタイトル行、２行目以降を集計対象であるデータ行とする
    CSVは1行あたり、最大80文字、最大４項目とする
    CSVは最大で10,000行とする
    CSVの項目は、文字列または数値とする
    項目が一意かどうかの判定は、一致しているかのみで決めること（正規化は不要）
    CSVの項目の中には制御文字や、エスケープを要する文字は含まれないものとする
    CSVはカンマ(,)区切りであり、項目を囲む括り文字はないものとする
    各列のユニークな項目の数を、CSV形式にて一行で標準出力に返すこと

以下、入力と出力例です。
<Cut>

データベースのインデックス設計において、カーディナリティはパフォーマンスやサイズを決める重要な指標です。
一般に低すぎるカーディナリティの列に対して、インデックスを作成するのは得策ではないため、
複数列を対象とした複合インデックスが検討されたりします。
それでは、是非挑戦してみてくださいね。
なお、本設問で用いるデータはすべて架空のものであることをご了承ください。
"""

import collections
import sys

def read_prob():
    inputs = []
    try:
        while True:
            line = input().strip()
            inputs.append(line)
    except EOFError:
        pass
    return inputs

# =============

def get_ordered_dict(first_line):
    d = collections.OrderedDict()
    for i, k in enumerate(first_line.split(',')):
        d[k] = set()
    return d

class Column(object):

    def __init__(self, index, name):
        self.index = index
        self.name = name


if __name__ == '__main__':
    inputs = read_prob()
    d = get_ordered_dict(inputs[0])
    # get k/v
    kvs = {k:v for k, v in enumerate(inputs[0].split(','))}
    for l in inputs[1:]:
        values = l.split(',')
        for i, v in enumerate(values):
            key = kvs[i]
            d[key].add(v)

    # print(d)
    cardinalies = [str(len(sets)) for k, sets in d.items()]
    print(",".join(cardinalies))
    sys.exit(0)
