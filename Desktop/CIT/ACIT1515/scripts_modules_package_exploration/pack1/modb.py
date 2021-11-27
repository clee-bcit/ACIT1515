from log_setup import log

log(f"module __name__ = {__name__} : start")


def modbfunc():
    log("executing modbfunc")


log(f"module __name__ = {__name__} : end")
