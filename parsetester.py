import ParseTemplate
import ParseTests

def main():
    template = ParseTemplate.ParseTemplate("template.xml")
    tests = ParseTests.ParseTests("test.xml")
    for test in tests.getTests():
        createTestCommands(template.getTemplateDict(), test)
    
def createTestCommands(tmplDict, test):
    command = tmplDict["Program"] + " "
    for arg in test:    
        command += tmplDict[arg[0]] + arg[1] + " "
    print command                


main()


