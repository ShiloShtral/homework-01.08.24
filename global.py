# היתרון בglobal הוא שהוא מאפשר לך לשנות משתנים גלובלים בתוך פונקציות , מקל על קוד שמבצע עדכונים על אותו משתנה , עוזר לשמור ערכים גלובלים 

# .החיסרון בשימוש בglobal הוא שהוא נכנס בקטע קוד במידה ומישהו אחר עושה import לפונקציה כלומר המשתנה שאני הגדרתי בglobal נכנס גם לקטע קוד שלו
# צריך להגדיר כל פעם את הגלובל מחדש או לבדוק שהוא לא נמצא בקטע קוד אחר

#מדוע כאן נקבל שגיאה-

x: int = 1
def foo():
print(x)
x = 4
foo()

#  פה תקבל שגיאה מכיוון שהx כבר מוגדר כ-1 כגלובלי ואחרי שאתה מדפיס אתה מנסה לשנות את הx כמשתנה חיצוני



