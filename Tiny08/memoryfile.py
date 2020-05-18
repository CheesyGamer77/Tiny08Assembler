class MemoryFile:
    """
    A class for interfacing with Logisim Memory files

    Memory files are where hexadecimal data for logisim ROM/RAM modules are stored.
    In this case, memory files are where the machine code for our Tiny08 Assembly programs
    are stored.

    Memory Files in logisim are a little goofy.
    For starters, when a memory file is saved, it includes a version header that I'm guessing
    displays the version format number. The current version is 2.0. In general, when you
    try to examine the contents of a memory file via this class, this header will NOT be included in the
    contents returned by MemoryFile.contents or MemoryFile.raw_contents.

    Another quirk relating to memory files is that consecutive memory cells of the same value are denoted
    with the following format:
        x*y - (denotes a total of x consecutive number of memory locations with the value y)
    In MemoryFile.raw_contents(), this format is preserved, whereas in MemoryFile.contents() these files are extracted
    into x consecutive array values of y.

    Finally, logisim memory files include no extension to the file by default. Despite
    being saved with no extension by default, these files can be opened in notepad just
    like any ordinary text file. With these files being saved without any extension by default,
    it is good practice to save all logisim memory files with the ".m" extension, and this is
    how memory files will be stored in this assembler.
    """

    def __init__(self, fp: str):
        self.path = fp

    @property
    def contents(self) -> list:
        """
        Returns a list containing the contents of a memory file

        :return: A list of strings representing the hexadecimal values found
                in the memory file
        """

        contents = []

        with open(self.path, "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()

            if line == "v2.0 raw":
                continue
            else:
                line = line.split(" ")

                for val in line:
                    if "*" in val:
                        # denotes multiple memory locations with the same value
                        count, value = val.split("*")
                        for i in range(int(count)):
                            if len(value) == 1:
                                contents.append(f"0{value}")
                            else:
                                contents.append(value)
                    else:
                        if len(val) == 1:
                            contents.append(f"0{val}")
                        else:
                            contents.append(val)

        return contents

    @property
    def raw_contents(self) -> list:
        """
        Returns a list of strings representing the raw contents of a memory
        file. Values such as "5*0", which in this case denotes 5 consecutive memory cells
        with the value of 0x00, will NOT be extracted into their proper form. In this example,
        the value "5*0" will not be converted to 5 consecutive locations in the array who's value
        is 0.

        One thing that will be changed however is that single hex digit values will have a leading 0 placed
        to the left of the digit.

        Memory files contain a header displaying the memory file version
        (the current version is 2.0). This header is displayed as "v2.0 raw".
        This header will not be included in the list of raw contents

        :return: A list of strings containing the raw contents of the memory file
        """

        raw_contents = []

        with open(self.path, "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()

            if line == "v2.0 raw":
                continue
            else:
                line = line.split(" ")

                for val in line:
                    if len(val) == 1:
                        raw_contents.append(f"0{val}")
                    else:
                        raw_contents.append(val)

        return raw_contents


if __name__ == "__main__":
    file = MemoryFile("C:/Users/User1/Desktop/Temp/TestFile.m")
    print(file.raw_contents)
    print(file.contents)
