#!/usr/bin/env python3
# 注意: このファイルはいじらないでください

import typing
from missmatch import add_one

assert typing.get_type_hints(add_one)["x"] == str, "引数xの型ヒントがintではありません"
assert (
    typing.get_type_hints(add_one)["return"] == str
), "戻り値の型ヒントがintではありません"
