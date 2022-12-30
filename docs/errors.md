# Downcast environment
<==  RfcLastError
 
RFC operation/code RfcCallReceive
ERROR/EXCEPTION
key     : RFC_IO5
status  : CODE=CM_PRODUCT_SPECIFIC_ERROR STATUS=??? DATA=??? ID=???
message : SAP_CMINIT3 : rc=20 > Connect to SAP gateway failed
Connect_PM  DEST=SLM, GWHOST=localhost, GWSERV=sapgw05, SYSNR=05
 
LOCATION    CPIC (TCP/IP) on local host
ERROR       partner 'localhost:3305' not reached
TIME        Wed Dec 28 15:38:32 2022
RELEASE
internal: IO HANDLE=1 DRV=EXT LINE=645 CODE=5
 
<==  RfcClose

# Incorrect password or name
<==  RfcLastError

 

FUNCTION: SXMI_LOGON
RFC operation/code SYSTEM_FAILURE
ERROR/EXCEPTION
key     : RFC_ERROR_SYSTEM_FAILURE
status  :
message : Name or password is incorrect (repeat logon)
internal:

# Incorrect host
<==  RfcLastError

 

RFC operation/code RfcCallReceive
ERROR/EXCEPTION
key     : RFC_IO5
status  : CODE=CM_PRODUCT_SPECIFIC_ERROR STATUS=??? DATA=??? ID=???
message : SAP_CMINIT3 : rc=20 > Connect to SAP gateway failed
Connect_PM  DEST=SLM, GWHOST=aaa, GWSERV=sapgw05, SYSNR=05

 

LOCATION    CPIC (TCP/IP) on local host
ERROR       hostname 'aaa' unknown
TIME        Wed Dec 28 15:32:00 2022
RELEASE     720
COMPONENT   NI
internal: IO HANDLE=1 DRV=EXT LINE=645 CODE=5