from django.shortcuts import render
from .models import Description

# Create your views here.
def index(request):
    header = Description()
    header.name = "How cool would it be, if you could cook and code at the same time ? ¯\_(ツ)_/¯"
    header.desc = """A CLI application that enables voice coding in your code editor."""
    header.img = "larynxcode.png"
    return render(request,'index.html',{"header" : header})

def general(request):
    title_icon = Description()
    title_icon.img = 'larynxcode.png'
    card0 = Description()
    card0.name = 'caster on'
    card0.desc = "Wakes casterup, activates the microphone"
    card1 = Description()
    card1.name = 'caster sleep'
    card1.desc = "Puts Caster into temporary sleep, deactivates microphone"
    card2 = Description()
    card2.name = 'clear, deli, shock'
    card2.desc = "Backspace, Delete, Enter"
    card3 = Description()
    card3.name = 'ace, tabby'
    card3.desc = "Space, Tab"
    card4 = Description()
    card4.name = 'lease, ross'
    card4.desc = "Left, Right"
    card5 = Description()
    card5.name = 'format <word>'
    card5.desc = "Write down the word that follows the key command 'format' "
    card6 = Description()
    card6.name = 'stoosh'
    card6.desc = 'Copy'
    card7 = Description()
    card7.name = 'cut'
    card7.desc = 'Cut'
    card8 = Description()
    card8.name = 'spark'
    card8.desc = "Paste"
    card9 = Description()
    card9.name = 'prekris, left prekris, right prekris'
    card9.desc = "(), (, )"
    card10 = Description()
    card10.name = 'dot'
    card10.desc = "."
    card11 = Description()
    card11.name = 'shackle'
    card11.desc = "Select the entire line on which the cursor is"

    cards = [card0,card1,card2,card3,card4,card5,card6,card7,
            card8,card9,card10,card11]
    return render(request,'general.html',{"cards" : cards, "title_icon" : title_icon})

def ccr(request):
    title_icon = Description()
    title_icon.img = 'larynxcode.png'
    card0 = Description()
    card0.name = 'enable <programming language>'
    card0.desc = "Tells Caster which language we want to code in"
    card1 = Description()
    card1.name = 'disable <programming language>'
    card1.desc = "Turns off the enabled programming language"
    card2 = Description()
    card2.name = 'add comment'
    card2.desc = "Start a comment in that language"
    card3 = Description()
    card3.name = 'breaker'
    card3.desc = "break comment"
    card4 = Description()
    card4.name = 'for loop'
    card4.desc = "Initiate for loop in that language"
    card5 = Description()
    card5.name = 'return, function'
    card5.desc = "return, function keywords in that language"
    card6 = Description()
    card6.name = 'print to console'
    card6.desc = 'print statement in that language'
    card7 = Description()
    card7.name = 'lodge and, lodge not, lodge or'
    card7.desc = 'Write AND, NOT and OR operators in that language'
    

    cards = [card0,card1,card2,card3,card4,card5,card6,card7]
    return render(request,'ccr.html',{"cards" : cards, "title_icon" : title_icon})
