import datetime
import math


def Menu():
	print("    \033[1;33m")  # 黄色
	print("                                                    nn  ")
	print("                        ┏━━━━━━━━━━━━━━━━┓      ＿ノ<  つ  ")
	print("                        ┃                ┗━  （･･      )")
	print("                        ┃    Dandelion   ┏━    てノ＼(＼")
	print("                        ┃                ┃          ＼(＼")
	print("                        ┗━━━━━━━━━━━━━━━━┛          ﾉ ~(＼")
	print("                                                 (ﾟДﾟ) (~ \\")
	print("                                                 (|  Ｕ  ~ | ")
	print("                                                    \\＿＿_ノ--● ")
	print("                                                      ∪  ∪      ")
	print("    \033[1;34m" + "\n")
	print("            ┏━━━━━━━━━┓ ┏━━┓  ┏━━┓      ┏━━┓     ┏━━┓  ┏━━━━━━┓  ┏━━━━━━┓    ")
	print("            ┃ ┏━┓ ┏━┓ ┃ ┃  ┗━━┛  ┃      ┃  ┃     ┃  ┃  ┃  ┏━━━┛  ┃  ┏━━━┛    ")
	print("            ┃ ┃ ┃ ┃ ┃ ┃ ┗━━┓  ┏━━┛      ┃  ┃     ┃  ┃  ┃  ┗━━━┓  ┃  ┗━━━┓    ")
	print("            ┃ ┃ ┃ ┃ ┃ ┃    ┃  ┃         ┃  ┗━━━┓ ┃  ┃  ┃  ┏━━━┛  ┃  ┗━━━┓    ")
	print("            ┗━┛ ┗━┛ ┗━┛    ┗━━┛         ┗━━━━━━┛ ┗━━┛  ┗━━┛      ┗━━━━━━┛    ")
	print("    \033[0m")
	print("                                       测试版 v1.1.0    2020 1 29  Copyright", end='\n\n')
	print("                                当前时间：", str(datetime.datetime.now()).split(' ')[0], end='\n\n\n')


class ProcessBar(object):
	"""一个打印进度条的类"""
	def __init__(self, total):  # 初始化传入总数
		self.shape = ['▏', '▎', '▍', '▋', '▊', '▉']
		self.shape_num = len(self.shape)
		self.row_num = 30
		self.now = 0
		self.total = total
	
	def print_next(self, now=-1):  # 默认+1
		if now == -1:
			self.now += 1
		else:
			self.now = now
		
		rate = math.ceil((self.now / self.total) * (self.row_num * self.shape_num))
		head = rate // self.shape_num
		tail = rate % self.shape_num
		info = self.shape[-1] * head
		if tail != 0:
			info += self.shape[tail - 1]
		full_info = '[%s%s] [%.2f%%]' % (info, (self.row_num - len(info)) * '', 100 * self.now / self.total)
		
		print("\r", end='', flush=True)
		print(full_info, end='', flush=True)
		
		if self.now == self.total:
			print('')


def process(num):
	pb = ProcessBar(num * 10000)
	for i in range(num * 10000):
		pb.print_next()
