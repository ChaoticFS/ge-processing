import requests
import json

def launch_settings(mode=None, set_type=None):
    def select_mode():
        modes = ("manual", "auto")
        mode = input(f"{modes}?: ")

        if mode.lower() in modes:
            return mode.lower()
        else:
            print("wrong mode input")
            select_mode()

    def select_set():
        sets = ("mapping", "latest", "5m", "1h")
        select_set = input(f"{sets}?: ")

        if select_set.lower() in sets:
            return select_set.lower()
        else:
            print("wrong set type input")
            select_set()

    if mode == None:
        mode = select_mode()
    if set_type == None:
        set_type = select_set()

    return (mode, set_type)



if __name__ == "__main__":
    settings = launch_settings() # List, index 0 = mode, index 1 = dataset
    url = f"https://prices.runescape.wiki/api/v1/osrs/{settings[1]}"
    headers = {"User-Agent": f"collecting data for portfolio project, {settings[0]} (Chaotic#1161)"}
    response = requests.get(url, headers=headers)


