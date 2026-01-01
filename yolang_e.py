print("This dev language is called YoLang.IT'S A JOKE PROGRAMMING LANGUAGE")
print("You can changed the codes as you want")
print("Some codes is AI builded,maybe have some bugs or funny things")
while True:
    codes=input("Enter your YoLang code:")
    def textshow(input_text):
        text=input('show text:')
        print(text)
    #show text
    def numbershow():
        num1=input('show number:')
        print(eval(num1))
    #show number
    def textinput(prompt_text):
        return input(prompt_text)
    #input text
    #check codes for run
    if "textshow(" in codes:
        start_index=codes.index("textshow(")+9
        end_index=codes.index(")",start_index)
        content=codes[start_index:end_index]
        textshow(content)
    elif "numbershow()" in codes:
        numbershow()
    elif "textinput()" in codes:
        start_index=codes.index("textinput(")+10
        end_index=codes.index(")",start_index)
        prompt=codes[start_index:end_index]
        result=textinput(prompt)
        print(result)
    else:
        print("Unknown YoLang Command")