# Tiny08Assembler
An assembler for the Tiny08 CPU Architecture used to teach Computer Architecture and Assembly/Machine Code Programming at Eastern Michigan University.

Please note that this is a Work-In-Progress project, and that the assembler is not complete and functional at this time.

## Repository
The root directory for this repository contains the following files:
* Tiny08 - Directory containing the Tiny08 Python Package
* LICENSE - MIT License
* README.md - This file
* Tiny08CPU.circ - Logisim circuit file of the Tiny08 CPU

## Dependancies
The Tiny08 CPU requires for the following dependancies to be installed:
* Python 3.5 or greater
* Logisim (if you would like to run and test your output machine code)

## Tiny08 ISA
The ISA for the Tiny08 CPU is very minimal, with only one general purpose register and only a total of 16 bytes of RAM.

### Operations
The Tiny08 CPU can perform a total of eight unique operations, with support for sequencial, iterative, and conditional programming structures.

The following operations, their respective assembly instructions, and their respective opcodes are defined:
* Addition (``ADD``) - Opcode ``0x0``
* Bitwise AND (``AND``) - Opcode ``0x1``
* Bitwise Left Shift (``SHL``) - Opcode ``0x2``
* Load Value From Memory (``LOAD``) - Opcode ``0x3``
* Store Value From Register (``STR``) - Opcode ``0x4``
* Display Contents of a Memory Location (``DISP``) - Opcode ``0x5``
* Unconditional Jump (``JMP``) - Opcode ``0x6``
* Conditional Jump (if previous result was zero) (``JZ``) - Opcode ``0x7``

### General Purpose Registers
The Tiny08 CPU contains one general purpose register available for the programmer to use: register ``D0``. Instructions that operate with register data, such as the ``LOAD``, ``STR``, and ``ADD`` instructions utilize the contents stored in register D0.

### Memory and Memory Access
The Tiny08 CPU contains a total of 16 bytes of RAM, for a total of 16 different memory locations, each holding eight bits. The Tiny08 ``LOAD`` and ``STR`` instructions utilize direct memory access. That is, the parameter supplied to the ``LOAD`` and ``STR`` instructions correspond to an exact location in memory. As an example: the instruction ``LOAD 0xf`` will load the contents of memory location ``0xf`` into the internal register D0.

### CPU Flags
The Tiny08 CPU contains one internal flag, which is the zero flag. This one bit flag is set to a value of 1 if the result of the previously executed instruction was zero. The value of this flag determines the execution of a conditional jump operation (``JZ``). If the zero flag is set to zero at the time of a ``JZ`` instruction being executed, the Program Counter will be set to the value set by the parameter of the ``JZ`` instruction, and will therefore "jump" to said memory location.

### Functional Completedness
The Tiny08 Instruction Set contains only one boolean operator (``AND``). Because of the lack of many fundamental boolean operations such as ``NOT``, ``OR``, ``NOR``, or ``NAND``, as well as the very small ammount of memory space, the Tiny08 CPU is not functionally complete.

## The Assembler
### Loading programs onto the Tiny08 CPU
Your assembly program is converted into a Logisim Memory File. This file can be loaded directly into the Tiny08 CPU's RAM module, and from there you can run your program. When compiling a Tiny08 assembly file, the output Memory File is stored as the original assembly file's name, but with the ``.m`` extension by default. There is also the option to define your output machine code's name/extension explicitly if desired.

### Preprocessor Directives
This assembler utilizes a preprocessor to allow for variable declarations, as well as expressing memory locations in the form of a hexadecimal or integer value.

#### .FILL
The ``.FILL`` directive instructs the preprocessor to define a variable with an initial value. Variables declared in this syntax can be used anywhere in your program by name. As an example, a line containing ``x .FILL 10`` will define a variable ``x`` within your program, which has an initial value of ``10``. The preprocessor determines an available memory location to where this variable will be stored. The memory location for a variable is determined *after* all other instructions are given a location in memory.

#### .END
The ``.END`` directive declares the end of a user program, and the beginning of the "data" section of the assembly program, where variables are declared. The data section of a program can be empty, where the ``.END`` directive is the last line of a program. This means that the program would not contain any variable declarations, and that all parameters are exact hexadecimal/integer values corresponding to an exact memory location.
