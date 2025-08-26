from pathlib import Path
import sys
import logging
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow


def configure_logging() -> None:
    log_path = Path.home() / "PwdTools.log"
    try:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            handlers=[
                logging.FileHandler(log_path, encoding="utf-8"),
            ],
        )
        logging.info("Logging initialized at %s", log_path)
    except Exception:
        logging.basicConfig(level=logging.INFO)


def main() -> int:
    configure_logging()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())