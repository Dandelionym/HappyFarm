import Places.supermarket as ps
import Places.bank as pb
import Places.hospital as ph


def Map():
	SubwayStation = [0, 2, "地铁站", 'a']
	Park = [2, 1, "森林公园", 'b']
	Home = [2, 0, "家", 'c']
	Post = [1, 0, "中国邮政", 'd']
	Supermarket = [1, 2, "华联超市", 'e']
	Theatre = [0, 0, "城市大剧院", 'f']
	Furniture = [1, 1, "家具市场", 'g']
	Hospital = [2, 2, "万康医院", 'h']
	Bank = [0, 1, "建设银行", 'i']

	M = [
		[Theatre, Bank, SubwayStation],
		[Post, Furniture, Supermarket],
		[Home, Park, Hospital]
	]
	return M


def Find_where():
	print("\033[5;35m")
	print("\t\t\t\t\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
	print("\t\t\t\t\t   a   地铁\t\t\tb   森林公园\t\tc   家 ")
	print("\t\t\t\t\t   d   中国邮政\t\te   超市\t\t\tf   大剧院 ")
	print("\t\t\t\t\t   g   市场\t\t\th   医院\t\t\ti   银行 ")
	print("\t\t\t\t\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
	print("\033[0m")
	while True:
		where = input("指令方式：a～i >> ")
		if where in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
			break
	return where


def Map_Switch(player, where, a=2, b=0):
	current = where
	if current == 'a':          # 地铁
		return
	elif current == 'b':        # 森林公园
		return
	elif current == 'c':        # 家
		return
	elif current == 'd':        # 邮政
		return
	elif current == 'e':        # 超市
		ps.in_supermarket(player)
		return
	elif current == 'f':        # 大剧院
		return
	elif current == 'g':        # 市场
		return
	elif current == 'h':        # 医院
		ph.in_Hospital(player)
	elif current == 'i':        # 银行
		pb.in_Bank(player)
