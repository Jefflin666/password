password='a123456'
x=3
while x>0:
	x=x-1
	pwd=input('請輸入密碼')
	if pwd==password:
		print('輸入成功')
		break
	else:
		print('輸入失敗')
		if x>0:
			print('輸入失敗還有',x,'次機會')
		else:
			print('帳號被鎖住了!')