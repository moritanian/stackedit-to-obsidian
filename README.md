# StackEdit to Obsidian Converter

A Python script to convert StackEdit workspace JSON files to Markdown files
compatible with Obsidian.

## Features

- Extract Markdown files from StackEdit backup JSON files
- Preserve original folder structure
- UTF-8 BOM support
- Safe filename conversion

## Usage

1. Export workspace from StackEdit and save as `stackedit_workspace.json`
2. Run the script:
   ```bash
   python3 import.py
   ```
3. Converted Markdown files will be created in the `obsidian_import/` folder

## Requirements

- Python 3.6 or higher
- Standard library only (no additional installation required)

## File Structure

```
.
├── import.py              # Main conversion script
├── stackedit_workspace.json  # StackEdit backup file (required)
└── obsidian_import/       # Converted Markdown files (auto-created)
```

## Notes

- `stackedit_workspace.json` and `obsidian_import/` folder contain personal data
  and are excluded from the Git repository
- Invalid characters in filenames are automatically converted to safe characters
- Existing `obsidian_import/` folder will be overwritten

## Troubleshooting

### UTF-8 BOM Error

If the StackEdit JSON file contains BOM, the script handles it automatically.

### Directory Structure Not Preserved

Please verify that the StackEdit backup file is in the correct format.
