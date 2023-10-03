from jinja2 import ChainableUndefined
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
templates.env.trim_blocks = True
templates.env.lstrip_blocks = True
templates.env.undefined = ChainableUndefined
