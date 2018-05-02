name        name          
----------  --------------
Batman      Justice League
Superman    Justice League
Thor        Avengers      
Iron Man    Avengers      
Wonder Wom  Justice League
Captain Am  Avengers      
Aquaman     Justice League
Black Pant  Avengers      
Black Wido  Avengers      
Hulk        Avengers      
Cyborg      Justice League
Green Lant  Justice League


Great!  We selected all the superheroes belonging to a team.  However, our formatting is messy.  Let’s rewrite this query to group all the above superheroes according to their team name.  Also, both columns are called `name`, so let’s set the `squads.name` to `team`.

def reformatted_query():

Cool!  But aren’t there some heroes belonging to no team?  Let’s write a query that returns the `name`s and `superpower`s of all the `superheroes` table regardless of their team affiliation.  Again, make sure to also include `squads.name` aliased as `team`.


name        superpower                       team      
----------  -------------------------------  ----------
Megaman     elemental-mechanical physiology            
StretcherF  enhanced flexibility                       
Goku        superstrength                              
Thor        summons lightning                Avengers  
Iron Man    ultra smart                      Avengers  
Captain Am  superstrength                    Avengers  
Black Pant  speed and agility                Avengers  
Black Wido  expert martial artist            Avengers  
Hulk        rage                             Avengers  
Batman      works hard                       Justice Le
Superman    superstrength                    Justice Le
Wonder Wom  superstrength                    Justice Le
Aquaman     breaths underwater               Justice Le
Cyborg      technorganic physiology          Justice Le
Green Lant  magic ring                       Justice Le


Notice that there is also one squad with NO members!  Write a `JOIN` statement that return the `name` of each squad and counts all of its members under the alias `num_of_members`.  (*Hint:* You will need to use a `GROUP BY clause` here.)

name        num_of_members
----------  --------------
Avengers    6             
Justice Le  6             
The Illumi  0             
