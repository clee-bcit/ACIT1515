from log_setup import log

log(f"module __name__ = {__name__} : start")


def moddfunc():
    log("executing moddfunc")


log(f"module __name__ = {__name__} : end")
