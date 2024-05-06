from pprint import pprint
from model.sample import Sample
from model.sample import TrainingKnownSample, KnownSample

if __name__ == "__main__":
    x = Sample(1, 2, 3, 4)
    pprint(x)

    s1 = TrainingKnownSample(
        sepal_length=5.1,
        sepal_width=3.5,
        petal_length=1.4,
        petal_width=0.2,
        species="Iris-setosa"
    )
    pprint(s1)
    s1.classification = "wrong"
    pprint(s1)
    pprint(s1.classification)

    # s2 = TrainingKnownSample(
    #     sample=KnownSample(
    #         sepal_length=5.1,
    #         sepal_width=3.5,
    #         petal_length=1.4,
    #         petal_width=0.2,
    #         species="Iris-setosa"
    #         )
    # )
    # pprint(s2)
