from flask import Flask, render_template,request
import speech_recognition as sr
import os


# CRITICAL for audio 404 fix
app = Flask(__name__, static_folder='audio') 



@app.route('/')
def home():
    # Renders the main dashboard page
    return render_template('main.html')

@app.route('/music')
def music_page():
    # Renders the main music dashboard page
    return render_template('music.html')

# ADD THIS NEW ROUTE
@app.route('/weekend')
def weekend_page():
    # Renders the Weekend-specific content page
    return render_template('weekend.html')

@app.route('/jb')
def jb_page():
    # Renders the Justin Bieber-specific content page
    return render_template('jb.html')



@app.route('/player')
def player_page():
    # Renders the audio player page
    return render_template('player.html')

@app.route('/eminem')
def eminem_page():
    # Renders the Eminem content page
    return render_template('eminem.html')

@app.route('/Travis')  
def travis_page():
    # Renders the Travis Scott content page
    return render_template('travis.html')

@app.route('/bruno')
def bruno_page():
    # Renders the Bruno Mars content page
    return render_template('bruno.html')

@app.route('/taylor')
def taylor_page():
    # Renders the Taylor Swift content page
    return render_template('taylor.html')

@app.route('/best')
def best_page():    
    # Renders the Best HipHop content page
    return render_template('best.html')

@app.route('/pop')
def pop_page():    
    # Renders the Best Pop Songs content page
    return render_template('pop.html')

@app.route('/rock')
def rock_page():    
    # Renders the Best Rock content page
    return render_template('rock.html')

@app.route('/rnb')
def rnb_page():    
    # Renders the Best RnB content page
    return render_template('rnb.html')

@app.route('/jazz')
def jazz_page():    
    # Renders the Best Jazz content page
    return render_template('jazz.html')

@app.route('/jp')
def jp_page():
    # Renders the Japanese Classics content page
    return render_template('jp.html')




if __name__ == '__main__':
    app.run(debug=True)