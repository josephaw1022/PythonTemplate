
class Application:
    """
    Application

    Let's get to work!
    """
    
    def __init__(self):
        self._helloWorld()
    
    
    @property
    def welcomeMessage(self):
        return "Delete me and get started on your project!"

    @staticmethod
    def addVertSpace(content: str):
        return f"\n\n{content}\n\n"

    def _helloWorld(self) -> None:
        print(self.addVertSpace(self.welcomeMessage))




Application()
    