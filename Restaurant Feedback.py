##################################
#                                #
#   This programe was made by    #
#                                #
#     Abdulrahman Basalamah      #
#                                #
#    Basalamah.a@hotmail.com     #
#                                #
##################################
-	-----	 -		---	- -		--	-- -			-	-	 -		-		-- -			--	- -		----	 -		-	--- -		-		-	 -		----	 -		-			- --	----- -	----	- -		----	 -			--		 -		----	 -		-		-- -		----	 -		-		-	 -		----	 -		-	--- 
from tkinter import *

window = Tk()
window.title("^_^ 3bodi & azoz ^_^")
#             (العرضXالطول)
window.geometry("320x390")
portee= IntVar()
portee1= IntVar()
portee11= IntVar()
portee111= IntVar()
#==================================================================================
entroo = Label(window,text = "! جامعة الأمير مقرن", font = "times 16")
entroo.grid (row = 1 , column = 30 , columnspan = 4 )
#==================================================================================
def effacer():
    br1.select()
    br2.select()
    br3.select()
    br4.select()
#==================================================================================

genbtn =  Label(window,text = "!الخدمة العامة كانت جيدة", font = "times 14")
witbtn =  Label(window,text = "! نظافة المطعم", font = "times 14")
cokbtn =  Label(window,text = "!الطعام كان مطهو جيدأً", font = "times 14")
sirbtn =  Label(window,text = "!اتلقى خدمات سريعة", font = "times 14")


genbtnE = Label(window,text = "The general service was good!", font = "times 14")
witbtnE = Label(window,text = "Clean restaurant!", font = "times 14")
cokbtnE = Label(window,text = "The food was cocked as I like!", font = "times 14")
sirbtnE = Label(window,text = "I'm getting a fast service!", font = "times 14")

#==================================================================================

br1 =        Radiobutton(window,text = "Nothing",value = 6 ,variabl = portee)
very_good1 = Radiobutton(window,text = "5",value = 5 ,variabl = portee)
good1 =      Radiobutton(window,text = "4",value = 4 ,variabl = portee)
normal1 =    Radiobutton(window,text = "3",value = 3 ,variabl = portee)
bad1 =       Radiobutton(window,text = "2",value = 2 ,variabl = portee)
very_bad1 =  Radiobutton(window,text = "1",value = 1 ,variabl = portee)


br2 =        Radiobutton(window,text = "Nothing",value = 6 ,variabl = portee1)
very_good2 = Radiobutton(window,text = "5",value = 5 ,variabl = portee1)
good2 =      Radiobutton(window,text = "4",value = 4 ,variabl = portee1)
normal2 =    Radiobutton(window,text = "3",value = 3 ,variabl = portee1)
bad2 =       Radiobutton(window,text = "2",value = 2 ,variabl = portee1)
very_bad2 =  Radiobutton(window,text = "1",value = 1 ,variabl = portee1)


br3 =        Radiobutton(window,text = "Nothing",value = 6 ,variabl = portee11)
very_good3 = Radiobutton(window,text = "5",value = 5 ,variabl = portee11)
good3 =      Radiobutton(window,text = "4",value = 4 ,variabl = portee11)
normal3 =    Radiobutton(window,text = "3",value = 3 ,variabl = portee11)
bad3 =       Radiobutton(window,text = "2",value = 2 ,variabl = portee11)
very_bad3 =  Radiobutton(window,text = "1",value = 1 ,variabl = portee11)


br4 =        Radiobutton(window,text = "Nothing",value = 6 ,variabl = portee111)
very_good4 = Radiobutton(window,text = "5",value = 5 ,variabl = portee111)
good4 =      Radiobutton(window,text = "4",value = 4 ,variabl = portee111)
normal4 =    Radiobutton(window,text = "3",value = 3 ,variabl = portee111)
bad4 =       Radiobutton(window,text = "2",value = 2 ,variabl = portee111)
very_bad4 =  Radiobutton(window,text = "1",value = 1 ,variabl = portee111)
#==================================================================================

