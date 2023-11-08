import textwrap
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
    

welcome="""Hello! Welcome to my escape room! I'd recommend having a piece of paper (graph paper will be the most useful) and pencil nearby to help you throughout the escape room. It'll also be a better experience if you turn the sound up, but it's not necessary to do so. There will be some occasions where you will have to type words into the command line, and for those times, it's crucial that you spell the words correctly, as precision is key in this escape room. Please only type into the command line when directed to, and please only use lowercase letters when answering questions, except when you're asked for your name. Keep in mind that it's always best to use resources that are given to you. Most importantly, have fun!"""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
print("")
while True:
    x=input("Type 'ready' when you want to start: ")
    if x=="Ready" or x=="ready":
        print("")
        name=input("Great! What would you like your name to be? ")
        break
    else:
        print("Type 'ready' when you want to start: ")
print("")
while True:
    answer=input("Welcome, " + name + ". Type 'yes' to confirm your name, and type 'no' if you want to change it: ")
    if answer=='yes':
        print("")
        print("What would you like your pronouns to be in this escape room?")
        break
    elif answer=='no':
        name=input("Type what you want your name to be: ")      
pronouns=input("1 = she/her, 2 = he/him, 3 = they/them, 4 = other: ")
print("")
welcome="""To set the scene, it's the summer before your sophomore year of high school, and you just moved to a new district. You signed up for a building tour, and you're currently waiting outside the school for your tour guide to show up."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
import time
time.sleep(10)
print("")
print("Just as you're starting to get impatient, you spot a tall girl with curly red hair walking towards you.")
time.sleep(5)
print("")
print("The girl smiles enthusiastically at you and says,", "'Hi, you must be " + name + ". My name is Scarlett.'")
time.sleep(3)
print("")
welcome="""Scarlett: I'm going to be showing you around the school today. I'm going to be a senior this year, so I've already spent a lot of time in this school. Sunville High School is such a great place, and I'm sure you'll love it here."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(7)
print("")
welcome="""She leads you to a pair of doors next to each other, and she uses a small key to unlock the door on the left."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
print("You hear the door slam shut behind you.")
time.sleep(3)
import winsound
winsound.PlaySound(resource_path("door.wav"), winsound.SND_FILENAME)
print("")
welcome="""You look around and notice that the interior of the school is a lot nicer than you expected. The floors are freshly polished, the trophy case is packed full, and there isn't the typical school smell of sweat mixed with bad body odor."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(10)
print("")
welcome="""Scarlett: Sunville High School is great, but it's pretty basic as far as schools go. Our graduating class last year had 75 students, so you'll get to know everyone here really well."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(10)
print("")
welcome="""Scarlett: One thing I love about this school is that it's hard to get lost because there's only one floor, with most of the classrooms branching off of the main hallway."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(10)
print("")
welcome="""Scarlett: The custodian unlocked all of the classroom doors this morning in preparation for the teachers coming in to get their classrooms ready, so I should be able to show you inside your classrooms."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(10)
print("")
welcome="""Scarlett: I'm about to throw a bunch of dimensions at you, so I'd recommend pulling out paper and pencil so that you can draw an accurate map of the building that will help you once the school year starts. You should probably give your map a scale of 4 ft because each floor tile is 4 ft by 4 ft. I'll stop and give you time to add to your map regularly throughout the tour."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(15)
print("")
welcome="""Scarlett: Right now, we're standing on the 4th tile forward from the leftmost front door in a hallway that extends 8 ft to either side of the front doors. A fun fact about this school is that all of the doors in the building are 4 ft wide. The door that's 12 ft to your right is the door to the Math Room, and the door that's 8 ft to your left is the door to the Science Room. Would you like to enter the Science Room?"""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
ciencias=input("'yes' or 'no': ")
print("")
matematicas=0
if ciencias=="yes" or ciencias=="Yes":
    matematicas+=1
    welcome="""Scarlett: Welcome to the Science classroom. The back wall is 40 ft away from the door, and the room extends 16 ft to the right of the door and 12 ft to the left of the door, so the leftmost wall is in line with the front door."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    school=input("Type 'done' once you finish adding to your map: ")
    while True:
        while school!="done":
            school=input("Type 'done' once you finish adding to your map: ")
        break
    print("")
    welcome="""Scarlett: I'm not sure how precise the dimensions will have to be on your map, but it's still helpful to have them be pretty accurate in case something happens because the school administration hasn't gotten around to printing maps for everyone."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(10)
    print("")
    welcome="""Scarlett: Mr. John, the Science teacher, isn't here right now, but it looks like Avery is. Avery was a member of the Science Olympiad team last year as an 8th grader, and his team won first place in a national competition."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(10)
    print("")
    print("Scarlett: Hi, Avery. This is " + name + ", a rising 10th grader who's new to the district.")
    time.sleep(3)
    print("")
    if pronouns=='1':
         print("Scarlett: I'm giving her a tour so that she doesn't get lost once the year starts.")
    elif pronouns=='2':
        print("Scarlett: I'm giving him a tour so that he doesn't get lost once the year starts.")
    elif pronouns=='3':
        print("Scarlett: I'm showing them around so that they don't get lost once the year starts.")
    else:
        print("Scarlett: I'm giving " + name + " a tour of the building right now.")
    time.sleep(5)
    print("")
    welcome="""Avery smiles at you, then returns to what he was working on before you walked in: combining different substances in a beaker to form a metallic blue liquid."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(10)
    print("")
    welcome="""Scarlett: There's not much else to see in here, as the rest is pretty self-explanatory, so I'll move on with the tour to not distract Avery any further."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    print("Scarlett leads you out of the room and right across the hall to a door with several math puns taped to it.")
else:
    print("Scarlett: Okay, let's move on to the next classroom.")
    time.sleep(5)
    print("")
    print("Scarlett leads you across the hall to a door covered with math puns.")
time.sleep(5)
print("")
print("Scarlett: I'm going to show you inside the Math Room because it's my favorite classroom in the building.")
time.sleep(5)
print("")
if matematicas==1:
    welcome="""Scarlett pushes open the door and tells you that this room has similar dimensions to the previous room - the back wall is 40 ft in front of you, and the room extends 12 ft to the right of the door and 16 ft to the left of the door."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    school=input("Type 'done' once you finish adding to your map: ")
    while True:
        while school!="done":
            school=input("Type 'done' once you finish adding to your map: ")
        break
    print("")
    welcome="""The main difference between this room and the Science Room is that these walls are covered from the floor to the ceiling with math riddles. The one closest to you reads: 'Why are obtuse angles so sad? Because they're never right.'"""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(10)
    print("")
else:
    welcome="""Scarlett pushes open the door and tells you that the back wall is 40 ft in front of you, and the room extends 12 ft to the right of the door and 16 ft to the left of the door."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    school=input("Type 'done' once you finish adding to your map: ")
    while True:
        while school!="done":
            school=input("Type 'done' once you finish adding to your map: ")
        break
    print("")
    welcome="""One thing that stands out to you is that the classroom walls are covered from the floor to the ceiling with math riddles. The one closest to you reads: 'Why are obtuse angles so sad? Because they're never right.'"""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(10)
    print("")
print("You estimate that there are around 25 desks in the room, each with a small basket next to it.")
time.sleep(5)
print("")
welcome="""Scarlett: Our school doesn't have lockers, so everyone is required to place their cell phones in these baskets at the start of class. I've learned that some teachers get too caught up in their teaching to notice if students are on their phones, but it's probably better to stay on the assumption that the teachers can see your every move."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(10)
print("")
print("Scarlett: Do you want to move on to the next classroom or spend more time looking around?")
answer=input("'stay' or 'go': ")
print("")
while True:
    if answer=="stay" or answer=="Stay":
        welcome="""You walk over to the windows, noting that they're all taped shut. Scarlett tells you that a couple of years ago, some seniors decided to jump out of the classroom windows to prove their bravery, but several of them ended up in the hospital with broken bones, so the administration ended up sealing all of the building windows."""
        first=textwrap.TextWrapper(width=100)
        hi=first.fill(text=welcome)
        print(hi)
        time.sleep(10)
        print("")
        print("You spend some more time browsing through the room before deciding to continue with the tour.")
        time.sleep(5)
        print("")
        break
    elif answer=="go" or answer=="Go":
        break
    else:
        print("Scarlett: Would you like to move on or spend more time here?")
        answer=input("'stay' or 'go': ")
welcome="""You turn to the right after leaving the classroom, and Scarlett leads you ahead 20 ft so that the door to the History classroom is on your right and there's a medieval-looking knight in front of you."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(15)
print("")
welcome="""The knight's armor is rusting, and it's radiating a faint smell of something rotten, although you're not sure why."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
welcome="""You must have a disgusted expression on your face because Scarlett says, 'Oh, that's just Spencer. He's our school mascot. A group of seniors put him outside the History door 20 years ago as a senior prank, and he hasn't been moved since. His mouth opens and closes, and sometimes people will toss their trash inside his mouth if they're too lazy to find a trash can.'"""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(15)
print("")
print("That explains the smell.")
time.sleep(5)
print("")
print("Scarlett directs your attention back to the tour and opens the door to your right.")
time.sleep(5)
print("")
if matematicas==1:
    welcome="""With some quick mental calculations, you figure out that the room is the same size as the Math and Science rooms, except this room extends 28 ft to the left of the door and there is a wall to the right of the door."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
else:
    welcome="""With some quick mental calculations, you figure out that the room is the same size as the Math room, except this room extends 28 ft to the left of the door and there is a wall to the right of the door."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
school=input("Type 'done' once you finish adding to your map: ")
while True:
    while school!="done":
        school=input("Type 'done' once you finish adding to your map: ")
    break
