from functions import SystemUtilities
from message_management import MessageManagement
from user_management import UserManagement
from user_authentication import UserAuthentication
import server_response


class CommandHandler:
    def __init__(self, server_logged_in_user_data):
        self.server_logged_in_user_data = server_logged_in_user_data
        self.username = ""
        self.comm = ""
        self.permissions = ""
        self.user_auth = UserAuthentication(self.server_logged_in_user_data)
        self.user_management = UserManagement()
        self.message_management = MessageManagement()
        self.sys_utils = SystemUtilities()

        self.all_users_commands = {
            "login": self.user_auth.login,
            "logout": self.user_auth.logout,
            "help": self.sys_utils.help,
            "info": self.sys_utils.info,
            "uptime": self.sys_utils.uptime,
            "clear": self.sys_utils.clear,
            "msg_count": self.message_management.msg_count,
            "msg-list": self.message_management.msg_list,
            "msg-snd": self.message_management.msg_snd,
            "msg-del": self.message_management.msg_del,
            "new_message": self.message_management.new_message,
            "msg-show": self.message_management.msg_show
        }
        self.admin_commands = {
            "stop": SystemUtilities.stop,
            "user-add": self.user_management.user_add,
            "user-list": self.user_management.user_list,
            "user-del": self.user_management.user_del,
            "user-perm": self.user_management.user_perm,
            "user-stat": self.user_management.user_stat,
            "user-info": self.user_management.user_info,
            "create_account": self.user_management.create_account
        }

    def use_command(self, entrance_comm):
        if isinstance(entrance_comm, dict):
            # Extract the first key, which is the username submitted
            self.username = next(iter(entrance_comm))
            # Based on this username, create a new dictionary with the command
            print(f'MENU username = {self.username}')
            self.comm = entrance_comm.pop(self.username)
            self.permissions = self.server_logged_in_user_data.server_logged_in_permissions
            print(f'NEW_COMMAND  = {self.comm}')
            print(f'ENTRANCE USERNAME = {self.username}')
            print(f'ENTRANCE PERMISSIONS: {self.permissions}')

        if isinstance(self.comm, dict):
            print(f'REAL COMMAND = {list(self.comm.keys())[0]}')
            command = list(self.comm.keys())[0]
            data = self.comm[command]
        else:
            command = self.comm
            data = None

        if command in self.all_users_commands:
            match command:
                case "login":
                    self.username = data[0]['username']

                case "logout":
                    data = self.username
                    self.username = None
                    self.permissions = None
                case "help":
                    data = self.permissions
                case "msg-list":
                    data = self.username
                case "msg-del":
                    data = {self.username: data}
                case "msg-show":
                    data = {self.username: data}
                case "msg_count":
                    data = self.username
                case _:
                    pass

            if data is not None:
                result = self.all_users_commands[command](data)
            else:
                result = self.all_users_commands[command]()

        elif command in self.admin_commands:
            if self.permissions == "admin":
                if data is not None:
                    result = self.admin_commands[command](data)
                else:
                    result = self.admin_commands[command]()
            else:
                result = server_response.E_COMMAND_UNAVAILABLE
        else:
            result = server_response.UNRECOGNISED_COMMAND

        print(f'Server response: {result}')
        print(f'EXIT USERNAME = {self.username}')
        print(f'EXIT PERMISSIONS: {self.permissions}')
        print(f'EXIT DATA = {data}')

        print(f'FROM USER_STATE = {self.server_logged_in_user_data}')
        print(f'FROM USER_STATE_USER  = {self.server_logged_in_user_data.server_logged_in_username}')
        print(f'FROM USER_STATE_PERM  = {self.server_logged_in_user_data.server_logged_in_permissions}')
        return result