genbtn.grid       ( row = 2 , column = 30 , columnspan = 4 )
witbtn.grid       ( row = 6 , column = 30 , columnspan = 4 )
cokbtn.grid       ( row = 10 , column = 30 , columnspan = 4 )
sirbtn.grid       ( row = 14 , column = 30 , columnspan = 4 )
#==================================================================================
genbtnE.grid      ( row = 3 , column = 30 , columnspan = 4 )
witbtnE.grid      ( row = 7 , column = 30 , columnspan = 4 )
cokbtnE.grid      ( row = 11 , column = 30 , columnspan = 4 )
sirbtnE.grid      ( row = 15 , column = 30 , columnspan = 4 )
#==================================================================================

very_good1.grid   (row = 4 , column = 34 , columnspan = 4 )
good1.grid        (row = 4 , column = 32 , columnspan = 4 )
normal1.grid      (row = 4 , column = 30 , columnspan = 4 )
bad1.grid         (row = 4 , column = 28 , columnspan = 4 )
very_bad1.grid    (row = 4 , column = 26 , columnspan = 4 )
very_good2.grid   (row = 8 , column = 34 , columnspan = 4 )
good2.grid        (row = 8 , column = 32 , columnspan = 4 )
normal2.grid      (row = 8 , column = 30 , columnspan = 4 )
bad2.grid         (row = 8 , column = 28 , columnspan = 4 )
very_bad2.grid    (row = 8 , column = 26 , columnspan = 4 )
very_good3.grid   (row = 12 , column = 34 , columnspan = 4 )
good3.grid        (row = 12 , column = 32 , columnspan = 4 )
normal3.grid      (row = 12 , column = 30 , columnspan = 4 )
bad3.grid         (row = 12 , column = 28 , columnspan = 4 )
very_bad3.grid    (row = 12 , column = 26 , columnspan = 4 )
very_good4.grid   (row = 16 , column = 34 , columnspan = 4 )
good4.grid        (row = 16 , column = 32 , columnspan = 4 )
normal4.grid      (row = 16 , column = 30 , columnspan = 4 )
bad4.grid         (row = 16 , column = 28 , columnspan = 4 )
very_bad4.grid    (row = 16 , column = 26 , columnspan = 4 )
#==================================================================================

Close = Button(window,text="Close", font = "times 14", command = window.destroy)
Close.grid(row = 20 , column = 25 , columnspan = 4)


reset = Button(window,text="Reset", font = "times 14",command = effacer)
reset.grid(row = 20 , column = 28 , columnspan = 4  )

supmit = Button(window,text="Submit!", font = "times 14")
supmit.grid(row = 20 , column = 33 , columnspan = 4  )

#==================================================================================
def enter(li):
    file = open(n1+".txt","w")
    file.write("Username:"+li[0]+"\n")
    file.write("Gender:"+li[1]+" \n")
    file.write("Age:"+ li[2]+"\n")
    file.write("Height:"+li[3]+"\n")
    file.write("Your goal:"+li[4]+"\n")
    file.close()

