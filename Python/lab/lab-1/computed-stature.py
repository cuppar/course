import math

title='''
4.编写程序，输入父母身高（厘米），预测小孩身高，并输出结果。
要求：小男孩身高 = (父亲身高+母亲身高)×1.08÷2(厘米)，
小女孩身高 = (父亲身高×0.923+母亲身高)÷2(厘米)。
'''
print(title)

father_stature=float(input("please input father's stature: "))
mother_stature=float(input("please input mother's stature: "))

son_stature=(father_stature+mother_stature)*1.08/2
daughter_stature=(father_stature*0.923+mother_stature)/2
print("son's stature:", son_stature)
print("daughter's stature:", daughter_stature)