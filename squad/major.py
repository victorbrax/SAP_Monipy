from squad.sergeant import *
from squad.soldiers import *

def punish_soldier(env, SD_Num, SD_Nm, SD_env, SD_hr, SD_val):
    with open(f'{env}/PRISON/dumbsoldiers.log', 'a') as log:
        sd_forms = {'Numero': SD_Num, 'Nome': SD_Nm, 'Alojamento': SD_env, 'Horario': SD_hr, 'Valor': SD_val}
        log.write(str(sd_forms)+"\n")
    return

def judge_soldiers(env):
    quarter = check_quarter(env)
    for sd in quarter:
        limit = maxdb_criterias[sd.numero]['Limit']  
        p = maxdb_criterias[sd.numero]['Priority']  
        op = maxdb_criterias[sd.numero]['Operator']  

        verification = verify_soldier(op, sd.valor, limit)

        if verification == False:
            
            prisoners = check_prison(env)
            if sd.numero in prisoners.keys():
                sd_delta = sd.horario - prisoners[sd.numero]["Horario"]
                if sd_delta.total_seconds() >= 43200:
                    print(f'{env}: Novo soldado punido por mais de 12h!')
                    print(f'Soldado {sd.numero}, {sd.nome} | Valor: {sd.valor}')
                    punish_soldier(env, sd.numero, sd.nome, sd.alojamento, datetime.datetime.now(), sd.valor)
                    print()
            else:
                punish_soldier(env, sd.numero, sd.nome, sd.alojamento, datetime.datetime.now(), sd.valor)
                print(f'{env}: Novo soldado punido, email enviado!')
                print(f'Soldado {sd.numero}, {sd.nome} | Valor: {sd.valor}')
                print()
    return