#----------------
"""
print("Welcome!")
print("Are you a new user? ")
b = input("print 'yes' or 'no'")

if b=="yes":
    a = int(input("Please enter (1) to fill the following information, (2) to fill the features or (3) to exit "))

    if a ==1:
        n1 = input("Username: ")
        n2 = input("Gender: ")
        n3 = input("Age: ")
        n4 = input("Height: ")
        n5 = input("Current weight: ")
        li = [n1,n2,n3,n4,n5]

        print("Do you want to fill the features? ")
        r=int(input('enter (1) to continue or (2) to exist'))
        if r==1:
            print("your goal:")
            print("choose the number that presents your goal:")
            m1=int(input("1_Lose weight"+"\n"+"2_Gain weight"+"\n"+"3_Maintain"))
            m2=int(input("What's your weekly goal:"))
            print('How active are you?')
            m3=int(input('1_Not very active(spend most of the day sitting e.g. bankteller,desk job)'+'\n'+'2_Lightly active(spend a good part of the day on your feet e.g. teacher,salesperson)'+'\n'+'3_Active(spend a good part of the day doing some physical activity e.g. food server,postal carrier)'+'\n'+'4_Very active(spend most of the day doing heavy physical activity e.g. bike messenger, carpenter)'))
            if m3==1:
                m3==12
            elif m3==2:
                m3==13
            elif m3==3:
                m3==14
            else:
                m3==15
            li2 = [m1,m2,m3]



        else:
            quit()

    elif a==2:
        print("your goal:")
        print("choose the number that presents your goal:")
        m1=int(input("1_Lose weight"+"\n"+"2_Gain weight"+"\n"+"3_Maintain"))
        m2=int(input("What's your weekly goal:"))
        print('How active are you?')
        m3=int(input('1_Not very active(spend most of the day sitting e.g. bankteller,desk job)'+'\n'+'2_Lightly active(spend a good part of the day on your feet e.g. teacher,salesperson)'+'\n'+'3_Active(spend a good part of the day doing some physical activity e.g. food server,postal carrier)'+'\n'+'4_Very active(spend most of the day doing heavy physical activity e.g. bike messenger, carpenter)'))
        WhICL7nAK1Nu69SYMU5gUgoDP2+IcOmPmafhtzBy42wxUsEtcJXynAVQyBOiiAN2q/wkOelCUtacz1hEz7ghOf4nuFCzEsgCCifkUsU6+WuFy1HUYuBIDbXzYIxmDDMyu0ArZNIAe37zXZf6badooJm/wbW+n5LNyqfFLi1GMUIgo8D0gzmISO9y1KOmxOY79u7c5eEjKz7Q62Jal28E9efBfZVYI8GDexYfDHJkj4luosgMqDUNFK6kdidKt6Bd
        if m3==1:
            m3==12
        elif m3==2:
            m3==13
        elif m3==3:
            m3==14
        else:
            m3==15
        li2 = [m1,m2,m3]
        print("Do you want to fill the informations? ")
        t=int(input('enter (1) to continue or (2) to exist'))

        if t==1:
            n1 = input("Username: ")
            n2 = input("Gender: ")
            n3 = input("Age: ")
            n4 = input("Height: ")
            n5 = input("Current weight: ")
            li = [n1,n2,n3,n4,n5]
        else:
            quit()
    else:
        quit()
else:
    c = input("Enter your file name: ")
    print('Do you want to update or enter new informaions?')
    i=int(input('type 1 for the update or 2 for start again.'))
    if i==1:
        #go to the user's file
    else:
        n1 = input("Username: ")
        n2 = input("Gender: ")
        n3 = input("Age: ")
        n4 = input("Height: ")
        n5 = input("Current weight: ")
        li = [n1,n2,n3,n4,n5]

"""

#output___________________________

if m1==3:
    pound=(n5*2.2)#convert to pound
    daily_need=pound*m3
    print('Your daily need of calories is:',daily_need,'claorie')
    carbs_need=(0.4*daily_need)/4
    print('40% carbohydrate',carbs_need,'gram')
    protein_need=(0.4*daily_need)/4
    print('40% protein',protein_need,'gram')
    fat_need=(0.2*daily_need)/9
    print('20% fat',fat_need,'gram')
elif m1==2:
    pound=(n5*2.2)#convert to pound
    daily_need=(pound*m3)+500
    print('Your daily need of calories is:',daily_need,'claorie')
    carbs_need=(0.4*daily_need)/4
    print('40% carbohydrate',carbs_need,'gram')
    protein_need=(0.4*daily_need)/4
    print('40% protein',protein_need,'gram')
    fat_need=(0.2*daily_need)/9
    print('20% fat',fat_need,'gram')
elif m1==1:
    pound=(n5*2.2)#convert to pound
    daily_need=(pound*m3)-500
    print('Your daily need of calories is:',daily_need,'claorie')
    carbs_need=(0.4*daily_need)/4
    print('40% carbohydrate',carbs_need,'gram')
    protein_need=(0.4*daily_need)/4
    print('40% protein',protein_need,'gram')
    fat_need=(0.2*daily_need)/9
    print('20% fat',fat_need,'gram')

window.mainloop()
