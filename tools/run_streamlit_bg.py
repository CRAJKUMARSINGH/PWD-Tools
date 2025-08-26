import subprocess
import threading
import time
import socket
import logging
from pathlib import Path
from typing import Tuple


def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def _wait_for_port(port: int, timeout_seconds: int = 30) -> bool:
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        try:
            socket.create_connection(("127.0.0.1", port), 1).close()
            return True
        except Exception:
            time.sleep(0.5)
    return False


def launch_streamlit(script_path: Path, port: int | None = None) -> Tuple[str, subprocess.Popen]:
    port = port or _free_port()
    cmd = [
        "streamlit",
        "run",
        "--server.headless",
        "true",
        "--server.port",
        str(port),
        "--server.address",
        "127.0.0.1",
        "--browser.gatherUsageStats",
        "false",
        str(script_path),
    ]
    logging.info("Starting Streamlit: %s", " ".join(cmd))
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if not _wait_for_port(port, 40):
        raise RuntimeError("Streamlit did not start on 127.0.0.1:%d" % port)
    return f"http://127.0.0.1:{port}", proc