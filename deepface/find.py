# for reference the da

from deepface import DeepFace

dfs = DeepFace.find(img_path = "../src/rau4.jpg", db_path = "../src/database/db/", enforce_detection=False)

for i in dfs:
    print(i)