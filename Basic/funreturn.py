def demo():
    exp=int(input(" enter your experience"))
    skill=input("enter the skill")
    if exp>=4 and exp<6 and skill =='python' or skill=='java':
        return "promoted as team leader"
    elif exp>=7 and exp<10 and skill=='ailge' or skill=='devops':
        return "promoted as project manager"
    return "be as associated"

desig=demo()
0