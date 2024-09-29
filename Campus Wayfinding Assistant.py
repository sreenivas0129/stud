import heapq

# Class representing the campus as a graph
class CampusMap:
    def __init__(self):
        self.graph = {}

    # Method to add a location (node)
    def add_location(self, location):
        if location not in self.graph:
            self.graph[location] = []

    # Method to add a path (edge) between two locations
    def add_path(self, from_location, to_location, distance):
        self.graph[from_location].append((to_location, distance))
        self.graph[to_location].append((from_location, distance))  # bidirectional

    # Get all locations in the campus
    def get_locations(self):
        return list(self.graph.keys())

    # Get all neighbors (adjacent nodes) of a location
    def get_neighbors(self, location):
        return self.graph[location]

# Dijkstra's algorithm to find the shortest path
def dijkstra(graph, start, end):
    # Priority queue to store (distance, location)
    queue = [(0, start)]
    distances = {location: float('inf') for location in graph.graph}
    distances[start] = 0
    previous_locations = {location: None for location in graph.graph}

    while queue:
        current_distance, current_location = heapq.heappop(queue)

        if current_location == end:
            break

        for neighbor, distance in graph.get_neighbors(current_location):
            new_distance = current_distance + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))
                previous_locations[neighbor] = current_location

    # Backtrack to find the path
    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous_locations[current]
    return path, distances[end]

# CLI interface to interact with the user
def main():
    # Create campus map and define locations
    campus = CampusMap()

    # Add some locations (nodes) to the campus map
    campus.add_location('Library')
    campus.add_location('Cafeteria')
    campus.add_location('Lecture Hall 1')
    campus.add_location('Lecture Hall 2')
    campus.add_location('Admin Building')

    # Add paths (edges) between locations with distances (in meters)
    campus.add_path('Library', 'Cafeteria', 200)
    campus.add_path('Library', 'Lecture Hall 1', 300)
    campus.add_path('Cafeteria', 'Lecture Hall 1', 100)
    campus.add_path('Lecture Hall 1', 'Lecture Hall 2', 150)
    campus.add_path('Admin Building', 'Library', 250)
    campus.add_path('Admin Building', 'Lecture Hall 2', 100)

    print("Welcome to the Campus Wayfinding Assistant")
    while True:
        # Prompt user for input
        start = input("Enter your current location (or type 'exit' to quit): ")
        if start == 'exit':
            break

        end = input("Enter your destination: ")

        # Validate input locations
        if start not in campus.get_locations() or end not in campus.get_locations():
            print("Invalid locations. Please try again.\n")
            continue

        # Find shortest path
        path, distance = dijkstra(campus, start, end)
        print(f"Shortest path from {start} to {end}: {path}")
        print(f"Total distance: {distance} meters\n")

if __name__ == "__main__":
    main()
