import datetime
import Tools.chatRobot as tc
import Tools.components as tp


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
	print("\n    \033[5;33m           " + H + "这里是城市公园，于2020年1月交付使用")
	
	
def getStatus():
	print("\n    \033[5;31m           1 聊天机器人       2 景区观赏       3 帮助          0 离开\033[0m\n")
	while True:
		status = input(" >> ")
		if status in ['0', '1', '2', '3']:
			break
	return int(status)

	
def ChatRobot():
	print("正在查找...")
	print("正在定位小乔的位置，稍等...")
	print("连接成功...")
	print("呼叫中...")
	tp.process(10)
	print("完成")
	print("正在准备聊天环境...")
	print("正在调整参数")
	print("你好，机器人小乔为您服务！(输入'exit'退出)")
	tc.run("小乔")


