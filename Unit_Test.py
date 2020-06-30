def Find_Surround_loc(Map_, a, b):
	"""
	:param a:   横坐标
	:param b:   纵坐标
	:param Map_:   标准地图
	:return:                位置标号，横纵坐标，[(0,0), (0,1) ... ]
	"""
	center = Map_[a][b][0], Map_[a][b][1]  # 返回本地的横纵坐标
	if center[0] == 0:
		front = None
	else:
		front = center[0] - 1, center[1]
	if center[0] == 2:
		rear = None
	else:
		rear = center[0] + 1, center[1]
	if center[1] == 0:
		left = None
	else:
		left = center[0], center[1] - 1
	if center[1] == 2:
		right = None
	else:
		right = center[0], center[1] + 1
	loc_lst = [front, left, right, rear, center]  # list of     tuple & None   数组中的位置

	Name = []
	c = 1
	for i in loc_lst:
		if i is not None:
			Name.append(str(c) + " " + Map_[i[0]][i[1]][2])
		else:
			Name.append(" " * 8)
		c += 1

	# print("\033[5;31m" + "━" * 70)
	print("【导航仪（输入1～4选择方向）】\n\n")
	print(" " * 10 + "                    " + Name[0] + "      ", end='\n')
	print(" " * 10 + " " + Name[1] + " " * 24 + Name[2], end='\n')
	print(" " * 10 + "                    " + Name[3] + "      \n\n")
	print("【当前位置：", Name[4], "】(输入5进入)" + " " * 30 + "【0 关闭导航仪】")
	# print("━" * 70, "\033[0m")

	while True:
		ans_str = input("\033[5;32m指令 >> \033[0m")
		if ans_str in ['0', '1', '2', '3', '4', '5']:
			break
	if ans_str == '0':
		center = False
	elif ans_str == '1' and (loc_lst[0] is not None):
		center = loc_lst[0]
	elif ans_str == '2' and (loc_lst[1] is not None):
		center = loc_lst[1]
	elif ans_str == '3' and (loc_lst[2] is not None):
		center = loc_lst[2]
	elif ans_str == '4' and (loc_lst[3] is not None):
		center = loc_lst[3]
	elif ans_str == '5':
		# os.system('clear')
		return Map_[center[0]][center[1]][3]
	return center  # Find_Surround_loc(Map_, a, b)