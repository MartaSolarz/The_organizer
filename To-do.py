from dataclasses import dataclass
import pickle

import click

FILENAME = r'todos.db'

@dataclass
class Todos:
    id_: int
    desc: str
    done: str

    def __post_init__(self):
        if not self.desc:
            raise ValueError('Description cannot be empty')


def save_data(content:list[Todos], option:bool=True) -> None:
    if option:
        mode = 'wb'
    else:
        mode = 'xb'
    
    with open(FILENAME, mode) as stream:
        pickle.dump(content, stream)


def read_data() -> Todos:
    try:
        with open(FILENAME, 'rb') as stream:
            content = pickle.load(stream)
    except FileNotFoundError:
        content = ''
            
    return content

def transform_status_symbol(element:Todos) -> str:
    if element.done == 'x':
        element.done = 'done'
    elif element.done == '-':
        element.done = 'undone'
    else:
        element.done = '???'

    return element.done


def example_example(example) -> str:
    if example:
        add_example = [Todos(1, 'zadanie nr 1', 'x'), 
        Todos(2, 'zadanie nr 2', '-'), 
        Todos(3, 'zadanie nr 3', 'x')]
    else:
        add_example = ''
    
    return add_example


def find_free_id(elements:list[Todos]) -> int:
    used_id = {el.id_ for el in elements}

    id_ = 1
    while id_ in used_id:
        id_ += 1

    return id_


def create_new_todo(todos:list[Todos], new_task:str) -> list[Todos]:
    new_id = find_free_id(todos)
    todo = Todos(new_id, new_task, 'undone')
    todos.append(todo)

    return todos


def headline() -> None:
    print()
    print('ID | STATUS | TASK DESCRIPTION')
    print('-------------------------------')


def print_table(element:Todos) -> None:
    element.done = transform_status_symbol(element)
    print(f'{element.id_:2} | {element.done.rjust(6)} | {element.desc}')


@click.group()
def cli():
    pass


@cli.command()
@click.option('--example', is_flag=True)
def init(example):
    add_example = example_example(example)
    save_data(add_example)


@cli.command()
def list():
    todos = read_data()
    headline()
    for todo in todos:
        print_table(todo)


@cli.command()
@click.argument('new_task')
def add(new_task):
    todos = read_data()

    if todos == '':
        todos = []

    try:
        todos = create_new_todo(todos, new_task)
    except ValueError as v:
        print(f'ERROR: {v.args[0]}')

    save_data(todos)


if __name__ == '__main__':
    cli()
