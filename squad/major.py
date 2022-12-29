def report_soldier(infoname, infonum, warhour, infovalue):
    with open('dumbsoldiers.log', 'a') as f:
        f.write(f'ERROR | {infonum} | {warhour} | {infoname} | {infovalue}\n')
        return
