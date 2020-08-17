#V3更新日志
#8.10：确定V3更新需求，分解需求，构思代码结构（0.5h）
#8.11：增加「第二关升级玩法」，编写情节文本，增加第一关至第二关过渡代码（1.5h）
#8.12：进一步完善第二关后续玩法代码，丰富「背包物品及功能」，并测试上述代码（4.5h）
#8.13：「游戏数值」测试及更新，更新「药品效果」代码，增加「游戏进度csv记录」功能，并测试上述代码（3h）
#8.14：测试代码（0.5h）


import time, progressbar, random, csv
import numpy as np

file = open('Record.csv','w',newline='',encoding='utf-8-sig')
writer = csv.writer(file)

def level01_basic_attribute():
	global potato, player, piggy, player_init
	potato = {
		'Name': 'Potato',
		'HP': 1000, # 体力值
		'MP': 320, # 魔力值
		'AD_total': 0, # 物理输出总值
		'AP_total': 0, # 法术输出总值
		'MC': 80, # 单次法术消耗魔力值
	}
	player = {
		'Name': player_name,
		'HP': 850,
		'MP': 300,
		'AD_total': 0,
		'AP_total': 0,
		'MC': 100,
	}
	player_init = {
		'HP': 850,
		'MP': 300,
	}
	piggy = {}


def level01_variable_attribute():
	potato['AD'] = random.randint(55, 80) # 单次物理输出值
	potato['DEF_rate'] = random.uniform(0.75, 0.95) # 防御率 （等于1-物理攻击吸收率）
	potato['AP'] = random.randint(70, 130) # 单次法术输出值
	potato['SPD'] = random.randint(20, 30) # 速度值

	player['AD'] = random.randint(60, 100)
	player['DEF_rate'] = random.uniform(0.7, 0.9)
	player['AP'] = random.randint(80, 150)
	player['SPD'] = random.randint(20, 30)


def level02_basic_attribute():
	global player, piggy, player_init
	# Improved 40%
	player = {
		'Name': player_name,
		'HP': 1190,
		'MP': 420,
		'AD_total': 0,
		'AP_total': 0,
		'MC': 100,
	}
	player_init = {
		'HP': 1190,
		'MP': 420,
	}
	piggy = {
		'Name': 'Piggy',
		'HP': 1500,  # 体力值
		'MP': 480,  # 魔力值
		'AD_total': 0,  # 物理输出总值
		'AP_total': 0,  # 法术输出总值
		'MC': 80,  # 单次法术消耗魔力值
	}


def level02_variable_attribute():
	piggy['AD'] = random.randint(70, 100) # 单次物理输出值
	piggy['DEF_rate'] = random.uniform(0.6, 0.8) # 防御率 （等于1-物理攻击吸收率）
	piggy['AP'] = random.randint(80, 150) # 单次法术输出值
	piggy['SPD'] = random.randint(18, 30) # 速度值

	# Improved 20%
	player['AD'] = random.randint(72, 120)
	player['DEF_rate'] = random.uniform(0.64, 0.88)
	player['AP'] = random.randint(96, 180)
	player['SPD'] = random.randint(24, 36)


class Drug:
	def __init__(self, name, effect, recover, state=0):
		self.name = name
		self.effect = effect
		self.recover = recover
		self.state = state
	def __str__(self):
		return '药品名称：%s\n药品功效：%s' % (self.name, self.effect)


