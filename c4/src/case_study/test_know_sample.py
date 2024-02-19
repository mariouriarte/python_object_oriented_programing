from model.enum_purpose import Purpose
from know_sample import KnownSample

if __name__ == '__main__':
    s2 = KnownSample(
        sepal_length=5.1,
        sepal_width=3.5,
        petal_length=1.4,
        petal_width=0.2,
        species="Iris-setosa",
        purpose=Purpose.TESTING.value
    )
    print(s2)
    print(s2.classification is None)
