from typing import Optional

# abstract class
class Formatter:
    def format(self, string: str) -> None:
        pass

# class definition into a function
def format_string(string: str, formatter: Optional[Formatter] = None) -> str:
    """
    Format a string using the formatter object, which
    is expected to have a format() method that accepts
    a string.
    """
    class DefaultFormatter(Formatter):
        """Format a string in title case."""
        def format(self, string: str) -> str:
            return str(string).title()
        
    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)

def main():
    hello = "hello world, how are you today?"
    print(f" input: {hello}")
    print(f" output: {format_string(hello)}")

if __name__ == "__main__":
    main()
