
import random

def checkalpha(password):
     ''' Returns True if a uppercase and lowercase alpahabetic charather is contained in password'''
     letuppercase=False
     letlowercase=False
     for x in password:
         if(x.isupper()):
             letuppercase=True
         if(x.islower()):
              letlowercase=True

     if(letuppercase and letlowercase):
          return True
     else:
          return False


def checknum(password):
     '''Returns True if a number is contained in the password'''
     for x in password: 
        if(x.isdigit()):
            return True

     return False

def checkchar(password):
     '''Returns True if a special character is contained in the password'''
     for x in password:
        if(x == '.' or "," or "/" or '?' or '>' or '<' or x == "'" or x == ':' or x == ';' or x == '!' or x == '@' or x == '#' or x == '$' or x == '%' or x == '^' or x == '&' or x == '*' or x == '(' or x == ')' or x == '-' or x == '+' or x == '=' or x == '_' or x == '[' or x == ']' or x == '{' or x == '}'):
            return True

     return False


def checkpassword(password):
     '''Returns True if the password contains a specail character,number and alpahabetical letter'''
     if(checkalpha(password) and checknum(password) and checkchar(password)):
        return True
     else:
        return False

def getchar():
     '''Returns a random Uppercase or Lowercase character'''
     chars=['a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
     random.shuffle(chars)
     toreturn = chars[random.randint(0,24)]
     if(random.randint(1,2)==2):
          return toreturn.upper()
     
     else:
          return toreturn
     
def getspecialchar():
     '''Returns a special character'''
     specialchars=['.',',',"'",'<','>','/','?',';',':',"'",'[',']','{','}','!','@','#',"$",'%','^','&','*','(',')','-','_','+','=']
     random.shuffle(specialchars)
     return specialchars[random.randint(0,27)] 

def makepassword(length):
     '''Returns a password'''
     password=[]
     choices=['c','n','s']
     random.shuffle(choices)
     for let in range(0,length):
          choiceindex=random.randint(0,2)
          if(choices[choiceindex]=='c'):
               password.append(getchar())
          elif(choices[choiceindex]=='n'):
               password.append(str(random.randint(0,9)))
          else:
               password.append(getspecialchar())

     return ''.join(password)

    
def main():
     '''Main program'''
     print('Welcome to the password generator! How long of a password do you want?')
     length = int(input())
     if(length<1):
          print('You can\'t do that! Try entering a number greater than 1')
          main()
     while(True):
          currentpassword=makepassword(length)
         
          if(checkpassword(currentpassword)):
               break
          else:
               continue

     print("Your password is \n{}".format(currentpassword))

main()
    
