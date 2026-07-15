## Warehouse Robot Command Parser

A Python project that uses **Natural Language Toolkit (NLTK)** and **Context-Free Grammar (CFG)** to validate warehouse robot commands before execution.

### Project Overview

This project simulates a command validation system for warehouse robots used in logistics operations. A Context-Free Grammar (CFG) is designed to ensure that only correctly structured commands are accepted, helping reduce command ambiguity and improve operational safety.

The parser validates commands such as:

* `pick item_45 from shelf_A ;`
* `move item_45 to packing_station ;`
* `deliver package_12 to dispatch_area ;`
* `return robot_2 to charging_station ;`
* `inspect shelf_A ;`

Invalid or ambiguous commands are rejected.

### Features

* Context-Free Grammar (CFG) for warehouse commands
* Python implementation using NLTK
* Validates robot instructions before execution
* Generates parse trees for valid commands
* Detects invalid or ambiguous command structures
* Demonstrates command parsing for warehouse automation

### Technologies Used

* Python 3
* NLTK (Natural Language Toolkit)

### Project Structure

```text
WarehouseRobotParser/
│
├── warehouse_parser.py
├── README.md
└── screenshots/
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/WarehouseRobotParser.git
```

2. Navigate to the project folder:

```bash
cd WarehouseRobotParser
```

3. Install the required package:

```bash
pip install nltk
```

### Usage

Run the parser:

```bash
python warehouse_parser.py
```

The program validates each warehouse command and displays whether it is **VALID** or **INVALID**. For valid commands, it also generates a parse tree illustrating the grammatical structure.

### Example Commands

**Valid**

```text
pick item_45 from shelf_A ;
move item_45 to packing_station ;
deliver package_12 to dispatch_area ;
return robot_2 to charging_station ;
inspect shelf_A ;
```

**Invalid**

```text
pick from shelf_A item_45 ;
move packing_station item_45 ;
```

### Learning Objectives

This project demonstrates:

* Context-Free Grammar (CFG) design
* Natural Language Processing with NLTK
* Command validation
* Parse tree generation
* Formal language concepts
* Industrial automation applications

### License

This project is intended for educational purposes.
