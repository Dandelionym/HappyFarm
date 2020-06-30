import datetime

Menu = [
	[1, "白菜", 0.80],
	[2, "芹菜", 2.00],
	[3, "胡萝卜", 1.50],
	[4, "生菜", 8.76 / 2],
	[5, "大葱", 0.35],
	[6, "金桔", 4.00],
	[7, "苹果", 3.00],
	[8, "菜花", 1.35],
	[9, "黄瓜", 1.50],
	[10, "海带", 0.33],
	[11, "黄豆芽", 0.88],
	[12, "茄子", 2.00],
	[13, "土豆", 1.30],
	[14, "甘蓝", 0.50],
	[15, "番茄", 3.00],
	[16, "西兰花", 5.25],
	[17, "新番茄", 4.98],
	[18, "红薯", 1.68],
	[19, "娃娃菜", 7.25],
	[20, "鲜姜", 7.00],
	[21, "西葫芦", 4.98],
]
Index = [str(Menu[x][0]) for x in range(len(Menu))]
Index.append('0')


def SAY_HELLO():
	H = ""
	now = str(datetime.datetime.now())
	hours = int(now.split(" ")[1].split(":")[0])
	if hours < 11:
		H = "早上好！"
	elif 11 <= hours < 13:
		H = "中午好！"
	elif 13 <= hours < 18:
		H = "下午好！"
	elif 18 <= hours:
		H = "晚上好！"
	print("\n    \033[5;33m           " + H + "超市机器人小光为您服务！请问您需要点什么呢？")


def getStatus():
	print("\n    \033[5;31m           1 购物（新价目表）       2 查询余额        0 离开\033[0m\n")
	while True:
		status = input(" >> ")
		if status in ['0', '1', '2']:
			break
	return int(status)


def menu():
	print(" <·> 价格表：(元/斤)")
	print("\t\t" + "-" * 38)
	print("\t\t\t\t\t 今日价表")
	for i in Menu:
		print("\t\t" + "{:<3} {:<12}\t      {:<6}元/斤".format(i[0], i[1], i[2]))
	print("\t\t" + "-" * 38)


def Select():
	"""
	:return:  选择后统计了总价是多少，返回总价
	"""
	c = 1
	ack = 'y'
	sum = 0
	sum_item = 0
	switch = True
	cart = []
	item = []
	cart_sum = True
	print("\t\t" + "      如要退出请在【物品序号】输入0   ")
	while 1:
		if switch is False:
			break
		else:
			while True:
				ans = input(str(c) + " 物品序号 >> ")
				if ans in Index:
					break
			
			if 1 <= int(ans) <= len(Menu):
				c += 1
				while 1:
					try:
						num = int(input("\t\t" + "   【!】" + "您想要多少斤" + Menu[int(ans) - 1][1] + " >> "))
						break
					except:
						pass
				if num == 0:
					print("\t\t" + "    好的，您不需要" + Menu[int(ans) - 1][1] + ".")
				else:
					print("\t\t" + "     好的，" + str(num) + "斤" + Menu[int(ans) - 1][1] + "已添加到购物车.")
					item.append(Menu[int(ans) - 1][1])
					item.append(num)
					item.append(Menu[int(ans) - 1][2] * num)
					cart.append(item)
					item = []
			
			else:
				if len(cart) == 0:
					print(" - 没有你喜欢的物品吗？欢迎您下次光临哦 (^_^)")
					ack = 'n'
					switch = False
					cart_sum = False
				elif int(ans) == 0:
					print("   【!】就这些吗? (y/n)")
					while 1:
						ack = input(" >> ")
						if ack == 'y' or ack == 'n':
							break
					# print(" -v ")
					if ack == 'y':
						switch = False
					elif ack == 'n':
						switch = True
					else:
						ack = input(" >> ")
	if cart_sum is False and len(item) == 0:
		print(" - 祝您愉快！")
		return 0.0
	else:
		print("\n 好的，您一共买了这些：")
		print("\t\t"+"-" * 38)
		for i in cart:
			print("\t\t"+"    {:<6}   {:>3}斤       共 {:<5}元".format(i[0], i[1], i[2]))
			sum += i[2]
		print("\t\t"+"-" * 38)
		print(" 共计 {:^.4} 元.".format(str(sum)))
		print("\n 确认支付吗？（y/n）")
		while 1:
			ack = input(" >> ")
			if ack == 'y' or ack == 'n':
				break
		if ack == 'y':
			print("\n您好，请在这里刷卡或扫二维码支付:")
			return sum
		if ack == 'n':
			print("\n 好的，期待您下次再来！")
			return 0.0


def pay(price):
	"""
	:param price:
	:return:    返回支付方式
	"""
	if price == 0.0:
		return False
	else:
		print("请选择您的付款方式 ：1-微信  2-支付宝  3-银行卡  4-代金券")
		pay_select = 1
		while 1:
			pay_select = input("(请在1～4内选择) >> ")
			if pay_select in ['1', '2', '3', '4']:
				break
		if pay_select == '1':
			return 1
		elif pay_select == '2':
			return 2
		elif pay_select == '3':
			return 3
		elif pay_select == '4':
			return 4


def confirm():
	"""
	:return:  正确确认
	"""
	ack = ''
	while 1:
		ack = input("   【!】确认吗? (y/n)")
		if ack in ['y', 'n']:
			break
	if ack == 'y':
		return True
	elif ack == 'n':
		return False


def in_supermarket(play):
	SAY_HELLO()
	while True:
		status = getStatus()
		if status == 0:             # 退出
			print("欢迎您下次再来！")
			return
		elif status == 1:           # 购物
			menu()
			price = Select()
			key = pay(price)
			play.consume(price, key)
		elif status == 2:           # 查询余额
			play.Query_Balance()

