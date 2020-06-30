import Places.MapExchange as pm


def Table():
	print("\033[5;31m")
	print("               ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
	print("                   1  地图          2  帮助        3  存档          0  退出")
	print("               ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
	print("\033[0m")
	while True:
		Cmd = input("指令方式：0～3 >> ")
		if Cmd in ['1', '2', '3', '0']:
			break
	return int(Cmd)


def Help_Switch():
	print("【帮助界面】")
	ex = input(" >> ")
	while True:
		if ex == '0':
			break
	return int(ex)


def Exit_Switch():
	exit(0)
	return False


def Creat_player_Switch():
	pass


"""  =========  Main  Function =========  """


def Scheduling_(Play, Cmd):
	"""
	:param Play: 玩家
	:param Cmd:  0, 1, 2, 3
	:return:
	"""
	if Cmd == 0:
		Exit_Switch()
	elif Cmd == 1:
		where = pm.Find_where()
		pm.Map_Switch(Play, where)
	elif Cmd == 2:
		Help_Switch()
	elif Cmd == 3:
		print("已保存...")


#
# while True:
# 	Function_ = Navigator_Switch()
# 	Position_(Function_)
