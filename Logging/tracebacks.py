
#when we dont know about the error the loggig will help us in identifying the error
import logging
import traceback
a=[12,3]
try:
    print(a[10])
except:
    logging.error('the error is %s',traceback.format_exc())