import base64, pickle
import matplotlib.pyplot as plt
from io import BytesIO



# Save DataFrame into session
def save_df(df):
    from flask import session as flask_session
    flask_session['df'] = base64.b64encode(pickle.dumps(df)).decode()

# Load DataFrame from session
def load_df():
    from flask import session as flask_session
    return pickle.loads(base64.b64decode(flask_session['df']))

# Analyze
def handle_action(df, action, request):
    result = ""
    plot_url = ""

    try:
        if action == 'head':
            result = df.head().to_string()
            
        elif action == 'describe':
            result = df.describe(include='all').to_string()
            
        elif action == 'columns':
            result = str(df.columns.tolist())
            
        elif action == 'value_counts':
            col = request.form.get('col')
            result = df[col].value_counts().to_string()
            
        elif action == 'plot':
            col = request.form.get('col')
            plot_type = request.form.get('plot_type')
            plt.figure(figsize=(8,5))
            if plot_type == 'bar':
                df[col].value_counts().plot(kind='bar')
            elif plot_type == 'line':
                df[col].plot(kind='line')
            elif plot_type == 'hist':
                df[col].plot(kind='hist')
            plt.title(f"{plot_type} of {col}")
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plot_url = base64.b64encode(buf.read()).decode()
            plt.close()
            
        elif action == 'filter':
            condition = request.form.get('condition')
            result = df.query(condition).to_string()
            
    except Exception as e:
        result = f"Error: {e}"

    return result, plot_url