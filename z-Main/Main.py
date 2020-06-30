import Tools.components as tc
import Tools.Schedule as ts
import Human.HumanBeings as hh
import Places.supermarket as ps


player = hh.HumanBeing()

tc.Menu()

while True:
	Cmd = ts.Table()
	ts.Scheduling_(player, Cmd)

