class Greeter:
    def greet(self, name=None):
        if name is not None:
            return f"Hello, {name}!"
        else:
            return "Hello!"

greeter = Greeter()

print(greeter.greet())
print(greeter.greet("John"))