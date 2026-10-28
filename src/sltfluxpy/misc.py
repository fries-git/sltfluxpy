from rich.console import Console
from rich.markdown import Markdown
import requests

def github():
    return("><> Come support and fork the project at: https://github.com/fries-git/sltfluxpy <><")

def readme():
    console = Console()
    with open("README.md") as readme:
        markdown = Markdown(readme.read())
    console.print(markdown)
    
def docs():
    console = Console()
    with open("DOCS.md") as readme:
        markdown = Markdown(readme.read())
    console.print(markdown)