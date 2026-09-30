import argparse
import subprocess
import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)

def find_script(script_name, folder_name):
    paths_to_try = [
        os.path.join(PARENT_DIR, folder_name, script_name),
        os.path.join(CURRENT_DIR, script_name),
        os.path.join(CURRENT_DIR, folder_name, script_name)
    ]

    for p in paths_to_try:
        if os.path.exists(p):
            return p
    return None

def run_script(script_path, args_list):
    if not script_path:
        print("[-] Chyba: Cílový skript nebyl nalezen! Zkontroluj strukturu složek.")
        return
    
    cmd = [sys.executable, script_path] + args_list
    print(f"[*] Spouštím: {' '.join(cmd)}\n")
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n[!] Operace přerušena.")

def interactive_menu():
    print("=" * 60)
    print("        RECON FRAMEWORK - INTERAKTIVNÍ ROZHRANÍ")
    print("=" * 60)
    print("1) Port Scanner (fast_scanner)")
    print("2) Banner Grabber (banner_grabber)")
    print("3) HTTP Directory Scanner (http_directory)")
    print("4) Ukončit")
    print("-" * 60)

    choice = input("Zvol možnost (1-4): ").strip()

    if choice == "1":
        target = input("Zadej cílovou IP / doménu: ").strip()
        ports = input("Zadej rozsah portů (např. 1-1024 nebo stiskni Enter): ").strip()
        args = ["-t", target]
        if ports:
            args.extend(["-p", ports])
        script = find_script("fast_scanner.py", "port scanner")
        run_script(script, args)

    elif choice == "2":
        target = input("Zadej cílovou IP / doménu: ").strip()
        port = input("Zadej port (výchozí 80): ").strip() or "80"
        script = find_script("banner_grabber.py", "banner grabber")
        run_script(script, ["-t", target, "-p", port])

    elif choice == "3":
        url = input("Zadej cílovou URL (např. seznam.cz): ").strip()
        wordlist = input("Zadej cestu k wordlistu: ").strip()
        exts = input("Přípony (např. php,html nebo stiskni Enter): ").strip()
        args = ["-u", url, "-w", wordlist]
        if exts:
            args.extend(["-x", exts])
        script = find_script("http_directory.py", "http directory")
        run_script(script, args)

    elif choice == "4":
        sys.exit()

def main():
    parser = argparse.ArgumentParser(description="Recon Framework CLI Orchestrator")
    subparsers = parser.add_subparsers(dest="mode", help="Dostupné moduly")

    p_ports = subparsers.add_parser("ports", help="Skenování portů")
    p_ports.add_argument("-t", "--target", required=True, help="Cílová IP / doména")
    p_ports.add_argument("-p", "--ports", help="Rozsah portů")

   
    p_banner = subparsers.add_parser("banner", help="Vytažení HTTP/SSL banneru")
    p_banner.add_argument("-t", "--target", required=True, help="Cílová IP / doména")
    p_banner.add_argument("-p", "--port", type=int, default=80, help="Cílový port")

  
    p_dir = subparsers.add_parser("dir", help="Enumerace HTTP adresářů")
    p_dir.add_argument("-u", "--url", required=True, help="Cílová URL")
    p_dir.add_argument("-w", "--wordlist", required=True, help="Cesta k wordlistu")
    p_dir.add_argument("-x", "--extensions", help="Přípony oddělené čárkou")

    args = parser.parse_args()

    if not args.mode:
        interactive_menu()
    elif args.mode == "ports":
        cmd_args = ["-t", args.target]
        if args.ports:
            cmd_args.extend(["-p", args.ports])
        script = find_script("fast_scanner.py", "port scanner")
        run_script(script, cmd_args)
    elif args.mode == "banner":
        script = find_script("banner_grabber.py", "banner grabber")
        run_script(script, ["-t", args.target, "-p", str(args.port)])
    elif args.mode == "dir":
        cmd_args = ["-u", args.url, "-w", args.wordlist]
        if args.extensions:
            cmd_args.extend(["-x", args.extensions])
        script = find_script("http_directory.py", "http directory")
        run_script(script, cmd_args)

if __name__ == "__main__":
    main()
