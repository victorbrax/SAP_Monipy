
# > SAP Environments
envs = ['ED1', 'EQ1', 'EP1', 'GRB', 'GRC', 'SLM']
#         0      1      2     3      4       5

# > Prisons
ed1_prisoners = {}
eq1_prisoners = {}
ep1_prisoners = {}
grb_prisoners = {}
grc_prisoners = {}
slm_prisoners = {}

# > Soldiers List
ed1_soldiers = []
eq1_soldiers = []
ep1_soldiers = []
grb_soldiers = []
grc_soldiers = []
slm_soldiers = []


# > Templates
templs = [
    'enqueue',      # 0
    'maxdb',        # 1
    'btc_serv',     # 2
    'diag_db_con',  # 3
    'diag_serv',    # 4
    'local_gate',   # 5
    'os_collector', # 6
    'rfc_queues',   # 7
    'spool_serv',   # 8
    'status',       # 9
    'sys_errors',   # 10
    'update_serv',  # 11
]

maxdb_criterias = {}
maxdb_criterias[0] = {"Priority": 1, "Limit": "ONLINE", "Operator": 0}
maxdb_criterias[1] = {"Priority": 2, "Limit": 92, "Operator": 1}
maxdb_criterias[2] = {"Priority": 1, "Limit": 50, "Operator": 1}
maxdb_criterias[3] = {"Priority": 2, "Limit": 90, "Operator": 1}
maxdb_criterias[4] = {"Priority": 1, "Limit": 90, "Operator": 1}
maxdb_criterias[5] = {"Priority": 3, "Limit": 59, "Operator": 1}
maxdb_criterias[6] = {"Priority": 1, "Limit": 1, "Operator": 1}
maxdb_criterias[7] = {"Priority": 1, "Limit": 8, "Operator": 1}
maxdb_criterias[8] = {"Priority": 3, "Limit": 2, "Operator": 1}
maxdb_criterias[9] = {"Priority": 4, "Limit": 1, "Operator": 1}
maxdb_criterias[10] = {"Priority": 1, "Limit": None, "Operator": 7}
maxdb_criterias[11] = {"Priority": 2, "Limit": None, "Operator": 7}
maxdb_criterias[12] = {"Priority": 1, "Limit": "Activated", "Operator": 0}
maxdb_criterias[13] = {"Priority": 4, "Limit": "Commands can be executed", "Operator": 0}
maxdb_criterias[14] = {"Priority": 3, "Limit": "Statements can be executed", "Operator": 0}
