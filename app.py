from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        yearly_interest = float(request.form['yearly_interest'])
        total_days = int(request.form['total_days'])
        deposit_amount = float(request.form['deposit_amount'])
        
        result = calculate_interest(yearly_interest, total_days, deposit_amount)
        return jsonify({'result': result})

    return render_template('index.html')

def calculate_interest(yearly_interest, total_days, deposit_amount):
    daily_interest_rate = yearly_interest / 365 / 100

    total_interest = deposit_amount * daily_interest_rate * total_days

    return total_interest
if __name__ == '__main__':
    app.run(debug=True)
