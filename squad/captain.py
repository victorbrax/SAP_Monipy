from squad.accommodations import *

def gen_commands(env, tmplt):
    for barracks in env:
        for idx, template in enumerate(tmplt):
            if barracks == 'ED1':
                cED1.append(f'./../src/check_sap_cons {barracks}_{template} SLM > barracks/{barracks}/SD_DOCS/{barracks}_FILE{idx+1}.txt')
            elif barracks == 'EQ1':
                cEQ1.append(f'./../src/check_sap_cons {barracks}_{template} SLM > barracks/{barracks}/SD_DOCS/{barracks}_FILE{idx+1}.txt')
            elif barracks == 'EP1':
                cEP1.append(f'./../src/check_sap_cons {barracks}_{template} SLM > barracks/{barracks}/SD_DOCS/{barracks}_FILE{idx+1}.txt')
            elif barracks == 'GRB':
                cGRB.append(f'./../src/check_sap_cons {barracks}_{template} SLM > barracks/{barracks}/SD_DOCS/{barracks}_FILE{idx+1}.txt')
            elif barracks == 'GRC':
                cGRC.append(f'./../src/check_sap_cons {barracks}_{template} SLM > barracks/{barracks}/SD_DOCS/{barracks}_FILE{idx+1}.txt')
            elif barracks == 'SLM':
                cSLM.append(f'./../src/check_sap_cons {barracks}_{template} SLM > barracks/{barracks}/SD_DOCS/{barracks}_FILE{idx+1}.txt')
    return