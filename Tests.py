from M07L08 import transform_status_symbol, example_example, find_free_id, Todos, save_data, read_data

def test_transform_status_symbol_when_done():
    status_symbol = Todos(1,'test','x')
    got = transform_status_symbol(status_symbol)
    expected = 'done'

    assert got == expected

def test_transform_status_symbol_when_undone():
    status_symbol = Todos(1,'test','-')
    got = transform_status_symbol(status_symbol)
    expected = 'undone'

    assert got == expected

def test_transform_status_symbol_when_other_symbol():
    status_symbol = Todos(1,'test','wykonano')
    got = transform_status_symbol(status_symbol)
    expected = '???'

    assert got == expected

def test_example_example_true():
    example = True
    got = example_example(example)
    expected = [Todos(1, 'zadanie nr 1', 'x'), 
        Todos(2, 'zadanie nr 2', '-'), 
        Todos(3, 'zadanie nr 3', 'x')]
    
    assert got == expected

def test_example_example_false():
    example = False
    got = example_example(example)
    expected = ''
    
    assert got == expected

def test_find_free_id_other_task_exists():
    example = [Todos(1, 'zadanie nr 1', 'x'), 
        Todos(2, 'zadanie nr 2', '-'), 
        Todos(3, 'zadanie nr 3', 'x')]
    got = find_free_id(example)
    expected = 4

    assert got == expected

def test_find_free_id_not_id_order():
    example = [Todos(1, 'zadanie nr 1', 'x'), 
        Todos(3, 'zadanie nr 2', '-'), 
        Todos(4, 'zadanie nr 3', 'x')]
    got = find_free_id(example)
    expected = 2

    assert got == expected

def test_find_free_id_empty_set():
    example = []
    got = find_free_id(example)
    expected = 1

    assert got == expected

    
def test_persistence(tmpdir):
    with tmpdir.as_cwd():
        todos = [Todos(1, 'zadanie nr 1', 'x'), 
            Todos(3, 'zadanie nr 2', '-'), 
            Todos(4, 'zadanie nr 3', 'x')]
        save_data(todos)
        got = read_data()
    assert got == todos