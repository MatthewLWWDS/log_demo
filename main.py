import logging.config
import time

import logconfig



MODE="LOG"

if MODE=="LOG":
    print("="*5,"start:LOG")

    conf_for_log=logconfig.readconfig()
    logging.config.dictConfig(conf_for_log)
    
    print("="*3,"root")
    logging.critical('LOG : CRITICAL') # CRITICALログ発生
    logging.error('LOG : ERROR({})'.format(66)) # ERRORログ発生
    logging.warning('LOG : WARNING') # WARNINGログ発生
    logging.info('LOG : INFO') # INFOログ発生
    logging.debug('LOG : DEBUG({})'.format(10)) # DEBUGログ発生
    
    print("="*3,"logger(simpleExample)")
    logger=logging.getLogger('simpleExample')
    logger.critical('LOG : CRITICAL') # CRITICALログ発生
    logger.error('LOG : ERROR({})'.format(66)) # ERRORログ発生
    logger.warning('LOG : WARNING') # WARNINGログ発生
    logger.info('LOG : INFO') # INFOログ発生
    logger.debug('LOG : DEBUG({})'.format(10)) # DEBUGログ発生

    print("="*5,"end:LOG")

elif MODE=='LOG_EXAMPLE':
    print("="*5,"start:",MODE)

    conf_for_log=logconfig.readconfig()
    logging.config.dictConfig(conf_for_log)

    print("===simple")
    logging.error('API call is failed') # ERRORログ発生
    
    time.sleep(1.4)

    print("\n===detail")
    logging.error({
        'action' : 'create', 
        'message' : 'API call is failed', 
        'name' : __name__,
        'status' : 'fail'
    })

    print("="*5,"end:",MODE)


