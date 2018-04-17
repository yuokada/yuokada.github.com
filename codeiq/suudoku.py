#!/usr/bin/env python3
"""
【概要】
簡単なナンプレの問題を解くプログラムを書いてみましょう。

【問題】
次のようなナンプレがあります。
・2x2のマス（Box）が縦横ふたつずつ並んだ4x4のマスがある
・それぞれのマスには1~4の数字が入り、それらは行／列の4つのマスに同じ数字がくることはない（行／列の合計は10となる）
・2x2のマス（Box）にも同じ数字がくることはなく、合計は10となる
・最初に1~4の数字がランダムにひとつずつ設定されている（同じ行／列／Boxに複数の数字が設定されることは無い）

初期状態の例（＿は数字の入っていない状態を表します）
┏━┯━┳━┯━┓
┃１│＿┃＿│＿┃
┠─┼─╂─┼─┨
┃＿│＿┃３│＿┃
┣━┿━╋━┿━┫
┃＿│＿┃＿│４┃
┠─┼─╂─┼─┨
┃＿│２┃＿│＿┃
┗━┷━┻━┷━┛

このナンプレを解くプログラムを書いて、数字を埋めてください。

【入出力】
CSV形式のテストデータを標準入力で受け取る想定で、結果を標準出力するプログラムを作ってください。

上図のナンプレでは、以下のようなCSVファイルが入力されます。
"""

import random
import sys

base = set([1, 2, 3, 4])


def read_prob():
    mass = []

    try:
        for i in range(4):
            line = input().strip().upper()
            mass.append([int(x) for x in line.split(",")])
    except EOFError:
        pass

    return mass

# =============


def set_row(line):
    r = list(filter(lambda x: x != 0, line))[0]
    nokori = list(base - set([r]))
    rand_ints = random.sample(nokori, len(nokori))
    ume = []
    for _, n in enumerate(line):
        if n:
            ume.append(n)
        else:
            ume.append(rand_ints.pop())
    return ume


def set_mass(mass):
    counter = 0
    while True:
        ume_mass = []
        for l in mass:
            ume_mass.append(set_row(l))
        result = calc_mass(ume_mass)
        if result:
            for l in ume_mass:
                print(",".join([str(s) for s in l]))
            break
        counter += 1
        if counter >= 1024 * 100:
            print("Not Found!")
            return False


def calc_mass(mass):
    ANSWER = 24
    for j, _ in enumerate(mass):
        tate = 1
        for m in mass:
            tate *= m[j]
        if tate != ANSWER:
            # 24( = 1 * 2 * 3 * 4) にならなかったらbreak
            break
    else:
        # 途中でbreakしなかったら正解の配置
        return True
    return False


if __name__ == '__main__':
    def_mass = [
        [1, 0, 0, 0],
        [0, 0, 3, 0],
        [0, 0, 0, 4],
        [0, 2, 0, 0],
    ]
    set_mass(def_mass)
    sys.exit(0)
    # mass = read_prob()
    # set_mass(mass)
