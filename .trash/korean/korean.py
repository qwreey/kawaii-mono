import fontforge

startKList = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'];
midKList = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'];
endKList = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'];

print(startKList.__len__())
print(midKList.__len__())
print(endKList.__len__())


def getCodepoint(start,mid,end):
    return (start * 588) + (mid * 28) + end

for start in range(19):
    for mid in range(21):
        for end in range(28):
            getCodepoint(start,mid,end)

# def

# local codes = utf8.codes;
# local floor = math.floor;
# local char = utf8.char;
# local concat = table.concat;
# local insert = table.insert

# function module.split(str)
# 	local returnStr = {};
# 	for _,code in codes(str) do -- 글자 utf 에서 코드를 가져옴
# 		if code >= 44032 and code <= 55199 then -- 한국어임
# 			local kcode = code - 44032; -- 한국어 시작점인 44032 를 뺀값

# 			local startK = floor(kcode / 588); -- 초성 인덱스
# 			local midK = floor((kcode - (startK * 588)) / 28); -- 중성 인덱스
# 			local endK = floor((kcode - (startK * 588) - (midK * 28))); -- 종성 인덱스

# 			insert(returnStr,startKList[startK]);
# 			insert(returnStr,midKList[midK]);
# 			insert(returnStr,endKList[endK]);
# 		else -- 한국어가 아님
# 			insert(returnStr,char(code));
# 		end
# 	end
# 	return concat(returnStr);
# end

# return module;
