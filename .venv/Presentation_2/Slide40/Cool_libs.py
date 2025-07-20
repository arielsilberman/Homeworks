from rich.console import Console
from faker import Faker
import pyfiglet


console = Console()
console.print("[bold green] Hello, DevOps World![/bold green]")
console.print("[blue] Autmotating tasks is fun![/blue]")

fake = Faker()
console.print(f"Name: [yellow] {fake.name()} [/yellow]")
console.print(f"Email: [yellow] {fake.email()} [/yellow]")
console.print(f"Address: [yellow] {fake.address()} [/yellow]")

ascii_banner = pyfiglet.figlet_format("DevOps Rocks!")
print(ascii_banner)