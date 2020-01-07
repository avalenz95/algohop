from flask import Flask, render_template
import plotly.graph_objects as go
import networkx as nx

app = Flask(__name__)


@app.route('/')
def index():

    #Creates empty graph
    G = nx.Graph()

    #Test add nodes
    G.add_nodes_from([2, 3])

    #Test add edges
    G.add_edges_from([(1, 2), (1, 3)])

    #provides number of nodes
    print(f"# Nodes: {G.number_of_nodes()}")

    #provides number of edges
    print(f"# Edges: {G.number_of_edges()}")
    edge_xpos = []
    edge_ypos = []
    for edge in G.edges():
        edge_xpos.append(edge[0])
        edge_ypos.append(edge[1])
        print(f"edge: {edge}")

    edge_trace = go.Scatter(
        x=edge_xpos, y=edge_ypos,
        line=dict(width=4, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_xpos = []
    node_ypos = []
    for node in G.nodes():
        node_xpos.append(node)
        node_ypos.append(node)

        print(f"node: {node}")

    node_trace = go.Scatter(
        x=node_xpos, y=node_ypos,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            color=[],
            #handles size of nodes
            size=30,
            #handles width of nodes
            line_width=5))


    fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
    figure = fig.show()



    return render_template('index.html', figure=figure)

if __name__ == "__main__":
    app.run(debug=True)