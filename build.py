import os
import sys
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/src"))
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/assets"))
from src.build import build
import config
if __name__ == "__main__": build(config.config)
