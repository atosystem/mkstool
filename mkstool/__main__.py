import sys
# from .classmodule import MyClass
# from .funcmodule import my_function
from .mks_module import MksTool_API

# import click
import cmd

import getpass

mkstool_api = MksTool_API()

class myCmdLine(cmd.Cmd):
    """Simple command processor example."""
    prompt = 'mkstool> '
    def do_help(self, line):
        print ("""
        Welcome to Makerspace ssh configuration tool(beta version)

        commands:
        
        login : login to the system (using ntu cc account)
        profile : show your ssh account status 
        ssh_create : create a ssh account (only for ntueesaad members)
        change_displayname : change your display name on MKS fingerprint system
        help : show all commands
        exit : exit the program

        ============admin only=================
        ls users : list all users
        change_role <row_id> <new role>: change user role by row id

        roles: admin,mks_member,student
         
        """)

    def do_exit(self, line):
           #this command will make you exit from the shell
        print("Bye")
        return True

    def do_login(self,line):
        u=input('Username: ')
        p=getpass.getpass('Password: ')
        mkstool_api.login(u,p)
        # pass
    def help_login(self,line):
        pass

    # def do_status(self,line):

    #     pass
    
    def do_profile(self,line):
        ret = mkstool_api.ssh_profile_view()
        if(ret['status']=="success"):
            if(ret['message']!=""):
                print(ret['message'])
            else:
                print("Your ssh login account: " + ret['data']['ssh_profile'])
        else:
            print(ret['message'])
    def help_profile(self,line):
        pass
    def do_ssh_create(self,line):
        mkstool_api.ssh_create()
    def do_ls(self,line):
        if(line == "users"):
            mkstool_api.ssh_users_list()
        else:
            print("Please type 'ls users'")
    def do_change_role(self,line):
        z = line.split()
        if(len(z)!=2):
            print("arguments count must be 2")
        else:
            mkstool_api.ssh_users_change_role(z[0],z[1])
    
    def do_change_displayname(self,line):
        mkstool_api.door_change_display_name()
        
    do_EOF = do_exit

def main(): 
    myCmdLine().cmdloop()


if __name__ == '__main__':
    main()
    # greeting()