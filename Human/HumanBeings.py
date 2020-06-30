import datetime


class HumanBeing:
	class Money:
		Lst = [
			['微信余额', 100.0, 1],
			['支付宝', 100.0, 2],
			['代金券', 0.0, 4],
			['银行卡', 0.0, '603 1125 0348 2520 132', '000000'],
			['工资卡', 1000.0, '603 1125 0347 3315 110', '000000'],
		]
		
		def Query_balance(self):
			for i in self.Lst:
				print("\t\t {:<5}\t\t{:^3} 元".format(i[0], i[1]))
		
		def use_balance(self, i):
			"""
			:param i:  0-w  1-a  2-b  3-r
			:return:  返回一个对应账户的余额
			"""
			return self.Lst[i][1]
		
		def Charge(self, insert):
			self.Lst[0][1] += insert
	
	name = ""
	sex = "女"
	age = 0
	birthday = ""
	height = 0
	weight = 0
	vision = 5.2
	
	ability = []
	money = 0
	ID_card = []
	degree = "未教育"
	
	isHealth = True
	isHappy = True
	isFlu = False
	isInfected = False
	
	isWalk = False
	isRun = False
	isDrink = False
	isEat = False
	
	canLactation = True  # 哺乳
	canFertility = True  # 生育
	
	M = Money()
	
	def __init__(self, Name="-", ID="630121", Height=172, Weight=56):
		self.name = Name
		self.ID_card.append(ID)
		self.height = Height
		self.weight = Weight
		self.birthday = str(datetime.datetime.now()).split(' ')[0]
	
	def Query_Self(self):
		print("{:>8}\t\t\t{:<5}".format("姓名", self.name))
		print("{:>8}\t\t\t{:<5}".format("性别", self.sex))
		print("{:>8}\t\t\t{:<5}".format("学位", self.degree))
		print("{:>8}\t\t\t{:<}".format("生日", self.birthday))
	
	def Query_Health(self):
		BMI = float(self.weight) / (float(self.height) / 100) ** 2
		print("{:>8}\t\t\t{:<4}（标准对数视力）".format("视力", self.vision))
		print("{:>8}\t\t\t{:<4}cm".format("身高", self.height))
		print("{:>8}\t\t\t{:<3}kg".format("体重", self.weight))
		print("{:>8}\t\t\t{:<.5}（18.5～24.9正常）".format("BMI指数", BMI))
	
	def Query_Balance(self):
		self.M.Query_balance()
	
	def Query_BankCards(self):
		print("识别完成.")
		print("已确认.")
		Temp = []
		print("\t\t注：")
		print("\t\t\t银行卡：用于取款，自动转入首选零用消费方式（暂只支持微信）")
		print("\t\t\t工资卡：用于存款，此卡仅存入工作收益、奖金等\n")
		for i in self.M.Lst:
			if len(i) == 4:
				print("\t\t账户类型：" + i[0] + "  账号：" + i[2] + "  余额：" + str(i[1]))
	
	
	def checkHealth(self):
		print("\t\t身体状况检测表：")
		print("\t\t\t脑神经系统：", "正常" if self.isHappy else "需检查")
		print("\t\t\t腰部运动系统：", "正常" if self.isWalk else "需检查")
		print("\t\t\t腿部关节及肌肉状态：", "正常" if self.isRun else "需检查")
		print("\t\t\t消化系统功能：", "正常" if self.isDrink else "需检查")
		print("\t\t\t骨骼及脊椎", "正常" if self.isEat else "需检查")
	
	
	
	def Deposit_Bank(self):
		while True:
			amount = input("\t\t存入额 >> ")
			try:
				if self.M.Lst[4][1] >= float(amount):
					break
			except:
				continue
		
		while True:
			ans = input("\t\t确认吗？（y/n）")
			if ans in ['y', 'n']:
				break
		if ans == 'y':
			self.M.Lst[3][1] += float(amount)
			self.M.Lst[4][1] -= float(amount)
			print("\t\t完成.")
			print("\t\t目前余额为：", self.M.Lst[3][1], "元")
		return
	
	def Withdrawal_Bank(self):
		while True:
			amount = input("\t\t取款额 >> ")
			try:
				if self.M.Lst[3][1] >= float(amount):
					break
			except:
				continue
		while True:
			ans = input("\t\t确认吗？（y/n）")
			if ans in ['y', 'n']:
				break
		if ans == 'y':
			self.M.Lst[3][1] -= float(amount)
			self.M.Lst[0][1] += float(amount)
			print("\t\t完成.")
			print("\t\t已存入您的零用账户.")
			print("\t\t目前余额为：", self.M.Lst[3][1], "元")
		return
	
	def consume(self, price, k):
		"""
		:param price: 需要消费多少钱
		:param k:  消费的类型
		:return:  消费状态
		"""
		print("您的消费方式为：", self.M.Lst[k - 1][0])
		print("您的原余额为：", self.M.Lst[k - 1][1])
		print("您需要支付：", price)
		if price > self.M.Lst[k - 1][1]:
			print("您的余额不足以消费，请充值！")
			return True
		else:
			bls = self.M.use_balance(k - 1)
			bls = bls - price
			self.M.Lst[k - 1][1] = bls
			print("您消费后的余额为：", self.M.Lst[k - 1][1])
			return False
