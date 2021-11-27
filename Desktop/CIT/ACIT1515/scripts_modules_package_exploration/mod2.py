from log_setup import log

log(f"module __name__ = {__name__} : start")

import mod1


def mod2func():
    log("executing mod2func")
    mod1.mod1func()


log(f"module __name__ = {__name__} : end")
