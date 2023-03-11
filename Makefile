build:
	@mkdir -p out
	@python3 build.py -B  2> out/err.log
	@py3clean .

install: build
	@cp out/KawaiiMonoRegularPatched.ttf ~/.local/share/fonts/KawaiiMonoRegular.ttf
	@fc-cache -f -v
