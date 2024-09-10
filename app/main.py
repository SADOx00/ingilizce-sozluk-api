import questionary
from rich import box
from rich.console import Console
from rich.table import Table
from termcolor import colored

from connection import Manage
while True:
    console = Console()

    answer = questionary.text("Hangi Kelimeyi İstiyorsunuz ?").ask()

    res = Manage(answer.strip())

    if not res.rslt():
        print(colored("HATALI KELİME LÜTFEN TEKRAR DENEYİNİZ.",color="red"))
    else:
        table = Table(title=colored(f"{answer} kelimesinin anlamları:", color="green", on_color="on_black",
                                    attrs=["bold", "underline"]), box=box.DOUBLE_EDGE)
        table.add_column("ID", style="red")
        table.add_column("EN kelime", style="blue")
        table.add_column("TR anlamları", style="magenta")

        for idx, i in enumerate(res.get_10_meanings()):
            table.add_row(str(idx + 1), str(answer).upper(), i.upper())
        console.print(table)

        table = Table(title=colored(f"{answer} kelimesinin cümleleri:", color="green", on_color="on_black",
                                    attrs=["bold", "underline"]), box=box.DOUBLE_EDGE)
        table.add_column("ID", style="red")
        table.add_column("EN cümle", style="blue")
        table.add_column("TR cümle", style="magenta")

        for idx, i in enumerate(res.get_sentences()):
            i = i.split("\n")
            table.add_row(str(idx + 1), f"{i[0].upper()}\n", f"{i[1].upper()}\n")

        console.print(table)

"""
𝓢4𝓓0 𝓟4𝓢𝓗4
FULLSTACK DEVELOPER
DATE: SEPTEMBER 10 2024
GİTHUB: https://github.com/SADOx00
"""
