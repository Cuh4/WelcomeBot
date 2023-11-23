# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Events
# // ---------------------------------------------------------------------

# // ---- Imports
import inspect

# // ---- Variables
events: dict[str, "event"] = {}

# // ---- Functions
def isCoroutine(func: "function"):
    return inspect.iscoroutinefunction(func)

def getSavedEvent(name: str):
    return events.get(name, None)

# // ---- Main
# // Event
# contains functions. when an event is called, all of its functions (callbacks) are called
class event:
    def __init__(self, name: str):
        self.name = name
        self.callbacks: list["callback"] = []
        self.callbackID = 0
        
    def save(self):
        events[self.name] = self
        return self
        
    def unsave(self):
        events.pop(self.name, None)
        return self
        
    def fire(self, *args, **kwargs):
        returnValue = None
        
        for callback in self.callbacks:
            if callback.isAsync:
                continue
            
            returnValue = callback.call(*args, **kwargs)
            
        return returnValue
    
    async def asyncFire(self, *args, **kwargs):
        returnValue = None
        
        for callback in self.callbacks:
            if not callback.isAsync:
                continue
            
            returnValue = await callback.asyncCall(*args, **kwargs)
            
        return returnValue
    
    def attach(self, func: "function"):
        self.callbackID += 1

        currentCallback = callback(
            func = func,
            id = self.callbackID
        )
        
        currentCallback.attach(self)

        return currentCallback
    
    def detach(self, callback: "callback"):
        callback.detach()
        return self
        
# function with extra steps
class callback:
    def __init__(self, func: "function", id: int):
        self.func = func
        self.id = id
        self.parent: "event" = None
        self.isAsync = isCoroutine(func)
        
    def attach(self, event: "event"):
        self.parent = event
        self.parent.callbacks.append(self)
        return self
        
    def detach(self):
        if self.parent is None:
            return self
        
        self.parent.callbacks.remove(self)
        return self
        
    def call(self, *args, **kwargs):
        if self.isAsync:
            return
        
        return self.func(*args, **kwargs)
    
    async def asyncCall(self, *args, **kwargs):
        if not self.isAsync:
            return
        
        return await self.func(*args, **kwargs)