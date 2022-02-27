import random as ran

HANGMANPICS = [

    '''
  +---+

  |   |

      |

      |

      |

      |

=========''',

    '''
  +---+

  |   |

  O   |

      |

      |

      |

=========''',

    '''
  +---+

  |   |

  O   |

  |   |

      |

      |

=========''',

    '''
  +---+

  |   |

  O   |

 /|   |

      |

      |

=========''',

    '''
  +---+

  |   |

  O   |

 /|\  |

      |

      |

=========''',

    '''
  +---+

  |   |

  O   |

 /|\  |

 /    |

      |

=========''',

    '''
  +---+

  |   |

  O   |

 /|\  |

 / \  |

      |

=========''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    word = ran.choice(wordList)
    # This function returns a random string from the passed list of strings.
    return word



def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):

    missedNum = len(missedLetters)
    print(HANGMANPICS[missedNum])
    print("missed letters: ", end= "")
    for i in missedLetters:
        print(i, end=" ")
    print()
    for i in secretWord:
        if i in correctLetters:
            print(i, end="")
        else:
            print("_", end="")
    print()


    # display the hangman pictures





def getGuess(alreadyGuessed):
    while True:
        guessedWord = input("알파벳 입력\n")
        if len(guessedWord) > 1:
            print("한 글자만 입력해주세요")
        elif guessedWord in alreadyGuessed:
            print("이미 입력했던 글자입니다")
        else:
            break
    return guessedWord


    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.



def playAgain():
    replay = input("다시 플레이 하시겠습니까?\n 예\n 아니요\n")
    if replay == "예":
        return True
    else:
        return False
    # This function returns True if the player wants to play again, otherwise it returns False.




print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False
win = False



while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    yourWord = getGuess(correctLetters + missedLetters)
    if yourWord in secretWord:
        correctLetters += yourWord
    else:
        missedLetters += yourWord

    win = True
    for i in secretWord: # goose
        if i not in correctLetters:
            win = False
            break

    if win:
        print("승리!")
        print("숨겨진 단어는 " + secretWord + "였습니다!")
        gameIsDone = True

    if len(missedLetters) == 6:
        gameIsDone = True
        print("이런! 행맨은 죽고 말았습니다. 당신의 무지함 때문에 말이죠.")
        print("당신이 맞춰낸 글자는 " + str(len(correctLetters)) + "개 이고 정답은 " + secretWord + "였습니다.")




    # Let the player type in a letter.

        # Check if the player has won
        # Check if player has guessed too many times and lost

    # Ask the player if they want to play again (but only if the game is done).

    if gameIsDone:
        if playAgain():
            print('H A N G M A N')
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            gameIsDone = False
        else:
            break