# with openの引数にmode="w"を指定してファイルの書き込みを行う
# mode="w"を使うと、上書きが実行される
with open("writing_file.txt", mode="w") as f:
    # truncatedされる：byte=0に切り詰める
    f.write("You can write contents texts\nuse 'backslash' to break the row\n")
    f.write("new write() doesn't break row\n")

    # print文を使って書くことも可能
    print("You can add a new using 'file parameter'", file=f)
    print("new print() method breaks the row for you", file=f)
    # print(f.read()) # mode="w" はreadはできないので注意する
