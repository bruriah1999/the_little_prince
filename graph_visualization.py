import networkx as nx
import matplotlib.pyplot as plt

def visualize_knowledge_graph(graph_data):
    """
    Visualizes a knowledge graph using networkx and matplotlib.

    Args:
        graph_data (dict): A dictionary containing nodes and edges.
            Example:
            {
                "nodes": [{"id": "PersonA", "label": "Person A"}, {"id": "PersonB", "label": "Person B"}],
                "edges": [{"source": "PersonA", "target": "PersonB", "label": "Knows"}]
            }
    """
    G = nx.DiGraph()

    # Add nodes
    for node in graph_data["nodes"]:
        G.add_node(node["id"], label=node["label"])

    # Add edges
    for edge in graph_data["edges"]:
        G.add_edge(edge["source"], edge["target"], label=edge["label"])

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold")
    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")
    plt.show()


def extract_graph_data(reasoning_steps):
    """
    Extracts graph data (nodes and edges) from the agent's reasoning steps.

    Args:
        reasoning_steps (list): A list of reasoning steps from the agent.

    Returns:
        dict: A dictionary containing nodes and edges for the graph.
    """
    graph_data = {"nodes": [], "edges": []}
    node_ids = set()

    for step in reasoning_steps:
        # Extract entities and relationships from the step
        if "entity" in step:
            entity_id = step["entity"]
            if entity_id not in node_ids:
                graph_data["nodes"].append({"id": entity_id, "label": entity_id})
                node_ids.add(entity_id)

        if "relationship" in step:
            graph_data["edges"].append({
                "source": step["relationship"]["source"],
                "target": step["relationship"]["target"],
                "label": step["relationship"]["type"]
            })

    return graph_data


reasoning_steps = [
    {"entity": "L61595148", "relationship": {"source": "L61595148", "target": "CompanyX", "type": "Works At"}},
    {"entity": "CompanyX", "relationship": {"source": "L61595148", "target": "Vehicle123", "type": "Owns"}}
]

def __main__():
    """
    Main function to run the knowledge graph visualization.
    """
    # Extract graph data from reasoning steps
    graph_data = extract_graph_data(reasoning_steps)
    
    # Visualize the knowledge graph
    visualize_knowledge_graph(graph_data)
if __name__ == "__main__":
    __main__()