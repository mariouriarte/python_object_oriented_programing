from model.enum_purpose import Purpose
from training_known_sample import TrainingKnownSample
from training_data import TrainingData
from know_sample import KnownSample

if __name__ == '__main__':
    valid = {"sepal_length": "5.1",
             "sepal_width": "3.5",
             "petal_length": "1.4",
             "petal_width": "0.2",
             "species": "Iris-setosa",
             "purpose": str(Purpose.TESTING)
             }
    rks = TrainingKnownSample.from_dict(valid)
    # print(rks)

    invalid_species = {"sepal_length": "5.1", "sepal_width": "3.5",
                       "petal_length": "1.4", "petal_width": "0.2",
                       "species": "nothing known by this app",
                       "purpose": str(Purpose.TESTING)
                       }
    # eks = TestingKnownSample.from_dict(invalid_species)

    trn_data = TrainingData('Mario')
    trn_data.load([
        invalid_species,
        valid,
        valid,
        valid,
        valid,
        valid,
        invalid_species,
        invalid_species
    ])
    print(trn_data)

    know_sample = KnownSample(
        "5.1",
        "3.5",
        "1.4",
        "0.2",
        "Iris-setosa",
        Purpose.TESTING,
    )
    print(know_sample)
