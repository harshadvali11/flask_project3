from flask import Flask,render_template

AI=Flask(__name__)

@AI.route('/wishes')
def wish():
    return render_template('wish.html')



@AI.route('/second')
def second():
    return render_template('second.html')

if __name__=='__main__':
    AI.run(debug=True)