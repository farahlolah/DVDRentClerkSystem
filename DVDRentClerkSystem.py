"""this program is designed for the use of Five Star Retro Video and intends to calculate the number of old or new videos rented out 
for however many nights that the user inputs and however many videos they buy, this is done based 
on the rate of the store that states old videos are 2$ a night and new videos are 3$ a night.

#inputs
how many new and old videos they are buying 

#outputs
the sum of both old and new videos
"""
newVideos = int(input("how many new videos will you be purchasing? "))
oldVideos = int(input("how many old videos will you be purchasing? "))

total = float((newVideos*3)+(oldVideos*2))
print("your total for today is: " ,total, " pounds.")

"""
Test cases :
1. prints (new videos) as a literal, fixed with missing comma
2. prints each total separatly tried sum() function did not work
3. made new variable to store total instead of doing it in the print, worked
4. did not look presentable so added the pound sign before the total, syntax error saying non-UTF8
5. wrapped total variable in float instead to make it look presentable
6. added pounds in words.
- would be better if total is to 2sf
"""