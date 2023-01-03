from squad.sergeant import *
from squad.soldiers import *

def check_prisoners(env):
    with open(f'barracks/{env}/PRISON/dumbsoldiers.log', 'r') as log:
        log = log.readlines()
        log = [x.strip('\n') for x in log]
        _log = [x.split(',') for x in log]

        if len(log) > 0: # If the log has filled lines
            for line in range(len(log)):
                punished_number = int(_log[line][0][11:])
                punished_docs = eval(log[line]) # Convert to dict
                add_prisoner(env, punished_number, punished_docs)
    return

def register_soldier(env):
    with open(f'barracks/{env}/SD_DOCS/{env}-documents-mxdb.txt', 'r') as file:
        file = file.readlines()
        file = [line.strip('\n') for line in file]
        file = [line.strip(' %') for line in file]
        file = [line.replace(' Days', '') for line in file]

        for idx, line in enumerate(file):
            line = line.split(' = ')
            new_soldier = Soldier(nm=line[0], num=idx, brrk=env, hr=datetime.datetime.now(), val=line[1])
            enlist_soldier(env, new_soldier)
    return

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

        verification = what_operator(opt, sd.value, lmt)

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