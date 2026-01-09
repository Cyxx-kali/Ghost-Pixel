# Developed by Cyxx
import sys
import os
import click
from stegano import lsb
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def print_banner():
    """Prints the GHOST-PIXEL banner."""
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}
   ______  __  ______  __________    ____  _______  _______    __ 
  / ____/ / / / / __ \\/ ___/_  _/   / __ \\/  _/   |/  / __/   / / 
 / / __  / /_/ / / / /\\__ \\ / /    / /_/ // / |   /  / _/    / /  
/ /_/ / / __  / /_/ /___/ // /    / ____// / /   |  / /___  / /___
\\____/ /_/ /_/\\____//____//_/    /_/   /___//_/|_/ /_____/ /_____/
                                                                  
{Fore.MAGENTA}          GHOST-PIXEL | Made by Cyxx
{Style.RESET_ALL}
"""
    click.echo(banner)

@click.group()
def cli():
    """Ghost-Pixel: A CLI Steganography Tool."""
    print_banner()

@cli.command()
@click.option('--image', '-i', required=True, type=click.Path(exists=True), help='Path to the carrier image (PNG).')
@click.option('--message', '-m', required=True, help='The secret message to hide.')
@click.option('--output', '-o', default='secret.png', help='Output filename for the hidden image.')
def hide(image, message, output):
    """Hide a secret message inside an image."""
    try:
        click.echo(f"{Fore.YELLOW}[*] Hiding message in {image}...")
        secret = lsb.hide(image, message)
        secret.save(output)
        click.echo(f"{Fore.GREEN}[+] Message hidden successfully! Output saved to: {output}")
    except Exception as e:
        click.echo(f"{Fore.RED}[!] Error: {str(e)}")

@cli.command()
@click.option('--image', '-i', required=True, type=click.Path(exists=True), help='Path to the image containing the hidden message.')
def reveal(image):
    """Reveal the hidden message from an image."""
    try:
        click.echo(f"{Fore.YELLOW}[*] Attempting to reveal message from {image}...")
        clear_message = lsb.reveal(image)
        if clear_message:
            click.echo(f"{Fore.GREEN}[+] Hidden Message: {Fore.WHITE}{clear_message}")
        else:
            click.echo(f"{Fore.RED}[!] No hidden message found.")
    except Exception as e:
        click.echo(f"{Fore.RED}[!] Error: {str(e)}")

if __name__ == '__main__':
    cli()
