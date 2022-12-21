"""
===============================================================================
ENGR 13300 Fall 2021

Program Description:  This program is a part of the game of mastermind and contains one function for the game. The function is called player2 and used to when the game is double player.

Assignment Information
    Assignment:     Final project
    Author:         Tanmay Singla, singlat@purdue.edu
    Team ID:        LC1 - 11 

Contributor:    Name, login@purdue [repeat for each]
    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""
import getpass #so that input can be hidden 


def player2(numdigits): #function for second player to input the number
    num = getpass.getpass(f'Player 2: please enter the {numdigits} digit number: ') #asking the user to input number
   # num = int(input(f"PLayer 2: please enter the {numdigits} digit number: "))
    num = int(num)
    while ((len(list(str(num)))) != numdigits): #input validation
        print(f'Invalid input! The number was {(len(list(str(num))))} digits')
        num = getpass.getpass(f'Player 2: please enter the {numdigits} digit number: ')
        num = int(num)
    return(num) #returns the actual inputted number