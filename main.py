import tkinter as tk
import psycopg2

def visualizza_output():
    try:
        connection_string = "host=localhost port=5432 dbname=checkups_db user=postgres password=postgres"

        with psycopg2.connect(connection_string) as connection:
            with connection.cursor() as cursor:
                query = "SELECT * FROM societa"
                cursor.execute(query)
                rows = cursor.fetchall()

                output_text.delete(1.0, tk.END)

                for row in rows:
                    id_societa, indirizzo, localita, provincia, telefono, descrizione, ente = row
                    output_text.insert(tk.END, f"ID: {id_societa}\n")
                    output_text.insert(tk.END, f"Indirizzo: {indirizzo}\n")
                    output_text.insert(tk.END, f"Localita: {localita}\n")
                    output_text.insert(tk.END, f"Provincia: {provincia}\n")
                    output_text.insert(tk.END, f"Telefono: {telefono}\n")
                    output_text.insert(tk.END, f"Descrizione: {descrizione}\n")
                    output_text.insert(tk.END, f"Ente: {ente}\n")
                    output_text.insert(tk.END, "\n")

    except Exception as ex:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Errore di connessione al database: {ex}\n")

def apri_finestra_modifica():
    finestra_modifica = tk.Toplevel(root)
    finestra_modifica.title("Modifica Dati Società")

    # Aggiungi elementi di input per i campi da modificare
    id_label = tk.Label(finestra_modifica, text="ID:")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(finestra_modifica)
    id_entry.grid(row=0, column=1)

    indirizzo_label = tk.Label(finestra_modifica, text="Indirizzo:")
    indirizzo_label.grid(row=1, column=0)
    indirizzo_entry = tk.Entry(finestra_modifica)
    indirizzo_entry.grid(row=1, column=1)

    # Aggiungi un pulsante per salvare le modifiche
    salva_button = tk.Button(finestra_modifica, text="Salva Modifiche", command=lambda: salva_modifiche(id_entry.get(), indirizzo_entry.get()))
    salva_button.grid(row=2, column=0, columnspan=2)


def salva_modifiche(id_societa, nuovo_indirizzo):
    try:
        connection_string = "host=localhost port=5432 dbname=checkups_db user=postgres password=postgres"

        with psycopg2.connect(connection_string) as connection:
            with connection.cursor() as cursor:
                query = "UPDATE societa SET indirizzo = %s WHERE id_societa = %s"
                cursor.execute(query, (nuovo_indirizzo, id_societa))
                connection.commit()
                print("QUERY MODIFICA TERMINATA")

        # Aggiorna l'output nella finestra principale dopo aver salvato le modifiche
        visualizza_output()
    except Exception as ex:
        # Mostra un messaggio di errore se c'è un problema nel salvataggio delle modifiche
        tk.messagebox.showerror("Errore", f"Errore durante il salvataggio delle modifiche: {ex}")



root = tk.Tk()
root.title("Visualizzatore Dati")

output_text = tk.Text(root, height=20, width=80)
output_text.pack()

scrollbar = tk.Scrollbar(root, command=output_text.yview)
output_text.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

visualizza_button = tk.Button(root, text="Visualizza Società", command=visualizza_output)
visualizza_button.pack()
modifica_button = tk.Button(root, text="Modifica Dati", command=apri_finestra_modifica)
modifica_button.pack()

root.mainloop()
