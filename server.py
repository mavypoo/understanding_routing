from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<word>') #word is a path_variable
def say_word(word):
    return f"Hi {word.capitalize()}!"


@app.route('/repeat/<int:num>/<phrase>')  #int/phrase is a path variable. We want to indicate an int in num because num will automatically default to a string.
def repeat_phrase(num, phrase):
    return f"{num * phrase}"  # * multiples the phrases


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


