#Small Site Generator

Practice Repo for my p5js journal project.

Basic HTML file creation from directory structure and markdown. 

## Usage

- `python3 make_sketch_html.py $NUM $RELATIVE_DIRECTORY_LOCATION` - will produce an embed file and an html file for the sketch in that folder. 
    - Uses a hardcoded location for p5js and css that do not currently exist in this repo. 
    - Overwrites any existing index.html or embed.html files.

- Temaplate html files use the `${variable_name}` syntax provided by built in python [Template Strings](https://docs.python.org/3/library/string.html#template-strings). In VSCode the extension `"fabiospampinato.vscode-highlight"` provides highlighting (see `.vscode/settings.json`).


## Resources

* https://www.digitalocean.com/community/tutorials/
* how-to-use-python-markdown-to-convert-markdown-text-to-html

* https://www.devdungeon.com/content/convert-markdown-html-python
* https://dev.to/nqcm/making-a-static-site-generator-with-python-part-1-3kn3
* https://rahmonov.me/posts/static-site-generator/

* https://docs.python.org/3/library/string.html
* https://docs.python.org/3/library/string.html#format-string-syntax
* https://docs.python.org/3/library/string.html#template-strings

* https://stackoverflow.com/questions/34360603/python-template-safe-substitution-with-the-custom-double-braces-format
* https://stackabuse.com/formatting-strings-with-the-python-template-class/

