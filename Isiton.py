import requests
import re

print("============================================================")
print("+                       I S I T O N ?                     +")
print("============================================================")

def checaPonto(site):
    if site.count(".") > 0:
        return True
    else:
        return False


def formataSite(site):
    if re.match(r'http', site):
        return site
    else:
        return "https://" + site


sites = input("Insira os domínios que deseja testar, separados por vírgula: ")
lista = sites.split(",")

for site in lista:
    site = site.strip().lower()
    if checaPonto(site):
        site_formatado = formataSite(site)
        try:
            teste = requests.get(site_formatado)
            print(f"O site {site_formatado} está online.")

        except Exception:
            print(f"O site {site_formatado} está offline.")

    else:
        print("Não é uma URL válida!")
