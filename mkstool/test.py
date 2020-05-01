import click

@click.command()
@click.option('-t', '--to', 'to', help='To who')
def greeting(to):
    '''Say hello to someone'''
    print(f'Hello, {to or "stranger"}!')


if __name__ == '__main__':
    greeting()