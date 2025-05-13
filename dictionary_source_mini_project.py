#dictionary project

dictionary={}

while True:
    print("1. Add a word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")

    selection=int(input("selection the option:"))

    if selection==1:
        Word=input("enter the word:").lower()
        meaning=input("enter the meaning:").lower()
        dictionary[Word]=meaning
        print("word added to dictionary successfully")

    elif selection==2:
        word=input("enter the word:").lower()
        print(dictionary.get(word))

    elif selection==3:
        word=input("enter the word:").lower()
        print(dictionary.items())
    elif selection==4:
        word=input("enter the word:").lower()
        meaning=input("enter the meaning:")
        dictionary[word]=meaning
        print("word updated to dictionary successfully:")
    elif selection==5:
        word=input("enter the word:").lower()
        dictionary.pop(Word)
        print("the given word is deletd successfully:")
    elif selection==6:
                  print("successfully exites")
                  break
    


   

       

        
              


    

      

     



    

       

          

          


            


        

            

        
         


   
      
       
    
    
 
    
    















