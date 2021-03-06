# AirBnB CLONE

## Starting
Ubuntu LTS - Operating system reqd.

## Prerequisites

- Must have git installed
- Must have repository cloned

## Description of the project

Write a command interpreter to manage your AirBnB objects. This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

Each task is linked and they are the next:

- Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- Create all classes used for AirBnB (User, State, City, Place) that inherit from BaseModel
- Create the first abstracted storage engine of the project: File storage
- Create all unittests to validate all our classes and storage engine


### Coommand interpreter

Do you remember the Shell? Its exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place).
- Retrieve an object from a file, a database etc.
- Do operations on objects (count, compute stats, etc).
- Update attributes of an object.
- Destroy an object.


## Files and Directories

- ### models directory : 
This will contain all classes used for the entire project. A class, called **"model"**in a OOP project is the representation of an object/instance.
- ### tests: 
This directory will contain all unit tests.
- ### console.py:
This file is the entry point of our command interpreter.
- ### models/base_model.py 
This path file is the base class of all our models. It contains common elements:
 * **attributes:** id, created_at and updated_at
 * **methods:** save() and to_json()
- ### models/engine:
This directory will contain all storage classes (using the same prototype). For the moment you will have only one: 
 * **file_storage.py**


### Commands

| Commands| Description|
| ------ | ------ |
| all | Prints all string representation of all instances based or not on the class name |
| create | Creates a new instance of class name, saves it (to the JSON file) and prints the id |
| upadate| Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
| destroy | Deletes an instance based on the class name and id (save the change into the JSON file) |
| help| List available commands with "help" or detailed help with "help cmd" |
| quit| Quit command to exit the program |
| show | Prints the string representation of an instance based on the class name and id |
| EOF | EOF command to exit the program |

### Installation
Clone this repository in your terminal
```
$ sudo apt-get install git
```

## Execution
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

## Builded in

 * bash
 * VsCode


## Authors

 * **Juan Sebastian Ocampo** @darkares23  -(https://github.com/darkares23)
 * **Maribel Serna**  @maryserar89 -(https://github.com/MarySerna)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

 * Holberton School (providing guidance) 📢