print("")
print("You see a teacher sitting at her desk, and the nameplate on her desk reads 'Ms. Snow.'")
time.sleep(5)
print("")
print("Ms. Snow: Hi! Are you " + name + "?")
time.sleep(2)
print("")
print("You nod, wondering how she already knows who you are.")
time.sleep(5)
print("")
welcome="""As if reading your mind, Ms. Snow says, 'We rarely get new students, and the freshman class has already been introduced to all the teachers, so every new student is a cause for celebration among the students and teachers. I'm guessing pretty much everyone in the building already knows who you are.'"""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(10)
print("")
print("It looks like any hopes you had of flying under the radar are gone.")
time.sleep(5)
print("")
print("Scarlett: Well, Ms. Snow, I'm sure you're very busy, so we'll let you get back to your work.")
time.sleep(3)
print("")
if pronouns=='1':
    this='her'
    print("Scarlett: I just wanted " + name + " to get the chance to meet one of " + this + " teachers.")
elif pronouns=='2':
    this='his'
    print("Scarlett: I just wanted " + name + " to get the chance to meet one of " + this + " teachers.")
elif pronouns=='3':
    this='their'
    print("Scarlett: I just wanted " + name + " to get the chance to meet one of " + this + " teachers.")
else:
    print("Scarlett: I just wanted to introduce you to " + name + ".")
time.sleep(5)
print("")
print("Ms. Snow smiles and waves goodbye as you leave the room.")
time.sleep(5)
print("")
print("Scarlett leads you directly across the hall to another door.")
time.sleep(5)
print("")
print("Scarlett: This is the door to the English Room. Would you like to go in?")
inglesh=input("'yes' or 'no': ")
stomach=0
if inglesh=="yes" or inglesh=="Yes":
    print("")
    stomach+=1
    welcome="""Scarlett: Just like all of the other rooms you've been in, the English Room is 40 ft long and 32 ft wide, although the door is at the far left in this room, with the room extending 28 ft to the right of the door."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    school=input("Type 'done' once you finish adding to your map: ")
    while True:
        while school!="done":
            school=input("Type 'done' once you finish adding to your map: ")
        break
    print("")
    welcome="""Scarlett: You get to read some great books during your sophomore year. My personal favorite was 'Great Expectations,' although I know that book isn't for everyone. A bunch of my friends enjoyed 'Little Fires Everywhere,' which is the first book you'll read this year."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)    
    time.sleep(10)
    print("")
    welcome="""You glance around the room while Scarlett is talking, and you notice that, just like in the Math Room, the walls are covered with posters. This time though, they're posters of what you presume are the books you'll be reading this year."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(10)
    print("")
    welcome="""Scarlett: Mrs. Williams, the English teacher, has a special system where she gives certain classes an ice cream party if nobody in the class misbehaves for two full weeks."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(10)
    print("")
    welcome="""Your stomach rumbles just thinking about it. Scarlett must hear that because she tells you that you only have a couple of rooms left before you'll get to the cafeteria, where there is always free food being handed out."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(10)
    print("")
    print("Scarlett: We should probably move on to get to the cafeteria quicker.")
    time.sleep(5)
    print("")
    welcome="""You follow Scarlett back into the hallway, and you turn to the left and walk forward 44 ft so that the door to the Spanish Room is on your left."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
else:
    print("")
    welcome="""You turn to the left and walk forward 44 ft so that the door to the Spanish Room is on your left."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
time.sleep(5)
print("")
print("Scarlett: Would you like to enter the room?")
espanol=input("'yes' or 'no': ")
if espanol=="yes" or espanol=="Yes":
    print("")
    welcome="""Scarlett opens the door and says that the dimensions are the same as the previous rooms, except the door is 12 ft from the leftmost wall."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    print("")
    school=input("Type 'done' once you finish adding to your map: ")
    while True:
        while school!="done":
            school=input("Type 'done' once you finish adding to your map: ")
        break
    print("")
    welcome="""You took Spanish at your previous school, but you always viewed it as a class where you could slack off with no consequences. Your hopes of continuing that trend are shattered when you see the rigorous work plan taped to the wall. You think to yourself, 'Who in their right mind would memorize 5 verb tenses in a month?'"""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(10)
    print("")
    if stomach==1:
        print("Your stomach rumbles audibly once again, so you decide to leave the room without looking around much.")
    else:
        print("Your stomach rumbles audibly, and you decide to leave the room without looking around much so that you'll get to the cafeteria quicker.")
    time.sleep(5)
print("")
welcome="""Scarlett leads you across the hall to the Nurse's Office, which she says is half the size of the other rooms you've been in so far, with the room extending 40 ft outward but only 12 ft to the right of the door."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
school=input("Type 'done' once you finish adding to your map: ")
while True:
    while school!="done":
        school=input("Type 'done' once you finish adding to your map: ")
    break
print("")
welcome="""Scarlett: As you can tell by looking around, this is like your typical Nurse's Office, with a cot at the back of the room and several medical books lying around. If you ever need a break from your classes, just tell your teacher you have a headache, and they'll let you come here to lie down for the rest of the period. Not like I've ever done that or anything."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(10)
print("")
print("You smile, but you know you'd get a firm lecture from your parents if they ever found out you did that.")
time.sleep(5)
print("")
print("Scarlett: I'm going to continue with the tour so that we don't run out of time.")
time.sleep(5)
print("")
welcome="""You walk out of the Nurse's Office, turn to the right, walk forward one floor tile, then turn right again so there's a long hallway ahead of you with a small door at the end."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
welcome="""Scarlett: This is the best part of the school because teachers don't care about what happens in this hallway. It's 72 feet long and 4 ft wide, and the door you see at the end is the door to the Janitor's closet."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(10)
print("")
print("Scarlett leads you 48 ft down the hallway to a place where there are doors on either side of you.")
time.sleep(10)
print("")
welcome="""From the door on your right, you hear what sounds like an amateur band practice, although most of it just sounds like kids playing around with drums."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
winsound.PlaySound(resource_path("band.wav"), winsound.SND_FILENAME)
time.sleep(5)
print("")
welcome="""Scarlett: In case you couldn't tell, the room on your right side is the Band Room, and the marching band is in there practicing right now."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
while True:
    print("Scarlett: Which music elective did you sign up for this year?")
    music=input("1=chorus, 2=band, 3=orchestra: ")
    if music=='1':
        break
    elif music=='2':
        break
    elif music=='3':
        break
print("")
if music=='2':
    welcome="""Scarlett: I'll show you inside the room so that you can get a sense of what your band classes will be like next year."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    welcome="""Scarlett opens the door, and you see a room noticeably smaller than the previous classrooms - it's 16 ft by 16 ft (Scarlett says all the music classrooms are this size), and the door is 4 ft away from the rightmost side of the room."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    school=input("Type 'done' once you finish adding to your map: ")
    while True:
        while school!="done":
            school=input("Type 'done' once you finish adding to your map: ")
        break
    print("")
    welcome="""Everyone stops playing when they see you. A girl holding a clarinet makes her way over to you and introduces herself as Caroline."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    print("Caroline: Hi, you must be " + name + ".")
    time.sleep(2)
    print("")
    print("Ms. Snow was right when she said everyone in the school already knows who you are.")
    time.sleep(5)
    print("")
    welcome="""Caroline: The school band meets every day to practice, and we have 4 concerts during the year. You can also choose to join the marching band if you want to. I'm the leader of the marching band, and I've been conducting our summer rehearsals. Once the school year starts, we'll meet after school every Monday and Thursday to practice."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(10)
    print("")
    welcome="""Caroline: Feel free to look around the room, but I'm going to go back to practicing right now since the marching band has a performance on the first day of school."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    print("Scarlett: Do you want to look around?")
    answer=input("'yes' or 'no': ")
    print("")
    if answer=="yes":
        welcome="""Since the room is pretty small, there's not much to see other than the large group of students practicing. There is a bin in the back corner of the room, but upon further inspection, you realize it's empty."""
        first=textwrap.TextWrapper(width=100)
        hi=first.fill(text=welcome)
        print(hi)
        time.sleep(5)
        print("")
        print("You can tell that Scarlett is itching to move on with the tour, so you decide to leave the room.")
        time.sleep(5)
        print("")
    else:
        print("Scarlett: Ok, let's move on with the tour.")
        time.sleep(2)
        print("")
        print("Scarlett leads you out of the room.")
        time.sleep(2)
        print("")
elif music=='3':
    print("That's cool. We'll get to that room later.")
    time.sleep(5)
    print("")
elif music=='1':
    print("We'll get to that room next.")
    time.sleep(3)
    print("")
print("Scarlett: The Chorus Room is directly across from the Band Room.")
time.sleep(5)
print("")
if music=='1':
    welcome="""Scarlett: I'll show you inside so that you know what to expect once the year starts."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    welcome="""Scarlett opens the door, and you see a room noticeably smaller than the previous classrooms - it's 16 ft by 16 ft (Scarlett says all the music classrooms are this size), and the door is 8 ft away from the rightmost side of the room."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    school=input("Type 'done' once you finish adding to your map: ")
    while True:
        while school!="done":
            school=input("Type 'done' once you finish adding to your map: ")
        break
    print("")
    welcome="""Scarlett: The room is empty right now, but during the school year it's packed full of students. The door that you see at the back of the room leads you to a storage closet that all of the music teachers share. I've personally never taken chorus, but I've heard that if you misbehave in class then you have to stay after school to clean the closet."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(10)
    print("")
    welcome="""Scarlett: That's pretty much the only interesting thing in this room. I'll move on with the tour so that you can finish soon."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    print("Scarlett leads you back into the hallway.")
    time.sleep(2)
    print("")
