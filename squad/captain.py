from squad.accommodations import *
from squad.sergeant import *
import os

def gen_commands(envs, tmplt):
    for barracks in envs:
        for idx, template in enumerate(tmplt):
            if barracks == 'ED1':
                cED1.append(f'./../src/check_sap_cons ed1_{template} SLM > barracks/{barracks}/SD_DOCS/{barracks}-documents-{idx+1}.txt')
            elif barracks == 'EQ1':
                cEQ1.append(f'./../src/check_sap_cons eq1_{template} SLM > barracks/{barracks}/SD_DOCS/{barracks}-documents-{idx+1}.txt')
            elif barracks == 'EP1':
                cEP1.append(f'./../src/check_sap_cons ep1_{template} SLM > barracks/{barracks}/SD_DOCS/{barracks}-documents-{idx+1}.txt')
            elif barracks == 'GRB':
                cGRB.append(f'./../src/check_sap_cons grb_{template} SLM > barracks/{barracks}/SD_DOCS/{barracks}-documents-{idx+1}.txt')
            elif barracks == 'GRC':
                cGRC.append(f'./../src/check_sap_cons grc_{template} SLM > barracks/{barracks}/SD_DOCS/{barracks}-documents-{idx+1}.txt')
            elif barracks == 'SLM':
                cSLM.append(f'./../src/check_sap_cons slm_{template} SLM > barracks/{barracks}/SD_DOCS/{barracks}-documents-{idx+1}.txt')
    return

def run_commands(envs):
    for barracks in envs:
        c_list = what_command(barracks)
        for command in c_list:
            os.system(command)
    return