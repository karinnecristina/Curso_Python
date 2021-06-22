'''Faça uma lista de tarefas com as seguintes opções:
   - Adicionar tarefa 
   - Listar tarefas
   - Desfazer (desfaz a última ação)
   - Refazer (refaz a última tarefa)
'''

def show_op(todo_list):
    '''Visualizar tarefas'''
    print()
    print('Tarefas: ')
    print(f'{todo_list}\n')
    
def do_undo(todo_list,redo_list):
    '''Desfazer a lista'''
    if not todo_list:
        print(f'Nada a desfazer\n')
        return
    
    last_todo = todo_list.pop()
    redo_list.append(last_todo)
    
def do_redo(todo_list,redo_list):
    if not redo_list:
        print(f'Nada a refazer\n')
        return
    
    last_redo = redo_list.pop()
    todo_list.append(last_redo)
    
def do_add(todo, todo_list):
    '''Adicionar tarefa'''
    todo_list.append(todo)
    
if __name__ == '__main__':
    todo_list = []
    redo_list = []
    
    while True:
        todo = input(f'Digite uma tarefa ou refazer ,desfazer ,listar: ')
        if todo == 'listar':
            show_op(todo_list)
            continue
        elif todo == 'refazer':
            do_undo(todo_list,redo_list)
            continue
        elif todo == 'desfazer':
            do_redo(todo_list,redo_list)
            continue
    
        do_add(todo,todo_list)
        
    
    