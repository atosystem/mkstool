import sys
# from .classmodule import MyClass
# from .funcmodule import my_function
from .mks_module import MksTool_API

# import click
import cmd

import getpass

mkstool_api = MksTool_API()

def maina():
    # print('in main')
    # args = sys.argv[1:]
    # print('count of args :: {}'.format(len(args)))
    # for arg in args:
    #     print('passed argument :: {}'.format(arg))
    # my_function('hello world')
    # my_object = MyClass('Thomas')
    # my_object.say_name()

    # mkstool_api = MksTool_API()
    # print("MakerSpace Service Tool v1.0")
    # u=input('Username: ')
    # p=getpass.getpass('Password: ')
    # if(not mkstool_api.login(u,p)):
    return
    #     return

# @click.command()
# @click.option('-t', '--to', 'to', help='To who')
# def main(to):
#     '''Say hello to someone'''
#     print(f'Hello, {to or "stranger"}!')
    

class myCmdLine(cmd.Cmd):
    """Simple command processor example."""
    prompt = 'mkstool> '
    def do_help(self, line):
        print ("""
        Welcome to Makerspace ssh configuration tool

        commands:
        
        login 
        profile : show your ssh account status
        ssh_create : create a ssh account
        exit 
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

    def do_status(self,line):

        pass
    
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
       
        
    do_EOF = do_exit

def main(): 
    myCmdLine().cmdloop()


if __name__ == '__main__':
    main()
    # greeting()