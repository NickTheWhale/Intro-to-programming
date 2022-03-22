modelYear = input("model year: ")
modelName = input("model name: ")
extra_years = ["1999", "2000", "2001", "2002"]
guzzler_years = ["2004", "2005", "2006", "2007"]
recalled = False
if any(x in modelYear for x in extra_years):
    if modelName == "Extravagant":
        recalled = True
elif any(x in modelYear for x in guzzler_years):
    if modelName == "Guzzler":
        recalled = True
print(recalled)