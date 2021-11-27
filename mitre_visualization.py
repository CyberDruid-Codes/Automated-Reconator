##
#Import Section
import networkx as nx
import matplotlib.pyplot as plt
##

##
techniq_len = 0

##
#method that formats the mitre result from dict to a list and gets the graph number of nodes
def formatting(techniques):
    
    global techniq_len

    #Gets the length of the techniques
    techniq_len = len(techniques)

    #list that creates the right ammount of numbers based on length
    count = []
    for x in range(techniq_len): 
        count.append(x)

    #formats the lists into a dict for the graph
    label_names = {count[i]:techniques[i]for i in range(0, techniq_len)}

    return label_names 
##

##
#creates the graph 
def mitre_graph(techniques,subtechniques):

    global techniq_len

    #List of techniques testing
    #techniques = ["Network", "T1595","T1592","T1588","T1587"]
    #subtechniques = ["T1595.001","T1592.002","T1595.002","T1587.004","T1588.006","T1588.005","T1592.001"]

    #creates labels for the nodes
    graph_labels = formatting(techniques) 

    #Creates the graph, of the right length
    G=nx.star_graph(techniq_len-1)
    
    G.add_node("Network")

    #Adds the technique nodes edges based on how many techniques there are
    nodes_len = techniq_len -1
    while (nodes_len >= 0):
        G.add_edge(0,nodes_len)
        nodes_len -=1


    #adds edges for each subtechnique parsed 
    for subt in subtechniques: 
        if "T1595" in subt:
            G.add_edge("T1595",subt)
        elif "T1592" in subt:
            G.add_edge("T1592",subt)
        elif "T1588" in subt:
             G.add_edge("T1588",subt)
        elif "T1587" in subt:
             G.add_edge("T1587",subt)
    
    #Labels the nodes to the techniques and subtechniques names
    H=nx.relabel_nodes(G,graph_labels)
    
    #Options for the graph (e.g. colour of nodes, nodes size, edges size )
    options = {
        "node_color": "#C63F1F",
        "width": 4,
        "node_size":2500,
        "with_labels": True,
        "font_size":9,
    }

    plt.figure(figsize=(10,8))
    nx.draw(H, **options)
    plt.savefig("mitre_visualization.jpeg")
    #plt.show()
##

