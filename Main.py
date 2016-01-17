import Classes
#import tkinter

class root():
    def __init__(self, HumanUI):
        self.run = True
        self.HumanUI = HumanUI


if __name__ == "__main__":

    #MenuOptions = ['Menu:\nGet parts', 'Create user', 'Delete user', 'Log out']

    #Dictionary used for testing
    TestDic = {
        'ric': {
            'Password': '123',
            'Admin': True
        },
        'Ty' : {
            'Password' : '123',
            'Admin': False
        }
    }
    PartTestDic = {
        'AN3-3A': {
            'BAG' : 'BAG 2987'
        },
        'ES=00007': {
            'BAG' : 'BAG 3000'
        }
    }

    PartData = Classes.Parts(PartTestDic)
    PData = Classes.PeopleDatabase(TestDic)
    Interface = Classes.HumanUI(PData)

    Core = root(Interface)
    while Core.run == True :
            Core.HumanUI.LogIn()
            if Core.HumanUI.LoggedIn:
                Interface.MainMenu()

