
patchVersion = 2 # 업데이트 후 캐시를 무시하기 위해서 사용

from . import select as selectGlyphs
from .download import download
from .cacheBuilder import getCachedFont
from .patcher import pasteGlyphs
