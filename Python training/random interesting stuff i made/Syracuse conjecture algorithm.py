def syracusenouveau(u):
    while u>1:
        if u==1:
            return 1
        else:
            if u%2==0:
                u=u//2
                print(u)
            else:
                u=3*u+1
                print(u)
        return syracusenouveau(u)
    u=(input("nouvelle valeur(stop pour arrêter) :"))
    if u=="stop" or u=="Stop":
        print("fin")
    else:
        u=int(u)
        syracusenouveau(u)

syracusenouveau(10)