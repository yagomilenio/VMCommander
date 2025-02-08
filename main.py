import argparse
import json
from tabulate import tabulate

# Archivo para guardar configuraciones
CONFIG_FILE = "vms_config.json"

# Cargar configuraciones
def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Guardar configuraciones
def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

# Función para listar VMs
def list_vms():
    config = load_config()
    table = []
    for name, details in config.items():
        table.append([
            name,
            details.get("status", "Desconocido"),
            details.get("startup_action", "-"),
            details.get("shutdown_action", "-"),
            details.get("schedule", "-")
        ])
    print(tabulate(table, headers=["Nombre", "Estado", "Acciones Inicio", "Acciones Apagado", "Programado"], tablefmt="grid"))

# Funciones para las acciones principales
def start_vm(name):
    print(f"Iniciando VM: {name}")

def stop_vm(name):
    print(f"Deteniendo VM: {name}")

def pause_vm(name):
    print(f"Pausando VM: {name}")

def restart_vm(name):
    print(f"Reiniciando VM: {name}")

def schedule_vm(name, action, time):
    config = load_config()
    if name not in config:
        print(f"La máquina virtual '{name}' no está configurada.")
        return
    config[name]["schedule"] = f"{action} a las {time}"
    save_config(config)
    print(f"Acción programada: {action} en la VM '{name}' a las {time}.")

# Configurar acciones al inicio y apagado
def set_startup(name, action):
    config = load_config()
    if name not in config:
        print(f"La máquina virtual '{name}' no está configurada.")
        return
    config[name]["startup_action"] = action
    save_config(config)
    print(f"Acción '{action}' configurada para el inicio de la VM '{name}'.")

def set_shutdown(name, action):
    config = load_config()
    if name not in config:
        print(f"La máquina virtual '{name}' no está configurada.")
        return
    config[name]["shutdown_action"] = action
    save_config(config)
    print(f"Acción '{action}' configurada para el apagado de la VM '{name}'.")

# Main
def main():
    parser = argparse.ArgumentParser(description="Gestor de Máquinas Virtuales")
    subparsers = parser.add_subparsers(dest="command")

    # Comandos
    subparsers.add_parser("list-vms", help="Lista todas las máquinas virtuales configuradas")

    start_vm_parser = subparsers.add_parser("start-vm", help="Inicia una máquina virtual")
    start_vm_parser.add_argument("name", help="Nombre de la máquina virtual")

    stop_vm_parser = subparsers.add_parser("stop-vm", help="Detiene una máquina virtual")
    stop_vm_parser.add_argument("name", help="Nombre de la máquina virtual")

    pause_vm_parser = subparsers.add_parser("pause-vm", help="Pausa una máquina virtual")
    pause_vm_parser.add_argument("name", help="Nombre de la máquina virtual")

    restart_vm_parser = subparsers.add_parser("restart-vm", help="Reinicia una máquina virtual")
    restart_vm_parser.add_argument("name", help="Nombre de la máquina virtual")

    schedule_parser = subparsers.add_parser("schedule", help="Programa una acción para una máquina virtual")
    schedule_parser.add_argument("name", help="Nombre de la máquina virtual")
    schedule_parser.add_argument("action", choices=["start", "stop", "pause", "restart"], help="Acción a programar")
    schedule_parser.add_argument("time", help="Hora (formato HH:MM)")

    startup_parser = subparsers.add_parser("set-startup", help="Configura una acción al inicio del sistema")
    startup_parser.add_argument("name", help="Nombre de la máquina virtual")
    startup_parser.add_argument("action", choices=["start", "stop", "pause", "restart"], help="Acción al inicio")

    shutdown_parser = subparsers.add_parser("set-shutdown", help="Configura una acción al apagar el sistema")
    shutdown_parser.add_argument("name", help="Nombre de la máquina virtual")
    shutdown_parser.add_argument("action", choices=["start", "stop", "pause", "restart"], help="Acción al apagar")

    args = parser.parse_args()

    # Ejecutar comandos
    if args.command == "list-vms":
        list_vms()
    elif args.command == "start-vm":
        start_vm(args.name)
    elif args.command == "stop-vm":
        stop_vm(args.name)
    elif args.command == "pause-vm":
        pause_vm(args.name)
    elif args.command == "restart-vm":
        restart_vm(args.name)
    elif args.command == "schedule":
        schedule_vm(args.name, args.action, args.time)
    elif args.command == "set-startup":
        set_startup(args.name, args.action)
    elif args.command == "set-shutdown":
        set_shutdown(args.name, args.action)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
