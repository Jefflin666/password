password='a123456'
x=3
while True:
	pwd=input('請輸入密碼')
	if pwd==password:
		print('輸入成功')
		break
	else:
		x=x-1
		print('輸入失敗還有',x,'機會')
		if x==0:
			break