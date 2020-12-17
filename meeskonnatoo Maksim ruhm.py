import random
iD=0 #global id for each object - глобальный ИД для всех объектов (включая дочерних) этого типа
footballSociety=[] #global society of captains and players - всё сообщество созданных игроков (ну или людей)
class Person:
    id #local id declaration - декларируем локальный ид, чтобы задать его каждому объекту этого класса
    skill=0
    team=0 #team nubmer - переменная для команды
    def __init__(self,t,s):
        global iD 
        global footballSociety
        self.team=t #team selection - выбор команды при создании объекта
        self.id=iD #this objects id - причисление ИД-номера при создании объекта
        iD+=1 #id change for next object - меняем глобальный ИД на +1, чтобы следующий объект был с другим ИД
        self.skill=s #persons football playing skill - устанавливаем умение игрока
        #every time person is created, he is added to and can be found in footbalSociety
        #каждый раз при создании игрока или капитана, он будет записан в массив footbalSociety, чтобы после чемпионата можно было проверить каждого игрока во всех прошедших играх
        footballSociety.append(self) 
        
        
    def getSkill(self): #we could use just h1.skill, but whatever, i cant explain why i added this
        return self.skill #мы могли использовать h1.skill, поэтому я даже не могу объяснить, почему сделал так
    def getId(self): #the same as getSkill() func - то же самое, что и строчкой выше
        return self.id
    def getPerson(self): #and when i was writing this it just hits me. but this func just contains print line i need, so this is fine
        #при создании этого метода, меня вдруг осенило, что можно было использовать...  но сама строчка уже нужна была
        print("This persons skill level is ", self.getSkill()," and he played in team ", self.team)
        
class Captain(Person):
    spec="Captain" #when searching for a player to define if it was a captain - когда позже будем искать игрока, чтобы понять, что это был капитан и действовать соответственно
    win=0 #each Captain starts with zero amount of wins - у всех капитанов на старте ни одной победы
    def winUp(self):
        self.win=self.win+1 #win - собсна, победа одного из капитанов
    def getWins(self):
        return self.win
        
class footbalPlayer(Person):
    spec="player"
    def followCaptain(self,Captain): #footbalPlayer plays in a team of one of the captains - игрок играет за одного из капитанов
        print("footbalPlayer #", self.id, " follows Captain #", Captain.id)

h1=Captain(1, random.randint(7, 10)) #new Captains must have high playing skills - у капитанов обязан быть высокий уровень игры
h2=Captain(2, random.randint(7, 10))

#now game begins
game=True
while game:
    team1=[] #team of captain 1 creation - команда для первого капитана
    for i in range(10): #football team consists of 11 players, and the captain is one of them - в команде 11 игроков, и капитан один из них
        team1.append(footbalPlayer(1,random.randint(1, 10)))
    team2=[] #team of captain 2 creation команда 2
    for i in range(10):
        team2.append(footbalPlayer(2,random.randint(1, 10)))
    
    teamSkill_1=h1.getSkill() #counting team skill, captains skill is always the same after captain craation - берём скиллы каждого из игроков, и прибавляем их к скиллу капитана
    for i in range (len(team1)): #but each player skill is different in every game (different players) - при каждой игре у капитана всегда один и тот же скилл, а у игроков всегда разный
        teamSkill_1+=team1[i].getSkill() #so we get each players skill and add it cumulatively to captains skill - потому что игроки при каждой игре разные
    
    teamSkill_2=h2.getSkill() #same for team 2 - то же самое для команды 2
    for i in range (len(team2)):
        teamSkill_2+=team2[i].getSkill()
    print(teamSkill_1," and ", teamSkill_2)
    #next fragment is skill comparison to define who won - сравнение скилла для определения победителя
    if teamSkill_1>teamSkill_2:
        h1.winUp()
        print("Captain 1 wins ", h1.getWins(), " times!")
    elif teamSkill_1<teamSkill_2:
        h2.winUp()
        print("Captain 2 wins ", h2.getWins(), " times!")
    else:
        print("Draw!") #this code makes draw quite rare - в данной программе ничья крайне редка
    
    if int(input("To continue enter 1, to exit enter any other number"))!=1: #just to stop the games - для остановки матчей
        game=False
        print("Championship statistics!\nTeam 1 with captains skill level ",h1.getSkill()," won ",h1.getWins()," times!") #championship results - выдаём результаты чемпионата по всем сыгранным матчам
        print("And team 2 with captains skill level ",h2.getSkill()," won ", h2.getWins(), " times!")
        #lets try to find a player and get his skill level and team - пробуем найти игрока и показать уровень его скилла и за какую он команду
        #search starts after championship is ended, so we enter another loop for it - поиск начинается после окончания всех игр, и для этого отдельный цикл
        search=True
        while search:
            ans=input("Enter players id to know his skill and team he played in") #введи ид игрока для поиска, либо exit для выхода из цикла
            if ans=="exit": #to exit this loop
                search=False
            elif int(ans)<=iD: #iD is global and unique for each created person type - ИД глобальная переменная и уникальна для каждого из созданных игроков или капитанов
                for k in range(len(footballSociety)): #search in footbalSociety for a player - ищем в том массиве нужного игрока
                    if footballSociety[k].getId()==int(ans):#and if id fits then this is right player - и если ид совпадает, то это искомый игрок
                        if footballSociety[k].spec=="Captain": #if this is a captain, add one more line with wins- если это капитан, то добавляем ещё одну строку с числом побед
                            print("This person is a Captain and he won ",footballSociety[k].getWins()," times!")
                        footballSociety[k].getPerson()
            else:
                print("There is no person with this ID!") #Нет человека с таким ИД
            