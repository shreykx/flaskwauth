import os

def GetVariable(name):
    try:
        return os.environ[name]
    except KeyError:
        return f'Environment variable {name} not found'

# Example usage
print(GetVariable('PORT'))
