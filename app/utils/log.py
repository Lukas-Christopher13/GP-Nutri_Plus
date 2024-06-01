import logging

def configurar_logger(nome_arquivo_log):

    logger = logging.getLogger('meu_logger')
    logger.setLevel(logging.DEBUG) 

    handler = logging.FileHandler(nome_arquivo_log)
    handler.setLevel(logging.DEBUG) 

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger

my_log = configurar_logger("logs/logs.txt")