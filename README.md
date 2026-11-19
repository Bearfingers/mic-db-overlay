# Mic dB Overlay

A handy, minimalist and transparent desktop overlay for Windows that displays your microphone volume in real-time (in decibels).

Perfect for streamers, online meetings, or simply keeping an eye on your audio levels (e.g. when children are sleeping).

Includes smart Peak Hold logic, dynamic color coding and a fully configurable right-click menu.

## Features

- Real-time dB measurement via `sounddevice` and `numpy`
- Smart Peak Hold – peaks stay clearly visible
- Three visualization modes (via right-click menu):
  - Simple bar
  - Bar + peak indicator (default)
  - LED style (segmented VU meter)
- Visual color coding:
  - 🟢 Green – normal level
  - 🟠 Orange – approaching the threshold
  - 🔴 Red – above the threshold / too loud
- Fully configurable via right-click menu:
  - Offset (dB calibration)
  - Custom orange & red thresholds
  - Overlay position (top-left, top-right, bottom-left, bottom-right)
  - Visualization mode
  - **Language** (Dutch / English)
  - **Font family & size**
- Settings are saved – they persist after restart
- Transparent, borderless overlay that always stays on top
- Exit with the `Escape` key

## How to use (end users)

1. Download the latest `mic_db_overlay.exe` from the [Releases](https://github.com/Bearfingers/mic-db-overlay/releases) page.
2. Double-click to start the overlay.
3. Right-click the overlay → menu with all settings.
4. Press `Escape` to close the overlay.

Settings are automatically saved in `mic_db_config.json` (next to the .exe).

## Development

### Requirements

- Python 3.9+
- `sounddevice`
- `numpy`
- `pyinstaller` (only needed for building the .exe)

### Installation

```bash
git clone https://github.com/Bearfingers/mic-db-overlay.git
cd mic-db-overlay
pip install sounddevice numpy pyinstaller
```

### Run

```bash
python mic_db_overlay.py
```

### Build .exe

```bash
pyinstaller mic_db_overlay.spec
```

### Configuration

| Setting            | Default   | Description                                      |
|--------------------|-----------|--------------------------------------------------|
| kalibratie         | 82.0      | dB offset / baseline                             |
| threshold_orange   | 52.0      | Turns orange from this value                     |
| threshold_red      | 63.0      | Turns red from this value                        |
| position           | topleft   | topleft / topright / bottomleft / bottomright    |
| viz_mode           | peak      | simple / peak / led                              |
| margin             | 20        | Distance from the edge of the screen             |
| language           | nl        | nl / en                                          |
| font_family        | Consolas  | Font family for the dB text                      |
| font_size          | 12        | Font size                                        |
