def report_soldier(infoname, infonum, warhour):
    with open('dumbsoldiers.log', 'a') as f:
        f.write(f'ERROR | {infonum} | {warhour} | {infoname}\n')
        return
