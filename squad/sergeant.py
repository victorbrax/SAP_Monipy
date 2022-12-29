from squad.lodge import sgt_list, envs
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

    sgt_list[infonum] = {
        'SD_Number': infonum, 
        'SD_Name': infoname,
        'SD_Value': val,
        'SD_Status': sd_stts,
        'Priority': prior,
        'War_Hour': clockpoint
        }
    return sgt_list[infonum]
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

        sgt_list[infonum] = {
        'SD_Number': infonum, 
        'SD_Name': infoname,
        'SD_Value': val,
        'SD_Status': sd_stts,
        'Priority': prior,
        'War_Hour': clockpoint
        }
    return sgt_list[infonum]
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

    sgt_list[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return sgt_list[infonum]
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

    sgt_list[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return sgt_list[infonum]
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

    sgt_list[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return sgt_list[infonum]
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

    sgt_list[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return sgt_list[infonum]
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

    sgt_list[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return sgt_list[infonum]
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

    sgt_list[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return sgt_list[infonum]
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

    sgt_list[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return sgt_list[infonum]
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

    sgt_list[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return sgt_list[infonum]
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

    sgt_list[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return sgt_list[infonum]
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

    sgt_list[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return sgt_list[infonum]
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

    sgt_list[infonum] = {
    'SD_Number': infonum, 
    'SD_Name': infoname,
    'SD_Value': val,
    'SD_Status': sd_stts,
    'Priority': prior,
    'War_Hour': clockpoint
    }
    return sgt_list[infonum]

def sgt_verify():
    maxdb_moni(envs[2], limit='ONLINE') # State Current State #! ALERT != "ONLINE"
    data_use(envs[2], limit=92) # Data Area Used Data Space #! ALERT >= 92
    log_use(envs[2], limit=50) # Log Area Used Log Space #! ALERT >= 50
    datahitrate(envs[2], limit=90) # Caches Data Cache Hitrate - total #! ALERT >= 90
    cataloghitrate(envs[2], limit=90) # Caches Catalog Cache Hitrate #! ALERT >= 90
    ustask(envs[2], limit=10) # User Tasks Connect Wait #! ALERT >= 10
    monilog(envs[2], limit=1) # Monitor Log Queue Overflows #! ALERT >= 1
    optistcs(envs[2], limit=8) # Optimizer Statistics Last Collection #! ALERT >= 8
    bkp(envs[2], limit=2) # Last Backup Last successful Complete Data Backup #! ALERT >= 2 Days
    badidx(envs[2], limit=1) # Bad Indexes Number of Bad Indexes #! ALERT >= 1
    dbanly(envs[2], limit='Activated') # Database Analyzer Status Database Analyzer #! ALERT != Activated
    comexec(envs[2], limit='Commands can be executed') # DBMRFC and Native SQL DBM Command Execution #! ALERT != Commands can be executed 
    statexec(envs[2], limit='Statements can be executed') # DBMRFC and Native SQL SQL Statement Execution #! ALERT != Statements can be executed
    return