from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/Name')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/temperature')
def temperature():
    """
    Temperature Conversion
    """
    main_menu = """C - Convert Celcius to Fahrenheit
    F - Convert Fahrenheit to Celcius
    Q - Quit Program"""
    print(main_menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celcius = float(input("Temp in Celcius: "))
            fahrenheit = celcius * 9.0 / 5 + 32
            print("Result: {:2f} F".format(fahrenheit))

        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celcius = 5 / 9 * (fahrenheit - 32)
            print("Result: {:2f} C".format(celcius))

        else:
            print("Invalid!")
            print(main_menu)
            choice = input(">>> ").upper()
    print("Program Completed! Thank You.")


if __name__ == '__main__':
    app.run()
