import tkinter as tk
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.downloader import DownloaderApp
from src.tracker import TrackerApp
from src.viewer import ViewerApp
from src.exporter import ExporterApp

BG_SIDEBAR = "#111111"
BG_CONTENT = "#0a0a0a"
ACCENT = "#c13584"
TEXT = "#ffffff"
MUTED = "#888888"

class ModernDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Instagram Studio 2026")
        self.geometry("1200x800")
        self.minsize(1000, 600)
        self.configure(bg=BG_CONTENT)
        
        self.apps = {}
        self.current_app = None
        self.nav_buttons = {}

        self._build_ui()

    def _build_ui(self):
        # --- Sidebar ---
        self.sidebar = tk.Frame(self, bg=BG_SIDEBAR, width=240)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # App Logo / Title
        title_frame = tk.Frame(self.sidebar, bg=BG_SIDEBAR)
        title_frame.pack(fill="x", pady=(30, 40))
        tk.Label(title_frame, text="IG Studio", font=("Segoe UI", 24, "bold"), 
                 bg=BG_SIDEBAR, fg=TEXT).pack()

        # Nav Buttons Container
        self.nav_container = tk.Frame(self.sidebar, bg=BG_SIDEBAR)
        self.nav_container.pack(fill="x", padx=10)

        # Content Area
        self.content_area = tk.Frame(self, bg=BG_CONTENT)
        self.content_area.pack(side="left", fill="both", expand=True)

        # Initialize Apps
        self.apps["downloader"] = DownloaderApp(self.content_area)
        self.apps["tracker"] = TrackerApp(self.content_area)
        self.apps["viewer"] = ViewerApp(self.content_area)
        self.apps["exporter"] = ExporterApp(self.content_area)

        # Create Nav Buttons
        self._create_nav_button("downloader", "\U0001f4e5  Downloader")
        self._create_nav_button("tracker", "\U0001f465  Follow Tracker")
        self._create_nav_button("viewer", "\U0001f441  Story Viewer")
        self._create_nav_button("exporter", "\U0001f3ac  MP4 Exporter")

        # Bottom of sidebar (Settings / Credits)
        bottom_frame = tk.Frame(self.sidebar, bg=BG_SIDEBAR)
        bottom_frame.pack(side="bottom", fill="x", pady=20)

        # Switch to first tab
        self.switch_tab("downloader")

        # Graceful close
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def _create_nav_button(self, app_id, text):
        btn = tk.Button(self.nav_container, text=text, bg=BG_SIDEBAR, fg=MUTED, 
                        font=("Segoe UI", 12, "bold"), relief="flat", anchor="w", 
                        padx=20, pady=12, cursor="hand2",
                        activebackground="#1e1e1e", activeforeground=TEXT,
                        command=lambda: self.switch_tab(app_id))
        btn.pack(fill="x", pady=2)
        
        def on_enter(e, b=btn, id=app_id):
            if self.current_app != id:
                b.config(bg="#1e1e1e", fg=TEXT)
                
        def on_leave(e, b=btn, id=app_id):
            if self.current_app != id:
                b.config(bg=BG_SIDEBAR, fg=MUTED)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        self.nav_buttons[app_id] = btn

    def switch_tab(self, app_id):
        # Hide current
        if self.current_app and self.current_app in self.apps:
            # Auto-pause viewer if switching away
            if self.current_app == "viewer":
                try:
                    self.apps["viewer"].pause_playback()
                except Exception:
                    pass
            self.apps[self.current_app].pack_forget()
            # Reset button style
            self.nav_buttons[self.current_app].config(bg=BG_SIDEBAR, fg=MUTED)

        self.current_app = app_id
        
        # Auto-resume viewer if switching back
        if app_id == "viewer":
            try:
                self.apps["viewer"].resume_playback()
            except Exception:
                pass

        # Show new
        self.apps[app_id].pack(fill="both", expand=True)
        # Highlight button
        self.nav_buttons[app_id].config(bg="#1e1e1e", fg=ACCENT)

    def on_close(self):
        try:
            self.apps["viewer"]._on_close()
        except Exception:
            pass
        self.destroy()

if __name__ == "__main__":
    app = ModernDashboard()
    app.mainloop()
