import sys

# declare variables
# command (text input)
# keyword (the function to call)
# parsedCommand (list) 
# arguments (everything after the first word in the command) 
# scriptFile (arg on cmdline)
# lines (a list that stores all the lines)
# lineNumber (the line we are on)

command = ""
keyword = ""
parsedCommand = []
arguments = ""
scriptFile = open(sys.argv[1])
lines = scriptFile.read()
lines = lines.splitlines()
lineNumber = 0
stackMemory = {}

# fetch new command
def newCommand():
    global command, lineNumber
    command = lines[lineNumber]
    lineNumber += 1

# split command into bits
def interpret():
    global arguments, keyword, parsedCommand
    parsedCommand = command.split()
    keyword = parsedCommand[0]
    parsedCommand.pop(0)
    arguments = parsedCommand.copy()

def outFunc(text):
    if " ".join(text) not in stackMemory:
        print(" ".join(text))
    else:
        print(stackMemory[" ".join(text)])

def inFunc(varName, content):
    global stackMemory
    stackMemory[varName] = content

def declareFunc(varName, content):
    global stackMemory
    stackMemory[varName] = content

def main():
    while lineNumber < len(lines):
        newCommand()
        interpret()

        match keyword:
            case "out":
                outFunc(arguments)
            case "in":
                inFunc(arguments[0], input())
            case "declare":
                declareFunc(arguments[0], arguments[1])

main()