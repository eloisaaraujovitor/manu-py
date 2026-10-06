from colorama import init, Fore, Back

# Reseta a cor automaticamente após cada print()
init(autoreset=True)

print(Fore.RED + 'Eloisa!')
print('Este texto já volta para a cor normal automaticamente!')
print(Back.GREEN + Fore.WHITE + 'Eloisa Araujo!')