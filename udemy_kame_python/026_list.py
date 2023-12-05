# List型（lists）：複数のオブジェクトを順序づけて保存するデータ型
# リストの中にある要素をindexと呼び、indexは0から始まる

fruits = ['apple', 'peach', 'melon', 'grapes']
hetro_list = ['string', 1, 3.4, True, fruits] # hetro_listの中にfruitsのListや様々なオブジェクトが入っている

print(hetro_list)

# リストの中の特定の要素を取り出す
# 最初の要素は[0]、左から0,1,2,3
print(fruits[0]) # apple

# 一番後ろは[−1]、左から-4,-3,-2,-1
print(fruits[-1]) # grapes
print(fruits[-4]) # apple

print(hetro_list[-1][-1]) # hetro_listの中の最後の要素：grapesを取り出す

# 文字列のIndexも取得することが可能
print("helloworld"[3]) #h,e,l,l の0,1,2,3のlの要素が取り出される

