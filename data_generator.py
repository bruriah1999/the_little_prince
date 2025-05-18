import random
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

num_people = 50
first_names = [fake.first_name() for _ in range(70)]
last_names = [fake.last_name() for _ in range(50)]
cities = [fake.city() for _ in range(30)]
companies = [fake.company() for _ in range(20)]
job_titles = [fake.job() for _ in range(30)]
skills = [fake.word() for _ in range(50)]
car_makes = ["Toyota", "Honda", "Ford", "BMW", "Mercedes", "Tesla", "Nissan", "Hyundai"]
car_models = ["Sedan", "SUV", "Truck", "Coupe", "Hatchback"]

personal_info = []
contact_info = []
work_details = []
identification_numbers = []
address_history = []
family_relationships = []
vehicle_ownership = []

for _ in range(num_people):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = f"{first_name} {last_name}"
    aliases = [fake.name()[:8] if random.random() < 0.3 else None,
               f"{first_name[0]}. {last_name}" if random.random() < 0.5 else None]
    location = random.choice(cities)
    age = random.randint(20, 65)
    gender = random.choice(["Male", "Female", "Other"])

    personal_info.append({
        "name": full_name,
        "aliases": [alias for alias in aliases if alias],
        "age": age,
        "gender": gender,
        "location": location
    })

    contact_info.append({
        "name": full_name, # Added name for potential linking
        "phone_numbers": [fake.phone_number() for _ in range(random.randint(1, 2))],
        "email_addresses": [fake.email() for _ in range(random.randint(1, 2))],
        "linkedin_handle": f"linkedin.com/in/{first_name.lower()}{last_name.lower()}{random.randint(10, 99)}" if random.random() < 0.7 else None
    })

    work_details.append({
        "name": full_name, # Added name for potential linking
        "employer": random.choice(companies) if random.random() < 0.8 else None,
        "job_title": random.choice(job_titles) if random.random() < 0.7 else None,
        "work_history": [{"company": random.choice(companies), "role": random.choice(job_titles), "years": f"{random.randint(2010, 2020)}-{random.randint(2021, 2024)}" } for _ in range(random.randint(0, 2))],
        "skills": random.sample(skills, random.randint(0, 5))
    })

    identification_numbers.append({
        "name": full_name, # Added name for potential linking
        "national_id": fake.ssn() if random.random() < 0.6 else None,
        "passport_number": fake.passport_number() if random.random() < 0.4 else None,
        "drivers_license": f"{random.choice(['A', 'B', 'C'])}{random.randint(100000, 999999)}" if random.random() < 0.5 else None
    })

    address_history.append({
        "name": full_name, # Added name for potential linking
        "current_address": fake.address() if random.random() < 0.7 else None,
        "previous_addresses": [fake.address() for _ in range(random.randint(0, 1))]
    })

    family_relationships.append({
        "name": full_name, # Added name for potential linking
        "spouse": random.choice(first_names) + " " + random.choice(last_names) if random.random() < 0.4 else None,
        "children": [random.choice(first_names) + " " + random.choice(last_names) for _ in range(random.randint(0, 2))] if random.random() < 0.3 else []
    })

    vehicle_ownership.append({
        "name": full_name, # Added name for potential linking
        "vehicles": [{"make": random.choice(car_makes), "model": random.choice(car_models), "year": random.randint(2015, 2024), "license_plate": fake.license_plate()} for _ in range(random.randint(0, 1))]
    })

# The unstructured data generation remains the same, and now uses name directly
linkedin_posts = []
whatsapp_conversations = []
gossip_text = []

for _ in range(30):
    author = random.choice(personal_info)
    mentioned = random.sample([p for p in personal_info if p != author], random.randint(0, 3))
    post = f"{fake.sentence()} by {author['name']}. "
    if mentioned:
        post += "Mentioning: " + ", ".join([m['name'].split()[0] for m in mentioned])
    linkedin_posts.append(post)

for _ in range(40):
    participants = random.sample(personal_info, random.randint(2, 4))
    conversation = f"Conversation between: {', '.join([p['name'].split()[0] for p in participants])}\n"
    for _ in range(random.randint(3, 7)):
        speaker = random.choice(participants)
        other = random.choice([p for p in participants if p != speaker])
        if random.random() < 0.7:
            conversation += f"{speaker['name'].split()[0]}: {fake.sentence(nb_words=random.randint(3, 15))}\n"
        else:
            conversation += f"{speaker['name'].split()[0]} (talking about {other['name'].split()[0]}): {fake.sentence(nb_words=random.randint(5, 20))}\n"
    whatsapp_conversations.append(conversation)

for _ in range(35):
    speaker = random.choice(personal_info)
    target = random.choice([p for p in personal_info if p != speaker])
    gossip = f"{speaker['name'].split()[0]} said about {target['name'].split()[0]}: {fake.paragraph(nb_sentences=random.randint(1, 3))}"
    gossip_text.append(gossip)



if __name__ == '__main__':
    print("Personal Info (first 2):\n", personal_info[:2])
    print("\nContact Info (first 2):\n", contact_info[:2])
    print("\nWork Details (first 2):\n", work_details[:2])
    print("\nIdentification Numbers (first 2):\n", identification_numbers[:2])
    print("\nAddress History (first 2):\n", address_history[:2])
    print("\nFamily Relationships (first 2):\n", family_relationships[:2])
    print("\nVehicle Ownership (first 2):\n", vehicle_ownership[:2])
    print("\nGenerated LinkedIn Posts (first 2):\n", linkedin_posts[:2])
    print("\nGenerated WhatsApp Conversations (first 1):\n", whatsapp_conversations[:1])
    print("\nGenerated Gossip Text (first 2):\n", gossip_text[:2])