import click
import os
import sys


@click.command()
@click.argument('payload')
def launch(payload):
    payload = str(payload)
    if payload.lower() == 'word':
        os.system(
            'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE')
    elif payload.lower() == 'excel':
        os.system(
            'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE')
    else:
        click.echo(' ')
        click.echo('Ion Launch - Argument not recognized: ', payload, '.')
        click.echo('Please check your spelling and try again.')
        click.echo(' ')
        sys.exit('SYS.EXIT (1) - Unknown Ion Launch argument given.')
