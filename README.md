# Mic dB Overlay

Een handige, minimalistische en transparante desktop-overlay voor Windows die real-time het volume van je microfoon (in decibel) weergeeft.  
Perfect voor streamers, online meetings, of om altijd een oogje te houden op je geluidsniveau (denk ook aan slapende kinderen).

Inclusief slimme **Peak Hold**-logica, dynamische kleurcodering en een instelbaar menu.

---

## Functies

* **Real-time dB-meting** via `sounddevice` en `numpy`
* **Slimme Peak Hold** – pieken blijven duidelijk zichtbaar
* **Drie visualisatie-modi** (via rechtermuisknop-menu):
  * Simpele balk
  * Balk + piekindicator (standaard)
  * LED-stijl (gesegmenteerde VU-meter)
* **Visuele kleuraanduiding**:
  * 🟢 Groen – normaal niveau
  * 🟠 Oranje – richting de drempel
  * 🔴 Rood – boven de drempel / te luid
* **Instelbaar via rechtermuisknop-menu**:
  * Offset (dB-kalibratie)
  * Eigen drempels voor oranje en rood
  * Positie van de overlay (linksboven, rechtsboven, linksonder, rechtsonder)
  * Visualisatie-modus kiezen
* **Instellingen worden opgeslagen** – blijven bewaard na herstart
* **Transparante, borderloze overlay** die altijd bovenop blijft
* **Afsluiten** met de `Escape`-toets

---

## Hoe te gebruiken (eindgebruikers)

1. Download de nieuwste `mic_db_overlay.exe` via de [Releases](https://github.com/Bearfingers/mic-db-overlay/releases) pagina.
2. Dubbelklik om de overlay te starten.
3. **Rechtermuisknop** op de overlay → menu met alle instellingen.
4. Druk op **Escape** om de overlay te sluiten.

De instellingen worden automatisch opgeslagen in `mic_db_config.json` (naast de .exe).

---

## Zelf aan de slag / Ontwikkeling

### Vereisten
- Python 3.9+
- `sounddevice`
- `numpy`
- `pyinstaller` (alleen voor het bouwen van de .exe)

### Installatie
```bash
git clone https://github.com/Bearfingers/mic-db-overlay.git
cd mic-db-overlay
pip install sounddevice numpy pyinstaller

### Starten
python mic_db_overlay.py

### .exe bouwen
pyinstaller mic_db_overlay.spec

### Configuratie
| Instelling | Standaard | Beschrijving |

| kalibratie | 82.0 | dB-offset / baseline |
| threshold_orange | 52.0 | Vanaf deze waarde oranje |
| threshold_red | 63.0 | Vanaf deze waarde rood |
| position | topleft | topleft / topright / bottomleft / bottomright |
| viz_mode | peak | simple / peak / led |
| margin | 20 | Afstand tot de rand van het scherm |
