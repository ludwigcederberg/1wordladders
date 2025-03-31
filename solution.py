import sys
from graph import Graph

def process_input(input_data):
    lines = []
    for line in input_data.splitlines():
        lines.append(line)
    return lines

    
def main():

    input_data = sys.stdin.read().strip()
    input_list = process_input(input_data)

    parts = input_list[0].split()
    num_words = int(parts[0])
    num_queries = int(parts[1])

    words = input_list[1:num_words + 1]
    queries = input_list[num_words + 1:]
    
    graph = Graph()
    
    graph.create_graph(words)
    
    
if __name__ == "__main__":
    main()