# リスト変換
number_tuple = (10,20,30)

# タプルをリスト名に変換
number_list= list(number_tuple)

#　０番目と１〜２番目を表示
print(number_list[0])
print(number_list[1:3])

#　１番目を21に置き換え
number_list[1] = 21
print(len(number_list))

#　３番目に40を追加
number_list.append(40)
print(number_list[3])

#　全リスト表示
print(number_list)