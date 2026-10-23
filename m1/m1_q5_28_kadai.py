days = ['月', '月', '火', '水', '木', '金', '金']

days.remove('月') # 最初の'月'を削除
days.remove('金') # 最初の'金'を削除

days.insert(0,  '日') # インデックス0に'日'を追加 
days.insert(6, '土') # インデックス6に'土'を追加 

print(days) # 削除・追加後のdaysを出力