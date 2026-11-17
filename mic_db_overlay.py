"""
Mic dB Overlay - Peak hold écht gefixt
======================================
"""

import tkinter as tk
import sounddevice as sd
import numpy as np
import threading
import time

# ============================================================
# INSTELLINGEN
# ============================================================
KALIBRATIE = 82.0
DREMPEL_DB = 63.0
SMOOTHING = 0.30
PEAK_HOLD_TIME = 5.0

MIN_DB = 30
MAX_DB = 100

POSITIE_X = 20
POSITIE_Y = 20
# ============================================================


class MicDbOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mic dB")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)

        self.bg = "#010101"
        self.root.configure(bg=self.bg)
        self.root.attributes("-transparentcolor", self.bg)

        container = tk.Frame(self.root, bg=self.bg)
        container.pack(padx=6, pady=5)

        self.label = tk.Label(
            container,
            text="Wachten...",
            font=("Consolas", 12, "bold"),
            fg="#00FF00",
            bg=self.bg
        )
        self.label.pack(anchor="w")

        self.bar_width = 180
        self.bar_height = 11
        self.canvas = tk.Canvas(
            container,
            width=self.bar_width,
            height=self.bar_height,
            bg=self.bg,
            highlightthickness=0
        )
        self.canvas.pack(pady=(4, 0))

        self.canvas.create_rectangle(
            0, 0, self.bar_width, self.bar_height,
            fill="#1a1a1a", outline="#444444", width=1
        )

        self.bar = self.canvas.create_rectangle(
            1, 1, 1, self.bar_height - 1,
            fill="#00FF00", outline=""
        )

        self.root.geometry(f"+{POSITIE_X}+{POSITIE_Y}")
        self.root.bind("<Escape>", self.stop)
        self.root.focus_force()

        self.current_db = -100.0
        self.smoothed_db = -100.0
        self.peak_db = -100.0
        self.peak_hold_until = 0.0
        self.running = True
        self.first_reading = True

        threading.Thread(target=self.audio_loop, daemon=True).start()
        self.update_display()

    def rms_to_db(self, rms):
        if rms < 1e-9:
            return -100.0
        return 20.0 * np.log10(rms) + KALIBRATIE

    def audio_callback(self, indata, frames, time_info, status):
        rms = np.sqrt(np.mean(np.square(indata)))
        self.current_db = self.rms_to_db(rms)

    def audio_loop(self):
        try:
            with sd.InputStream(
                channels=1,
                samplerate=44100,
                blocksize=2048,
                dtype="float32",
                callback=self.audio_callback
            ):
                while self.running:
                    time.sleep(0.05)
        except Exception as e:
            print("Fout bij microfoon:", e)
            self.running = False

    def get_color(self, db):
        if db >= DREMPEL_DB:
            return "#FF2222"
        elif db >= DREMPEL_DB - 11:
            return "#FF9900"
        else:
            return "#00FF00"

    def update_display(self):
        if not self.running:
            return

        # Eerste meting
        if self.first_reading and self.current_db > -50:
            self.smoothed_db = self.current_db
            self.peak_db = self.current_db
            self.peak_hold_until = time.time() + PEAK_HOLD_TIME
            self.first_reading = False

        # Afvlakking
        if self.current_db > -50:
            self.smoothed_db = (SMOOTHING * self.current_db) + ((1.0 - SMOOTHING) * self.smoothed_db)

        now = time.time()

        # Peak Hold
        if self.smoothed_db > self.peak_db:
            self.peak_db = self.smoothed_db
            self.peak_hold_until = now + PEAK_HOLD_TIME
        elif now > self.peak_hold_until:
            self.peak_db = self.smoothed_db

        # === NIEUWE TEKST LOGICA ===
        # Laat de piek altijd zien zolang die hoger is dan de drempel
        if self.peak_db < MIN_DB:
            text = "Te stil..."
            color = "#888888"
        else:
            # Toon altijd de piek, ook als de live waarde al zacht is
            text = f"{self.smoothed_db:5.1f} dB   piek {self.peak_db:5.1f}"
            color = self.get_color(self.smoothed_db)

        self.label.config(text=text, fg=color)

        # Balk (gebruikt de live waarde)
        level = (self.smoothed_db - MIN_DB) / (MAX_DB - MIN_DB)
        level = max(0.0, min(1.0, level))
        length = int(level * (self.bar_width - 2))

        self.canvas.coords(self.bar, 1, 1, 1 + length, self.bar_height - 1)
        self.canvas.itemconfig(self.bar, fill=self.get_color(self.smoothed_db))

        self.root.after(40, self.update_display)

    def stop(self, event=None):
        self.running = False
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    print("Mic dB Overlay gestart.")
    print("Druk op Escape om te stoppen.")
    app = MicDbOverlay()
    app.run()