# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Misc
# // ---------------------------------------------------------------------

# // ---- Main
# // String
def doesStringOnlyContainLetter(string: str, letters: str):
    return set(string) <= set(letters)

def truncateIfTooLong(string: str, maxLength: int, ending: str = "..."):
    if len(string) > maxLength:
        return string[:maxLength - len(ending)] + ending
    
    return string

# // Number
def clamp(number: float|int, min: float|int, max: float|int):
    if number < min:
        return min
    
    if number > max:
        return max
    
    return number

# // Interactions
class failChecks:
    def __init__(self):
        self.__failed = False
        self.__message = ""

    def fail(self, message: str):
        if self.__failed:
            return
        
        self.__message = message
        self.__failed = True
        
    def result(self):
        return self.__failed, self.__message