class DrugManager:
	drugs = []
	def __init__(self):
		drug1 = Drug('血还丹','在战斗过程中恢复大量气血', 250)
		drug2 = Drug('聚元丹','在战斗过程中恢复少量气血', 100)
		drug3 = Drug('聚灵丹','在战斗过程中恢复少量魔法', 100)
		drug4 = Drug('乾坤丹','在战斗过程中恢复大量魔法', 200)
		drug5 = Drug('凝神丹','减少单次法术攻击所需魔法', 75)
		drug6 = Drug('毒蒺藜','对敌人造成大量的气血伤害', 200)
		self.drugs.append(drug1)
		self.drugs.append(drug2)
		self.drugs.append(drug3)
		self.drugs.append(drug4)
		self.drugs.append(drug5)
		self.drugs.append(drug6)

	def backpack_fillup(self):
		random.shuffle(self.drugs)
		while True:
			self.drug_choice = input('\n请随机抽取你的补给药品💊\n请输入数字1至数字6内的任意数字，其他输入无效：')
			if self.drug_choice in ['1', '2', '3', '4', '5', '6']:
				self.drug_choice = int(self.drug_choice) - 1
				print('🎉恭喜你抽到补给药品：')
				print(self.drugs[self.drug_choice])
				return self.drugs[self.drug_choice]
				break
			else:
				print('请玩家重新输入正确的数字进行物品抽取。')


def init(system):
	global drug, drug_for_L2
	drug_for_L2 = []
	print('%s初始血量❤️：%d，初始魔法💙：%d' % (system['Name'], system['HP'], system['MP']))
	print('%s初始血量❤️：%d，初始魔法💙：%d' % (player['Name'], player['HP'], player['MP']))
	time.sleep(0.5)
	bonus = DrugManager()
	if system == potato:
		drug = bonus.backpack_fillup()
	elif system == piggy:
		print('\n【背包🎒第一格药品补给】')
		drug_for_L2.append(bonus.backpack_fillup())
		print('\n【背包🎒第二格药品补给】')
		drug_for_L2.append(bonus.backpack_fillup())
	time.sleep(1)
	print('\n\n⏳PK即将开始:\n')
	p = progressbar.ProgressBar()
	N = 100
	for i in p(range(N)):
		time.sleep(0.02)


def level01_init():
	global player_name
	print('欢迎来到小游戏「Running Potato」')
	time.sleep(1)
	player_name = input('请输入玩家名称：')
	level01_basic_attribute()
	init(potato)


def level02_init():
	time.sleep(2)
	print('欢迎来到小游戏第二关「Angry Piggy」')
	time.sleep(1)
	level02_basic_attribute()
	init(piggy)


def get_player_choice():
	while True:
		player_choice = input('请玩家进行战斗选择：\n1. 物理攻击\n2. 法术攻击\n3. 防御\n4. 背包\n5. 逃跑\n请输入有效的数字指令，其他输入无效：')
		if player_choice in ['1', '2', '3', '4', '5']:
			player_choice = int(player_choice)
			return player_choice
			break
		else:
			print('请玩家重新输入正确的数字指令进行操作。')


def get_system_choice(system):
	if system['MP'] >= system['MC']:
		system_choice = np.random.choice([1, 2, 3], 1, replace=True, p=[0.65, 0.3, 0.05])
	else:
		system_choice = np.random.choice([1, 3], 1, replace=True, p=[0.8, 0.2])
	return system_choice


def physical_attack(attacker, receiver, mode=0):
	if mode == 0: # 正常物理攻击模式
		receiver['HP'] -= attacker['AD']
		narratage = '%s向%s发起了物理攻击⚔️(AD：%d)，%s剩余血量❤️：%d' % (attacker['Name'], receiver['Name'], attacker['AD'], receiver['Name'], receiver['HP'])
		print(narratage)
		writer.writerow([narratage])
		attacker['AD_total'] += attacker['AD']

	elif mode == 1: # 对方处于防御状态下物理攻击模式
		attacker['AD'] = int(attacker['AD'] * receiver['DEF_rate'])
		receiver['HP'] -= attacker['AD']
		narratage = '%s向%s发起了物理攻击⚔️(AD：%d)，%s剩余血量❤️：%d' % (
		attacker['Name'], receiver['Name'], attacker['AD'], receiver['Name'], receiver['HP'])
		print(narratage)
		writer.writerow([narratage])
		attacker['AD_total'] += attacker['AD']


