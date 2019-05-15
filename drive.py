from flask import Flask

app = Flask(__name__) #__main

@app.route('/home')
def greeting():
	return 'Welcome!'


if __name__ == '__main':
		app.run(port=3000)
