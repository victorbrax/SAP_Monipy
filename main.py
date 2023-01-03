import datetime
from squad.accommodations import *
from squad.captain        import *
from squad.major          import *
from squad.sergeant       import *
from squad.soldiers       import *

# > Generate Soldier Documents.
gen_commands(envs, templates)
run_commands(envs)

# > Check who is already arrested.
for barracks in envs:
    check_prisoners(barracks)

# > Enroll new soldiers.
for barracks in envs:
    register_soldier(barracks)

# > Judge the soldiers who didn't behave.
for barracks in envs:
    judge_soldiers(barracks)