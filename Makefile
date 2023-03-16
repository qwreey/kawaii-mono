build:
	@mkdir -p out
	@python3 build.py -B  2> out/err.log || { echo "Build Failed. Please check out/err.log for detailed information"; false; }
	@py3clean .

install:
	@cp out/KawaiiMonoRegularPatched.ttf ~/.local/share/fonts/KawaiiMonoRegular.ttf
	@fc-cache -f -v
