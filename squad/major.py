import json
from squad.lodge import dumb_soldiers

def report_soldier(sdNum, sdName, sdVal, sdStts, sdPrio, sdHour):
    dumb_soldiers[sdNum] = {
    'SD_Number': sdNum, 
    'SD_Name': sdName,
    'SD_Value': sdVal,
    'SD_Status': sdStts,
    'SD_Priority': sdPrio,
    'SD_Hour': sdHour
    }
    return(dumb_soldiers[sdNum])

def punish_soldier(x: dict):
    with open('dumbsoldiers.log', 'a') as log:
        log.write(str(x)+"\n")
    return