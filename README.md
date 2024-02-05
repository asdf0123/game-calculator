# game-calculator
it record some code about playing games
here are games done or to be done. they are in the format description & code & code description. 

## soluna

https://boardgamearena.com/gamepanel?game=soluna

soluna.cpp

it compresses the status and calculate status transition. after that it knows it is bound to win or loss when given the current status. its core is perfect now.

## can't stop

https://boardgamearena.com/gamepanel?game=cantstop

cantstop.py

it calulates Poisson Distributuin to find threshold of giving up. in fact, the gain is increasing linearly, but the loss is increasing exponentially, under the circunstance that the probolity of gaining is getting lower if you choose to continue. thus, finding a threshold to stop matters. 

## turing machine

https://boardgamearena.com/gamepanel?game=turingmachine

turingmachine.py

it uses the rule that every verifier matters to narrow possible answers. and then another part helps to find best query strategy by hand. in extreme mode or hard level, there're multiple criterions for a verifier but only one criterion is valid. the solution is ragarding "which one in the verifier is valid" as another variable like "whether my number will pass the verifer or not", enumerating and using query to narrow candidates. sometimes, you are able to know the passcode even if not knowing "which one in some verifier is valid".

## 3\*8=24

given 4 cards from deck, calculate 24 using these 4 cards and operators like +,-,\*,/.

https://asdf0123.github.io/html/3824.html (obviously, you can inspect to view the javascript code)

it is easy to evaluate an expression, but the key is to remove duplicate cases( like 1\*2\*3\*4=4\*3\*2\*1) when commutativity law( of +,-,\*,/) or associative law( of +,\*) are applied. it generates the parse tree and uses pivot method to distinguish and remove duplicate cases.


