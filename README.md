#  Mic dB Overlay

Een handige, minimalistische en transparante desktop-overlay voor Windows die real-time het volume van je microfoon (in decibel) weergeeft. Perfect voor streamers, tijdens online meetings, of om altijd een oogje (of oortje) te houden op je geluidsniveau.

Inclusief een slimme **Peak Hold**-logica zodat pieken netjes zichtbaar blijven, en dynamische kleurcodering (groen, oranje, rood) op basis van je drempelwaarden[cite: 1, 2].

---

## Functies
* **Real-time dB-meting:** Direct inzicht in je microfoonniveau via `sounddevice` en `numpy`[cite: 1, 2].
* **Slimme Peak Hold:** Pieken blijven helder in beeld, zelfs als je stem daarna zachter wordt[cite: 1, 2].
* **Visuele kleuraanduiding:** 
  * 🟢 Normaal niveau (`#00FF00`)[cite: 1, 2]
  * 🟠 Richting de drempel (`#FF9900`)[cite: 1, 2]
  * 🔴 Boven de drempel / te luid (`#FF2222`)[cite: 1, 2]
* **Transparante, borderloze overlay:** Staat altijd netjes bovenop (`topmost`) zonder storende vensterranden[cite: 1, 2].
* **Eenvoudig af te sluiten:** Druk op **Escape** om de overlay direct te sluiten[cite: 1, 2].

---

## Hoe te gebruiken (Voor eindgebruikers)
Wil je de tool alleen gebruiken zonder Python te installeren?
1. Download de kant-en-klare `mic_db_overlay.exe` via de [Releases](https://github.com/JOUW-NIEUWE-USERNAME/mic-db-overlay/releases) pagina.
2. Dubbelklik op het bestand om de overlay te starten.
3. Druk op **Escape** op je toetsenbord om de overlay weer af te sluiten[cite: 1, 2].

---

## Zelf aan de slag / Ontwikkeling (Voor developers)
Als je de code wilt inzien of aanpassen:

1. Clone deze repository:
   ```bash
   git clone [https://github.com/bearfingers/mic-db-overlay.git](https://github.com/bearfingers/mic-db-overlay.git)
