from rich import print

def error(input):
    print(f"[red][ERROR] [/red][bold red]{input}[/bold red]!")
def success(input):
    print(f"[green][SUCCESS] [/green][bold green]{input}[/bold green]!")