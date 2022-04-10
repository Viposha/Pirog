# GIT and VCS related stuff 
0) Setup git account via PyCharm -> 
you should be able to pull/push commits within your IDE
1) Add a .gitignore file to your repo
2) after updating your local repo from portal, for any
further refactoring or development **create a separate brunch**;
e.g. for today's refactoring create `refactoring_Apr_10` brunch
Do not create merge requests yet, simply add you changes in different branches
Tip -> first checkout new brunch, than start coding
   1) try to switch between branches and try to spot the difference


# Refactoring of the existing code base
1) Rename file into main.py [x]
2) Add default python design via 
if __name__ == __main__ :
   1) IDE raises error for main function -> define a corresponding func
      1) You can use `pass` keyword for now
      
3) Split the range size input number with the thousand separator
   (Make a commit here) Tip - look for underscore sign
4) Format the output of object size to use a thousand separator (e.g. _2,800,496_ bytes) ; 
Tip - look for f-string internal syntax formatting
5) Combine 2 print calls on lines 16-17 into 1, the strings should be still displayed on separate lines
Tip - look for `sep` parameter
6) Round your execution duration output to only 4 decimal places
7) Return to this point after going through point 1 of the next section
   1) Resolve an issue with shadowing built-in objects

# Ongoing tasks and further development
1) Call list and tuple conversions several times more after line 10
   1) After you resolve the issue - create a new brunch from your **main** - `feature_Apr_10`
   and continue developing
2) Prettify the output - add a header line of 79 equality signs as the first output 
3) Repeat the same line as the bottom of the output, e.g.:
> ================
>  your prints
> ================
4) Repeat your memory measurement but now use list comprehension expression for list
and generator expression for tuple
5) Display results for all 4 cases


