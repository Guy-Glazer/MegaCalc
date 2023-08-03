from flask import Flask, render_template, request
from interest_calculator import calculate_interest

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        yearly_interest = float(request.form["yearly_interest"]) / 100
        deposit_amount = float(request.form["deposit_amount"])
        total_days = int(request.form["total_days"])
        withdrawal_days = int(request.form["withdrawal_days"])

        total_interest = calculate_interest(yearly_interest, deposit_amount, total_days, withdrawal_days)
        result = f"{total_interest:.2f}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
