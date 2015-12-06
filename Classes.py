import Main

class DatabaseSetup():
    def __init__(self):
        pass

class HumanUI():
    def __init__(self, PeopleDatabase):
        self.LoggedIn = False
        self.UserId = None
        self.AdminUser = False
        self.PeopleDatabase = PeopleDatabase
        self.PasswordTrys = 4
        self.Attempts = 0
        self.MainMenuOptions = ['Get parts', 'Create user', 'Delete user', 'Log out']
        self.MenuSelection = None
        self.PartsDatabse = Parts

    def LogIn(self):
        if self.UserId is None :
            self.UserId = input('UserID: ').capitalize()
            #print(self.UserId)
        else:
            while (self.PasswordTrys > self.Attempts) and (self.LoggedIn is False):
                if self.PeopleDatabase.UserCheck(self.UserId):
                    self.UserPassword = input('Password: ')
                    if self.PeopleDatabase.PasswordCheck(self.UserId, self.UserPassword):
                        if self.PeopleDatabase.IsAdmin(self.UserId):
                            self.AdminUser = True
                        else :
                            self.AdminUser = False
                        self.Attempts = 0
                        self.LoggedIn = True
                        print('Log in success\n')
                    else:
                        self.Attempts = self.Attempts + 1
                        print('You have ' +  str(self.PasswordTrys - self.Attempts) + ' Attempts remaining.')
                        if self.Attempts == self.PasswordTrys:
                            print('User locked out.')
                            self.LogOut()
                            return
                else:
                    print('Contact sytem admin to create Account.\n')
                    self.LogOut()
                    return
                     #self.PeopleDatabase.CreateUser(self.UserId)

    def LogOut(self):
        self.UserId = None
        self.UserPassword = None
        self.Attempts = 0

    def MainMenu(self):
        if self.AdminUser == True:
            for line in self.MainMenuOptions:
                print(line)
            self.MenuSelection = input('What would you like to do? #:')
            self.AdminSelection(self.MenuSelection)
        elif self.AdminUser == False:
        #only one option for basic users right now
            self.MenuSelection = '1'
            self.BasicUserSelection(self.MenuSelection)

    def AdminSelection(self,Choice):
        if Choice =='1':
            self.GetParts()
        elif Choice == '2':
            self.CreateUser()
        elif Choice == '3':
            self.DeleteUser()
        elif Choice == '4':
            self.LogOut()

    def BasicUserSelection(self,Choice):
        if Choice == '1':
            self.GetParts()
            self.PartNumber
        else:
            return

    def GetParts(self):
        self.PartNumber = input('What part are you looking for:').upper()
        if self.PartsDatabse(self.Partnumber):
            self.PartQty = input('How many do you need?')
            try:
                self.PartQty = int(self.PartQty)
            except:
                return None

        #Needs work, database broken 12/3/15, 10:47am
    def CreateUser(self):
        print('\nCreate user')
        NewUserName = input('Who are you adding?')
        NewUserPass = input('Enter thier password')
        if input('Are they an Admin? Y/N:').upper() == 'Y':
            Admin = True
        else:
            Admin = False
        PeopleDatabase.TestDic[NewUserName] = {'Password': NewUserPass, 'Admin' : Admin}
        print('User Created')
        return

    def DeleteUser(self):
        print('Delete user')

    def LogOut(self):
        self.LoggedIn = False
        self.UserId = None
        self.UserPassword = None
        self.Attempts = 0
        print('Session Ended\n')


#Check Point
class PeopleDatabase():
    def __init__(self, debug):
        self.Database = debug

    def UserCheck(self, UserId):
        if UserId in self.Database:
            return True

    def PasswordCheck(self, UserId, UserPassword):
        if UserPassword == self.Database[UserId]['Password']:
            return True

    def IsAdmin(self, UserId):
        if self.Database[UserId]['Admin']:
            return True
        else:
            return False


    def LogOut(self):
        pass

    def CreateUser(self,UserId):
        pass

    def DeleteUser(self):
        pass

class Attendence():
    def __init__(self):
        pass

class Parts():
    def __init__(self,PartDebug):
        self.PartDabase = PartDebug
    #checks the partdatbase for the parts
    def PartCheck(self, PartNumber):
        if PartNumber in self.PartDabase:
            return True
        else:
            return False
