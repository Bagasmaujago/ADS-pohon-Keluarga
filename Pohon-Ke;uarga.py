from collections import deque

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

# === Bangun Pohon Keluarga ===
def build_family_tree():
    root = Node("George Joestar & Mary Joestar")
    
    Jonathan_Joestar = Node("Jonathan Joestar & Erina Joestar")
    Dio_Brando = Node("Dio Brando & Jane Doe")
    root.children = [Jonathan_Joestar, Dio_Brando]
    
    Jonathan_Joestar.children = [Node("George Joestar II")]
    Dio_Brando.children = [Node("Giorno Giovanna"), Node("Donatello Versus")]
    
    return root

# === 1. Cari level dengan BFS
def cari_level_bfs(root, target_name):
    if not root:
        return -1
    
    queue = deque([(root, 1)])  # (node, level) → mulai dari 1
    while queue:
        node, level = queue.popleft()
        if node.name == target_name:
            return level
        for child in node.children:
            queue.append((child, level + 1))
    return -1

# === 2. DFS: Cetak seluruh pohon dengan level (mulai dari 1) ===
def print_dfs(node, level=1, prefix=""):
    print(f"{prefix}└─ {node.name} (Level {level})")
    for i, child in enumerate(node.children):
        new_prefix = prefix + ("    " if i == len(node.children) - 1 else "│   ")
        print_dfs(child, level + 1, new_prefix)
# === Gabungkan: Cari + Tampilkan ===
def analyze(root, name):
    level = cari_level_bfs(root, name)
    if level == -1:
        print(f"{name} tidak ditemukan.")
        return
    
    print(f"{name} ada di generasi (level): {level}")
    
    # Cari node target
    queue = deque([root])
    target_node = None
    while queue:
        node = queue.popleft()
        if node.name == name:
            target_node = node
            break
        queue.extend(node.children)
    
    if target_node and target_node.children:
        print(f"\nKeturunan {name}:")
        print_dfs(target_node, level)
    else:
        print(f"{name} tidak punya anak.")

# === Main ===
root = build_family_tree()

print("=== Seluruh Pohon Keluarga ===")
print_dfs(root)  # tampilkan seluruh pohon dengan level (root = level 1)

print("\n=== Analisis ===")
analyze(root, "Jonathan Joestar & Erina Joestar")
print("\n---")
analyze(root, "Dio Brando & Jane Doe")