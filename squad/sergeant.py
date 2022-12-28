from squad.lodge import s_handlist
import datetime as dt

def supervision(env):
    with open(f'squad/soldiers-bedroom/{env}_FILE2.txt') as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]
    return content

def maxdb_moni(env, limit):
    content = supervision(env)
    val = str(content[0][22:])
    sd_stts = int
    prior = 1
    infoname = content[0][:19] 
    infonum = 0
    clockpoint = dt.datetime.now()


    if val != limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
        'Info_Name': infoname,
        'Info_Val': val,
        'SD_Status': sd_stts,
        'Priority': prior,
        'War_Hour': clockpoint
        }
    return s_handlist[infonum]

def data_use(env, limit):
    content = supervision(env)
    val = float(content[1][28:31])
    sd_stts = int
    prior = 3
    infoname = content[1][:25]
    infonum = 1
    clockpoint = dt.datetime.now()

    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

        s_handlist[infonum] = {
        'Info_Name': infoname,
        'Info_Val': val,
        'SD_Status': sd_stts,
        'Priority': prior,
        'War_Hour': clockpoint
        }
    return s_handlist[infonum]


def log_use(env, limit):
    content = supervision(env)
    val = float(content[2][26:28])
    sd_stts = 1
    prior = 1
    infoname = content[2][:24]
    infonum = 2
    clockpoint = dt.datetime.now()
    
    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'Info_Name': infoname,
    'Info_Val': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]

def datahitrate(env, limit):
    content = supervision(env)
    val = float(content[3][36:37])
    sd_stts = 1
    prior = 1
    infoname = content[3][:36]
    infonum = 3
    clockpoint = dt.datetime.now()

    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'Info_Name': infoname,
    'Info_Val': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]

def cataloghitrate(env, limit):
    content = supervision(env)
    val = float(content[4][31:35])
    sd_stts = 1
    prior = 1
    infoname = content[4][:29]
    infonum = 4
    clockpoint = dt.datetime.now()
    
    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'Info_Name': infoname,
    'Info_Val': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]

def ustask(env, limit):
    content = supervision(env)
    val = float(content[5][26:29])
    sd_stts = 1
    prior = 1
    infoname = content[5][:24]
    infonum = 5
    clockpoint = dt.datetime.now()

    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'Info_Name': infoname,
    'Info_Val': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]

def monilog(env, limit):
    content = supervision(env)
    val = float(content[6][30:34])
    sd_stts = 1
    prior = 1
    infoname = content[6][:36]
    infonum = 6
    clockpoint = dt.datetime.now()
   
    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'Info_Name': infoname,
    'Info_Val': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]

def optistcs(env, limit):
    content = supervision(env)
    val = int(content[7][39:40])
    sd_stts = 1
    prior = 1
    infoname = content[7][:37]
    infonum = 7
    clockpoint = dt.datetime.now()

    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'Info_Name': infoname,
    'Info_Val': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]

def bkp(env, limit):
    content = supervision(env)
    val = int(content[8][51:53])
    sd_stts = 1
    prior = 1
    infoname = content[8][:49]
    infonum = 8
    clockpoint = dt.datetime.now()
  
    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'Info_Name': infoname,
    'Info_Val': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]

def badidx(env, limit):
    content = supervision(env)
    val = int(content[9][36:39])
    sd_stts = 1
    prior = 1
    infoname = content[9][:34]
    infonum = 9
    clockpoint = dt.datetime.now()

    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'Info_Name': infoname,
    'Info_Val': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]

def dbanly(env, limit):
    content = supervision(env)
    val = str(content[12][45:54])
    sd_stts = 1
    prior = 1
    infoname = content[12][:43]
    infonum = 12
    clockpoint = dt.datetime.now()

    if val != limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'Info_Name': infoname,
    'Info_Val': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]

def comexec(env, limit):
    content = supervision(env)
    val = str(content[13][46:70])
    sd_stts = 1
    prior = 1
    infoname = content[13][:44]
    infonum = 13
    clockpoint = dt.datetime.now()

    if val != limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'Info_Name': infoname,
    'Info_Val': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]

def statexec(env, limit):
    content = supervision(env)
    val = str(content[14][48:74])
    sd_stts = 1
    prior = 1
    infoname = content[14][:46]
    infonum = 14
    clockpoint = dt.datetime.now()

    if val != limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'Info_Name': infoname,
    'Info_Val': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]