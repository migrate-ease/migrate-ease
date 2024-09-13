class NaiveCommentParser:

    """
    Naive comment parser.
    """

    def __init__(self):
        #  Are we in a multi-line comment?
        self.in_comment = False

    def parse_line(self, line):
        """
        Parse comments in a source line.

        Args:
            line (str): The line to parse.

        Returns:
            bool: Is this line a comment?
        """
        if line.lstrip().startswith('//'):
            return True

        if self.in_comment:
            if '*/' in line:
                self.in_comment = False
            return True
        else:
            if line.lstrip().startswith('/*'):
                if not '*/' in line:
                    self.in_comment = True
                    return True
                elif line.rstrip().rstrip('\\').endswith('*/'):
                    return True
        return False