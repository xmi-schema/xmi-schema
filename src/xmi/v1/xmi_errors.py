class XmiError(Exception):
    def __init__(self, message, error_code=None, problem_data=None):
        # Call the base class constructor
        super().__init__(message)

        # Store additional information
        self.error_code = error_code
        self.problem_data = problem_data
    """Raised when data consistency is violated."""

    def __str__(self):
        """Return a string representation of the exception."""
        base_msg = super().__str__()

        # Include error code in the message, if it is provided
        if self.error_code is not None:
            base_msg += f" (Error Code: {self.error_code})"

        # Include problematic data in the message, if it is provided
        if self.problem_data is not None:
            base_msg += f" (Problem Data: {self.problem_data})"

        return base_msg


class XmiInconsistentDataAttributeError(XmiError):
    pass
