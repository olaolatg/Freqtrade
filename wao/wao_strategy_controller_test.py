import sys
sys.path.append("wao/")
from wao_strategy_controller import WAOStrategyController
import time
import datetime
brain = 'Freq_bb_15m'
dup = 0.1
mode = "test"
coin = "ETH"
sell_reason = 'sell_signal'
current_time = str(datetime.datetime.now()).replace('.', '+')
time_out_hours = 7

controller = WAOStrategyController(brain, time_out_hours, dup)


controller.on_buy_signal(current_time,  coin)
#
time.sleep(10)
#
# current_time = str(datetime.datetime.now()).replace('.', '+')
#
controller.on_sell_signal(sell_reason, current_time, coin)
