# تعريف الصنف Employee
class Employee:
    def __init__(self, name, id_number, salary):
        self.name = name
        self.id_number = id_number
        self.salary = salary

    def display_employee_info(self):
        return f"Name: {self.name}, ID: {self.id_number}, Salary: {self.salary}"

# تعريف الصنف Accountant الذي يرث من Employee
class Accountant(Employee):
    def __init__(self, name, id_number, salary, certification, clients):
        super().__init__(name, id_number, salary)
        self.certification = certification
        self.clients = clients

    def display_accountant_info(self):
        employee_info = self.display_employee_info()
        return f"{employee_info}, Certification: {self.certification}, Clients: {', '.join(self.clients)}"

    def add_client(self, client_name):
        self.clients.append(client_name)
        return f"Client {client_name} added."

    def remove_client(self, client_name):
        if client_name in self.clients:
            self.clients.remove(client_name)
            return f"Client {client_name} removed."
        else:
            return f"Client {client_name} not found."

# مثال على استخدام الأصناف
employee = Employee("John Doe", "E123", 50000)
accountant = Accountant("Jane Smith", "A456", 70000, "CPA", ["Client1", "Client2"])

print(employee.display_employee_info())
print(accountant.display_accountant_info())
print(accountant.add_client("Client3"))
print(accountant.display_accountant_info())
print(accountant.remove_client("Client1"))
print(accountant.display_accountant_info())
