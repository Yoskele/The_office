from flask import Flask
from flask import render_template, request, url_for, session, redirect


import auth
from messages import get_messages, save_messages, get_messages, get_message, get_max_id, add

app = Flask(__name__)
app.secret_key = b'aj(>,m&*@#NxmaiOxH23Kkmlb128($'

# Denna är klar! 
def is_logged_in():
    '''If 'username' is in the session as a key, return True.
    Otherwise, return False.'''
    return 'username' in session

# Börja med denna fixa login redirect to login... 
# Sedan Do show messegeses if loged in.


# is_logged_in() är en funktion ovanför. kollar om man är inlogad eller inte.
@app.route("/")
@app.route("/messages/")
def show_messages():
    if not is_logged_in():
        return redirect(url_for('login'))
    else:
        username = session['username']
        messages = get_messages(username)
        return render_template('messages.html',messages=messages)
    '''To do: If the user is logged in, render the 'messages.html' template
    together with the user's messages ('inbox').
    If the user is NOT logged in, redirect to the login page.'''
    # DONE



# Dont Touch this
@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        # Login was successful:
        if auth.login(username, password):
            session['username'] = username
            return redirect(url_for('show_messages'))
        else:
            return render_template('login.html')
    else:
        print('login with GET')
        return render_template('login.html')

# Dont Touch this
@app.route("/logout/")
def logout():
    session.pop('username', None)
    return redirect(url_for('show_messages'))

# Done
@app.route("/message/<int:id>/")
def show_message(id):
    email = get_message(id)
    return render_template('message.html', email = email, id=id)
    '''To do: find the given message by its id.
    Then display it in a rendered template.'''




# Denna är inte klar men new_mail är som det ska vara så ska det vara! Sa Yair
@app.route("/message/compose/", methods=["GET", "POST"])
def compose():
    if request.method == 'GET':
        return render_template('compose.html')
        
        # To do: render the relevant page with no data
    elif request.method == 'POST':
        new_mail = {}

        new_mail['from'] = request.form.get('from', None)
        new_mail['subject'] = request.form.get('subject', None)
        new_mail['body'] = request.form.get('body', None)
        
        return redirect(url_for('show_messages'))
        '''To do: 'unpack' the form data, and process it:
        1. Prepare the data in an appropriate data structure
        2. Save the data to your data store (Make use of existing functions
            you may have)
        3. Once the data is saved to file, redirect to the /messages/ page.'''
