"""
Simple logging setup module

Configures logging and creates alias to debug logger called: log
"""
# Setup Logging
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="{filename:<22} {module:<22} {funcName:<12} {message}",
    style="{",
)  # Use new style string formatter

log = logging.getLogger(__name__).debug

filename = "filename"
module = "module"
funcName = "function"
message = "message"
header = f"{filename:<22} {module:<22} {funcName:<12} {message}"
print(header)
header = "-" * 90
print(header)