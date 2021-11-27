from log_setup import log

log(f"module __name__ = {__name__} : start")


def modafunc():
    log("executing modafunc")


log(f"module __name__ = {__name__} : end")
