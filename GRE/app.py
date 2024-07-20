from flask import Flask, redirect, render_template , url_for, request
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'gre_001'

with open('artifacts\words_and_meanings.json', 'r') as file:
        data = json.load(file)

def generate_deck(data,deck_number):
      num = 20*(deck_number-1)
      for i in range(num,num+20):
           pass
            
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/practice', methods = ['GET','POST'])
def practice():
    if request.method == 'POST':
        deck = (int)(request.form.get('deck'))
        num:int = 20*(deck-1)
        print(num)
        print(num+20)
        data_items = {}
        data_dict = list(data.items())
        print(len(data_dict))
        for i in range(num,min(num+20,len(data_dict))):
            key,value = data_dict[i]
            data_items[key] = value

    return render_template('practice.html',data_items = data_items,deck=deck)

if __name__ == "__main__":
      app.run(debug=True)