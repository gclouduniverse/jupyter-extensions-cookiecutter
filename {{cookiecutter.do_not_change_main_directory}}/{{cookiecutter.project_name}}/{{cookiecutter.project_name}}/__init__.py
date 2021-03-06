from notebook.utils import url_path_join

from {{cookiecutter.project_name}}.handlers import ListHandler
from {{cookiecutter.project_name}}.version import VERSION

__version__ = VERSION

def _jupyter_server_extension_paths():
    return [{
        'module': '{{cookiecutter.project_name}}'
    }]

def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.
    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    host_pattern = '.*$'
    app = nb_server_app.web_app
    gcp_v1_endpoint = url_path_join(
      app.settings['base_url'], '{{cookiecutter.api_name}}', 'v1')
    app.add_handlers(host_pattern, [
      # TODO(cbwilkes): Add auth checking if needed.
      # (url_path_join(gcp_v1_endpoint, auth'), AuthHandler)
      (url_path_join(gcp_v1_endpoint, 'list') + '(.*)', ListHandler),
    ])

