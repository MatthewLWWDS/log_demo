import logging.config
import time

import dummymodule
import logconfig


if __name__=="__main__":

    conf_for_log=logconfig.readconfig()
    logging.config.dictConfig(conf_for_log)

    print("="*3,"root")
    logging.critical({
        'massage' : 'root:critical',
        'name' : __name__})
    logging.warning({
        'massage' : 'root:warning',
        'name' : __name__}) 
    logging.debug({
        'massage' : 'root:debug',
        'name' : __name__}) 
    
    print("="*3,"logger(simpleExample)")
    dummymodule.dm("good") # no problem
    dummymodule.dm() # warning
    dummymodule.dm(3) # error and stop

    


