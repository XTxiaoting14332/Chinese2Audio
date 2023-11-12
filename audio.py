from pypinyin import pinyin
from pydub import AudioSegment
from pydub.playback import play
import string
import os

def split_pinyin_characters(chinese_word):
    pinyin_list = pinyin(chinese_word)
    result = []

    for pinyin_word in pinyin_list:
        for pinyin_char in pinyin_word[0]:
            result.append(pinyin_char)

    return ''.join(result)


def is_punctuation(char):
    return char in string.punctuation


def audio(char, text):
    out = char
    #a
    if char == "a" or char == "ā" or char == "á" or char == "ǎ" or char == "à":
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "n":
            if i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "g":
                out = char + "ng"
            else:
                out = char + "n"
        elif i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "i":
            out = char + "i"
        elif i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "o":
            out = char + "o"
        else:
            out = char

    #o
    elif char == "o" or char == "ō" or char == "ó" or char == "ǒ" or char == "ò":
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "n":
            if i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "g":
                out = char + "ng"
            else:
                out = char + "n"
        elif i - 1 >= 0 and pinyin_string[i - 1] == "a" or i - 1 >= 0 and pinyin_string[i - 1] == "ā" or i - 1 >= 0 and pinyin_string[i - 1] == "á" or i - 1 >= 0 and pinyin_string[i - 1] == "ǎ" or i - 1 >= 0 and pinyin_string[i - 1] == "à":
            out = ''
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "u":
            out = char + 'u'


    #e            
    elif char == "e" or char == "ē" or char == "é" or char == "ě" or char == "è":
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "n":
            if i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "g":
                out = char + "ng"
            else:
                out = char + "n"
        elif i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "i":
            out = char + "i"
        elif i + 1  < len(pinyin_string) and pinyin_string[ i + 1] == "r":
            out = char + "r"
        elif i - 1 >= 0 and pinyin_string[i - 1] == "i" or i - 1 >= 0 and pinyin_string[i - 1] == "u" or i - 1 >= 0 and pinyin_string[i - 1] == "y":
            out = ''
        else:
            out = char
            
    #i
    elif char == "i" or char == "i" or char == "ī" or char == "í" or  char == "ǐ" or char == "ì":
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "n":
            if i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "g":
                out = char + "ng"
            else:
                out = char + "n"
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "e" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ē" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "é" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ě" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "è":
            out = char + pinyin_string[i + 1]
        elif i - 1 >= 0 and pinyin_string[i - 1] == "z" or i - 1 >= 0 and pinyin_string[i - 1] == "c" or i - 1 >= 0 and pinyin_string[i - 1] == "s" or i - 1 >= 0 and pinyin_string[i - 1] == "r":
            out = ''
        elif i - 1 >=0 and pinyin_string[i - 1] == "h" or i - 1 >=0 and pinyin_string[i - 1] == "y" or i - 1 >= 0 and pinyin_string[i - 1] == "u":
            out = ''
        elif i - 1 >= 0 and pinyin_string[i - 1] == "a" or i - 1 >= 0 and pinyin_string[i - 1] == "ā" or i - 1 >= 0 and pinyin_string[i - 1] == "á" or i - 1 >= 0 and pinyin_string[i - 1] == "ǎ" or i - 1 >= 0 and pinyin_string[i - 1] == "à":
            out = ''
        elif i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "u" or  i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ū" or  i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ú" or  i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ǔ" or  i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ù":
            out = char + pinyin_string[i + 1]




        else:
            out = char

    #s
    elif char == "s":
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "h":
            if i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "i" or i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "ī" or i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "í" or i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "ǐ" or i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "ì":
                out = char + "h" + pinyin_string[i + 2]
            else:
                out = char + "h"
        elif i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "i" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ī" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "í" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ǐ" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ì":
            out = char + pinyin_string[i + 1]
        else:
            out = char

    #c
    elif char == "c":
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "h":
            if i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "i" or i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "ī" or i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "í" or i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "ǐ" or i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "ì":
                out = char + "h" + pinyin_string[i + 2]
            else:
                out = char + "h"
        elif i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "i" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ī" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "í" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ǐ" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ì":
            out = char + pinyin_string[i + 1]

        else:
            out = char

    #z
    elif char == "z":
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "h":
            if i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "i" or i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "ī" or i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "í" or i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "ǐ" or i + 2 < len(pinyin_string) and pinyin_string[i + 2] == "ì":
                out = char + "h" + pinyin_string[i + 2]
            else:
                out = char + "h"

        elif i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "i" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ī" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "í" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ǐ" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ì":
            out = char + pinyin_string[i + 1]        
        else:
            out = char

    #r
    elif char == "r":
            if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "i" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ī" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "í" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ǐ" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ì":
                out = char + pinyin_string[i + 1]
            elif i - 1 >= 0 and pinyin_string[i - 1] == "e" or i - 1 >= 0 and pinyin_string[i - 1] == "ē" or i - 1 >= 0 and pinyin_string[i - 1] == "é" or i - 1 >= 0 and pinyin_string[i - 1] == "ě" or i - 1 >= 0 and pinyin_string[i - 1] == "è":
                out = ''
            else:
                out = char

    #u
    elif char == "u":       
        if i - 1 >= 0 and pinyin_string[i - 1] == "y":
            out = 'ü'
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ī" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "í" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ǐ" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ì" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "e" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ē" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "é" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ě" or i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "è":
            out = char + pinyin_string[i + 1]
        if i - 1 >= 0 and pinyin_string[i - 1] == "o"  or i - 1 >= 0 and pinyin_string[i - 1] == "ō" or i - 1 >= 0 and pinyin_string[i - 1] == "ó" or i - 1 >= 0 and pinyin_string[i - 1] == "ǒ" or i - 1 >= 0 and pinyin_string[i - 1] == "ò":
            out = ''
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "n":
            if i - 1 >= 0 and pinyin_string[i - 1] == "y" or i - 1 >= 0 and pinyin_string[i - 1] == "x" or i - 1 >= 0 and pinyin_string[i - 1] == "q" or i - 1 >= 0 and pinyin_string[i - 1] == "j": 
                out = 'ü' + pinyin_string[i + 1]
            else:
                out = char + pinyin_string[i + 1]


    elif char == "ū":
        if i - 1 >= 0 and pinyin_string[i - 1] == "y" or i - 1 >= 0 and pinyin_string[i - 1] == "x" or i - 1 >= 0 and pinyin_string[i - 1] == "q" or i - 1 >= 0 and pinyin_string[i - 1] == "j": 
            out = 'ǖ'
        if i - 1 >= 0 and pinyin_string[i - 1] == "i":
            out = ''
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "n":
            if i - 1 >= 0 and pinyin_string[i - 1] == "y" or i - 1 >= 0 and pinyin_string[i - 1] == "x" or i - 1 >= 0 and pinyin_string[i - 1] == "q" or i - 1 >= 0 and pinyin_string[i - 1] == "j": 
                out = 'ǖ' + pinyin_string[i + 1]
            else:
                out = char + pinyin_string[i + 1]



    elif char == "ú":
        if i - 1 >= 0 and pinyin_string[i - 1] == "y" or i - 1 >= 0 and pinyin_string[i - 1] == "x" or i - 1 >= 0 and pinyin_string[i - 1] == "q" or i - 1 >= 0 and pinyin_string[i - 1] == "j":   
            out = 'ǘ' 
        if i - 1 >= 0 and pinyin_string[i - 1] == "i":
            out = ''
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "n":
            if i - 1 >= 0 and pinyin_string[i - 1] == "y" or i - 1 >= 0 and pinyin_string[i - 1] == "x" or i - 1 >= 0 and pinyin_string[i - 1] == "q" or i - 1 >= 0 and pinyin_string[i - 1] == "j": 
                out = 'ǘ' + pinyin_string[i + 1]
            else:
                out = char + pinyin_string[i + 1]


    elif char == "ǔ":
        if i - 1 >= 0 and pinyin_string[i - 1] == "y" or i - 1 >= 0 and pinyin_string[i - 1] == "x" or i - 1 >= 0 and pinyin_string[i - 1] == "q" or i - 1 >= 0 and pinyin_string[i - 1] == "j":  
            out = 'ǚ'  
        if i - 1 >= 0 and pinyin_string[i - 1] == "i":
            out = ''
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "n":
            if i - 1 >= 0 and pinyin_string[i - 1] == "y" or i - 1 >= 0 and pinyin_string[i - 1] == "x" or i - 1 >= 0 and pinyin_string[i - 1] == "q" or i - 1 >= 0 and pinyin_string[i - 1] == "j": 
                out = 'ǚ' + pinyin_string[i + 1]
            else:
                out = char + pinyin_string[i + 1]


    elif char == "ù":
        if i - 1 >= 0 and pinyin_string[i - 1] == "y" or i - 1 >= 0 and pinyin_string[i - 1] == "x" or i - 1 >= 0 and pinyin_string[i - 1] == "q" or i - 1 >= 0 and pinyin_string[i - 1] == "j":
            out = 'ǜ'
        if i - 1 >= 0 and pinyin_string[i - 1] == "i":
            out = ''
        if i + 1 < len(pinyin_string) and pinyin_string[i + 1] == "n":
            if i - 1 >= 0 and pinyin_string[i - 1] == "y" or i - 1 >= 0 and pinyin_string[i - 1] == "x" or i - 1 >= 0 and pinyin_string[i - 1] == "q" or i - 1 >= 0 and pinyin_string[i - 1] == "j": 
                out = 'ǜ' + pinyin_string[i + 1]
            else:
                out = char + pinyin_string[i + 1]
    



    ######n与g等的检测
    elif char == "n":
        if i - 1 >= 0 and (pinyin_string[i - 1] == "a" or pinyin_string[i - 1] == "ā" or pinyin_string[i - 1] == "á" or pinyin_string[i - 1] == "ǎ" or pinyin_string[i - 1] == "à") or i - 1 >= 0 and pinyin_string[i - 1] == "o" or pinyin_string[i - 1] == "ō" or pinyin_string[i - 1] == "ó" or pinyin_string[i - 1] == "ǒ" or pinyin_string[i - 1] == "ò" or i - 1 >= 0 and pinyin_string[i - 1] == "e" or pinyin_string[i - 1] == "ē" or pinyin_string[i - 1] == "é" or pinyin_string[i - 1] == "ě" or pinyin_string[i - 1] == "è":
            out = ''
        elif i - 1 >= 0 and pinyin_string[i - 1] == "i" or i - 1 >= 0 and pinyin_string[i - 1] == "i" or i - 1 >= 0 and pinyin_string[i - 1] == "ī" or i - 1 >= 0 and pinyin_string[i - 1] == "í" or i - 1 >= 0 and pinyin_string[i - 1] == "ǐ" or i - 1 >= 0 and pinyin_string[i - 1] == "ì":
            out = ''
        elif i - 1 >= 0 and pinyin_string[i - 1] == "u" or i - 1 >= 0 and pinyin_string[i - 1] == "ū" or i - 1 >= 0 and pinyin_string[i - 1] == "ú" or i - 1 >= 0 and pinyin_string[i - 1] == "ǔ" or i - 1 >= 0 and pinyin_string[i - 1] == "ù":
            out = ''

    elif char == "g":
        if i - 2 >= 0 and pinyin_string[i - 1] == "n":
            out = ''
        else:
            out = char
    
    elif char == "h":
        if i - 1 >= 0 and pinyin_string[i - 1] == "z" or i - 1 >= 0 and pinyin_string[i - 1] == "c" or i - 1 >= 0 and pinyin_string[i - 1] == "s":
            out = ''
        else:
            out = char

    elif char == "o":
        if i - 1 >= 0 and pinyin_string[i - 1] == "a" or i - 1 >= 0 and pinyin_string[i - 1] == "ā" or i - 1 >= 0 and pinyin_string[i - 1] == "á" or i - 1 >= 0 and pinyin_string[i - 1] == "ǎ" or i - 1 >= 0 and pinyin_string[i - 1] == "à":
            out = ''
        else:
            out = char

    #y
    elif char == "y":
        if 1 + 1 < len(pinyin_string) and pinyin_string[i + 1] == "e" or 1 + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ē" or 1 + 1 < len(pinyin_string) and pinyin_string[i + 1] == "é" or 1 + 1 < len(pinyin_string) and pinyin_string[i + 1] == "ě" or 1 + 1 < len(pinyin_string) and pinyin_string[i + 1] == "è":
            out = char + pinyin_string[i + 1]


    else:
        if is_punctuation(text) == True or text == "、" or text == "，" or text == "。" or text == "？" or text == "《" or text == "》" or text == "“" or text == "”" or text == "——" or text == "【" or text == "】" or text == "：":
            out = "none"
        else:
            out = char
    cache = "cache/" + text
    with open(cache, 'a') as file:
        if len(out) == 0:
            pass
        else:
            file.write(out + '\n')
    return out


