import  logging
from logging import handlers


class Initlog():

  fmt="%(asctime)s  %(levelname)s  %(filename)s  %(funcName)s    %(lineno)d  %(message)s"
  formatter =logging.Formatter(fmt)

  sh =logging.StreamHandler()
  fh = logging.handlers.TimedRotatingFileHandler("./log/a.log",when="D",interval=1,backupCount=7,encoding="utf-8")

  sh.setFormatter(formatter)
  fh.setFormatter(formatter)

  logger =logging.getLogger()

  logger.addHandler(sh)
  logger.addHandler(fh)

  logger.setLevel(logging.INFO)


#logging.info("zz")
