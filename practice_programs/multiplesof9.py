x = []
states = ["Abia", "Adamawa", "Anambra", "Akwa Ibom", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River", "Delta", "Ebonyi", "Enugu", "Edo", "Ekiti", "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"]
def Sorting(lst):
    lst2 = sorted(lst, key=len,reverse=True)
    return lst2[5]
print(Sorting(states))


    