else:
    welcome="""Scarlett: You probably won't ever have to go in this room, so I won't waste time showing you the classroom."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
print("You walk 16 ft farther down the hallway to another place with doors on either side of you.")
time.sleep(10)
print("")
print("From the door on your right, you hear someone playing the same section of music repeatedly.")
winsound.PlaySound(resource_path("updatedcello.wav"), winsound.SND_FILENAME)
winsound.PlaySound(resource_path("updatedcello.wav"), winsound.SND_FILENAME)
winsound.PlaySound(resource_path("updatedcello.wav"), winsound.SND_FILENAME)
print("")
print("It all sounds exactly the same to you, but the person must be doing something different every time.")
time.sleep(5)
print("")
welcome="""Scarlett: That's the Orchestra Room. Not many people take Orchestra here, and people often use the room as a personal practice room like someone's doing right now."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
if music=='3':
    welcome="""Scarlett: I'll show you inside so that you know what to expect once the year starts."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    welcome="""Scarlett opens the door, and you see a room noticeably smaller than the previous classrooms - it's 16 ft by 16 ft (Scarlett says all the music classrooms are this size), and the door is 8 ft away from the leftmost side of the room."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    school=input("Type 'done' once you finish adding to your map: ")
    while True:
        while school!="done":
            school=input("Type 'done' once you finish adding to your map: ")
        break
    print("")
    welcome="""There is a boy playing cello in the room, and he's so engrossed in his music that he doesn't notice you come in."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    welcome="""Scarlett whispers to you, 'That's James. He's the first chair cello in the school orchestra.'"""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    print("James finally notices you and stops practicing his piece.")
    time.sleep(5)
    print("")
    welcome="""James: Hi, sorry I didn't see you there. I was just trying to perfect the piece that I'm playing for districts this year, but I keep messing up the dynamics."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    print("James: I'll show you around the room to familiarize you with it.")
    time.sleep(5)
    print("")
    welcome="""James: As you can see, the chairs are arranged in a semi-circle so that we can hear each other when we play. Everyone's cases go against the back wall, but mine is the only case there right now."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(10)
    print("")
    welcome="""James: That's pretty much it. I'd love to stay and talk, but I have to perfect this piece before my audition tomorrow, so I'm going to go back to practicing."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    print("James goes back to playing the same section of his piece.")
    winsound.PlaySound(resource_path("updatedcello.wav"), winsound.SND_FILENAME)
    winsound.PlaySound(resource_path("updatedcello.wav"), winsound.SND_FILENAME)
    print("")
    welcome="""Scarlett: We should probably leave James to his practicing so that we don't distract him."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    print("Scarlett leads you back into the hallway.")
    time.sleep(2)
    print("")
else:
    welcome="""Scarlett: I won't stop here since you aren't taking Orchestra this year."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
print("Scarlett: Right across from the Orchestra Room is the Library.")
time.sleep(5)
print("")
welcome="""Scarlett opens the door to the Library, and you see a room that's the same size as the music classrooms, with the door 4 ft away from the leftmost wall."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
school=input("Type 'done' once you finish adding to your map: ")
while True:
    while school!="done":
        school=input("Type 'done' once you finish adding to your map: ")
    break
print("")
welcome="""Scarlett: This is one of the saddest libraries I've ever seen in my life because there are probably only 50 books here. The room is mostly used as a social space for students when they aren't in class."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
welcome="""You look around and see that Scarlett was right - there's only one bookshelf, and the rest of the room is taken up by large tables."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
welcome="""You're itching to finish the tour and get back to watching Netflix, so you tell Scarlett that you're ready to go to the next room, and she leads you back into the hallway."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
welcome="""Scarlett: If you continue 8 ft farther down the hallway, then the door to the Janitor's closet will be right in front of you. In the interest of time, I won't show you inside since it's just like every other janitor's closet you've encountered in your lifetime."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(10)
print("")
welcome="""Scarlett leads you back down the hallway, and you turn right once you come back into the main hallway. Once you walk forward 8 ft, you see a door on your right."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(10)
print("")
welcome="""Scarlett: This is the door to the Main Office. I think the principal is coming in later today, but I can still show you around the room now."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
print("Scarlett opens the door, and you see a very narrow room that's also surprisingly empty for an office.")
time.sleep(5)
print("")
welcome="""Scarlett: The room extends 40 ft outward, but it's only 12 ft wide, with the room extending 4 ft from either side of the door."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
school=input("Type 'done' once you finish adding to your map: ")
while True:
    while school!="done":
        school=input("Type 'done' once you finish adding to your map: ")
    break
print("")
welcome="""Scarlett: Usually this room is crammed with people complaining about school, which is why there isn't much in the room except for a large desk at the back where the principal usually sits to field complaints."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
welcome="""Scarlett: You probably won't have to spend much time here unless you misbehave frequently. I have faith in you to stay out of trouble, though."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
print("You smile, knowing that you've always been great at behaving well.")
time.sleep(5)
print("")
welcome="""You ask Scarlett to continue with the tour since you don't think you'll have to know much about this room."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
welcome="""You follow Scarlett back into the hallway, where you turn right and walk forward 4 tiles so that there's a door to your right."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
print("Scarlett: This is the Guidance Office. Would you like to go in?")
goff=input("'yes' or 'no': ")
print("")
if goff=="Yes" or goff=="yes":
    welcome="""Scarlett opens the door, and you see a room the same size as the Main Office, but in this room, the leftmost wall is directly to the left of the door, and the room extends 8 ft to the right of the door."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    school=input("Type 'done' once you finish adding to your map: ")
    while True:
        while school!="done":
            school=input("Type 'done' once you finish adding to your map: ")
        break
    print("")
    welcome="""Scarlett: The only time you're required to meet with Ms. Quinn, the guidance counselor, is when you're completing the college application process. However, feel free to visit Ms. Quinn whenever you have questions for her, or if you just want someone to talk to."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(10)
    print("")
    welcome="""Ms. Quinn's desk is in the back left corner, and there is a jar full of lollipops on her desk. Do you want to take one?"""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    lollipop=input("'yes' or 'no': ")
    print("")
    if lollipop=="Yes" or lollipop=="yes":
        print("You take one and unwrap it immediately. It's chocolate flavored, your favorite.")
        time.sleep(5)
        print("")
    welcome="""When you look around the room, you realize that it's a typical Guidance Office: inspirational posters on the wall, pamphlets about destressing scattered around the room, and various chairs in the room that are supposed to be comfortable but really make your back hurt for days."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    print("You're not a big fan of inspirational posters, so you go back into the hallway.")
    time.sleep(5)
    print("")
else:
    welcome="""Scarlett: I don't blame you. It's not a very interesting place. Okay, I just have one more place to show you before we can end our tour in the cafeteria."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
welcome="""Scarlett leads you ahead 12 ft, then right 8 ft, so that you end up in front of a door that's directly to the right of another door."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
print("Scarlett: These are the doors to the Gymnasium.")
time.sleep(5)
print("")
welcome="""Scarlett pushes the doors open, and you see a room that is much larger than the other rooms that you've encountered."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
welcome="""Scarlett: The gym here is massive because Sunville High students really like sports. It only extends 36 feet outwards, but it's 104 ft wide with 48 ft on either side of the doors."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
school=input("Type 'done' once you finish adding to your map: ")
while True:
    while school!="done":
        school=input("Type 'done' once you finish adding to your map: ")
    break
print("")
print("You spot a rope attached to the ceiling that's hanging in the center of the room, which intrigues you.")
time.sleep(4)
print("")
print("Would you like to try climbing up it?")
rope=input("'yes' or 'no': ")
print("")
if rope=="Yes" or rope=="yes":
    welcome="""Despite Scarlett's half-hearted protests, you walk over to the rope and glance up to see how tall it is. It's definitely taller than anything you've ever climbed."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    welcome="""However, it's height is what prompts you to start climbing. You think to yourself that you'll be fine if you fall because there's a thick mat underneath you."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    welcome="""You only make it 10 ft up the rope before your arms give out and you fall back onto the mat. You were right to think that it would cushion your landing, but a spark of pain still shoots through your back, and you know that you'll be feeling that tomorrow."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    welcome="""When you glance back over at Scarlett, you can tell that she's trying her hardest to stifle her laughter."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    print("You walk back over to her and ask if there's anything else to do in the gym.")
    time.sleep(5)
    print("")
else:
    welcome="""That's probably for the better because the mat underneath the rope doesn't look thick enough to cushion your landing."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
welcome="""Scarlett: As you can see from here, there is a supply closet in the back corner of the room. That's where all of the sports equipment is stored. Unfortunately, it's locked right now, and the gym teacher is the only person with the key, so there isn't much else to do here unless you want to run laps around the gym."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
print("Do you want to run around?")
run=input("'yes' or 'no': ")
print("")
if run=="Yes" or run=="yes":
    print("You only make it 5 laps around the gym before you collapse on the floor from exhaustion.")
    time.sleep(5)
    print("")
    welcome="""Scarlett: We should probably go to the cafeteria now so that you still have enough energy for the rest of the day."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
welcome="""You follow Scarlett back into the hallway through the door on your right. She leads you 16 ft forward and 8 ft to the right so that you're standing in front of the cafeteria door."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
welcome="""When she opens the door, you see that the cafeteria is 40 ft long and 20 ft wide, with the door 4 ft away from the leftmost wall."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
school=input("Type 'done' once you finish adding to your map: ")
while True:
    while school!="done":
        school=input("Type 'done' once you finish adding to your map: ")
    break
print("")
welcome="""Your eyes are immediately drawn to the snack bar that's against the back wall. You spot a plate of cookies and a bowl of apples."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
welcome="""Scarlett: Help yourself to the food over there. The snacks at the snack bar are free, then there's a vending machine to the right of that where you can buy junk food."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
print("What food do you want?")
food=input("1=free food, 2=vending machine food: ")
print("")
if food=='1':
    print("You walk over to the snack bar and grab an apple and a cookie.")
    time.sleep(5)
    print("")
    welcome="""The food is a lot better than you expected from cafeteria food, and it's enough to stop your stomach from grumbling."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    welcome="""After you finish eating, your mouth feels dry, so you walk over to a water fountain on the opposite side of the cafeteria."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
elif food=='2':
    welcome="""You walk over to the vending machine and press the number to give you a bag of chips. You're happy that you brought money with you because the chips cost $1."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    welcome="""The food is a lot better than you expected from cafeteria food, and it's enough to stop your stomach from grumbling."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
    time.sleep(5)
    print("")
    welcome="""After you finish eating, your mouth feels dry, so you walk over to a water fountain on the opposite side of the cafeteria."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
else:
    welcome="""You don't stop to get any food, but your mouth feels dry, so you walk over to a water fountain on the opposite side of the cafeteria."""
    first=textwrap.TextWrapper(width=100)
    hi=first.fill(text=welcome)
    print(hi)
