import datetime


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
	print("\n    \033[5;33m           " + H + "\t银行大厦感谢您的到来,请问需要什么帮助？")
	
	
def getStatus():
	print("\n    \033[5;31m           1 自助服务       2 银行动态        0 离开\033[0m\n")
	while True:
		status = input(" >> ")
		if status in ['1', '2', '0']:
			break
	return int(status)


def getStatus_SEREVER():
	print("\n    \033[5;31m           1 存款       2 取款       3 查询        0 离开\033[0m\n")
	while True:
		status = input(" >> ")
		if status in ['1', '2', '3', '0']:
			break
	return int(status)


def Deposit(player):
	player.Query_BankCards()
	player.Deposit_Bank()


def Withdrawal(player):
	player.Query_BankCards()
	player.Withdrawal_Bank()


def in_Bank(play):
	SAY_HELLO()
	while True:
		status = getStatus()
		if status == 1:
			status_s = getStatus_SEREVER()
			if status_s == 1:
				Deposit(play)
			elif status_s == 2:
				Withdrawal(play)
			elif status_s == 3:
				play.Query_Balance()
			else:
				return
		elif status == 2:
			print("\n\t\t银行暂无动态.\n")
		else:
			return


