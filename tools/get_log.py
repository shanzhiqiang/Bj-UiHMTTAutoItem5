import logging.handlers
class GetLog:
    __logger = None
    # 获取日志器方法
    @classmethod
    def get_logger(cls):
        if cls.__logger is None:
            # 获取 日志器
            cls.__logger = logging.getLogger()
            # 设置 日志器默认级别
            cls.__logger.setLevel(logging.INFO)
            # 获取 处理器 根据时间切割
            th = logging.handlers.TimedRotatingFileHandler(filename="./log/hmtt.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 获取 格式器
            fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fmt = logging.Formatter(fm)
            # 将格式器添加到处理器中
            th.setFormatter(fmt)
            # 将处理器添加到日志器中
            cls.__logger.addHandler(th)
        return cls.__logger

