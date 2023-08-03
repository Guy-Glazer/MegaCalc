from flask import Flask, render_template, request
from interest_calculator import calculate_interest
import os

app = Flask(__name__)

# Explicitly specify the template folder
template_dir = os.path.abspath('./')  # Assuming index.html is in the same directory as app.py
app = Flask(__name__, template_folder=template_dir)

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
