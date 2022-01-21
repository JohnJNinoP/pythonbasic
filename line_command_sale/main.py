import sys


clients = "pablo,ricardo"

def create_client(name_client):
    global clients 

    if(name_client not in clients):
        _add_comma()
        clients += name_client
    else:
        print("Cliente already is in the client\'s list")

def _add_comma():
    global clients 
    clients +=","

def list_clients():
    global clients
    print(clients)

def update_clients(name_client,update_client_name):
    global clients
    _cliets_replace(name_client,update_client_name)
        
def delete_client_name(name_client):
    global clients
    _cliets_replace(name_client,"")

def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input("what is the client name?")


    if client_name.lower() == 'exit':
        sys.exit()
    
    return client_name

def _cliets_replace(name_client,update_client_name):
    global clients
    if (name_client in clients):
        clients = clients.replace(name_client,update_client_name)
    else:
        print("Client not found in list")

def search_client(name_client) :
    global clients
    list_clients = clients.split(",")
    
    for client in list_clients:
        if client == name_client:
            return True
    return False

def print_welcome():
    print("WELCOME TO SALES")
    print('*'*50)
    print('What would you like to to today?')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]update client')
    print('[S]earch client')

if __name__ == '__main__':
    print_welcome()
    list_clients()
    command_input = input()
    command_input = command_input.upper()
    if(command_input =="C"):
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif(command_input == "D"):
        client_name = _get_client_name()
        delete_client_name(client_name)
        list_clients()
    elif(command_input == 'U'):
        client_name = _get_client_name()
        print("New name client")
        update_client_name = _get_client_name()
        update_clients(client_name,update_client_name)
        list_clients()
    elif(command_input == 'S'):
        client_name = _get_client_name()
        found = search_client(client_name)
        if(found):
            print("CLient exists in the cliet´s list")
        else:
            print(f'Client {client_name} not exists in the list')
    else:
        print("invalid command") 
    
    