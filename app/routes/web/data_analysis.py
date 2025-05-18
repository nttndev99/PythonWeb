
from flask import Blueprint, flash, redirect, render_template, request, session, url_for

import pandas as pd

from app.services.data_analysis_service import handle_action, load_df, save_df

data_analysis_bp = Blueprint('data_analysis', __name__)



@data_analysis_bp.route('/upload-analyze', methods=['GET', 'POST'])
def upload_analyze():
    result = ""
    plot_url = ""
    columns = []

    if request.method == 'POST':
        action = request.form.get('action')
        file = request.files.get('file')

        if file:
            df = pd.read_csv(file)
            save_df(df)
        elif 'df' in session:
            df = load_df()
        else:
            df = None

        if df is not None:
            columns = df.columns.tolist()
            result, plot_url = handle_action(df, action, request)

    return render_template("data_analysis_templates/upload_analyze.html", result=result, plot_url=plot_url, columns=columns)



@data_analysis_bp.route("/analyze/end")
def end_analysis():
    session.pop("df", None)  # remove session
    flash("The session with data is over.")
    return redirect(url_for("data_analysis.upload_analyze"))