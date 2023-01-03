import datetime
from squad.accommodations import *

def verify_soldier(operator, sd_value, crit_limit):
    if operator == 0:
        verification = str(sd_value) == crit_limit
        return verification

    elif operator <= 1:
        verification = float(sd_value) <= crit_limit
        return verification

    elif operator == 7:
        return "SKIP"

def enlist_soldier(env, new_soldier):
    if env == 'ED1':
        ed1_soldiers.append(new_soldier)   
    if env == 'EQ1':
        eq1_soldiers.append(new_soldier)   
    if env == 'EP1':
        ep1_soldiers.append(new_soldier)   
    if env == 'GRB':
        grb_soldiers.append(new_soldier)   
    if env == 'GRC':
        grc_soldiers.append(new_soldier)   
    if env == 'SLM':
        slm_soldiers.append(new_soldier)
    return  

def enlist_prisoner(env, npun, credentials):
    if env == 'ED1':
        ed1_prisoners[npun] = credentials
        return ed1_prisoners[npun]
    if env == 'EQ1':
        eq1_prisoners[npun] = credentials
        return eq1_prisoners[npun]
    if env == 'EP1':
        ep1_prisoners[npun] = credentials
        return ep1_prisoners[npun]
    if env == 'GRB':
        grb_prisoners[npun] = credentials
        return grb_prisoners[npun]
    if env == 'GRC':
        grc_prisoners[npun] = credentials
        return grc_prisoners[npun]
    if env == 'SLM':
        slm_prisoners[npun] = credentials
        return slm_prisoners[npun]

def check_prisoners(env):
    with open(f'{env}/PRISON/dumbsoldiers.log', 'r') as log:
        log = log.readlines() # Leia linha por linha
        log = [x.strip('\n') for x in log] # Retire o "\n" do final de cada linha
        _log = [x.split(',') for x in log] # Separe o dicionário separado por vírgulas

        if len(log) > 0: # Se tiver linhas no log:
            for line in range(len(log)): # Para cada linha no arquivo .log:
                npun = int(_log[line][0][11:]) # Obtenha o número desse preso
                credentials = eval(log[line]) # E as credenciais dele
                enlist_prisoner(env, npun, credentials) # Passe o quartel, o numero e as credenciais para o SGT enlista
    return 

def check_quarter(env):
    if env == 'ED1':
        return ed1_soldiers   
    if env == 'EQ1':
        return eq1_soldiers   
    if env == 'EP1':
        return ep1_soldiers   
    if env == 'GRB':
        return grb_soldiers   
    if env == 'GRC':
        return grc_soldiers   
    if env == 'SLM':
        return slm_soldiers
    return  

def check_prison(env):
    if env == 'ED1':
        return ed1_prisoners   
    if env == 'EQ1':
        return eq1_prisoners   
    if env == 'EP1':
        return ep1_prisoners   
    if env == 'GRB':
        return grb_prisoners   
    if env == 'GRC':
        return grc_prisoners   
    if env == 'SLM':
        return slm_prisoners
    return  