from difflib import get_close_matches
import json
import time

""" Intracting page """
def home_page():
    print("""  
           ***********************************************************************************************************************************************************************
          *                                                                                                                                                                      *
          *                                                              THIS IS BARNAAN DICTIONARY                                                                              * 
          *                                                                                                                                                                      *
          *                                                                   find any word or                                                                                   *
          *                                                                   customize and                                                                                      *
          *                                                                    add yourown                                                                                       *
          *                                                                       word                                                                                           *
          *                                                                                                                                                                      *
          *                                                                                                                                                                      *
          *                                                                                                                                                                      *
           **********************************************************************************************************************************************************************
               """)
    time.sleep(1)
    print("""  
                                                                   { 1. Start Searching     }
             """)
    time.sleep(1)
    print("""  
                                                                   { 2. About the Developer }
          """)
    
    time.sleep(1)
    print("""  
                                                                   { 0. Exit }    
       """)
    try:
      choice = int(input("your choice : "))
      if choice == 0:
          exit()
      elif choice == 1:
          main()
      elif choice == 2:
             print("""  
           ***********************************************************************************************************************************************************************
          *                                                                                                                                                                      
          *                                                              software engineer Barnabas Tekkalign                                                                            
          *                                                                                                                                                                      
          *                                                              programming languages :  python, dart, javascript , java, c++,  and c#      
          *                                                              Frameworks: Django, flutter, laravel
          *                                                              contact me: barnaantekalign@gmail.com 
          
                            I'm happy to collaborate in projects that involves the above languages or frameworks, Thanks for visting my github repo.
          *                                                                                                                                                      
          *                                                                                                                                                                      
          *                                                                                                                                                                     
          *                                                                                                                                                                      
           ***********************************************************************************************************************************************************************
               """)
      else:
          print("Invalid Input")
          
    
    except:
        print("Invalid Input")
        
        
        
        
        
        
        
# to convert the stored json data to python dictionary

file = open('data.json','r') 
data = json.load(file)
file.close()
def add_new_word(word):
    defination = input("insert defination of your word ")
    data[word] = [defination]
    file = open('data.json','w')
    file.write(json.dumps(data))
    file.close()
    return "you have sucessfully added a new word !"

def translate(word):
    if word in data: 
        return data[word]
    else:
        guessed_list = get_close_matches(word,data.keys(),n=5)
        words_length = len( guessed_list )
        if words_length == 0 :
            yes_or_no = input ("the word you searched for does not exist in the dictionary! do you want to add it ? Y/N : ").lower()
            if yes_or_no  == 'y':
              return  add_new_word(word)
            elif yes_or_no  == 'n':
                return "Thank you"
            else: 
                return "Invalid Input"
            
        else:
            count = 1
            for item in guessed_list: 
                if count == 1:
                     print( " no word matches your search !  is there any word match your intention in the following ", words_length ," words?") 
                print("[",count , "] " + item)
                count += 1
            yes_or_no = input("Y/N : ").lower()
            if   yes_or_no  == "y":
                try:
                    index = int(input('select index number : '))
                    return data[guessed_list[index-1]]
                except:
                    return "Invalid input"
            elif  yes_or_no == "n":
                yes_or_no  = input(" do you want to add your new word to the dictionary? Y/N: ").lower()

                if yes_or_no  =="y":
                  return  add_new_word(word)
                elif yes_or_no  == "n":
                    return "your word doesn't exist in the dictionary"
                else: 
                    return "Invalid Input"
            else: 
                return "Invalid Input"
            
                     
def main():    
    while True:
        word = input("Word: ")
        if word ==  "0":
            break
        output = translate(word)
        if type(output) == list:
        	for item in output:
        		print(item)
        else:
        	print(output)
  

home_page()
