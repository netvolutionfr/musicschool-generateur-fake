'''
Generate fake data for testing purposes.
'''

import faker
import csv

fake = faker.Faker('fr_FR')


def generate_fake_data():
    '''
    Generate fake data for testing purposes.
    '''
    fiche = {
        'nom': fake.last_name(),
        'prenom': fake.first_name(),
        'adresse': fake.street_address(),
        'email': fake.email(),
        'codepostal': fake.postcode(),
        'ville': fake.city(),
        'tel': fake.phone_number(),
        'formule': fake.random_int(min=1, max=6, step=1),
        'etudiant': fake.boolean(),
        'age': fake.random_int(min=18, max=99, step=1),
    }
    jeune = fake.boolean(chance_of_getting_true=67)
    if jeune:
        fiche['age'] = fake.random_int(min=5, max=24, step=1)
    else:
        fiche['age'] = fake.random_int(min=25, max=80, step=1)

    if 18 < fiche['age'] < 25:
        fiche['etudiant'] = fake.boolean(chance_of_getting_true=67)
    else:
        fiche['etudiant'] = False

    return fiche


if __name__ == '__main__':
    with open('fakedata.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=generate_fake_data().keys(), delimiter=';')
        writer.writeheader()
        for _ in range(1000):
            writer.writerow(generate_fake_data())
