import csv
import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Define bucket name and CSV file key
bucket_name = 'pokemon-counters'
csv_file_key = 'Pokemon Data.csv'

# Download CSV file from S3
response = s3.get_object(Bucket=bucket_name, Key=csv_file_key)
csv_content = response['Body'].read().decode('utf-8')

# Strip the BOM character
if csv_content.startswith('\ufeff'):
    csv_content = csv_content[1:]

# Split the CSV content by lines to ensure proper newline handling
csv_lines = csv_content.splitlines()

pokemon_dict = {'Game': {}}

# Parse CSV content
csv_reader = csv.DictReader(csv_lines)
for row in csv_reader:
    # Check if the "Rematch" value is either "Yes" or "No"
    game = row['Game']
    city = row['City']
    gym_leader = row['Gym Leader']
    pokemon_name = row['Pokemon Name']
    rematch = row['Rematch']

    if game not in pokemon_dict['Game']:
        pokemon_dict['Game'][game] = {city: {gym_leader: {rematch: {'Pokemon Name': {}}}}}
    elif city not in pokemon_dict['Game'][game]:
        pokemon_dict['Game'][game][city] = {gym_leader: {rematch: {'Pokemon Name': {}}}}
    elif gym_leader not in pokemon_dict['Game'][game][city]:
        pokemon_dict['Game'][game][city][gym_leader] = {rematch: {'Pokemon Name': {}}}
    elif rematch not in pokemon_dict['Game'][game][city][gym_leader]:
        pokemon_dict['Game'][game][city][gym_leader][rematch] ={'Pokemon Name': {}}
    pokemon_dict['Game'][game][city][gym_leader][rematch]['Pokemon Name'][pokemon_name] = {
        'Gym Badge': row['Gym Badge'],
        'Gym Entry Requirement': row['Gym Entry Requirement'],
        'Pokemon Type': row['Pokemon Type'],
        'Pokemon Level': int(row['Pokemon Level']),
        'Pokemon Counters': row['Pokemon Counters'],
        'Pokemon Countered by': row['Pokemon Countered By'],
        'Rematch': row['Rematch']  # Include the rematch value in the data
    }
