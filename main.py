import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--value', prompt='Enter the value to convert', type=float, help='Value to convert')
@click.option('--from-unit', prompt='From unit', help='Unit to convert from')
@click.option('--to-unit', prompt='To unit', help='Unit to convert to')
def convert(value, from_unit, to_unit):
    """Convert units of measurement"""
    conversion_factors = {
        # Length
        'meters': {'meters': 1, 'feet': 3.28084, 'inches': 39.3701},
        
        # Weight
        'kilograms': {'kilograms': 1, 'pounds': 2.20462, 'grams': 1000},
        
        # Volume
        'liters': {'liters': 1, 'gallons': 0.264172, 'milliliters': 1000}
    }

    if from_unit in conversion_factors and to_unit in conversion_factors:
        result = value * (conversion_factors[from_unit][to_unit])
        click.echo(f'{value} {from_unit} is equal to {result} {to_unit}')
    else:
        click.echo('Invalid unit conversion. Check your units.')

if __name__ == '__main__':
    cli()
