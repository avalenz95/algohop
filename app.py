from flask import Flask, render_template
import plotly.graph_objects as go


app = Flask(__name__)


@app.route('/')
def index():

    fig = go.Figure(
        data=[go.Scatter(x=[0, 1], y=[0, 1])],
        layout=go.Layout(
            xaxis=dict(range=[0, 5], autorange=False),
            yaxis=dict(range=[0, 5], autorange=False),
            title="Start Title",
            updatemenus=[dict(
                type="buttons",
                buttons=[dict(label="Play",
                            method="animate",
                            args=[None])])]
        ),
        frames=[go.Frame(data=[go.Scatter(x=[1, 2], y=[1, 2])]),
                go.Frame(data=[go.Scatter(x=[1, 4], y=[1, 4])]),
                go.Frame(data=[go.Scatter(x=[3, 4], y=[3, 4])],
                        layout=go.Layout(title_text="End Title"))]
    )

    gplot = fig.show()

    return render_template('index.html',figure=gplot)

if __name__ == "__main__":
    app.run_server(debug=True)