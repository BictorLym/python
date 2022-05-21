import pickle

gameOption = {
    "Sound": 8,
    "VideoQuality": "HIGH",
    "Money": 100000,
    "WeaponList": [ "gun", "missile", "knife"]
    }

#이진파일 오픈
file = open("C:\\Users\\mycom0703\\Desktop\\save.p","wb")

pickle.dump(gameOption, file)

file.close()