def magical_attack(attacker, receiver):
	receiver['HP'] -= attacker['AP']
	attacker['MP'] -= attacker['MC']
	narratage = '%s向%s发起了法术攻击🔥(AP：%d)，%s剩余血量❤️：%d' % (attacker['Name'], receiver['Name'], attacker['AP'], receiver['Name'], receiver['HP'])
	print(narratage)
	writer.writerow([narratage])
	print('%s消耗魔法值%d，剩余魔法值💙：%d' % (attacker['Name'], attacker['MC'], attacker['MP']))
	attacker['AP_total'] += attacker['AP']


def escape(system):
	global upgrade
	upgrade = 'N'
	narratage = '\n%s，我先走一步💨，下次有机会再切磋切磋！👊🏻' % system['Name']
	print(narratage)
	writer.writerow([narratage])
	print('%s少侠别跑呀！😂' % player['Name'])


def backpack(supply):
	while True:
		answer = input('确定要使用%s💊？\n1.确定\n2.我再想想\n请输入有效的数字指令，其他输入无效：' % supply.name)
		if answer in ['1', '2']:
			answer = int(answer)
			return answer
			break
		else:
			print('请玩家重新输入正确的数字指令进行操作。')


def drug_effect(supply, system):
	if (supply.name == '血还丹') or (supply.name == '聚元丹'):
		if player['HP'] <= (player_init['HP'] - supply.recover):
			player['HP'] += supply.recover
		else:
			player['HP'] = player_init['HP']
		print('%s成功使用%s💊，恢复%d气血，%s剩余血量❤️：%d' % (player['Name'], supply.name, supply.recover, player['Name'], player['HP']))
	elif (supply.name == '乾坤丹') or (supply.name == '聚灵丹'):
		if player['MP'] <= (player_init['MP'] - supply.recover):
			player['MP'] += supply.recover
		else:
			player['MP'] = player_init['MP']
		print('%s成功使用%s💊，恢复%d魔法，%s剩余魔法值💙：%d' % (player['Name'], supply.name, supply.recover, player['Name'], player['MP']))
	elif supply.name == '凝神丹':
		player['MC'] = supply.recover
		print('%s成功使用%s💊，单次法术攻击消耗魔法变为%d。' % (player['Name'], supply.name, supply.recover))
	elif supply.name == '毒蒺藜':
		system['HP'] -= supply.recover
		print('%s成功使用%s💊，对%s造成%d点气血伤害，%s剩余血量❤️：%d' % (player['Name'], supply.name, system['Name'], supply.recover, system['Name'], system['HP']))
	supply.state = 1


def attribute_in_battle(system):
	if system == potato:
		level01_variable_attribute()
	elif system == piggy:
		level02_variable_attribute()


