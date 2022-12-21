"""
===============================================================================
ENGR 13300 Fall 2021

Program Description:  This program is the game of mastermind, both double player and single-player (inputted by user). This game would ask the user to guess a set of numbers and tell them if they guessed the number correctly or not, and if not if they guessed numbers at certain places right or if not by outputting the number and the place of the number you got right. This will run until the user guesses the right number. For double player, this function will run twice and user 1 would be asked to enter user 2 guesses and vice versa. The winner would be declared and the number of tries it took them. The number of digits they want to play for will also be user inputted. 

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

import random #imports random to generate random numbers
import getpass #so that input can be hidden 
import mastermind2 as m2

def option(): #function to asks the user for which mode they want to play and does input validation
    
    print("Do you want to play double player or single player?")
    option= input("Type 0 to play double player or type 1 to play single player: ") #asking for single or double player game
    
    while option.isdigit() == False: #input validation
        option= (input("Please enter value input. Type 0 to play double player or type 1 to play single player: "))   
   
    option = int(option)
   
    while option != 0 and option != 1: #input validation
        option= int(input("Please enter value input. Type 0 to play double player or type 1 to play single player: "))
    
    option = int(option)
  
    return(option) #returns the option


def numout(option): #asks user for digits they want to play for and does input validation and does the first step depending on the option entered
    
    numdigits = (input("Please enter the number of digits you want to play for: ")) #asking for number of digits
    while numdigits.isdigit() == False: #input validation
        numdigits= (input("Please enter value input. Please enter the number of digits you want to play for: "))   
   
    numdigits = int(numdigits)
     
    if option == 0:   #if double player
        #num = int(input(f"Please enter the {numdigits} digit number: "))
        num = getpass.getpass(f'Player 1: please enter the {numdigits} digit number: ') #asking user to input number (hidden)
        num = int(num)
        while ((len((str(num)))) != numdigits): #input validation
            print(f'Invalid input! The number was {(len(list(str(num))))} digits')
            num = getpass.getpass(f'Player 1: please enter the {numdigits} digit number: ')
            num = int(num)
    
    elif option == 1: #if single player
        num = random.randrange(10**(numdigits-1), (10**numdigits))  #random number in the range of digits entered
    return(numdigits,num) #returns number of digits and the actual number


def game(numdigits,num): #the calculation function that checks number guessed to the actual number.
    n = int(input(f"Guess the {numdigits} digit number: "))
      
    # condition to check the input. function terminates if true.
    if (n == num):  
        print("Wow! You guessed the number in just 1 try! You are truely a Mastermind!")
        return(1)
    
    else:    
        ctrx = 0  #initializes variable for number of tries the player takes to guess the number.      
       
        while (n != num):   #iterates until user gets answer right
       
            ctrx += 1  #adds every time the loop is executed
            count = 0 #variable to check how many digits were guessed right
           
            n = str(n)   # converting to a string in order to take digits
            num = str(num)  
            correct = ['X']*numdigits # stores correct answer places
      
            for i in range(0, numdigits):  #runs for the number of digits entered
      
                if (n[i] == num[i]):  # checking if digits match
                    count += 1  # counts increments
                    correct[i] = n[i]  #changing correct list accordingly
                else:
                    continue
      
            # if not all digits are guessed correctly.
            if (count < numdigits) and (count != 0):  
                print("Not all the digits were correct, but you did get ", count, " digit(s) correct!")
                print("These numbers were correct.")
                for k in correct:
                    print(k, end=' ')
                print('\n')
        
                n = int(input("Enter your next choice of numbers: "))
      
            # if none are guessed correctly.
            elif (count == 0):  
                print("None of the numbers in your input match.")
                n = int(input("Enter your next choice of numbers: "))
        
    # condition for equality.
            if n == num:  
                print("You have become a Mastermind!")
                print(f"It took you only, {ctrx}, tries.")
        
    return(ctrx) #returns the tries


def main():
    #function calls
    option1 = option() #getting the option
    numdigits, num = numout(option1) #getting number of digits and actual number
    #checking what to do based on option
    if option1 == 1: 
        game(numdigits,num) #checks using the computer generated number
    if option1 == 0:     
        p1 = game(numdigits,num) #checks using player enetered number
        num = m2.player2(numdigits)  #asks the player 2 to enter the number
        p2 = game(numdigits,num) #checks using player enetered number
        print()
        
        #decides the winner depending about the tries
        if p1 > p2: 
            print("Player 1: You are the winner")
        elif p2 > p1: 
            print("Player 2: You are the winner")
        if p1 == p2:
            print("You guys tied")
        
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    