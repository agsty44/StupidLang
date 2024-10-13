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

def ifFunc(var1, comparator, var2):
    global lineNumber
    match comparator:
        case "=":
            if not var1 == var2:
                # we increase the iterator to skip through the code
                lineNumber = lines.index("end", lineNumber) + 1

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
            case "if":
                ifFunc(stackMemory[arguments[0]], arguments[1], stackMemory[arguments[2]])

main()