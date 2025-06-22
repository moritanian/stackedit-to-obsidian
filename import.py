import json
import os
import sys
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Convert StackEdit workspace to Obsidian format')
parser.add_argument('input_file', help='StackEdit workspace JSON file')
parser.add_argument('--output-dir', default='obsidian_import', help='Output directory (default: obsidian_import)')

args = parser.parse_args()
input_file = args.input_file
output_dir = args.output_dir

# Input file (StackEdit backup JSON)
with open(input_file, "r", encoding="utf-8-sig") as f:
    data = json.load(f)

os.makedirs(output_dir, exist_ok=True)


def get_item_path(item_id, data, path_cache=None):
    """Get the full path of an item"""
    if path_cache is None:
        path_cache = {}

    if item_id in path_cache:
        return path_cache[item_id]

    item = data.get(item_id)
    if not item:
        return ""

    parent_id = item.get("parentId")
    name = item.get("name", "")

    # Convert to safe file/folder name
    safe_name = "".join(c for c in name if c.isalnum() or c in (" ", "-", "_")).rstrip()

    if parent_id is None:
        # Root level
        path_cache[item_id] = safe_name
        return safe_name
    else:
        # Get parent path and combine
        parent_path = get_item_path(parent_id, data, path_cache)
        full_path = os.path.join(parent_path, safe_name) if parent_path else safe_name
        path_cache[item_id] = full_path
        return full_path


# Initialize path cache
path_cache = {}

# Extract each file
for item_id, item_data in data.items():
    # Process only file type items
    if item_data.get("type") == "file":
        file_id = item_data.get("id")
        name = item_data.get("name", f"note_{file_id}")

        # Find corresponding content
        content_id = file_id + "/content"
        content_data = data.get(content_id, {})
        content = content_data.get("text", "")

        # Get file's full path
        file_path = get_item_path(file_id, data, path_cache)

        # Convert to safe filename (add extension)
        filename = os.path.join(output_dir, file_path + ".md")

        # Create directory
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Save
        with open(filename, "w", encoding="utf-8") as out_file:
            out_file.write(content)

# Count files
file_count = sum(1 for item in data.values() if item.get("type") == "file")
print(f"{file_count} notes saved to {output_dir}/")

# Output debug information
print(f"Total items processed: {len(data)}")
content_count = sum(1 for item in data.values() if item.get("type") == "content")
print(f"Content items: {content_count}")
