from sklearn.preprocessing import LabelEncoder

basket = ['apple', 'orange', 'grape', 'strawberry', 'melon', 'plum', 'plum', 'grape', 'watermelon', 'melon', 'orange']

encoder = LabelEncoder()
labels = encoder.fit_transform(basket)
print(labels)

for i in range (len(encoder.classes_)):
    print(f"{i} : {encoder.classes_[i]}")