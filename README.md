# Mass / Bulk XML formatter
A small python script to format (pretty print) multiple XML files at once.
> :warning: Python version 3.9 or higher is required!
```
/home/user/Documents/input-dir/document-one.xml
--->
/home/user/Documents/output-dir/document-one.xml

/home/user/Documents/input-dir/document-two.xml
--->
/home/user/Documents/output-dir/document-two.xml

+-----------------------+
Formatted files: 2
+-----------------------+
```
## Usage
`./format-xml.py --input INPUT_DIR [--output OUTPUT_DIR] [--ignore-subdirs]`  

- input
  - Path to the input directory which contains the XML files.
- output
  - Path to the directory where the formatted XML files should be saved. If none is specified, a new one will be created automatically.
- ignore-subdirs
  - If this flag is set, only files from the specified directory are formatted. Files in nested directories are ignored.
