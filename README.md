# The organizer #
## *Add and view to-do tasks* ##

### List of contents: ###
1. Description of how the code works
2. Available functionalities
3. Used Python modules

![Picture](https://images2.minutemediacdn.com/image/upload/c_fill,w_1080,ar_16:9,f_auto,q_auto,g_auto/shape%2Fcover%2Fsport%2F94735-istock-863607936-b27c422700db46a2d9b0c224305663d6.jpg)

### 1. Description of how the code works ###

The program is used to construct a list of tasks to be performed and present a summary of the implemented tasks. It displays the task name, and execution status, and also generates the first free index for a new sentence. The Todos class has been prepared, which stores indexes, descriptions, and the status of task execution.

It has several optional parameters (see more: 2. Available functionalities). The available options have been built using the click module. 

A set of unit tests has also been prepared for the program in the Tests.py file.

### 2. Available functionalities ###

**Feature List:**
- init 

It is used to create a new database (todos.db file). It has a special argument --example, in which if given, a sample list of tasks is added to the created database. 
**ATTENTION!** Automatically the todos.db file is not overwritten, you can change this functionality with the options parameter.

- list

Selecting this option display the task list in the todos.db file in the console.

- add

It allows you to add a new task to the todos.db file. The user is obliged to provide the name of the new task (otherwise, ValueError will be raised). By default: the status of a newly added task is unknown, and the index will be generated automatically.

### 3. Used Python modules ###
- dataclasses
- pickle
- click
- pytest (tests)

**Author:** Marta Solarz