def battle(system):
	global round
	round = 1
	while (system['HP'] > 0) and (player['HP'] > 0):
		attribute_in_battle(system)
		narratage = '\n👉「第' + str(round) + '回合」👈'
		print(narratage)
		writer.writerow([narratage])
		system_choice = get_system_choice(system)
		player_choice = get_player_choice()
		loop = 1
		while loop:
			if (player_choice == 2) and (player['MP'] < player['MC']):
				print('玩家魔法值不足，本回合无法使用法术攻击，请重新选择数字指令。')
				player_choice = get_player_choice()
			elif (player_choice == 4):
				if system == potato:
					if drug.state == 0:
						drug_choice = backpack(drug)
						if drug_choice == 1:
							drug_effect(drug, potato)
							loop = 0
							if system_choice == 1:
								physical_attack(system, player)
							elif system_choice == 2:
								magical_attack(system, player)
							elif system_choice == 3:
								print('%s本回合进行防御🛡️' % system['Name'])
						else:
							player_choice = get_player_choice()
					elif drug.state == 1:
						print('你的背包里空无一物！')
						player_choice = get_player_choice()

				if system == piggy:
					if len(drug_for_L2) == 0:
						print('你的背包里空无一物！')
						player_choice = get_player_choice()
					elif len(drug_for_L2) == 2:
						while True:
							n = input('请选择本回合要使用的药品：1.%s，2.%s，请输入数字指令，其他输入无效：' % (drug_for_L2[0].name, drug_for_L2[1].name))
							if n in ['1','2']:
								n = int(n)-1
								break
							else:
								print('请玩家重新输入正确的数字指令进行操作。')
						drug_choice = backpack(drug_for_L2[n])
						if drug_choice == 1:
							drug_effect(drug_for_L2[n], piggy)
							del drug_for_L2[n]
							loop = 0
							if system_choice == 1:
								physical_attack(system, player)
							elif system_choice == 2:
								magical_attack(system, player)
							elif system_choice == 3:
								print('%s本回合进行防御🛡️' % system['Name'])
						else:
							player_choice = get_player_choice()
					elif len(drug_for_L2) == 1:
						drug_choice = backpack(drug_for_L2[0])
						if drug_choice == 1:
							drug_effect(drug_for_L2[0], piggy)
							del drug_for_L2[0]
							loop = 0
							if system_choice == 1:
								physical_attack(system, player)
							elif system_choice == 2:
								magical_attack(system, player)
							elif system_choice == 3:
								print('%s本回合进行防御🛡️' % system['Name'])
						else:
							player_choice = get_player_choice()
			else:
				loop = 0

		if player_choice == 5:
			escape(system)
			round += 1
			break

		elif player_choice == 3:
			if system_choice == 1:
				print('%s本回合进行防御🛡️' % player['Name'])
				physical_attack(system, player, mode=1)
			if system_choice == 2:
				print('%s本回合进行防御🛡️' % player['Name'])
				magical_attack(system, player)
			if system_choice == 3:
				print('双方都进行防御🛡️，此回合无人伤亡。')

		elif player_choice == 2:
			if system_choice == 1:
				if player['SPD'] >= system['SPD']:
					print('%s率先出手🌪'% player['Name'])
					magical_attack(player, system)
					if system['HP'] > 0:
						physical_attack(system, player)
					else:
						round += 1
						break
				else:
					print('%s率先出手🌪' % system['Name'])
					physical_attack(system, player)
					if player['HP'] > 0:
						magical_attack(player, system)
					else:
						round += 1
						break
			elif system_choice == 2:
				if player['SPD'] >= system['SPD']:
					print('%s率先出手🌪' % player['Name'])
					magical_attack(player, system)
					if system['HP'] > 0:
						magical_attack(system, player)
					else:
						round += 1
						break
				else:
					print('%s率先出手🌪' % system['Name'])
					magical_attack(system, player)
					if player['HP'] > 0:
						magical_attack(player, system)
					else:
						round += 1
						break
			elif system_choice == 3:
				print('%s本回合进行防御🛡️' % system['Name'])
				magical_attack(player, system)

		elif player_choice == 1:
			if system_choice == 1:
				if player['SPD'] >= system['SPD']:
					print('%s率先出手🌪' % player['Name'])
					physical_attack(player, system)
					if system['HP'] > 0:
						physical_attack(system, player)
					else:
						round += 1
						break
				else:
					print('%s率先出手🌪' % system['Name'])
					physical_attack(system, player)
					if player['HP'] > 0:
						physical_attack(player, system)
					else:
						round += 1
						break
			elif system_choice == 2:
				if player['SPD'] >= system['SPD']:
					print('%s率先出手🌪' % player['Name'])
					physical_attack(player, system)
					if system['HP'] > 0:
						magical_attack(system, player)
					else:
						round += 1
						break
				else:
					print('%s率先出手🌪' % system['Name'])
					magical_attack(system, player)
					if player['HP'] > 0:
						physical_attack(player, system)
					else:
						round += 1
						break
			elif system_choice == 3:
				print('%s本回合进行防御🛡️' % system['Name'])
				physical_attack(player, system, mode=1)

		round += 1
		time.sleep(1)


