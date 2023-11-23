# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Slash Commands Init
# // ---------------------------------------------------------------------

def start():
    # importing the commands will automatically start them
    # is this a good way to do things? probably not
    from .preview import command as _
    from .restart import command as _
    from .setup import command as _