import tkinter
import random
mainwindow=tkinter.Tk()
mainwindow.title("Black-Jack")
mainwindow.geometry("640x480")
mainwindow.config(background="green")

#Function to load card images

def load_images(card_images):
    suits= ['heart','club','diamond','spade']
    face_cards= ['jack','queen','king']
    for suit in suits:
        for card in range(1,11):
            name='cards/{}_{}.ppm'.format(str(card),suit)
            image=tkinter.PhotoImage(file=name)
            card_images.append((card,image,))
            
    for card in face_cards:
        name='cards/{}_{}.ppm'.format(str(card),suit) 
        image=tkinter.PhotoImage(file=name)
        card_images.append((10,image,))    
        
        
#Function to calculate score in a hand
def score_hand(hand):
    #calculate the total score of cards in the list
    #only one ace can have the value 11.and this will reduce to 1 if the hand is a bust
    score=0
    ace = False     
    for next_card in hand:
        card_value=next_card[0]
        if card_value==1 and not ace:
            ace=True
            card_value=11
        score +=card_value
        #if we bust, check if there is an ace and subtract 10
        if score>21 and ace:
            score-=10
            ace=False
    return score  
        
#Function to deal cards
def deal_card(frame):
    #pop the next card of the top of the deck
    next_card=deck.pop(0)
    #add the card back to the top of the deck
    deck.append(next_card)
    #add the image to a label and display the label
    tkinter.Label(frame,image=next_card[1],relief='raised').pack(side='left')
    #return the card's face value
    return next_card
 
def deal_dealer():
    #dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score = score_hand(dealer_hand)
    while 0<dealer_score<17:
        dealer_hand.append(deal_card(dealer_card_frame))
        #dealer_score_label.set(dealer_score)
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    player_score = score_hand(player_hand)    
    if player_score>21:
        result_text.set("Dealer Wins!")
    elif dealer_score>21 or dealer_score<player_score:
        result_text.set("Player Wins!")
    elif dealer_score>player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw!")
        

def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score =score_hand(player_hand)
    player_score_label.set(player_score)
#    deal_card(dealer_card_frame)
    if player_score >21:
        result_text.set("Dealer Wins")
        
def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    #destroy and reload embedded frames
    dealer_card_frame.destroy()
    dealer_card_frame=tkinter.Frame(card_frame,background="green")
    dealer_card_frame.grid(row=0,column=1,sticky='ew',rowspan=2)  
    player_card_frame.destroy()
    player_card_frame=tkinter.Frame(card_frame,background="green")
    player_card_frame.grid(row=2,column=1,rowspan=2,sticky="ew")
    dealer_hand=[]
    player_hand=[]
    result_text.set("")
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()

#Label at the top to display result
result_text=tkinter.StringVar()
result=tkinter.Label(mainwindow,textvariable=result_text)
result.grid(row=0,column=0,sticky="ew",columnspan=3)
#frame 1 to hold 2 frames:one for dealer card and one for user card
card_frame=tkinter.Frame(mainwindow,borderwidth=1,relief="sunken",background="green")
card_frame.grid(row=1,column=0,sticky="ew",columnspan=3,rowspan=2)

#dealer score label
dealer_score_label=tkinter.IntVar()
tkinter.Label(card_frame,text="Dealer",background="green",fg="white").grid(row=0,column=0)
tkinter.Label(card_frame,textvariable=dealer_score_label,background="green",fg="white").grid(row=1,column=0)

#embedded frame 1:dealer's frame

dealer_card_frame=tkinter.Frame(card_frame,background="green")
dealer_card_frame.grid(row=0,column=1,rowspan=2,sticky="ew")

#player score label
player_score_label=tkinter.IntVar()

tkinter.Label(card_frame,text="Player",background="green",fg="white").grid(row=2,column=0)
tkinter.Label(card_frame,textvariable=player_score_label,background="green",fg="white").grid(row=3,column=0)

#embedded frame2: player's frame
player_card_frame=tkinter.Frame(card_frame,background="green")
player_card_frame.grid(row=2,column=1,rowspan=2,sticky="ew")

#frame to hold buttons

button_frame=tkinter.Frame(mainwindow, background="green")
button_frame.grid(row=3,column=0,sticky="ew",columnspan=3)

dealer_button=tkinter.Button(button_frame,text="Dealer",command=deal_dealer)
dealer_button.grid(row=0,column=0)

player_button=tkinter.Button(button_frame,text="Player",command=deal_player)
player_button.grid(row=0,column=1)

new_button=tkinter.Button(button_frame,text="New Game",command=new_game)
new_button.grid(row=0,column=2)
#load cards
cards=[]
load_images(cards)
print(cards)

#create a new deck of cards and shuffle them
deck=list(cards)
random.shuffle(deck)

#create a list to store the dealer's and player's hand
dealer_hand=[]
player_hand=[]

deal_player()
dealer_hand.append(deal_card(dealer_card_frame))
dealer_score_label.set(score_hand(dealer_hand))
deal_player()

mainwindow.mainloop()