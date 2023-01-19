build:
	python3 build.py
	py3clean .

install: build
	cp out/KawaiiMonoRegularPatched.ttf ~/.local/share/fonts/KawaiiMonoRegular.ttf
