# Changelog

All notable changes to this project will be documented in this file.

## [2.1.0] - 2026-11-19

### Added
- **Language support** – Switch between Dutch and English via the right-click menu
- **Font customization** – Choose font family and size from the right-click menu
- New configuration options: `language`, `font_family`, `font_size`
- Full English translation of all UI text, dialogs and status messages

### Changed
- Menu is now dynamically rebuilt when the language is changed
- Font changes are applied immediately and persisted

### Improved
- Configuration loading now validates language and font settings
- Overlay position is recalculated after changing font size

## [2.0.0] - Previous

### Added
- Configurable right-click menu
- Three visualization modes: Simple bar, Bar + peak indicator, LED style
- Adjustable orange and red thresholds
- Overlay position selection (four corners)
- Persistent settings via `mic_db_config.json`
- Peak Hold logic
- Color coding (green / orange / red)

### Features
- Real-time microphone dB measurement
- Transparent always-on-top overlay
- Exit with Escape key
