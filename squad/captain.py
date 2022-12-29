from squad.lodge import *

def cap_gen_commands(env, templ):
    for sapenv in env:
        for count, saptempl in enumerate(templ):
            if sapenv == 'ed1':
                cED1.append(f'./../src/check_sap_cons {sapenv}_{saptempl} SLM > squad/soldiers-bedroom/{sapenv}_FILE{count+1}.txt')
            if sapenv == 'eq1':
                cEQ1.append(f'./../src/check_sap_cons {sapenv}_{saptempl} SLM > squad/soldiers-bedroom/{sapenv}_FILE{count+1}.txt')
            if sapenv == 'ep1':
                cEP1.append(f'./../src/check_sap_cons {sapenv}_{saptempl} SLM > squad/soldiers-bedroom/{sapenv}_FILE{count+1}.txt')
            if sapenv == 'grb':
                cGRB.append(f'./../src/check_sap_cons {sapenv}_{saptempl} SLM > squad/soldiers-bedroom/{sapenv}_FILE{count+1}.txt')
            if sapenv == 'grc':
                cGRC.append(f'./../src/check_sap_cons {sapenv}_{saptempl} SLM > squad/soldiers-bedroom/{sapenv}_FILE{count+1}.txt')
            if sapenv == 'slm':
                cSLM.append(f'./../src/check_sap_cons {sapenv}_{saptempl} SLM > squad/soldiers-bedroom/{sapenv}_FILE{count+1}.txt')
    return