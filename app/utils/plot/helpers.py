import itertools


def get_unique_style(index: int) -> tuple[str, str, str]:
    line_styles = ['-', '--', '-.', ':']
    markers = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p',
               '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_']
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    combinations = list(itertools.product(markers, line_styles, colors))
    return combinations[index % len(combinations)]
