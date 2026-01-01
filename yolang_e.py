print("This dev language is called YoLang.IT'S A JOKE PROGRAMMING LANGUAGE")
print("You can changed the codes as you want")
print("Some codes is AI builded,maybe have some bugs or funny things")
while True:
    codes=input("Enter your YoLang code:")
    def textshow(input_text):
        print(input_text)
    #show text
    def textinput(prompt_text):
        return input(prompt_text)
    #input text
    def numberinput(prompt_text):
        num1=input(prompt_text)
        return eval(num1)
    if "textshow(" in codes:
        start_index=codes.index("textshow(")+9
        end_index=codes.index(")",start_index)
        content=codes[start_index:end_index]
        textshow(content)