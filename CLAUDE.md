# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python utility that converts StackEdit workspace JSON files to Markdown files compatible with Obsidian. The tool preserves folder structure and handles UTF-8 BOM encoding automatically.

## Key Commands

### Running the Converter
```bash
python3 import.py <input_file> [--output-dir <directory>]
```

Examples:
```bash
python3 import.py stackedit_workspace.json
python3 import.py backup.json --output-dir my_notes
```

### Testing Changes
Since this is a simple utility script, test by running it with sample data:
```bash
python3 import.py stackedit_workspace.json --output-dir test_output
```

## Architecture

The script follows a simple single-file architecture:

1. **Argument parsing**: Uses `argparse` to handle input file and optional output directory
2. **JSON parsing**: Loads StackEdit workspace JSON with UTF-8-BOM support
3. **Path resolution**: Recursive function `get_item_path()` builds full paths from StackEdit's parent-child relationships
4. **File extraction**: Processes items with `type: "file"` and matches them with corresponding content items
5. **Safe filename conversion**: Converts names to filesystem-safe characters
6. **Output generation**: Creates directory structure and writes Markdown files

## Important Data Structures

- StackEdit workspace JSON contains items with `id`, `type`, `name`, and `parentId` fields
- Content is stored separately as `{file_id}/content` items with `text` field
- The script uses a path cache to avoid recomputing folder paths

## Development Notes

- Personal data files (`stackedit_workspace.json`, `obsidian_import/`) are gitignored
- The script requires only Python standard library (no external dependencies)
- Error handling focuses on file I/O and JSON parsing
- Output directory is created automatically if it doesn't exist