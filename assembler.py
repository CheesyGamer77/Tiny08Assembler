class Assembler:
    """
    Represents an instance of a Tiny08Assembler.
    This is used to compile and assemble Tiny08 Assembly Code.

    The following parameters may be passed to the Assembler:
        - path: The desired path to save
    """

    def __init__(self, **kwargs):
        self.path = kwargs.get("path") if "path" in kwargs.keys() else None
        self.code = None

    def _compile(self, code: dict):
        """
        Compiles a dict containing both instructions and data for
        a Tiny08 Assembly program.

        This does the same shid as Assembler.compile_from_code except
        it never saves the resulting machine code into a file.

        :param code:
        :return:
        """

        instruction_index = {
            "ADD": 0,
            "AND": 1,
            "SHL": 2,
            "LOAD": 3,
            "STR": 4,
            "DISP": 5,
            "JMP": 6,
            "JZ": 7
        }

        out = [line for line in code["instructions"]]

        linenum = 0
        for line in out:
            linenum += 1
            line = line.strip().split(" ")

            # convert the instruction into the correct hex digit
            try:
                instruction = instruction_index[line[0]]
            except KeyError:
                # invalid instruction
                raise SyntaxError(f"Line {linenum}: Unknown instruction '{line[0]}'")

            # try to convert the parameter into a memory location (integer)
            # if the conversion fails, assume it's a variable
            try:
                if line[1] not in ["0xa", "0xb", "0xc", "0xd", "0xe", "0xf"]:
                    location = int(line[1])
                else:
                    location = line[1].replace("0x", "")
            except ValueError:
                # this is likely a variable name, check if the variable
                # exists in the data section of the input dict
                if line[1] not in code["data"].keys():
                    # variable does not exist, raise syntax error
                    raise SyntaxError(f"Line {linenum}: Unknown variable '{line[1]}'")
                else:
                    # variable found in the data section. replace the variable name in the
                    # current line in the output codes with the proper memory location
                    location = code["data"][line[1]]["location"].replace("0x", "")

                out[linenum-1] = f"{instruction}{location}"

        return out

    def compile_from_code(self, code: dict, outfile: str):
        """
        Compiles a dict containing both instructions and data for
        a Tiny08 Assembly program.

        The dict should be structured as the following:
            code {
                "instructions": list(str),

                "data": {
                    "var1": {
                        "value": val1,
                        "location": location1
                    },

                    "var2": {
                        "value": val2,
                        "location": location2
                    }
                    ...
                }
            }

        :param code: The dictionary of assembly code and
        :param outfile: Path to where the output mem file will be saved, if desired.
                Setting outfile to None will result in the out file not being saved,
                and only returning the list of codes
        :return: A list of strings containing the output machine code (in hex)
        """

        return self._compile(code)

    def compile_from_file(self, infile: str, outfile: str):
        """
        Compiles a Tiny08 Assembly file into Tiny08 machine code

        :param infile: Path to the Tiny08 Assembly file
        :param outfile: Path to where the output mem file will be saved, if desired.
                Setting outfile to None will result in the file not being saved,
                and only returning the list of codes
        :return: A list of strings containing the output machine code (in hex)
        """

        pass


if __name__ == "__main__":
    code = {
        "instructions": {
            "LOAD x",
            "ADD y",
            "STR z"
        },
        "data": {
            "x": {
                "value": 0,
                "location": "0xd"
            },
            "y": {
                "value": 0,
                "location": "0xe"
            },
            "z": {
                "value": 0,
                "location": "0xf"
            }
        }
    }
    assembler = Assembler()
    print(assembler.compile_from_code(code, ""))
