import requests
import pandas as pd

url = "https://remotive.com/api/remote-jobs?category=software-dev"

response = requests.get(url)
data = response.json()

vagas = []

for job in data["jobs"]:
    local = job["candidate_required_location"].lower()

    # Vagas remotas compatíveis com quem mora no Brasil
    if (
        "brazil" in local
        or "brasil" in local
        or "latam" in local
        or "latin america" in local
        or "americas" in local
        or "worldwide" in local
        or "anywhere" in local
    ):
        vagas.append({
            "Título": job["title"],
            "Empresa": job["company_name"],
            "Local": job["candidate_required_location"],
            "Link": job["url"]
        })

df = pd.DataFrame(vagas)
df.to_excel("vagas_remotas_para_brasil.xlsx", index=False)

print(f"{len(vagas)} vagas remotas compatíveis com Brasil encontradas!")
input("Pressione ENTER para sair...")
