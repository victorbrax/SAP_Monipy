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
    sd_num = 0
    sd_name = content[0][:19] 
    sd_val = str(content[0][22:])
    sd_stts = int
    sd_prio = 1
    sd_hour = dt.datetime.now()

    if sd_val != limit:
        sd_stts = 1
    else:
        sd_stts = 0

    sgt_list[sd_num] = {
        'SD_Number': sd_num, 
        'SD_Name': sd_name,
        'SD_Value': sd_val,
        'SD_Status': sd_stts,
        'SD_Priority': sd_prio,
        'SD_Hour': sd_hour
        }
def data_use(env, limit):
    content = supervision(env)
    sd_num = 1
    sd_name = content[1][:25]
    sd_val = float(content[1][28:])
    sd_stts = int
    sd_prio = 2
    sd_hour = dt.datetime.now()

    if sd_val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

        sgt_list[sd_num] = {
        'SD_Number': sd_num, 
        'SD_Name': sd_name,
        'SD_Value': sd_val,
        'SD_Status': sd_stts,
        'SD_Priority': sd_prio,
        'SD_Hour': sd_hour
        }
    return sgt_list[sd_num]
def log_use(env, limit):
    content = supervision(env)
    sd_num = 2
    sd_name = content[2][:23]
    sd_val = float(content[2][26:])
    sd_stts = 1
    sd_prio = 1
    sd_hour = dt.datetime.now()
    
    if sd_val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    sgt_list[sd_num] = {
    'SD_Number': sd_num, 
    'SD_Name': sd_name,
    'SD_Value': sd_val,
    'SD_Status': sd_stts,
    'SD_Priority': sd_prio,
    'SD_Hour': sd_hour
    }
    return sgt_list[sd_num]
def datahitrate(env, limit):
    content = supervision(env)
    sd_num = 3
    sd_name = content[3][:33]
    sd_val = float(content[3][36:])
    sd_stts = 1
    sd_prio = 4
    sd_hour = dt.datetime.now()

    if sd_val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    sgt_list[sd_num] = {
    'SD_Number': sd_num, 
    'SD_Name': sd_name,
    'SD_Value': sd_val,
    'SD_Status': sd_stts,
    'SD_Priority': sd_prio,
    'SD_Hour': sd_hour
    }
    return sgt_list[sd_num]
def cataloghitrate(env, limit):
    content = supervision(env)
    sd_num = 4
    sd_name = content[4][:28]
    sd_val = float(content[4][31:])
    sd_stts = 1
    sd_prio = 1
    sd_hour = dt.datetime.now()
    
    if sd_val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    sgt_list[sd_num] = {
    'SD_Number': sd_num, 
    'SD_Name': sd_name,
    'SD_Value': sd_val,
    'SD_Status': sd_stts,
    'SD_Priority': sd_prio,
    'SD_Hour': sd_hour
    }
    return sgt_list[sd_num]
def ustask(env, limit):
    content = supervision(env)
    sd_num = 5
    sd_name = content[5][:23]
    sd_val = float(content[5][26:])
    sd_stts = 1
    sd_prio = 2
    sd_hour = dt.datetime.now()

    if sd_val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    sgt_list[sd_num] = {
    'SD_Number': sd_num, 
    'SD_Name': sd_name,
    'SD_Value': sd_val,
    'SD_Status': sd_stts,
    'SD_Priority': sd_prio,
    'SD_Hour': sd_hour
    }
    return sgt_list[sd_num]
def monilog(env, limit):
    content = supervision(env)
    sd_num = 6
    sd_name = content[6][:26]
    sd_val = float(content[6][30:])
    sd_stts = 1
    sd_prio = 3
    sd_hour = dt.datetime.now()
   
    if sd_val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    sgt_list[sd_num] = {
    'SD_Number': sd_num, 
    'SD_Name': sd_name,
    'SD_Value': sd_val,
    'SD_Status': sd_stts,
    'SD_Priority': sd_prio,
    'SD_Hour': sd_hour
    }
    return sgt_list[sd_num]
def optistcs(env, limit):
    content = supervision(env)
    sd_num = 7
    sd_name = content[7][:36]
    sd_val = int(content[7][39:])
    sd_stts = 1
    sd_prio = 3
    sd_hour = dt.datetime.now()

    if sd_val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    sgt_list[sd_num] = {
    'SD_Number': sd_num, 
    'SD_Name': sd_name,
    'SD_Value': sd_val,
    'SD_Status': sd_stts,
    'SD_Priority': sd_prio,
    'SD_Hour': sd_hour
    }
    return sgt_list[sd_num]
def bkp(env, limit):
    content = supervision(env)
    sd_num = 8
    sd_name = content[8][:48]
    sd_val = int(content[8][51:])
    sd_stts = 1
    sd_prio = 1
    sd_hour = dt.datetime.now()
  
    if sd_val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    sgt_list[sd_num] = {
    'SD_Number': sd_num, 
    'SD_Name': sd_name,
    'SD_Value': sd_val,
    'SD_Status': sd_stts,
    'SD_Priority': sd_prio,
    'SD_Hour': sd_hour
    }
    return sgt_list[sd_num]
def badidx(env, limit):
    content = supervision(env)
    sd_num = 9
    sd_name = content[9][:33]
    sd_val = int(content[9][36:])
    sd_stts = 1
    sd_prio = 3
    sd_hour = dt.datetime.now()

    if sd_val >= limit:
        sd_stts = 1
    else:
        sd_stts = 0

    sgt_list[sd_num] = {
    'SD_Number': sd_num, 
    'SD_Name': sd_name,
    'SD_Value': sd_val,
    'SD_Status': sd_stts,
    'SD_Priority': sd_prio,
    'SD_Hour': sd_hour
    }
    return sgt_list[sd_num]
def dbanly(env, limit):
    content = supervision(env)
    sd_num = 12
    sd_name = content[12][:42]
    sd_val = str(content[12][45:])
    sd_stts = 1
    sd_prio = 3
    sd_hour = dt.datetime.now()

    if sd_val != limit:
        sd_stts = 1
    else:
        sd_stts = 0

    sgt_list[sd_num] = {
    'SD_Number': sd_num, 
    'SD_Name': sd_name,
    'SD_Value': sd_val,
    'SD_Status': sd_stts,
    'SD_Priority': sd_prio,
    'SD_Hour': sd_hour
    }
    return sgt_list[sd_num]
def comexec(env, limit):
    content = supervision(env)
    sd_num = 13
    sd_name = content[13][:43]
    sd_val = str(content[13][46:])
    sd_stts = 1
    sd_prio = 1
    sd_hour = dt.datetime.now()

    if sd_val != limit:
        sd_stts = 1
    else:
        sd_stts = 0

    sgt_list[sd_num] = {
    'SD_Number': sd_num, 
    'SD_Name': sd_name,
    'SD_Value': sd_val,
    'SD_Status': sd_stts,
    'SD_Priority': sd_prio,
    'SD_Hour': sd_hour
    }
    return sgt_list[sd_num]
def statexec(env, limit):
    content = supervision(env)
    sd_num = 14
    sd_name = content[14][:46]
    sd_val = str(content[14][47:])
    sd_stts = 1
    sd_prio = 1
    sd_hour = dt.datetime.now()

    if sd_val != limit:
        sd_stts = 1
    else:
        sd_stts = 0

    sgt_list[sd_num] = {
    'SD_Number': sd_num, 
    'SD_Name': sd_name,
    'SD_Value': sd_val,
    'SD_Status': sd_stts,
    'SD_Priority': sd_prio,
    'SD_Hour': sd_hour
    }
    return sgt_list[sd_num]

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