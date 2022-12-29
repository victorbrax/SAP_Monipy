from squad.lodge import s_handlist
import datetime as dt

# MaxDB Monitoring
def supervision(env):
    with open(f'squad/soldiers-bedroom/{env}_FILE2.txt', 'r') as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]
        content = [x.strip(' %') for x in content]
        content = [x.replace(' Days', '') for x in content]
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
        'SD_Number': infonum, 
        'SD_Name': infoname,
        'SD_Value': val,
        'SD_Status': sd_stts,
        'Priority': prior,
        'War_Hour': clockpoint
        }
    return s_handlist[infonum]
def data_use(env, limit):
    content = supervision(env)
    val = float(content[1][28:])
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
        'SD_Number': infonum, 
        'SD_Name': infoname,
        'SD_Value': val,
        'SD_Status': sd_stts,
        'Priority': prior,
        'War_Hour': clockpoint
        }
    return s_handlist[infonum]
def log_use(env, limit):
    content = supervision(env)
    val = float(content[2][26:])
    sd_stts = 1
    prior = 1
    infoname = content[2][:23]
    infonum = 2
    clockpoint = dt.datetime.now()
    
    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]
def datahitrate(env, limit):
    content = supervision(env)
    val = float(content[3][36:])
    sd_stts = 1
    prior = 1
    infoname = content[3][:33]
    infonum = 3
    clockpoint = dt.datetime.now()

    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]
def cataloghitrate(env, limit):
    content = supervision(env)
    val = float(content[4][31:])
    sd_stts = 1
    prior = 1
    infoname = content[4][:28]
    infonum = 4
    clockpoint = dt.datetime.now()
    
    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]
def ustask(env, limit):
    content = supervision(env)
    val = float(content[5][26:])
    sd_stts = 1
    prior = 1
    infoname = content[5][:23]
    infonum = 5
    clockpoint = dt.datetime.now()

    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]
def monilog(env, limit):
    content = supervision(env)
    val = float(content[6][30:])
    sd_stts = 1
    prior = 1
    infoname = content[6][:26]
    infonum = 6
    clockpoint = dt.datetime.now()
   
    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]
def optistcs(env, limit):
    content = supervision(env)
    val = int(content[7][39:])
    sd_stts = 1
    prior = 1
    infoname = content[7][:36]
    infonum = 7
    clockpoint = dt.datetime.now()

    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]
def bkp(env, limit):
    content = supervision(env)
    val = int(content[8][51:])
    sd_stts = 1
    prior = 1
    infoname = content[8][:48]
    infonum = 8
    clockpoint = dt.datetime.now()
  
    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]
def badidx(env, limit):
    content = supervision(env)
    val = int(content[9][36:])
    sd_stts = 1
    prior = 1
    infoname = content[9][:33]
    infonum = 9
    clockpoint = dt.datetime.now()

    if val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]
def dbanly(env, limit):
    content = supervision(env)
    val = str(content[12][45:])
    sd_stts = 1
    prior = 1
    infoname = content[12][:42]
    infonum = 12
    clockpoint = dt.datetime.now()

    if val != limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]
def comexec(env, limit):
    content = supervision(env)
    val = str(content[13][46:])
    sd_stts = 1
    prior = 1
    infoname = content[13][:43]
    infonum = 13
    clockpoint = dt.datetime.now()

    if val != limit:
        sd_stts = 1
    else:
        sd_stts = 0

    s_handlist[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]
def statexec(env, limit):
    content = supervision(env)
    val = str(content[14][47:])
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
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return s_handlist[infonum]