time.sleep(5)
print("")
print("Once you quench your thirst, you go back over to where Scarlett is standing.")
time.sleep(5)
print("")
welcome="""Scarlett: That's pretty much it for the tour. I don't think there's anything else that I have to show you."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
print("Scarlett: I'll lead you back outside now.")
time.sleep(2)
print("")
welcome="""You start to follow Scarlett, then realize that you have to go to the bathroom because you drank so much water. You ask Scarlett if there's a bathroom in the school."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
print("Scarlett: Of course, how could I forget that? I'll show you where it is.")
time.sleep(5)
print("")
print("She leads you to a door directly to the left of the Guidance Office door.")
time.sleep(5)
print("")
print("Scarlett: I'll wait for you outside the school.")
time.sleep(5)
print("")
welcome="""You open the door and see a small room that's 8 ft wide, with the room extending 4 ft to the left of the door, and 16 ft long. It's a pretty basic bathroom, with only a sink and a toilet in the room."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
school=input("Type 'done' once you finish adding to your map: ")
while True:
    while school!="done":
        school=input("Type 'done' once you finish adding to your map: ")
    break
print("")
welcome="""Once you're ready to leave, you walk over to the front door, only to find that it won't open. You push against it, but it still won't move. You hear Scarlett calling to you from the other side of the door."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
welcome="""Scarlett: A couple of years ago, the principal changed the locks to keep the front door locked from both sides except at the beginning and end of the day because students kept leaving campus in the middle of the day. I had a key with me, but I can't find it now, so I must have dropped it in one of the rooms. I followed Ms. Snow out of the building because she had a key, but she already left."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(10)
print("")
print("Scarlett: I'm so sorry, " + name + ", but I think you'll have to search all of the classrooms for my key.")
time.sleep(5)
print("")
welcome="""Now's when the fun part begins. Scarlett's key is somewhere inside the school building, and it's up to you to find it."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
time.sleep(5)
print("")
welcome="""Instructions: Use the map that you drew to navigate your way around the school. You'll be prompted to type your movement into the command line, and that's how you'll move around the building. 'f' makes you move forward 4 ft, 'l' makes you move to the left 4 ft, 'r' makes you move to the right 4 ft, 'b' makes you move backward 4 ft, and 'o' makes you open a door. Please note that moving to the left and right doesn't turn you in that direction, so you're always facing away from the front doors. Whenever you're inside a room, you won't have to use these commands, and instead, you either type 'e' to exit the room or 's' to search the room. Use only lowercase letters when entering your movement. Right now, you're standing in front of the same front door you entered, and you're facing in the opposite direction from the door."""
first=textwrap.TextWrapper(width=100)
hi=first.fill(text=welcome)
print(hi)
print("")
while True:
    x=input("Type 'ready' when you want to start: ")
    if x=="Ready" or x=="ready":
        break
