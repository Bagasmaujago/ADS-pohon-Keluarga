from collections import deque

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

# === Bangun Pohon Keluarga ===
def build_family_tree():
    root = Node("Ahadi & Uru")
    
    Mufasa = Node("Mufasa & Sarabi")
    Scar = Node("Scar & Zira")
    root.children = [Mufasa, Scar]
    
    Mufasa.children = [Node("Simba & Nala"), Node("Kion")]
    Scar.children = [Node("Nuka"), Node("Vitani")]
    
    return root

# === 1. Cari level seseorang dengan BFS (mulai dari level 1) ===
def find_level_bfs(root, target_name):
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
def dfs_print_with_levels(node, level=1, prefix=""):
    print(f"{prefix}└─ {node.name} (Level {level})")
    for i, child in enumerate(node.children):
        new_prefix = prefix + ("    " if i == len(node.children) - 1 else "│   ")
        dfs_print_with_levels(child, level + 1, new_prefix)

# === Gabungkan: Cari + Tampilkan ===
def analyze_person(root, name):
    level = find_level_bfs(root, name)
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
        dfs_print_with_levels(target_node, level)
    else:
        print(f"{name} tidak punya anak.")

# === Main ===
root = build_family_tree()

print("=== Seluruh Pohon Keluarga ===")
dfs_print_with_levels(root)  # tampilkan seluruh pohon dengan level (root = level 1)

print("\n=== Analisis ===")
analyze_person(root, "Mufasa & Sarabi")
print("\n---")
analyze_person(root, "Scar & Zira")