try:
    # 获取输入
    input_text = input('Input: ')
    
    for text in input_text:
        # 获取逐个字分解的拼音
        pinyin_string = split_pinyin_characters(text)
        
        # 创建缓存文件

        if text.isspace():
            cache = "cache/none"
            text = "none"
        else:
            cache = "cache/" + text
        with open(cache, 'w', encoding='utf-8') as file:
            for i in range(len(pinyin_string)):
                result = audio(pinyin_string[i], text)
                if len(result) == 0:
                    pass
                else:
                    file.write(result + '\n')

        # 提取拼音并合成
        with open(cache, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            try:
                print("正在朗读："+text)
                if len(lines) == 1:
                        audio1 = "audio/" + lines[0].rstrip("\n") + ".mp3"
                        audioload1 = AudioSegment.from_file(audio1)
                        combined_audio = audioload1
                        combined_audio = combined_audio.speedup(playback_speed=3)
                        combined_audio = combined_audio + 5
                        play(combined_audio)
                        os.remove(cache)                
                elif len(lines) == 2:
                        audio1 = "audio/" + lines[0].rstrip("\n") + ".mp3"
                        audio2 = "audio/" + lines[1].rstrip("\n") + ".mp3"
                        audioload1 = AudioSegment.from_file(audio1)
                        audioload1 = audioload1 - 2
                        audioload1 = audioload1.speedup(playback_speed=20)
                        audioload2 = AudioSegment.from_file(audio2)
                        audioload2 = audioload2 
                        #audioload2 = audioload2.speedup(playback_speed=1)
                        combined_audio = audioload1 + audioload2
                        combined_audio = combined_audio.speedup(playback_speed=3)
                        combined_audio = combined_audio + 5
                        play(combined_audio)
                        os.remove(cache)
                elif len(lines) == 3:
                        audio1 = "audio/" + lines[0].rstrip("\n") + ".mp3"
                        audio2 = "audio/" + lines[1].rstrip("\n") + ".mp3"
                        audio3 = "audio/" + lines[2].rstrip("\n") + ".mp3"
                        audioload1 = AudioSegment.from_file(audio1)
                        audioload1 = audioload1 - 2
                        audioload1 = audioload1.speedup(playback_speed=10)
                        audioload2 = AudioSegment.from_file(audio2)
                        audioload2 = audioload2 - 5
                        audioload2 = audioload2.speedup(playback_speed=5)  
                        audioload3 = AudioSegment.from_file(audio3)
                        audioload3 = audioload3 + 5
                        combined_audio = audioload1 + audioload2 + audioload3
                        combined_audio = combined_audio + 5
                        combined_audio = combined_audio.speedup(playback_speed=3)
                        combined_audio = combined_audio
                        play(combined_audio)
                        os.remove(cache)
            except OSError:
                print("正在朗读："+text)
                audio1 = "audio/none.mp3"
                audioload1 = AudioSegment.from_file(audio1)
                audioload1 = audioload1.speedup(playback_speed=5)
                play(audioload1)
                os.remove(cache)
        
except KeyboardInterrupt:
    print("\n操作被用户取消")