print("")
w='wall'
x='emptyspace'
s='sciencedoor'
m='mathdoor'
h='historydoor'
e='englishdoor'
sp='spanishdoor'
mo='mainoffice'
caf='cafeteria'
br='bathroom'
go='guidanceoffice'
no='nurseoffice'
b='banddoor'
c='chorusdoor'
l='librarydoor'
o='orchdoor'
j='janitorcloset'
g='gymdoor'
k='knight'
f='frontdoor'
school_layout =[
[w,w,w,g,g,w,w,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,br],
[w,x,x,x,x,x,x,go],
[caf,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,mo],
[w,x,x,x,x,x,x,w,w,w,w,w,w,w,w,w,w,w,c,w,w,w,l,w,w],
[w,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,j],
[sp,x,x,x,x,x,x,no,w,w,w,w,w,w,w,w,w,w,b,w,w,w,o,w,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,k,w],
[e,x,x,x,x,x,x,h],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[s,x,x,x,x,x,x,m],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[w,x,x,x,x,x,x,w],
[w,w,w,f,f,w,w,w]]
x=29
y=3
position=school_layout[x][y]
hkey=0
jkey=0
fkey=0
mkey=0
collision=0
success=0
kn=0
his=0
ja=0
ma=0
while success==0:
    person=input("Type how you want to move: ")
    if person=='f':
        if school_layout[x-1][y]=='wall':
            print("You run into a wall.")
            collision+=1
            if collision==10:
                welcome="""You have to sit down for 15 seconds to allow your body to recover from running into the wall so many times."""
                first=textwrap.TextWrapper(width=100)
                hi=first.fill(text=welcome)
                print(hi)
                time.sleep(15)
                collision-=10
        if school_layout[x-1][y]=='gymdoor':
            print("You run into the door to the Gymnasium.")
        if school_layout[x-1][y]=='chorusdoor':
            print("You run into the door to the Chorus Room.")
        if school_layout[x-1][y]=='librarydoor':
            print("You run into the door to the Library.")
        if school_layout[x-1][y]=='knight':
            print("You run into the knight statue.")
            print("Would you like to search it?")
            answer=input("'yes' or 'no': ")
            print("")
            if answer=="yes":
                if kn==0:
                    welcome="""You stick your hand down the knight's throat and you feel your fingers brush up against many slimy things. After a minute of rummaging through the old garbage in the knight's mouth, you feel something sharp."""
                    first=textwrap.TextWrapper(width=100)
                    hi=first.fill(text=welcome)
                    print(hi)
                    print("Would you like to pull it out to see what it is?")
                    statue=input("'yes' or 'no': ")
                    print("")
                    if statue=='yes':
                        welcome="""You pull it out through the knight's mouth, and you see that it's a key covered in an unidentifiable slime. You wipe it off and put it in your pocket."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        jkey+=1
                        kn+=1
                    print("Would you like to keep searching through the knight's mouth?")
                    search=input("'yes' or 'no': ")
                    print("")
                    if search=='yes':
                        welcome="""You spend some more time feeling through the knight's mouth, but you don't find anything else other than garbage."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                else:
                    print("You don't find anything other than garbage.")
        if school_layout[x-1][y]=='emptyspace':
            x-=1
            position=school_layout[x][y]
    elif person=='b':
        if school_layout[x+1][y]=='wall':
            print("You run into a wall.")
            collision+=1
            if collision==10:
                welcome="""You have to sit down for 15 seconds to allow your body to recover from running into the wall so many times."""
                first=textwrap.TextWrapper(width=100)
                hi=first.fill(text=welcome)
                print(hi)
                time.sleep(15)
                collision-=10
        if school_layout[x+1][y]=='frontdoor':
            print("You run into the front door.")
        if school_layout[x+1][y]=='nurseoffice':
            print("You run into a wall.")
        if school_layout[x+1][y]=='banddoor':
            print("You run into the door to the Band Room.")
        if school_layout[x+1][y]=='orchdoor':
            print("You run into the door to the Orchestra Room.")
        if school_layout[x+1][y]=='knight':
            print("You run into the knight statue.")
            print("Would you like to search it?")
            answer=input("'yes' or 'no': ")
            print("")
            if answer=="yes":
                if kn==0:
                    welcome="""You stick your hand down the knight's throat and you feel your fingers brush up against many slimy things. After a minute of rummaging through the old garbage in the knight's mouth, you feel something sharp."""
                    first=textwrap.TextWrapper(width=100)
                    hi=first.fill(text=welcome)
                    print(hi)
                    print("Would you like to pull it out to see what it is?")
                    statue=input("'yes' or 'no': ")
                    print("")
                    if statue=='yes':
                        welcome="""You pull it out through the knight's mouth, and you see that it's a key covered in an unidentifiable slime. You wipe it off and put it in your pocket."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        jkey+=1
                        kn+=1
                    print("Would you like to keep searching through the knight's mouth?")
                    search=input("'yes' or 'no': ")
                    print("")
                    if search=='yes':
                        welcome="""You spend some more time feeling through the knight's mouth, but you don't find anything else other than garbage."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                else:
                    print("You don't find anything other than garbage.")
        if school_layout[x+1][y]=='emptyspace':
            x+=1
            position=school_layout[x][y]
    elif person=='l':
        if school_layout[x][y-1]=='wall':
            print("You run into a wall.")
            collision+=1
            if collision==10:
                welcome="""You have to sit down for 15 seconds to allow your body to recover from running into the wall so many times."""
                first=textwrap.TextWrapper(width=100)
                hi=first.fill(text=welcome)
                print(hi)
                time.sleep(15)
                collision-=10
        if school_layout[x][y-1]=='sciencedoor':
            print("You run into the door to the Science Room.")
        if school_layout[x][y-1]=='englishdoor':
            print("You run into the door to the English Room.")
        if school_layout[x][y-1]=='spanishdoor':
            print("You run into the door to the Spanish Room.")
        if school_layout[x][y-1]=='cafeteria':
            print("You run into the door to the Cafeteria.")
        if school_layout[x][y-1]=='knight':
            print("You run into the knight statue.")
            print("Would you like to search it?")
            answer=input("'yes' or 'no': ")
            print("")
            if answer=="yes":
                if kn==0:
                    welcome="""You stick your hand down the knight's throat and you feel your fingers brush up against many slimy things. After a minute of rummaging through the old garbage in the knight's mouth, you feel something sharp."""
                    first=textwrap.TextWrapper(width=100)
                    hi=first.fill(text=welcome)
                    print(hi)
                    print("Would you like to pull it out to see what it is?")
                    statue=input("'yes' or 'no': ")
                    print("")
                    if statue=='yes':
                        welcome="""You pull it out through the knight's mouth, and you see that it's a key covered in an unidentifiable slime. You wipe it off and put it in your pocket."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        jkey+=1
                        kn+=1
                    print("Would you like to keep searching through the knight's mouth?")
                    search=input("'yes' or 'no': ")
                    print("")
                    if search=='yes':
                        welcome="""You spend some more time feeling through the knight's mouth, but you don't find anything else other than garbage."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                else:
                    print("You don't find anything other than garbage.")
        if school_layout[x][y-1]=='emptyspace':
            y-=1
            position=school_layout[x][y-1]
    elif person=='r':
        if school_layout[x][y+1]=='wall':
            print("You run into a wall.")
            collision+=1
            if collision==10:
                welcome="""You have to sit down for 15 seconds to allow your body to recover from running into the wall so many times."""
                first=textwrap.TextWrapper(width=100)
                hi=first.fill(text=welcome)
                print(hi)
                time.sleep(15)
                collision-=10
        if school_layout[x][y+1]=='mathdoor':
            print("You run into the door to the Math Room.")
        if school_layout[x][y+1]=='historydoor':
            print("You run into the door to the History Room.")
        if school_layout[x][y+1]=='nurseoffice':
            print("You run into the door to the Nurse's Office.")
        if school_layout[x][y+1]=='janitorcloset':
            print("You run into the door to the Janitor's Closet.")
        if school_layout[x][y+1]=='mainoffice':
            print("You run into the door to the Main Office.")
        if school_layout[x][y+1]=='guidanceoffice':
            print("You run into the door to the Guidance Office.")
        if school_layout[x][y+1]=='bathroom':
            print("You run into the bathroom door.")
        if school_layout[x][y+1]=='knight':
            print("You run into the knight statue.")
            print("Would you like to search it?")
            answer=input("'yes' or 'no': ")
            print("")
            if answer=="yes":
                if kn==0:
                    welcome="""You stick your hand down the knight's throat and you feel your fingers brush up against many slimy things. After a minute of rummaging through the old garbage in the knight's mouth, you feel something sharp."""
                    first=textwrap.TextWrapper(width=100)
                    hi=first.fill(text=welcome)
                    print(hi)
                    print("Would you like to pull it out to see what it is?")
                    statue=input("'yes' or 'no': ")
                    print("")
                    if statue=='yes':
                        welcome="""You pull it out through the knight's mouth, and you see that it's a key covered in an unidentifiable slime. You wipe it off and put it in your pocket."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        jkey+=1
                        kn+=1
                    print("Would you like to keep searching through the knight's mouth?")
                    search=input("'yes' or 'no': ")
                    print("")
                    if search=='yes':
                        welcome="""You spend some more time feeling through the knight's mouth, but you don't find anything else other than garbage."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                else:
                    print("You don't find anything other than garbage.")
        if school_layout[x][y+1]=='emptyspace':
            y+=1
            position=school_layout[x][y+1]
    elif person=='o' and school_layout[x][y+1]=='mathdoor':
        while True:
            print("")
            print("What would you like to do in the Math Room?")
            math=input("'e' or 's': ")
            if math=='e':
                print("You leave the room, and you're standing right outside the door now.")
                time.sleep(3)
                print("")
                break
            elif math=='s':
                welcome="""When you glance around the room, you notice the teacher's desk, the phone baskets, and a supply closet."""
                first=textwrap.TextWrapper(width=100)
                hi=first.fill(text=welcome)
                print(hi)
                time.sleep(3)
                while True:
                    print("")
                    print("What would you like to look at?")
                    maths=input("'d'=desk, 'b'=baskets, 'c'=closet, 'e'=exit: ")
                    if maths=='e':
                        print("You leave the room, and you're standing right outside the door now.")
                        time.sleep(3)
                        print("")
                        break
                    elif maths=='d':
                        welcome="""You walk over to the teacher's desk and search for a key, but all you find is a stack of attendance lists that you presume are for the upcoming year."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(5)
                    elif maths=='b':
                        welcome="""You walk up and down the rows of desks, peering in all of the baskets, but they're all empty except for one which has a used piece of gum stuck to the bottom of it."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(5)
                    elif maths=='c':
                        welcome="""You pry open the closet doors, hoping that Scarlett's key somehow ended up in here, but you only see a pile of cleaning supplies organized on a rack."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(5)
                    else:
                        print("That's not a valid action.")
                break
            else:
                print("That's not a valid move.")
    elif person=='o' and school_layout[x][y+1]=='historydoor':
        print("The door is locked because Ms. Snow already left.")
        print("Do you have the key?")
        answer=input("'yes' or 'no': ")
        if answer=='yes':
            if hkey==1:
                welcome="""You pull out the keychain from the Janitor's closet and try the keys in the lock until one of them works and the door swings open."""
                first=textwrap.TextWrapper(width=100)
                hi=first.fill(text=welcome)
                print(hi)
                while True:
                    print("What would you like to do in the History Room?")
                    history=input("'e' or 's': ")
                    if history=='e':
                        print("You leave the room, and you're standing right outside the door now.")
                        time.sleep(3)
                        print("")
                        break
                    elif history=='s':
                        mouse=1
                        welcome="""When you glance around the room, you see the whiteboard, a cupboard at the back of the room, and the teacher's desk."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(3)
                        while True:
                            print("")
                            print("What would you like to look at?")
                            histories=input("'w'=whiteboard, 'c'=cupboard, 'd'=desk, 'e'=exit: ")
                            if histories=='e':
                                print("You leave the room, and you're standing right outside the door now.")
                                time.sleep(3)
                                print("")
                                break
                            elif histories=='w':
                                welcome="""You scan the area around the whiteboard for Scarlett's key, but all you find is some dry erase markers."""
                                first=textwrap.TextWrapper(width=100)
                                hi=first.fill(text=welcome)
                                print(hi)
                                time.sleep(5)
                            elif histories=='c':
                                if mouse==2:
                                    print("All you see inside the cupboard is textbooks.")
                                    time.sleep(3)
                                if mouse==1:
                                    welcome="""When you open the cupboard doors, a small mouse scurries out over your feet. You jump up in surprise, banging your hand on the door in the process. When you finally calm down enough to look inside the cupboard, you see rows of textbooks and nothing else."""
                                    first=textwrap.TextWrapper(width=100)
                                    hi=first.fill(text=welcome)
                                    print(hi)
                                    time.sleep(5)
                                    mouse+=1
                            elif histories=='d':
                                if his==0:
                                    welcome="""You walk over to Ms. Snow's desk, and you spot an open jar on her desk. Inside the jar is a key, and you're guessing that Ms. Snow found it on the floor and put it on her desk to be reclaimed. Would you like to pick up the key?"""
                                    first=textwrap.TextWrapper(width=100)
                                    hi=first.fill(text=welcome)
                                    print(hi)
                                    answer=input("'yes' or 'no': ")
                                    if answer=='yes':
                                        fkey+=1
                                        print("You put the key in your pocket.")
                                    his+=1
                                else:
                                    print("You see the empty jar on the desk where you found a key earlier.")
                                    time.sleep(3)
                            else:
                                print("That's not a valid action.")
                        break
                    else:
                        print("That's not a valid move.")
            else:
                print("You search in your pockets for the key but then realize you don't actually have it.")
                print("Without the key, you're not able to go into the room.")
        else:
            print("Without the key, you're not able to go into the room.")
    elif person=='o' and school_layout[x][y+1]=='nurseoffice':
        while True:
            print("")
            print("What would you like to do in the Nurse's Office?")
            nurse=input("'e' or 's': ")
            if nurse=='e':
                print("You leave the room, and you're standing right outside the door now.")
                time.sleep(3)
                print("")
                break
            elif nurse=='s':
                print("You find a first-aid kit, a cot with blankets on it, and a cabinet with medicine bottles.")
                time.sleep(3)
                while True:
                    print("")
                    print("What would you like to look at more closely?")
                    nurses=input("'f'=first-aid kit, 'c'=cot, 'cab'=cabinet, 'e'=exit: ")
                    if nurses=='e':
                        print("You leave the room, and you're standing right outside the door now.")
                        time.sleep(3)
                        print("")
                        break
                    elif nurses=='f':
                        print("You see a couple of band-aids, some tweezers, and a pair of gloves, but nothing else.")
                        time.sleep(5)
                    elif nurses=='c':
                        print("You don't find anything hidden among the blankets.")
                        time.sleep(3)
                    elif nurses=='cab':
                        print("The cabinet doors are locked, and you don't have the key.")
                        time.sleep(3)
                    else:
                        print("That's not a valid action.")
                break
            else:
                print("That's not a valid move.")
    elif person=='o' and school_layout[x][y+1]=='janitorcloset':
        print("The door is locked.")
        print("Do you have the key?")
        answer=input("'yes' or 'no': ")
        if answer=='yes':
            if jkey==1:
                print("You find that the key from the knight fits perfectly into the keyhole.")
                time.sleep(4)
                welcome="""The door opens, and you see that the closet is 4 ft wide, 8 ft long, and barely tall enough for you to fit inside."""
                first=textwrap.TextWrapper(width=100)
                hi=first.fill(text=welcome)
                print(hi)
                while True:
                    print("")
                    print("What would you like to do in the Janitor's Closet?")
                    janitor=input("'e' or 's': ")
                    if janitor=='e':
                        print("You leave the room, and you're standing right outside the door now.")
                        time.sleep(3)
                        print("")
                        break
                    elif janitor=='s':
                        welcome="""The Janitor's closet is pretty crowded, not surprisingly. The things that stand out to you are 2 buckets full of supplies and a jacket hanging from a hook on the wall."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(3)
                        while True:
                            print("")
                            print("What would you like to look at more closely?")
                            janitors=input("'1'=bucket #1, '2'=bucket #2, 'j'=jacket, 'e'=exit: ")
                            if janitors=='e':
                                print("You leave the room, and you're standing outside the door now.")
                                time.sleep(3)
                                print("")
                                break
                            elif janitors=='1':
                                welcome="""When you dig through the bucket, all you find is old mop parts that still smell faintly of cleaning materials."""
                                first=textwrap.TextWrapper(width=100)
                                hi=first.fill(text=welcome)
                                print(hi)
                                time.sleep(5)
                            elif janitors=='2':
                                welcome="""You pull everything out of the bucket to make sure you don't miss anything important, but all you find is Lysol wipes."""
                                first=textwrap.TextWrapper(width=100)
                                hi=first.fill(text=welcome)
                                print(hi)
                                time.sleep(5)
                            elif janitors=='j':
                                if ja==0:
                                    welcome="""You pat the jacket, trying to feel for a key. You finally reach something that seems out of place, located in one of the jacket pockets. You stick your hand into the pocket and pull out a keychain with around 10 keys attached to it."""
                                    first=textwrap.TextWrapper(width=100)
                                    hi=first.fill(text=welcome)
                                    print(hi)
                                    time.sleep(5)
                                    print("")
                                    print("You pocket the keychain just in case it will be helpful later.")
                                    time.sleep(3)
                                    hkey+=1
                                    ja+=1
                                else:
                                    print("You don't find anything in the jacket.")
                                    time.sleep(3)
                            else:
                                print("That's not a valid action.")
                        break
                    else:
                        print("That's not a valid move.")
            else:
                print("You search in your pockets for the key but then realize you don't actually have it.")
                print("Without the key, you're not able to go into the room.")
        else:
            print("Without the key, you're not able to go into the room.")
    elif person=='o' and school_layout[x][y+1]=='mainoffice':
        while True:
            print("")
            print("What would you like to do in the Main Office?")
            main=input("'e' or 's': ")
            if main=='e':
                print("You leave the room, and you're standing right outside the door now.")
                time.sleep(3)
                print("")
                break
            elif main=='s':
                welcome="""You see a desk at the back of the room, along with a file cabinet along the right wall that's right next to a lost and found bin."""
                first=textwrap.TextWrapper(width=100)
                hi=first.fill(text=welcome)
                print(hi)
                time.sleep(3)
                while True:
                    print("")
                    print("What would you like to look at?")
                    mains=input("'d'=desk, 'c'=cabinet, 'l'=lost and found, 'e'=exit: ")
                    if mains=='e':
                        print("You leave the room, and you're standing outside the door now.")
                        time.sleep(3)
                        print("")
                        break
                    elif mains=='d':
                        if ma==0:
                            mkey+=1
                            welcome="""You look through each of the desk drawers, hoping you'll find something useful, and in the bottom right drawer, you come across a small key. You pick it up, hoping that it will be useful later."""
                            first=textwrap.TextWrapper(width=100)
                            hi=first.fill(text=welcome)
                            print(hi)
                            winsound.PlaySound(resource_path("drawer.wav"), winsound.SND_FILENAME)
                            winsound.PlaySound(resource_path("drawerclosing.wav"), winsound.SND_FILENAME)
                            time.sleep(5)
                            ma+=1
                        else:
                           print("You don't find anything useful in the desk drawers.")
                    elif mains=='c':
                        if mkey==1:
                            print("The cabinet is locked. Do you have the key?")
                            maink=input("'yes' or 'no': ")
                            if maink=='yes':
                                welcome="""You fit the key from the principal's desk into the lock, and the drawers slide open. Inside, you see rows and rows of folders. Would you like to look through them?"""
                                first=textwrap.TextWrapper(width=100)
                                hi=first.fill(text=welcome)
                                print(hi)
                                cabinet=input("'yes' or 'no': ")
                                if cabinet=='yes':
                                    welcome="""Each of the folders has a student's name on it. Most of the folders have around 5 pieces of paper inside of them, including yours. Do you want to read what is on those papers?"""
                                    first=textwrap.TextWrapper(width=100)
                                    hi=first.fill(text=welcome)
                                    print(hi)
                                    folder=input("'yes' or 'no': ")
                                    if folder=='yes':
                                        welcome="""Although you feel somewhat guilty looking through what is clearly confidential information, that doesn't stop you from pulling the papers out of your folder and reading them."""
                                        first=textwrap.TextWrapper(width=100)
                                        hi=first.fill(text=welcome)
                                        print(hi)
                                        time.sleep(5)
                                        print("")
                                        welcome="""Disappointingly, all you see on the papers is your schedule, along with your grades from your previous school. You put all of the folders back into place and try to erase all traces of your snooping."""
                                        first=textwrap.TextWrapper(width=100)
                                        hi=first.fill(text=welcome)
                                        print(hi)
                                        time.sleep(5)
                        else:
                            print("The cabinet is locked")
                    elif mains=='l':
                        welcome="""At first, you think you've hit a jackpot since the lost and found bin is the most likely place Scarlett's key would end up, but you quickly realize that the bin was recently emptied, so the only objects in it are a water bottle and a notebook."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(5)
                    else:
                        print("That's not a valid action.")
                break
            else:
                print("That's not a valid move.")
    elif person=='o' and school_layout[x][y+1]=='guidanceoffice':
        while True:
            print("")
            print("What would you like to do in the Guidance Office?")
            guidance=input("'e' or 's': ")
            if guidance=='e':
                print("You leave the room, and you're standing right outside the door now.")
                time.sleep(3)
                print("")
                break
            elif guidance=='s':
                if goff!='yes':
                    welcome="""You notice that the room is 40 ft long and 16 ft wide, with the door on the far left side."""
                    first=textwrap.TextWrapper(width=100)
                    hi=first.fill(text=welcome)
                    print(hi)
                    time.sleep(5)
                    print("You see a jar of lollipops, a desk, and a stack of papers on the desk.")
                    time.sleep(3)
                else:
                    print("You see the jar of lollipops, a desk, and a stack of papers on the desk.")
                while True:
                    print("")
                    print("What would you like to look at?")
                    guidances=input("'l'=lollipops, 'd'=desk, 'p'=papers, 'e'=exit: ")
                    if guidances=='e':
                        print("You leave the room, and you're standing right outside the door now.")
                        time.sleep(3)
                        print("")
                        break
                    elif guidances=='l':
                        welcome="""You don't find anything unusual in the jar, and you grab a lollipop for yourself after you look through the jar."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(5)
                    elif guidances=='d':
                        welcome="""Most of the desk drawers are locked, and the ones that you can open contain many different papers but no key."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        winsound.PlaySound(resource_path("drawer.wav"), winsound.SND_FILENAME)
                        winsound.PlaySound(resource_path("drawerclosing.wav"), winsound.SND_FILENAME)
                        time.sleep(3)
                    elif guidances=='p':
                        welcome="""The papers are all for seniors applying to college, and you don't spend too long looking through those so that you don't stress yourself out."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(5)
                    else:
                        print("That's not a valid action.")
                break
            else:
                print("That's not a valid move.")
    elif person=='o' and school_layout[x][y+1]=='bathroom':
        while True:
            print("")
            print("What would you like to do in the bathroom?")
            bathroom=input("'e' or 's': ")
            if bathroom=='e':
                print("You leave the room, and you're standing right outside the door now.")
                time.sleep(3)
                print("")
                break
            elif bathroom=='s':
                welcome="""You don't find a key in the room, so you leave the room, and you're standing right outside the door now."""
                first=textwrap.TextWrapper(width=100)
                hi=first.fill(text=welcome)
                print(hi)
                time.sleep(3)
                print("")
                break
            else:
                print("That's not a valid move.")
    elif person=='o' and school_layout[x][y-1]=='cafeteria':
        while True:
            print("")
            print("What would you like to do in the Cafeteria?")
            caf=input("'e' or 's': ")
            if caf=='e':
                print("You leave the room, and you're standing right outside the door now.")
                time.sleep(3)
                print("")
                break
            elif caf=='s':
                welcome="""All of the tables are stacked up against the back wall since it's still summertime. From where you're standing, you spot a couple of objects located by the food at the snack bar, and you also see some coins on the ground by the vending machine."""
                first=textwrap.TextWrapper(width=100)
                hi=first.fill(text=welcome)
                print(hi)
                time.sleep(3)
                while True:
                    print("")
                    print("What would you like to look at?")
                    cafs=input("'t'=tables, 's'=snack bar, 'v'=vending machine, 'e'=exit: ")
                    if cafs=='e':
                        print("You leave the room, and you're standing right outside the door now.")
                        time.sleep(3)
                        print("")
                        break
                    elif cafs=='t':
                        print("All you find on the tables is dried up food that looks like it won't ever come off.")
                        time.sleep(3)
                    elif cafs=='s':
                        welcome="""When you get closer to the snack bar, you see that the objects that you saw earlier are just discarded candy wrappers."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(5)
                    elif cafs=='v':
                        print("You don't see anything out of place in the vending machine.")
                        time.sleep(3)
                    else:
                        print("That's not a valid action.")
                break
            else:
                print("That's not a valid move.")
    elif person=='o' and school_layout[x][y-1]=='spanishdoor':
        while True:
            print("")
            print("What would you like to do in the Spanish Room?")
            spanish=input("'e' or 's': ")
            if spanish=='e':
                print("You leave the room, and you're standing right outside the door now.")
                time.sleep(3)
                print("")
                break
            elif spanish=='s':
                if espanol!='yes':
                    welcome="""You see that the room is 40 ft long and 32 ft wide, with the door 12 ft from the leftmost wall."""
                    first=textwrap.TextWrapper(width=100)
                    hi=first.fill(text=welcome)
                    print(hi)
                    time.sleep(5)
                welcome="""When you glance around the classroom, you notice the teacher's desk, the student desks, and a shelf along the back wall."""
                first=textwrap.TextWrapper(width=100)
                hi=first.fill(text=welcome)
                print(hi)
                time.sleep(3)
                while True:
                    print("")
                    print("What would you like to look at?")
                    spanishes=input("'t'=teacher's desk, 'sd'=student desks, 's'=shelf, 'e'=exit: ")
                    if spanishes=='e':
                        print("You leave the room, and you're standing right outside the door now.")
                        time.sleep(3)
                        print("")
                        break
                    elif spanishes=='t':
                        welcome="""The top of the desk is clear, and when you open the drawers, you find some stray papers and a moldy apple."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(5)
                    elif spanishes=='sd':
                        welcome="""The only interesting thing on the desks is the graffiti. One desk has a rude depiction of someone, who you assume is the Spanish teacher, and there are a bunch of random doodles on other desks."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(5)
                    elif spanishes=='s':
                        print("The shelves have lots of Spanish books on them, but you don't find a key there.")
                        time.sleep(4)
                    else:
                        print("That's not a valid action.")
                break
            else:
                print("That's not a valid move.")
    elif person=='o' and school_layout[x][y-1]=='englishdoor':
        while True:
            print("")
            print("What would you like to do in the English Room?")
            english=input("'e' or 's': ")
            if english=='e':
                print("You leave the room, and you're standing right outside the door now.")
                time.sleep(3)
                print("")
                break
            elif english=='s':
                if inglesh!='yes':
                    welcome="""You see that the English room is 40 ft long and 32 ft wide, with the door at the far left."""
                    first=textwrap.TextWrapper(width=100)
                    hi=first.fill(text=welcome)
                    print(hi)
                    time.sleep(5)
                welcome="""When you glance around the classroom, you see a shelf full of books, large black circles on the floor, and a large green jar on the teacher's desk."""
                first=textwrap.TextWrapper(width=100)
                hi=first.fill(text=welcome)
                print(hi)
                time.sleep(3)
                while True:
                    print("")
                    print("What would you like to look at more closely?")
                    englishes=input("'b'=bookshelf, 'c'=circles, 'j'=jar, 'e'=exit: ")
                    if englishes=='e':
                        print("You leave the room, and you're standing outside the door now.")
                        time.sleep(3)
                        print("")
                        break
                    elif englishes=='b':
                        welcome="""From one look at the bookshelves, you can tell that your English teacher is an avid reader. You estimate that there are over 100 books on the shelves, with some spilling off the shelves onto the floor. However, you don't find a key among the books."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(5)
                    elif englishes=='c':
                        welcome="""Upon further investigation, you notice that the circles are numbered, and you presume that the English teacher uses the circles for group work. Even though you spend extra time looking at the circles to make sure there isn't a key blending in with them, you don't find anything."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(5)
                    elif englishes=='j':
                        if inglesh=='yes':
                            welcome="""You see a couple of marbles inside the jar, and, remembering back to Scarlett's description of English class, you assume that the marbles are how the teacher keeps track of the number of days without a student misbehaving."""
                            first=textwrap.TextWrapper(width=100)
                            hi=first.fill(text=welcome)
                            print(hi)
                            time.sleep(5)
                        else:
                            welcome="""You see a couple of marbles inside the jar, although you're not sure what their purpose is."""
                            first=textwrap.TextWrapper(width=100)
                            hi=first.fill(text=welcome)
                            print(hi)
                            time.sleep(4)
                        print("Other than that, you don't find anything interesting.")
                    else:
                        print("That's not a valid action.")
                break
            else:
                print("That's not a valid move.")
    elif person=='o' and school_layout[x][y-1]=='sciencedoor':
        while True:
            print("What would you like to do in the Science Room?")
            science=input("'e' or 's': ")
            if science=='e':
                print("You leave the room, and you're standing right outside the door now.")
                time.sleep(3)
                print("")
                break
            elif science=='s':
                if ciencias!='yes':
                    welcome="""You see that the room extends 40 ft outward from the door, there's 12 feet of wall on the left side of the door, and 16 ft of wall to the right of the door."""
                    first=textwrap.TextWrapper(width=100)
                    hi=first.fill(text=welcome)
                    print(hi)
                    time.sleep(5)
                    welcome="""When you glance around, you notice a large whiteboard next to a cabinet with safety goggles, and a boy standing by some beakers at the back of the room."""
                    first=textwrap.TextWrapper(width=100)
                    hi=first.fill(text=welcome)
                    print(hi)
                    time.sleep(3)
                    while True:
                        print("")
                        print("What would you like to look at closer?")
                        sciences=input("'w'=whiteboard, 'c'=cabinet, 'b'=boy, 'e'=exit: ")
                        if sciences=='e':
                            print("You leave the room, and you're standing right outside the door now.")
                            time.sleep(3)
                            print("")
                            break
                        elif sciences=='w':
                            welcome="""The whiteboard is freshly cleaned, with no apparent marks on it. You don't find a key in the area around the whiteboard."""
                            first=textwrap.TextWrapper(width=100)
                            hi=first.fill(text=welcome)
                            print(hi)
                            time.sleep(5)
                        elif sciences=='c':
                            print("Although there are around 30 pairs of goggles in the cabinet, none of them have a key near them.")
                            time.sleep(5)
                        elif sciences=='b':
                            welcome="""You walk over to the boy to ask him if he knows where the key to the front door is. He tells you that Ms. Snow mentioned a key to him before she left the building, but he's not sure if she left it in her room or put it in the lost and found bin in the main office. He says that he just followed Ms. Snow into the building when he arrived in the morning, and he doesn't have his own key."""
                            first=textwrap.TextWrapper(width=100)
                            hi=first.fill(text=welcome)
                            print(hi)
                            time.sleep(10)
                            print("")
                            print("You thank him and let him go back to working on a science experiment that involves mixing different substances to create a metallic blue liquid.")
                            time.sleep(5)
                        else:
                            print("That's not a valid action.")
                else:
                    welcome="""When you glance around, you notice a large whiteboard next to a cabinet with safety goggles, and you see that Avery is still working on his experiment."""
                    first=textwrap.TextWrapper(width=100)
                    hi=first.fill(text=welcome)
                    print(hi)
                    while True:
                        print("")
                        print("What would you like to look at closer?")
                        sciences=input("'w'=whiteboard, 'c'=cabinet, 'a'=Avery, 'e'=exit: ")
                        if sciences=='e':
                            print("You leave the room, and you're standing right outside the door now.")
                            time.sleep(3)
                            print("")
                            break
                        elif sciences=='w':
                            welcome="""The whiteboard is freshly cleaned, with no apparent marks on it. You don't find a key in the area around the whiteboard."""
                            first=textwrap.TextWrapper(width=100)
                            hi=first.fill(text=welcome)
                            print(hi)
                            time.sleep(5)
                        elif sciences=='c':
                            print("Although there are around 30 pairs of goggles in the cabinet, none of them have a key near them.")
                            time.sleep(5)
                        elif sciences=='a':
                            welcome="""You walk over to Avery to ask him if he knows where the key to the front door is. He tells you that Ms. Snow mentioned a key to him before she left the building, but he's not sure if she left it in her room or put it in the lost and found bin in the main office. He says that he just followed Ms. Snow into the building when he arrived in the morning, and he doesn't have his own key."""
                            first=textwrap.TextWrapper(width=100)
                            hi=first.fill(text=welcome)
                            print(hi)
                            time.sleep(10)
                            print("")
                            print("You thank him and let him go back to working on his science experiment.")
                            time.sleep(4)
                        else:
                            print("That's not a valid action.")
                break
            else:
                print("That's not a valid move.")
    elif person=='o' and school_layout[x+1][y]=='orchdoor':
        print("Would you like to open the door in front of you or the door behind you?")
        answer=input("'f'=in front of you, 'b'=behind you: ")
        if answer=='b':
            while True:
                print("")
                print("What would you like to do in the Orchestra Room?")
                orch=input("'e' or 's': ")
                if orch=='e':
                    print("You leave the room, and you're standing right outside the door now.")
                    time.sleep(3)
                    print("")
                    break
                elif orch=='s':
                    if music!='3':
                        welcome="""You notice that the room is 16 ft by 16 ft, with the door 8 ft from the leftmost wall."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        print("")
                        time.sleep(3)
                        welcome="""When you glance around the room, you see a bunch of music stands, a boy playing cello, and the boy's cello case."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(5)
                        while True:
                            print("")
                            print("What would you like to look at?")
                            orchestras=input("'b'=boy, 'c'=cello case, 's'=music stands, 'e'=exit: ")
                            if orchestras=='e':
                                print("You leave the room, and you're standing right outside the door now.")
                                time.sleep(3)
                                print("")
                                break
                            elif orchestras=='b':
                                welcome="""You walk over to the boy, and he introduces himself as James. When you ask him if he knows where to find a key to the front door, he tells you that there might be a spare key in the main office, but he's not completely sure. He says he just followed the band students into the building, so he doesn't have his own key."""
                                first=textwrap.TextWrapper(width=100)
                                hi=first.fill(text=welcome)
                                print(hi)
                                time.sleep(8)
                                print("")
                                print("You thank him and let him go back to his practicing.")
                                time.sleep(3)
                            elif orchestras=='c':
                                print("All you find inside the cello case is a cloth and a piece of rosin.")
                                time.sleep(3)
                            elif orchestras=='s':
                                print("The only things you find on the stands are pieces of sheet music and a couple of pencils.")
                                time.sleep(4)
                            else:
                                print("That's not a valid action.")
                    else:
                        welcome="""When you glance around the room, you see that James is still practicing his cello piece, and you also see his cello case leaning against the back wall behind some music stands."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        while True:
                            print("")
                            print("What would you like to look at?")
                            orchestras=input("'j'=James, 'c'=cello case, 's'=music stands, 'e'=exit: ")
                            if orchestras=='e':
                                print("You leave the room, and you're standing right outside the door now.")
                                time.sleep(3)
                                print("")
                                break
                            elif orchestras=='j':
                                welcome="""You walk over to James and ask him if he knows where to find a key to the front door. He tells you that there might be a spare key in the main office, but he's not completely sure. He says he just followed the band students into the building, so he doesn't have his own key."""
                                first=textwrap.TextWrapper(width=100)
                                hi=first.fill(text=welcome)
                                print(hi)
                                time.sleep(8)
                                print("")
                                print("You thank him and let him go back to his practicing.")
                            elif orchestras=='c':
                                print("All you find inside the cello case is a cloth and a piece of rosin.")
                                time.sleep(3)
                            elif orchestras=='s':
                                print("The only things you find on the stands are pieces of sheet music and a couple of pencils.")
                                time.sleep(3)
                            else:
                                print("That's not a valid action.")
                    break
                else:
                    print("That's not a valid move.")
        elif answer=='f':
            while True:
                print("")
                print("What would you like to do in the Library?")
                library=input("'e' or 's': ")
                if library=='e':
                    print("You leave the room, and you're standing right outside the door now.")
                    time.sleep(3)
                    print("")
                    break
                elif library=='s':
                    welcome="""The only things that stand out to you in the room are the tables, the bookshelf, and the librarian's desk."""
                    first=textwrap.TextWrapper(width=100)
                    hi=first.fill(text=welcome)
                    print(hi)
                    print("")
                    time.sleep(3)
                    while True:
                        print("")
                        print("What would you like to look at?")
                        libraries=input("'t'=tables, 'b'=bookshelf, 'd'=desk, 'e'=exit: ")
                        if libraries=='e':
                            print("You leave the room, and you're standing right outside the door now.")
                            time.sleep(3)
                            print("")
                            break
                        elif libraries=='t':
                            welcome="""You find a couple of pieces of old gum that look like they're permanently stuck to the tables."""
                            first=textwrap.TextWrapper(width=100)
                            hi=first.fill(text=welcome)
                            print(hi)
                            time.sleep(5)
                        elif libraries=='b':
                            welcome="""You leaf through the pages of the books, hoping to find a key hidden within one of the books, but you don't find anything."""
                            first=textwrap.TextWrapper(width=100)
                            hi=first.fill(text=welcome)
                            print(hi)
                            time.sleep(5)
                        elif libraries=='d':
                            welcome="""The librarian's desk is pretty much empty, probably because the school year hasn't started yet, and all you find is an old library card and some bookmarks."""
                            first=textwrap.TextWrapper(width=100)
                            hi=first.fill(text=welcome)
                            print(hi)
                            time.sleep(5)
                        else:
                            print("That's not a valid action.")
                    break
                else:
                    print("That's not a valid move.")
        else:
            print("That's not an option.")
    elif person=='o' and school_layout[x+1][y]=='frontdoor':
        print("The door is locked.")
        print("Do you have the key?")
        answer=input("'yes' or 'no': ")
        if answer=='yes':
            if fkey==1:
                print("You remember the key that you found in the History room, and you pull it out of your pocket.")
                time.sleep(3)
                print("")
                print("With a satisfying click, you fit the key into the hole, and with that, the front door opens.")
                time.sleep(2)
                print("")
                print("Congratulations! You managed to escape!")
                time.sleep(2)
                print("")
                print("You see Scarlett waiting for you on a nearby bench, and you give her back her key.")
                time.sleep(3)
                print("")
                print("Scarlett: Thank you so much, " + name + ". You're basically an expert at the school layout now.")
                time.sleep(5)
                print("")
                print("Scarlett: I have to go now, but it was nice to meet you.")
                time.sleep(2)
                print("")
                welcome="""Scarlett walks over to her car and drives off. You find your mom in the parking lot waiting for you, and you walk back to your house with her, feeling satisfied that you made it out of the school."""
                first=textwrap.TextWrapper(width=100)
                hi=first.fill(text=welcome)
                print(hi)
                time.sleep(5)
                print("")
                print("The end! Thank you for trying my escape room!")
                time.sleep(20)
                success+=1
            else:
                print("You search through your pockets for the key but don't find it.")
        else:
            print("Without the key, you're not able to unlock the door.")
    elif person=='o' and school_layout[x-1][y]=='chorusdoor':
        print("Would you like to open the door in front of you or the door behind you?")
        answer=input("'f'=in front of you, 'b'=behind you: ")
        if answer=='f':
            while True:
                print("")
                print("What would you like to do in the Chorus Room?")
                chorus=input("'e' or 's': ")
                if chorus=='e':
                    print("You leave the room, and you're standing right outside the door now.")
                    time.sleep(3)
                    print("")
                    break
                elif chorus=='s':
                    if music!='1':
                        print("The room is 16 ft by 16 ft, with the door 4 ft from the leftmost wall.")
                        time.sleep(3)
                    welcome="""You see several music stands in the room, and there's also a piano in front of a door at the back of the room."""
                    first=textwrap.TextWrapper(width=100)
                    hi=first.fill(text=welcome)
                    print(hi)
                    time.sleep(3)
                    while True:
                        print("")
                        print("What would you like to look at closer?")
                        chori=input("'s'=music stands, 'p'=piano, 'd'=door, 'e'=exit: ")
                        if chori=='e':
                            print("You leave the room, and you're standing right outside the door now.")
                            time.sleep(3)
                            print("")
                            break
                        elif chori=='s':
                            print("All you find on the stands is a couple of stray pieces of sheet music.")
                            time.sleep(3)
                        elif chori=='p':
                            welcome="""Your attention is drawn to something on top of the piano because its shape resembles that of a key, but when you get closer, you realize it's just an oddly shaped pen. Other than that, there isn't anything useful on the piano."""
                            first=textwrap.TextWrapper(width=100)
                            hi=first.fill(text=welcome)
                            print(hi)
                            time.sleep(6)
                        elif chori=='d':
                            print("The door is locked. Do you have the key?")
                            answer=input("'yes' or 'no': ")
                            if answer=='yes':
                                if hkey==1:
                                    welcome="""You try all of the keys from the keyring you found in the Janitor's closet, and you eventually find one that fits."""
                                    first=textwrap.TextWrapper(width=100)
                                    hi=first.fill(text=welcome)
                                    print(hi)
                                    time.sleep(5)
                                    welcome="""When you open the door, you see a cramped closet that you barely fit inside. There are several cabinets along the walls, but when you look inside of them, all you find is sheet music. Nothing catches your eye as out of place in this room, so you leave."""
                                    first=textwrap.TextWrapper(width=100)
                                    hi=first.fill(text=welcome)
                                    print(hi)
                                    time.sleep(7)
                                else:
                                    print("You search in your pockets for a key that fits, but you're unsuccessful.")
                            else:
                                print("Without the key, you're not able to open the door.")
                        else:
                            print("That's not a valid action.")
                    break
                else:
                    print("That's not a valid move.")
        elif answer=='b':
            while True:
                print("")
                print("What would you like to do in the Band Room?")
                band=input("'e' or 's': ")
                if band=='e':
                    print("You leave the room, and you're standing right outside the door now.")
                    time.sleep(3)
                    print("")
                    break
                elif band=='s':
                    if music!='2':
                        print("You notice that the room is 16 ft by 16 ft, with the door 8 ft from the leftmost wall.")
                        time.sleep(3)
                        welcome="""When you glance around, you see a bin at the back of the room, a couple of music stands, and a group of students who you presume are members of the school marching band."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(5)
                        while True:
                            print("")
                            print("What would you like to look at?")
                            bands=input("'b'=bin, 's'=music stands, 'm'=marching band, 'e'=exit: ")
                            if bands=='e':
                                print("You leave the room, and you're standing right outside the door now.")
                                time.sleep(3)
                                print("")
                                break
                            elif bands=='b':
                                print("When you walk over to the bin, you see that it's empty.")
                                time.sleep(3)
                            elif bands=='s':
                                print("All you find on the music stands is sheet music and a couple of stray batons and pencils.")
                                time.sleep(4)
                            elif bands=='m':
                                welcome="""You wait until the band takes a break from playing to walk over to them and ask if they know how to unlock the front door. The band leader says that they were let into the building by the band director, who had a key, but he left soon after, and they are planning on staying until he comes back. They offer to let you stay with them until then, but you decide it would be quicker for you to find Scarlett's key instead, so you decline their offer."""
                                first=textwrap.TextWrapper(width=100)
                                hi=first.fill(text=welcome)
                                print(hi)
                                time.sleep(10)
                                print("")
                                print("You thank them and let them go back to their practicing.")
                                time.sleep(3)
                            else:
                                print("That's not a valid action.")
                    else:
                        print("When you examine the room, you see the bin at the back of the room, a couple of music stands, and the marching band students who are practicing their music.")
                        time.sleep(5)
                        while True:
                            print("")
                            print("What would you like to look at more closely?")
                            bands=input("'b'=bin, 's'=music stands, 'm'=marching band, 'e'=exit: ")
                            if bands=='e':
                                print("You leave the room, and you're standing right outside the door now.")
                                time.sleep(3)
                                print("")
                                break
                            elif bands=='b':
                                print("Just like when you looked at it before, the bin is still empty.")
                                time.sleep(3)
                            elif bands=='s':
                                print("All you find on the music stands is sheet music and a couple of stray batons and pencils.")
                                time.sleep(3)
                            elif bands=='m':
                                welcome="""You wait until the band takes a break from playing to walk over to them and ask if they know how to unlock the front door. Caroline says that the band was let into the building by the band director, who had a key, but he left soon after, and they are planning on staying until he comes back. They offer to let you stay with them until then, but you decide it would be quicker for you to find Scarlett's key instead, so you decline their offer."""
                                first=textwrap.TextWrapper(width=100)
                                hi=first.fill(text=welcome)
                                print(hi)
                                time.sleep(10)
                                print("")
                                print("You thank them and let them go back to their practicing.")
                                time.sleep(3)
                            else:
                                print("That's not a valid action.")
                    break
                else:
                    print("That's not a valid move.")
        else:
            print("That's not an option.")
    elif person=='o' and school_layout[x-1][y]=='gymdoor':
        while True:
            print("")
            print("What would you like to do in the Gymnasium?")
            gym=input("'e' or 's': ")
            if gym=='e':
                print("You leave the room, and you're standing right outside the same door you came in.")
                time.sleep(3)
                print("")
                break
            elif gym=='s':
                welcome="""You spot the rope hanging in the center of the room, the supply closet in the back corner, and a closed set of bleachers along the back wall."""
                first=textwrap.TextWrapper(width=100)
                hi=first.fill(text=welcome)
                print(hi)
                time.sleep(3)
                while True:
                    print("")
                    print("What would you like to look at?")
                    gyms=input("'r'=rope, 'c'=closet, 'b'=bleachers, 'e'=exit: ")
                    if gyms=='e':
                        print("You leave the room, and you're standing right outside the same door you came in.")
                        time.sleep(3)
                        print("")
                        break
                    elif gyms=='c':
                        print("The door is locked. Do you have the key?")
                        gkey=input("'yes' or 'no': ")
                        if gkey=='yes':
                            print("You search in your pockets for a key that fits in the lock, but you're unsuccessful.")
                    elif gyms=='b':
                        welcome="""You pinch your fingers when you try to feel underneath the bleachers for a key. Unfortunately, the pain is for nothing because you don't find anything other than dust under the bleachers."""
                        first=textwrap.TextWrapper(width=100)
                        hi=first.fill(text=welcome)
                        print(hi)
                        time.sleep(5)
                    elif gyms=='r':
                        print("Looking at the rope brings back memories of when you were in here earlier.")
                        time.sleep(4)
                        if rope=='yes' or rope=='Yes':
                            print("The mat underneath still has an imprint from when you fell onto it.")
                            time.sleep(3)
                        else:
                            print("You still don't regret your decision to not climb it.")
                            time.sleep(3)
                        print("You don't find anything in the area around the rope.")
                        time.sleep(3)
                       
                    else:
                        print("That's not a valid action.")
                break
            else:
                print("That's not a valid move.")
    else:
        print("That's not a valid move.")


