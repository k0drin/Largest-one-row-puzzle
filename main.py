from collections import defaultdict


def find_largest_sequence(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            fragments = [line.strip() for line in file]
        if not fragments:
            raise ValueError("Input file is empty or contains invalid data.")

        graph = defaultdict(list)
        for frag1 in fragments:
            for frag2 in fragments:
                if frag1 != frag2 and frag1[-2:] == frag2[:2]:
                    graph[frag1].append(frag2)

        def dfs(current, chain, visited, longest_chain):
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    dfs(neighbor, chain + neighbor[2:], visited, longest_chain)
            visited.remove(current)
            longest_chain[0] = max(longest_chain[0], chain, key=len)

        longest_sequence = ""
        for fragment in fragments:
            visited = set()
            longest_chain = [fragment]
            dfs(fragment, fragment, visited, longest_chain)
            if len(longest_chain[0]) > len(longest_sequence):
                longest_sequence = longest_chain[0]

        return longest_sequence

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    return ""


if __name__ == "__main__":
    input_file = 'source.txt'
    result = find_largest_sequence(input_file)
    if result:
        print("Largest Sequence:", result)
