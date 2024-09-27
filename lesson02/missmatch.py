# 型のミスマッチが起こすバグの例


def add_one(x: int) -> int:
    return x + 1


def is_int_list(lst: list[any]) -> bool:
    for item in list:
        if not isinstance(item, int):
            return False
    return True


print(f"{__name__ =}")

if __name__ == "__main__":
    pass  # ここに上記関数を使うコードを書いてみる
    #
    # print(f"{add_one(42) + 3 = }")
    print(f"{is_int_list([1,2,3])}")
    print(f"{is_int_list([1,'2',3])}")
    print(f"{is_int_list(1)}")
