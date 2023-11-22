# AirBnB Clone - Command Interpreter

## Description

This project encompasses the initial and subsequent stages of the AirBnB clone, focusing on constructing a command interpreter to manage AirBnB objects. It acts as the foundational element for the entire AirBnB web application, including HTML/CSS templating, database storage, API, and front-end integration.

## Command Interpreter

The command interpreter serves as a command-line interface enabling interaction with AirBnB objects, allowing various operations like creation, update, deletion, and listing of objects. It's an essential tool for managing different classes utilized in AirBnB, such as User, State, City, Place, among others.

## Getting Started

### Installation

1. Clone the project repository to your local machine:
   `git clone https://github.com/yourusername/AirBnB_clone.git`

2. Change your working directory to the project folder:
   `cd AirBnB_clone`

3. Run the command interpreter:
   `./console.py`

## Using the Command Interpreter

Once the command interpreter is active, interact with it by entering commands and respective arguments. Below are some fundamental commands and their usage:

- **Create an object:**
  `create <classname> <param1>=<value1> <param2>=<value2> ...`

- **Show an object:**
  `show <classname> <object_id>`

- **Exit the interpreter:**
  `quit`

For more detailed instructions and commands, use the `help` command within the interpreter.

## Examples

Here are some examples demonstrating the usage of the command interpreter:

1. Creating a new User:
   `create User first_name="amin" last_name="omari"`

2. Listing all City objects:
   `all City`

Additionally, this project includes setting up a MySQL server
