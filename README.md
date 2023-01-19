
# Building

## Linux 에서 (Ubuntu 추천)

**Dependence** : fontforge, python3 패키지를 받습니다  
```
sudo apt install fontforge python3
```
*Ubuntu 에 기본설치되는 gnu make 또한 필요합니다.*

config.py 파일을 필요에 맞게 편집합니다. 설명은 해당 파일을 열어 확인하세요  
```
vim config.py
```

폰트를 빌드합니다. 일반적으로 out 폴더에 ttf 파일이 출력됩니다  
```
make build
```
리눅스에서 사용하는 경우, ~/.local/share/fonts 에 자동으로 ttf 파일을 복사하도록 `make install` 을 사용할 수도 있습니다  

## Docking

향후 추가 예정

# License

license 파일을 참고해주세요.
submodule 을 제외한 이 리포지토리의 모든 파일은 (KawaiiMono**.sfd 포함한) 다음의 라이선스에 영향받습니다  

| Permissions | Limitations | Conditions |
|-------------|-------------|------------|
| ✅ Commercial use | ❎ Warranty | ❓ License and copyright notice |
| ✅ Modification | ❎ Liability | |
| ✅ Distribution | ❎ Being Rude | |
| ✅ Private use | ❎ Copy without any modification | |

사용된 Noto Mono 는 Google 이 소유하며, OFL 라이선스를 따릅니다.  
사용된 NanumSquareNeo 는 Naver 가 소유하며, OFL 라이선스를 따릅니다.  
사용된 Nerd Fonts 글리프는 [여기](https://github.com/ryanoasis/nerd-fonts/blob/master/license-audit.md) 에서 라이선스 정보를 확인해 주세요.  

# Issue

가독성이나 미적인 토론(?) 은 이슈를 이용하거나 qwreey75@gmail.com 으로 메일링 할 수 있습니다.  

# TODO

1. 합자자를 추가합니다.
2. 기울임 폰트를 추가합니다.
3. 굵은 폰트를 추가합니다.
4. Nerd Fonts 를 지원합니다.
5. B 와 같은 둥근 글리프의 가독성을 향상시킵니다.

## 안 이루워질 TODO

~~일해라 쿼리~~

ps1 스크립트로 윈도우 설치 자동화와, 윈도우 호환성을 만듭니다(가능한가 의문)  
