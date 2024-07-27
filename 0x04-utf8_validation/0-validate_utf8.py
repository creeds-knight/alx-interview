#!/usr/bin/python3
"""
    A method that determined if a given data set represents a valid UTF-8
    encoding:
        - Returns true if data is a valid UTF-8 encoding else False
        - A character in UTF-8 can be 1-4 bytes long
        - The dataset can contain multiple characters
        - The dataset will be represented as a list of integers
        - Each integer represents 1byte of data, only 8 least significant
          bits of each integer are needed
"""


def validUTF8(data):
    """
        Returns true or false if data is UTF-8 encoded
    """

    def helper(byte):
        """
            This method takes in a byte and checks if a byte is a byte
            is a continuation byte
        """
        return (byte & 0xC0) == 0x80

    number_of_bytes = 0

    for byte in data:
        if number_of_bytes == 0:
            # Determine the number of bytes in this character
            if (byte & 0x80) == 0x00:
                # 1-byte character
                number_of_bytes = 0
            elif (byte & 0xE0) == 0xC0:
                # 2-byte character
                number_of_bytes = 1
            elif (byte & 0xF0) == 0xE0:
                # 3-byte character
                number_of_bytes = 2
            elif (byte & 0xF8) == 0xF0:
                # 4-byte character
                number_of_bytes = 3
            else:
                return False
        else:
            if not helper(byte):
                return False
            number_of_bytes -= 1
    return number_of_bytes == 0
