from log_setup import log

log(f"module __name__ = {__name__} : start")


def modcfunc():
    log("executing modcfunc")


log(f"module __name__ = {__name__} : end")
