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
	print("\n    \033[5;33m           " + H + "这里是医院门诊大楼，请问您需要什么帮助？")


def getStatus():
	print("\n    \033[5;31m           1 中医       2 西医       3 中西医结合       4 体质检查        0 离开\033[0m\n")
	while True:
		status = input(" >> ")
		if status in ['0', '1', '2', '3', '4']:
			break
	return int(status)


def in_Hospital(player):
	SAY_HELLO()
	while True:
		status = getStatus()
		if status == 1:
			print("\t\t中医学治疗基本理念：")
			print("\t\t1. 调理阴阳")
			print("\t\t2. 扶正祛邪")
			print("\t\t\t①把握虚之指征，做到辨证准确，剔除疑似，如乏力未必气虚、口渴未必阴虚、怕冷未必阳虚等。")
			print("\t\t\t②辨明虚之成分。中医学所言之正气，内容主要包括气、血、阴、阳。")
			print("\t\t\t③弄清虚之所在，即虚之脏腑定位，如肾阳虚、肾阴虚，脾气虚、肺气虚，心血虚、肝血虚等。")
			print("\t\t\t④知晓气血阴阳之间、脏腑之间关系。")
			print("\t\t\t⑤可直接补，如益气、养血、温阳、滋阴等；也可间接补，如补土生金、滋水涵木等。")
			print("\t\t3. 三因制宜")
			print("\t\t\t“三因”之中，重在“因人”，兼顾时、地。")
			print("\t\t\t辨证时应综合分析，治疗时当区别对待，由此产生了“异病同治”、“同病异治”的特色现象。")
			print("")
			print("\t\t参考自：《素问·生气通天论》、《素问·阴阳应象大论》")
		elif status == 2:
			print("\t\t西医通道暂时关闭.")
		elif status == 3:
			print("\t\t中西医结合通道暂时关闭.")
		elif status == 4:
			player.checkHealth()
		else:
			break
