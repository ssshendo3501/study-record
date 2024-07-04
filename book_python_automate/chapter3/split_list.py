# 売上データを顧客ごとに集計するプログラム
# 1. matome.xlsxを開く
# 2. 顧客ごとにデータを分割
# 3. 請求金額を求める

import openpyxl as excel, json


# 入出力ファイルの指定
in_file = 'matome.xlsx'
out_file = 'matome.json'

# main処理
def split_list():
    # Excelシートのデータを顧客ごとに分ける
    users = read_and_split(in_file)
    # 顧客ごとのデータを集計する
    result = {}
    for name, rows in users.items():
        result[name] = calc_user(rows)
        print(name, result[name]['total'])
    # ファイル結果をjsonで保存
    with open(out_file, 'wt') as fp:
        json.dump(result, fp)
    

# 入力ファイルを読んで顧客ごとに分割
def read_and_split(in_file):
    users = {}
    # ブックを開いてシートに全行読む
    sheet = excel.load_workbook(in_file).active
    
    for row in sheet.iter_rows(min_row=1, values_only=True):
        # シートを一行取り出してリストに保存
        values = list(row)
        name = values[1]
        # 初出ならリスト初期化
        if name not in users: 
            users[name] = []
        # データを顧客ごとに分ける
        users[name].append(values)
        # print(name, values[1], values)
        # print('--------------')
    return users


# 顧客一人分のデータを集計する
def calc_user(rows):
    total = 0
    items = []
    # 集計処理を行う
    for row in rows:
        # 請求書に必要な項目だけ抽出して請求書明細の形式で追加
        date, _, item, cnt, price, _ = row
        date_s = date.strftime('%m/%d')
        items.append([date_s, item, cnt, price]) 
        # 合計金額を計算
        total += cnt * price 
    # 集計結果を辞書形式で返す)
    # print(f'items: {items}, total: {total}')
    return {'items': items, 'total': total}

    
if __name__ == '__main__':
    split_list()

