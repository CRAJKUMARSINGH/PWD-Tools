from pathlib import Path
import sys
import logging
from typing import Optional, Tuple
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QMessageBox
from PySide6.QtWebEngineWidgets import QWebEngineView
from tools.run_streamlit_bg import launch_streamlit


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PWD Tools Desktop")
        self.resize(1200, 800)

        self._tabs = QTabWidget()
        self._tabs.setDocumentMode(True)
        self._tabs.setMovable(True)
        self.setCentralWidget(self._tabs)

        self._streamlit_proc = None

        self._init_menu()
        self._init_tabs()

    def _init_menu(self) -> None:
        menu = self.menuBar().addMenu("View")

        self._action_reload = QAction("Reload Current Tab", self)
        self._action_reload.setShortcut(QKeySequence.Refresh)
        self._action_reload.triggered.connect(self._reload_current_tab)
        menu.addAction(self._action_reload)

        self._action_devtools = QAction("Open DevTools (F12)", self)
        self._action_devtools.setShortcut(QKeySequence(Qt.Key_F12))
        self._action_devtools.triggered.connect(self._open_devtools)
        menu.addAction(self._action_devtools)

    def _init_tabs(self) -> None:
        # Tab 1: Streamlit app hosted locally
        streamlit_url, proc = self._start_streamlit(Path("app.py"))
        self._streamlit_proc = proc
        self._add_web_tab("Hub (Streamlit)", QUrl(streamlit_url))

        # Tab 2: Example static content (if exists)
        static_index = Path("static/index.html")
        if static_index.exists():
            self._add_web_tab("Static Site", QUrl.fromLocalFile(str(static_index.resolve())))

    def _start_streamlit(self, script_path: Path) -> Tuple[str, object]:
        try:
            url, proc = launch_streamlit(script_path)
            logging.info("Streamlit started at %s for %s", url, script_path)
            return url, proc
        except Exception as exc:
            logging.exception("Failed to start Streamlit: %s", exc)
            QMessageBox.critical(self, "Streamlit Error", str(exc))
            # Fallback to an about:blank page
            return "about:blank", None

    def _add_web_tab(self, title: str, url: QUrl) -> None:
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)

        view = QWebEngineView(container)
        view.setUrl(url)
        layout.addWidget(view)

        self._tabs.addTab(container, title)

    def _reload_current_tab(self) -> None:
        widget = self._tabs.currentWidget()
        if widget is None:
            return
        view = widget.findChild(QWebEngineView)
        if view is not None:
            view.reload()

    def _open_devtools(self) -> None:
        widget = self._tabs.currentWidget()
        if widget is None:
            return
        view = widget.findChild(QWebEngineView)
        if view is not None:
            try:
                view.page().setDevToolsPage(view.page())
            except Exception:
                pass

    def closeEvent(self, event) -> None:  # type: ignore[override]
        try:
            if self._streamlit_proc is not None:
                self._streamlit_proc.terminate()
        except Exception:
            pass
        super().closeEvent(event)