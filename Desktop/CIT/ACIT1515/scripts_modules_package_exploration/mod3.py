from log_setup import log

log(f"module __name__ = {__name__} : start")


def mod3func():
    log("executing mod3func")


log(f"module __name__ = {__name__} : end")
