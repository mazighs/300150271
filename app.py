import psycopg
import json

conn = psycopg.connect("dbname=ecole user=postgres password=postgres host=localhost port=5432")
cur = conn.cursor()

nouvel_etudiant = {"nom": "Diana", "age": 28, "competences": ["DevOps", "Kubernetes"]}
cur.execute("INSERT INTO etudiants (data) VALUES (%s)", [json.dumps(nouvel_etudiant)])
conn.commit()
print("INSERT OK - Diana ajoutee")

print("\nTous les etudiants :")
cur.execute("SELECT data FROM etudiants")
for row in cur.fetchall():
    print(row[0])

print("\nRecherche Alice :")
cur.execute("SELECT data FROM etudiants WHERE data->>'nom' = 'Alice'")
for row in cur.fetchall():
    print(row[0])

print("\nEtudiants avec Python :")
cur.execute("SELECT data FROM etudiants WHERE data->'competences' ? 'Python'")
for row in cur.fetchall():
    print(row[0])

cur.execute("UPDATE etudiants SET data = jsonb_set(data, '{age}', '25') WHERE data->>'nom' = 'Bob'")
conn.commit()
print("\nBob mis a jour :")
cur.execute("SELECT data FROM etudiants WHERE data->>'nom' = 'Bob'")
for row in cur.fetchall():
    print(row[0])

cur.execute("DELETE FROM etudiants WHERE data->>'nom' = 'Charlie'")
conn.commit()
print("\nCharlie supprime")

print("\nListe finale :")
cur.execute("SELECT data FROM etudiants")
for row in cur.fetchall():
    print(row[0])

cur.close()
conn.close()
print("\nConnexion fermee.")