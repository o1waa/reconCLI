# Recon CLI Framework

Modulární Python framework určený pro základní průzkum (reconnaissance) webových aplikací a síťové infrastruktury.

## Složení modulů
- **Fast Scanner (`fast_scanner.py`)**: Vícevláknový port scanner pro rychlou detekci otevřených portů.
- **Banner Grabber (`banner_grabber.py`)**: Vytažení HTTP/SSL hlaviček a identifikace služeb.
- **HTTP Directory Scanner (`http_directory.py`)**: Fuzzing a enumerace skrytých adresářů a souborů.
- **Orchestrator (`recon_cli.py`)**: Jednotné CLI a interaktivní menu pro spouštění všech modulů.

## Použití

### Interaktivní režim
```bash
python recon_cli.py
