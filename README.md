# game-calculator
it record some code about playing games
here are games done or to be done. they are in the format description & code & code description. 

#soluna
https://boardgamearena.com/gamepanel?game=soluna
?
it compresses the status and calculate status transition. after that it knows it is bound to win or loss when given the current status

#can't stop
https://boardgamearena.com/gamepanel?game=cantstop
?
it calulates Poisson Distributuin to find threshold of giving up.

#turing machine
https://boardgamearena.com/gamepanel?game=turingmachine
tm.py
it uses the rule that every verifier matters to narrow possible answers. and then another part helps to find best query strategy by hand.

#3\*8=24
given 4 cards from deck, calculate 24 using these 4 cards and operators like +,-,\*,/.
https://asdf0123.github.io/html/3824.html(obviously, you can inspect to view the javascript code)
it is easy to evaluate an expression, but the key is to remove duplicate cases( like 1\*2\*3\*4=4\*3\*2\*1) when commutativity law( of +,-,\*,/) or associative law( of +,\*) are applied. it generates the parse tree and uses pivot method to distinguish and remove duplicate cases.