def battle_record(winner, loser):
	print('【%s胜🏆】\n%s倒地，心悦诚服地道：%s你赢了，在下技不如人，甘拜下风！👍🏻' % (winner['Name'], loser['Name'], winner['Name']))
	n0 = '【%s胜🏆】' % winner['Name']
	writer.writerow([n0])
	n1 = '【战绩回顾📜】\n' + '本轮PK一共进行' + str(round-1) + '个回合。'
	n2 = '%s的物理攻击⚔️总数值为：%d，法术攻击🔥总数值为：%d' % (winner['Name'], winner['AD_total'], winner['AP_total'])
	n3 = '%s的物理攻击⚔️总数值为：%d，法术攻击🔥总数值为：%d' % (loser['Name'], loser['AD_total'], loser['AP_total'])
	print(n1)
	writer.writerow([n1])
	print(n2)
	writer.writerow([n2])
	print(n3)
	writer.writerow([n3])


def potato_end():
	global upgrade
	print('\n\n-------------------------游戏结束！--------------------------')
	if (player['HP'] > 0) and (potato['HP'] <= 0):
		battle_record(player, potato)
		print('\n🎉🎉🎉恭喜玩家升级⬆，基础属性获得40%加成，附加属性获得20%加成，背包扩容为两格。🎉🎉🎉')
		time.sleep(3.5)
		print('\n话说Potato惨败后，心有不忿，奈何技不如人却又无从抱怨，于是整日闷在苗圃中不肯出门。\
        \n小师妹Piggy看着日渐消瘦的Potato内心十分担忧，但其又深知Potato不服输的个性。\
		\n为了让Potato可以重振旗鼓，Piggy做出了一个大胆地决定，她给%s下了一封战书，打算独自前去为师兄报仇。' % player['Name'])
		time.sleep(1)
		while True:
			upgrade = input('\n请问玩家是否接受Piggy的挑战？Y代表接受，N代表婉拒，其他输入无效：')
			if upgrade in ['Y', 'N']:
				if upgrade == 'Y':
					print('料想你们淀粉派都是一群乌合之众，不足为惧，尽管放马过来吧！\n\n')
					break
				else:
					print('听闻淀粉派人才济济，在下素来佩服。只是Piggy师妹一路上风尘仆仆，在下胜之不武，何不休养几日，双方再战？')
					break
			else:
				print('请玩家重新输入正确的指令代码进行选择。')

	elif (player['HP'] <= 0) and (potato['HP'] > 0):
		battle_record(potato, player)
		upgrade = 'N'
		file.close()


def piggy_end():
	print('\n\n-------------------------第二关游戏结束！--------------------------')
	if (player['HP'] > 0) and (piggy['HP'] <= 0):
		battle_record(player, piggy)
		time.sleep(2)
		print('\nPiggy想着虽然输了决斗，未能帮Potato报仇，但不能有损淀粉派的名声，于是仍抱拳与%s端端正正地行了一个礼。\
		\n之后，便头也不回地朝着点粉派苗圃的方向走去。\
		\n\"也不知道淀粉派还会不会再遣人来？\"%s心想。' % (player['Name'], player['Name']))
		print('\n---------完----------')
	elif (player['HP'] <= 0) and (piggy['HP'] > 0):
		battle_record(piggy, player)
		time.sleep(2)
		print('\nPiggy获胜后内心并没有太多波澜，只是想着尽早赶回淀粉派，将这一好消息告诉师兄Potato，好让其尽快恢复。\
		\n对着%s抱拳说了句\"承让\"后，便头也不回地朝着点粉派苗圃的方向走去。' % player['Name'])
		print('\n---------完----------')


def level01_main():
	writer.writerow(['「Running Potato」'])
	level01_init()
	battle(potato)
	potato_end()

def level02_main():
	if upgrade == 'Y':
		writer.writerow([''])
		writer.writerow(['「Angry Piggy」'])
		level02_init()
		battle(piggy)
		piggy_end()
		file.close()
	else:
		file.close()

level01_main()
level02_main()
