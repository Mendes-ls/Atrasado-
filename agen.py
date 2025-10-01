import schedule
import time as tm
from datetime import time
from schedule import repeat, every

@repeat(every(10).seconds)
def tarefa():
    print("Executando tarefa agendada...")

#schedule.every(10).seconds.do(tarefa)
#schedule.every().day.at("15:42").do(tarefa)
#schedule.every().second.until(time(15,53,10)).do(tarefa)
while True:
    schedule.run_pending()
    tm.sleep(1)