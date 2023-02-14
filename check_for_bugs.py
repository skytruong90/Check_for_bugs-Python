import pylint.lint

def check_for_bugs(filename):
    # Configure pylint to produce output in the desired format
    pylint_opts = ['--output-format=text']
    pylint.lint.Run([filename] + pylint_opts)

# Example usage: check the bugs in a file named 'example.py'
check_for_bugs('example.py')
