def report_soldier(infoname, infonum, warhour):
    with open('dumbsoldiers.txt', 'a') as f:
        f.write(f'SOLDIER: {infoname} | NUMBER: {infonum} | WAR HOUR: {warhour}\n')
        return
