import winreg
import subprocess
import sys
import os

try:
    import questionary
except ImportError:
    print("\033[91mPor favor, instala questionary primero ejecutando: pip install questionary\033[0m")
    sys.exit(1)

CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def get_installed_programs():
    registry_paths = [
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),
        (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
    ]

    programs = {}
    for root_key, path in registry_paths:
        try:
            key = winreg.OpenKey(root_key, path)
        except FileNotFoundError:
            continue

        for i in range(winreg.QueryInfoKey(key)[0]):
            try:
                subkey_name = winreg.EnumKey(key, i)
                subkey = winreg.OpenKey(key, subkey_name)
                
                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                uninstall_string = winreg.QueryValueEx(subkey, "UninstallString")[0]
                
                if display_name and uninstall_string:
                    programs[display_name.strip()] = uninstall_string
            except OSError:
                pass
    return programs

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    if os.name == 'nt':
        os.system('color')
    
    banner = f"""{CYAN}
  _____ ____      _    ____ __   ___    ____   ___  ____  
 |_   _|  _ \\    / \\  |  _ \\\\ \\ / / \\  |  _ \\ / _ \\|  _ \\ 
   | | | |_) |  / _ \\ | |_) |\\ V / _ \\ | | | | | | | |_) |
   | | |  _ <  / ___ \\|  __/  | | ___ \\| |_| | |_| |  _ < 
   |_| |_| \\_\\/_/   \\_\\_|     |_/_/   \\_\\____/ \\___/|_| \\_\\
    {RESET}"""
    print(banner)
    
    print(f"{YELLOW}Escaneando el registro en busca de programas instalados...{RESET}\n")
    programs = get_installed_programs()
    
    if not programs:
        print(f"{RED}No se encontraron programas o no se pudo leer el registro. ¿Estás en Windows?{RESET}")
        return

    program_names = sorted(programs.keys())

    selected_programs = questionary.checkbox(
        "Usa las flechas ARRIBA/ABAJO para navegar. Presiona ESPACIO para seleccionar. Presiona ENTER para confirmar:",
        choices=program_names
    ).ask()

    if not selected_programs:
        print(f"\n{YELLOW}Ningún programa seleccionado. Saliendo de forma segura.{RESET}")
        return

    print(f"\n{GREEN}Has seleccionado {len(selected_programs)} programa(s) para desinstalar.{RESET}")
    
    confirm = questionary.confirm("¿Estás seguro de que deseas continuar? Los desinstaladores se iniciarán ahora.").ask()

    if not confirm:
        print(f"\n{YELLOW}Operación cancelada.{RESET}")
        return

    for name in selected_programs:
        uninstall_cmd = programs[name]
        print(f"\n{CYAN}{'-'*40}{RESET}")
        print(f"{YELLOW}Desinstalando:{RESET} {name}")
        print(f"{YELLOW}Comando:{RESET} {uninstall_cmd}")
        
        if "msiexec" in uninstall_cmd.lower() and "/I" in uninstall_cmd:
            uninstall_cmd = uninstall_cmd.replace("/I", "/X")
        
        try:
            subprocess.run(uninstall_cmd, shell=True)
            print(f"{GREEN}Proceso de desinstalación finalizado para {name}.{RESET}")
        except Exception as e:
            print(f"{RED}Error al iniciar el desinstalador para {name}: {e}{RESET}")

    print(f"\n{CYAN}{'-'*40}{RESET}\n{GREEN}Proceso de desinstalación masiva completado.{RESET}")

if __name__ == "__main__":
    main()