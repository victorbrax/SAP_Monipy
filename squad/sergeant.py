from squad.lodge import s_handlist

def supervision(env):
    with open(f'{env}_FILE2.txt') as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]
    return content

def maxdb_moni(env, limit):
    content = supervision(env)
    val = str(content[0][22:])
    sd_stts = 1
    prior = 1
    infoname = content[0][:21] 

    if val != limit:
        return print('FALHA') # Mail
    else:
        return print('TUDO CERTO') # None

def data_use(env, limit):
    content = supervision(env)
    val = float(content[1][28:31])
    sd_stts = 1
    prior = 1
    infoname = content[0][:28]

    if val >= limit:
        return print('FALHA') # Mail
    else:
        return print('TUDO CERTO') # None

def log_use(env, limit):
    content = supervision(env)
    val = float(content[2][26:28])
    sd_stts = 1
    prior = 1
    infoname = content[0][:26]

    if val >= limit:
        return print('FALHA') # Mail
    else:
        return print('TUDO CERTO') # None

def datahitrate(env, limit):
    content = supervision(env)
    val = float(content[3][36:39])
    sd_stts = 1
    prior = 1
    infoname = content[0][:36]

    if val >= limit:
        return print('FALHA') # Mail
    else:
        return print('TUDO CERTO') # None

def cataloghitrate(env, limit):
    content = supervision(env)
    val = float(content[4][31:35])
    sd_stts = 1
    prior = 1
    infoname = content[0][:31]

    if val >= limit:
        return print('FALHA') # Mail
    else:
        return print('TUDO CERTO') # None

def ustask(env, limit):
    content = supervision(env)
    val = float(content[5][26:29])
    sd_stts = 1
    prior = 1
    infoname = content[0][:26]

    if val >= limit:
        return print('FALHA') # Mail
    else:
        return print('TUDO CERTO') # None

def monilog(env, limit):
    content = supervision(env)
    val = float(content[6][30:34])
    sd_stts = 1
    prior = 1
    infoname = content[0][:30]

    if val >= limit:
        return print('FALHA') # Mail
    else:
        return print('TUDO CERTO') # None

def optistcs(env, limit):
    content = supervision(env)
    val = int(content[7][39:40])
    sd_stts = 1
    prior = 1
    infoname = content[0][:39]

    if val >= limit:
        return print('FALHA') # Mail
    else:
        return print('TUDO CERTO') # None

def bkp(env, limit):
    content = supervision(env)
    val = int(content[8][51:53])
    sd_stts = 1
    prior = 1
    infoname = content[0][:51]
  
    if val >= limit:
        return print('FALHA') # Mail
    else:
        return print('TUDO CERTO') # None

def badidx(env, limit):
    content = supervision(env)
    val = int(content[9][36:39])
    sd_stts = 1
    prior = 1
    infoname = content[0][:36]

    if val >= limit:
        return print('FALHA') # Mail
    else:
        return print('TUDO CERTO') # None

def dbanly(env, limit):
    content = supervision(env)
    val = str(content[12][45:54])
    sd_stts = 1
    prior = 1
    infoname = content[0][:45]

    if val != limit:
        return print('FALHA') # Mail
    else:
        return print('TUDO CERTO') # None

def comexec(env, limit):
    content = supervision(env)
    val = str(content[13][46:70])
    sd_stts = 1
    prior = 1
    infoname = content[0][:46]

    if val != limit:
        return print('FALHA') # Mail
    else:
        return print('TUDO CERTO') # None

def statexec(env, limit):
    content = supervision(env)
    val = str(content[14][48:74])
    sd_stts = 1
    prior = 1
    infoname = content[0][:48]

    if val != limit:

        return print('FALHA') # Mail
    else:
        return print('TUDO CERTO') # None
