## GitHub Actions
An introduction to the workflow.

### PyTests (`Python Application`)
Tests are performed from the testfiles located in the `Tests` directory. This can be used for any more advanced modules. When a push is sent to the repo, it will create a python environment to run its tests.
### TODO to Issue
This automation will run when there is a push to the repo. It will scan the code for TODO comments (e.g `# TODO: Description`). 
If it finds any new ones, it will create a new issue with the description as well as the surrounding code. This is handy to communicate issues or to keep track of something.
### Labeling new Issue
If a new issue is created manually, it will scan the body of the message to automatically assign tags based on the content.

## Folder Structure
Currently, the structure is not set up for packaging. This means it will need to change before the program can be deployed

### API
This folder contains all functions needed for the interaction of the API. Each API/Module has it's own respective file, and is triggered directly by `Main.py`.

### Tests
Location for PyTests. Good practice for larger, more complicated modules.
