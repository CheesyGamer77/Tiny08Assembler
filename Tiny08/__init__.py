"""
Tiny08Assembler - An assembler for the Tiny08 Assembly Language

:copyright: (c) 2020 CheesyGamer77
:license:
    The MIT License:
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.


The Tiny08 Assembly Language is used in Eastern Michigan University to
teach the basics of programming in an assembly language.

The Tiny08 CPU itself is simulated within Logisim, and programs are loaded through
"memory files" that are loaded into the Tiny08 CPU RAM component. Because of
this, compiled Tiny08 Machine Code is saved with the ".m" extension.

Valid Tiny08 Assembly Instructions and their Machine Code counterparts include:
    ADD x - 0x (Adds the value in register D0 with the value at memory location x
    AND x - 1x (Executes a bitwise AND operation in the D0 register (D0 = D0 & x)
    SHL x - 2x (Executes a left shift operation at memory location x)
    LOAD x - 3x (Loads the value at memory location x into the D0 register)
    STR x - 4x (Stores the value in register D0 into memory location x)
    DISP x - 5x (Displays the value at memory location x)
    JMP x - 6x (Moves the program counter to memory location x)
    JZ x - 7x (Moves the program counter to memory location x if the previous arithmetic operation
            resulted in a 0)
"""

__title__ = "Tiny08Assembler"
__author__ = "CheesyGamer77"
__license__ = "MIT"
__copyright__ = "Copyright 2020 CheesyGamer77"
__version__ = "1.0"

from .assembler import Assembler
from .memoryfile import MemoryFile
