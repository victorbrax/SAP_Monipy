from squad.sergeant import *
from squad.soldiers import *

def punish_soldier(env, SD_Num, SD_Nm, SD_env, SD_hr, SD_val):
    with open(f'barracks/{env}/PRISON/dumbsoldiers.log', 'a') as log:
        sd_forms = {'Number': SD_Num, 'Name': SD_Nm, 'Barracks': SD_env, 'Hour': SD_hr, 'Value': SD_val}
        log.write(str(sd_forms)+"\n")
    return

def judge_soldiers(env):
    barrack = what_barracks(env)
    
    for sd in barrack:
        opt = maxdb_criterias[sd.number]['Operator']  
        lmt = maxdb_criterias[sd.number]['Limit']  
        prt = maxdb_criterias[sd.number]['Priority']  

        verification = verify_soldier(opt, sd.value, lmt)

        if verification == False:
            prisoners = what_prison(env)

            if sd.number in prisoners.keys():
                sd_delta = sd.hour - prisoners[sd.number]["Hour"]

                if sd_delta.total_seconds() >= 43200:
                    print(f'{env}: Novo soldado punido por mais de 12h!')
                    print(f'Soldado {sd.number}, {sd.name} | Valor: {sd.value}')
                    punish_soldier(env, sd.number, sd.name, sd.barracks, datetime.datetime.now(), sd.value)
            else:
                punish_soldier(env, sd.number, sd.name, sd.barracks, datetime.datetime.now(), sd.value)
                print(f'{env}: Novo soldado punido, email enviado!')
                print(f'Soldado {sd.number}, {sd.name} | Valor: {sd.value}')
    return