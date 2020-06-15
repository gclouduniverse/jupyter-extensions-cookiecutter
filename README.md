# Cookie Cutter Extension

Cloud AI Platform Notebooks JupyterLab extension cookiecutter project for quickly generating a JupyterLab extension that follows AI Platform best practices. The extension will display a list of strings retrieved from a JupyterLab backend in a React-based side panel widget. Follow the Quick Start instructions to get JupyterLab up and running with a custom example extension installed.

## Prerequisites

* Python 3.5+
* [NPM](https://nodejs.org/en/) (For local development)

## Quick Start

Install [cookiecutter](https://pypi.org/project/cookiecutter/):

```bash
pip install cookiecutter
```

Install [pipenv](https://github.com/pypa/pipenv#installation):

```bash
pip install pipenv
```

Generate a new extension from the template. Press enter at each of the prompts to accept the default value or add the `--no-input` flag:

```bash
cookiecutter https://github.com/cbwilkes/jupyter-extensions-cookiecutter -o my_extension
```

Change to the generated project directory:

```bash
cd my_extension/jupyter-extensions # Change this to the generated main directory
```

To build, install, and launch run:

```bash
npm install && \
npm run bootstrap && \
pipenv shell && \
pipenv install && \
npm run link
```

Change to the generated extension directory:

```bash
cd jupyterlab_cookies # Change this to the generated extension directory
npm run install-extension
```

Return to the main directory, and start the development server:

```
cd ..
npm run devserver
```


