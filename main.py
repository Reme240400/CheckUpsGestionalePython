import psycopg2

def main():
    connection_string = "host=localhost port=5432 dbname=checkups_db user=postgres password=postgres"

    try:
        # Creare una nuova connessione PostgreSQL
        with psycopg2.connect(connection_string) as connection:
            # Aprire la connessione al database
            with connection.cursor() as cursor:
                # Eseguire una query per recuperare alcuni dati dalla tabella "societa"
                query = "SELECT id_societa FROM societa"
                cursor.execute(query)

                # Ottenere il risultato della query
                rows = cursor.fetchall()

                # Leggere e stampare i dati
                for row in rows:
                    id = row[0]
                    # name = row[1]  # Se hai altre colonne nella query, puoi leggerle qui
                    print("CIAOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                    # Fare qualcosa con i dati (in questo caso, stamparli)
                    print(f"ID: {id}")

    except Exception as ex:
        # Gestione delle eccezioni in caso di errore di connessione
        print("Errore di connessione al database:", ex)

if __name__ == "__main__":
    main()
