
# from a deck of cards fetch 3 cards find probability of belows:
# 1. find that one  card is a face card
# 2. find 2 cards to be an ace card
# 3. find that all cards are multiple of 2



import random 

not_multi_of_2 = 16
multi_of_2=20

face_cards = 12
ace_cards=4

total_cards=not_multi_of_2+multi_of_2+face_cards+ace_cards


num_simulation=100000

face_cards_count=0
ace_cards_2_count=0
all_multi_of_2_count=0

for i  in range (num_simulation):
    deck=['multi'] * 20 + ['not_multi']* 16 +['face']* 12 + ['ace'] * 4
    drawn_cards=[]
    random.shuffle(deck)
    drawn_cards.append(deck[0:1])
    random.shuffle(deck)
    drawn_cards.append(deck[0:1])
    random.shuffle(deck)
    drawn_cards.append(deck[0:1])

    

    if drawn_cards[0]==['face'] or drawn_cards[1]==['face'] or drawn_cards[2]==['face']:
        face_cards_count+=1
            
    if ((drawn_cards[0]==['ace'] and drawn_cards[1]==['ace'] and drawn_cards[2]!=['ace'])
        or
        (drawn_cards[0]==['ace'] and drawn_cards[1]!=['ace'] and drawn_cards[2]==['ace'])
        or
        (drawn_cards[0]!=['ace'] and drawn_cards[1]==['ace'] and drawn_cards[2]==['ace'])
        
        ):

        ace_cards_2_count+=1
    
    if drawn_cards[0]==['multi'] and drawn_cards[1]==['multi'] and drawn_cards[2]==['multi']:
        all_multi_of_2_count+=1
            
    
prob_one_face_card=face_cards_count/num_simulation
prob_2_ace_cards = ace_cards_2_count / num_simulation
prob_all_multi_of_2 =  all_multi_of_2_count / num_simulation


print(f"PROBABILITY OF ONE OF THREE CARD BEING FACE CARD IS:{prob_one_face_card:.4f}")
print(f"PROBABILITY OF TWO OF THREE CARD BEING ACE CARD IS:{prob_2_ace_cards:.4f}")
print(f"PROBABILITY OF ALL OF THE THREE CARD BEING BEING MULTIPLE OF 2 IS:{prob_all_multi_of_2:.4f}")

# two dice are rolled  50 times, so find probability for :
# 1. second number is sdjecent successor of firt number 
# 2. sum of both should be factor of 12 
# 3. sum of both should multiple of 3 and 2



