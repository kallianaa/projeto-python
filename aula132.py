# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)


class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user): # setter
        self.user = user

    def set_password(self, password): # setter
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(mensagem):
        print("Log:", mensagem)

# connection1 = Connection()
connection1 = Connection.create_with_auth("kalli", "12345")
# connection1.set_user("kalli")
# connection1.set_password("12345")

print(connection1.user)
print(connection1.password)
print(Connection.log("Conexão criada com sucesso!"))