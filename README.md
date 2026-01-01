# YoLang
One new Programming language for devloper.Yolang well update every day(maybe)
## Below is the full syntax of YoLang (you can also understand YoLang's syntax through **yolang_e.py**. To put it simply, YoLang is very similar to English)
### 1.Text Section
1.1 Show Text<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.1.1 Used `textshow()`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Source Code:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;def textshow(input_text):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text=input('show text:')<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(text)<br>
  2.<br>
  if "textshow(" in codes:<br>
    start_index=codes.index("textshow(")+9<br>
    end_index=codes.index(")",start_index)<br>
    content=codes[start_index:end_index]<br>
    textshow(content)<br>
  
