import glob
import openpyxl as excel


# 対象フォルダと保存先ファイル名を指定
target_dir = './salesbooks'
save_file = 'matome.xlsx'


# メイン処理
def read_files():
    # 売上一覧を書き込むブックを用意する
    book = excel.Workbook()
    main_sheet = book.active
    
    # ファイルを列挙して読む
    enumfiles(main_sheet)
    book.save(save_file)
    

# ファイルを列挙する
def enumfiles(main_sheet):
    # Excelファイルの一覧を得る
    files = glob.glob(f'{target_dir}/*.xlsx')
    # 各Excelファイルを次々と読み込んでいく
    for fname in files:
        read_book(main_sheet, fname)


# ブックを開いて中身を読む
def read_book(main_sheet, fname):
    print("read", fname)
    # Excelブックに読み込む
    book = excel.load_workbook(fname, data_only=True)
    sheet = book.active
    # 売上データをのある範囲を読み取る
    rows = sheet['A4': 'F99']
    for row in rows:
        # セルの値をリストとして得る
        values = [cell.value for cell in row]
        if values[0] is None: break
        print(values)
        # メインシートに値をコピー
        main_sheet.append(values)
  
    
# メインプログラムを実行
if __name__ == '__main__':
    read_files()